# Baseline response: project bundle safety

你最早缺的前置概念可能是：**文件路径不是文件内容本身。**

普通文件可以粗略理解成：

```text
路径名 → 文件内容
```

符号链接则多了一次跳转：

```text
仓库内的 outside.txt → /etc/hosts → /etc/hosts 的内容
```

`outside.txt` 这个名字确实在仓库里，但它只是一个“路标”，真正的数据可能在仓库外。判断“路径字符串看起来在仓库内”因此还不够。

ZIP 打包也包含两个独立部分：

- ZIP 中显示的名字，例如 `launch-github-project/outside.txt`
- 从磁盘读取并写进去的字节

当前代码在打包每个文件时，先用仓库根目录名和相对路径生成 ZIP 内部名称，再通过 `path.read_bytes()` 读取源文件字节并交给 `archive.writestr()`：[build_release_bundle.py:93](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L93)、[build_release_bundle.py:95](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L95)、[build_release_bundle.py:99](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L99)。

问题就在这里：`read_bytes()` 会跟随符号链接。旧实现看到仓库内的 `outside.txt`，却实际读取了它指向的仓库外文件，然后仍以仓库内名称写进 ZIP。项目自己的安全复盘明确记录了这个根因和旧版结果：[self-audit-bundle-safety.md:7](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/examples/self-audit-bundle-safety.md#L7)、[self-audit-bundle-safety.md:20](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/examples/self-audit-bundle-safety.md#L20)。

所以，符号链接必须在读取之前处理。若先执行 `read_bytes()`、之后才检查，仓库外的内容已经越过安全边界进入打包进程；即使随后删除 ZIP，也太晚了。

当前实现的顺序是：

1. `build()` 先调用 `collect()`，尚未打开 ZIP：[build_release_bundle.py:85](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L85)、[build_release_bundle.py:90](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L90)。
2. 遍历目录时，遇到目录符号链接就记录为不安全并且不进入该目录：[build_release_bundle.py:46](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L46)、[build_release_bundle.py:49](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L49)、[build_release_bundle.py:53](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L53)。
3. 遇到文件符号链接同样只记录、不加入待打包列表：[build_release_bundle.py:58](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L58)、[build_release_bundle.py:62](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L62)。
4. 对剩余条目使用不会跟随链接的 `lstat()` 读取类型，只允许普通文件，FIFO、设备、socket 等也会被拒绝：[build_release_bundle.py:65](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L65)、[build_release_bundle.py:70](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L70)。
5. `is_within()` 把路径解析成实际位置，再检查它是否仍处于解析后的仓库根目录下；逃到根目录外就不会加入列表：[build_release_bundle.py:35](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L35)、[build_release_bundle.py:73](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L73)。
6. 只要发现任何不安全条目，`collect()` 整体抛错；只有完全通过后，代码才创建输出目录、打开 ZIP，并执行 `read_bytes()`：[build_release_bundle.py:77](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L77)、[build_release_bundle.py:91](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L91)。

这里有一个值得记住的区别：

- `path.relative_to(root)` 只是在处理路径文字，不能证明实际文件在仓库内。
- `path.resolve().relative_to(root.resolve())` 先解析符号链接指向的实际位置，再做边界判断：[build_release_bundle.py:23](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L23)、[build_release_bundle.py:37](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L37)。

测试分别创建了指向仓库外的文件链接和目录链接，并要求 `build()` 抛出包含“symbolic link”的错误：[test_release_tools.py:29](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/tests/test_release_tools.py#L29)、[test_release_tools.py:42](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/tests/test_release_tools.py#L42)。只读运行这组三个打包测试，当前全部通过。

这条安全结论需要准确限定：它阻止的是这次发现的**符号链接路径逃逸**，不是在证明整个项目绝对安全；项目文档自己也明确作了这个限制：[self-audit-bundle-safety.md:39](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/examples/self-audit-bundle-safety.md#L39)。此外，它假定扫描与读取期间项目没有被恶意并发替换；当前“先收集、后读取”的结构不是抵御竞态攻击的强沙箱。

理解检查可以在项目根目录只读运行：

```bash
find . -type l -print
```

它默认不会跟随链接。当前输出为空，表示这个工作树目前没有符号链接。请预测：如果它显示仓库内有 `outside.txt -> /etc/hosts`，打包器会不会把 `/etc/hosts` 写入 ZIP？正确答案是不会；它会在 `collect()` 阶段报错，根本到不了第 99 行的读取操作。即使链接只指向仓库内另一个文件，当前策略也仍会拒绝，因为它采取的是“发布包不接受任何符号链接”，而不只是“拒绝指向外部的链接”。

检查过的文件：`build_release_bundle.py`、`test_release_tools.py`、`examples/self-audit-bundle-safety.md`、`README.zh-CN.md`、`README.md`、`SECURITY.md`、`references/release-checklist.md`。
