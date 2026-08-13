# Response with Grounded AI Mentor: project bundle safety

你最早缺的前置概念不是 ZIP，而是这一句：

> 路径只是“名字和位置”，不等于最终被读取的数据。

例如仓库里看见：

```text
project/outside.txt
```

它看起来位于仓库内，但如果它是一个符号链接（symbolic link，简称 symlink）：

```text
project/outside.txt → /private-data/private.txt
```

那么程序执行 `read()` 时，操作系统通常会沿链接找到真正目标，读到仓库外的 `private.txt`。

最短的系统路径是：

```text
仓库路径
→ 操作系统解析路径和符号链接
→ Python 读取目标文件字节
→ zipfile 给字节指定 ZIP 内名称
→ 写入 ZIP
```

ZIP 并不会自己“复制项目”。程序必须给它两样东西：

1. ZIP 里显示的名字；
2. 要写进去的真实字节。

因此完全可能出现：

```text
ZIP 内名称：project/outside.txt
真实字节来源：/private-data/private.txt
```

这就是为什么必须在读取字节之前处理符号链接。若已经执行了 `read_bytes()`，仓库外内容就已经进入进程；之后再发现路径不安全已经太迟。

当前项目里，一个普通文件进入 ZIP 的过程是：

1. 命令行入口接收项目根目录和输出路径，并把它们转为解析后的绝对路径，见 [build_release_bundle.py:103](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L103)，具体调用在第 109–114 行。
2. `build()` 先要求 ZIP 输出位于项目外，再调用 `collect()` 收集候选文件，见 [build_release_bundle.py:85](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L85) 第 85–90 行。
3. `collect()` 使用 `os.walk()` 遍历目录树，见 [build_release_bundle.py:43](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L43) 第 43–46 行。
4. `.git`、`.env`、缓存、本地状态等先由 `include()` 排除，见 [build_release_bundle.py:22](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L22) 第 22–32 行。
5. 只有完成安全检查的路径才会加入 `files`，第 76 行。
6. 全部文件收集成功后才打开 ZIP，第 93 行；程序计算 ZIP 内名称 `arcname`，第 95 行。
7. 真正读取文件并写入 ZIP 的动作在同一处：`path.read_bytes()` 得到字节，`archive.writestr()` 写入 ZIP，见 [build_release_bundle.py:93](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L93) 第 93–100 行。

当前实现用四道检查阻止“仓库内名字读到仓库外内容”：

- 遇到目录符号链接，第 53–55 行记录为不安全，并且不把它放回待遍历目录列表。
- 遇到文件符号链接，第 62–64 行记录为不安全，不让它进入文件列表。
- `lstat()` 检查路径自身而不是跟随链接后的目标，并只接受普通文件，见第 65–72 行。
- `is_within()` 对解析后的路径执行 `relative_to(root)`；不能落在根目录内便返回 `False`，见 [build_release_bundle.py:35](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/skills/launch-github-project/scripts/build_release_bundle.py#L35) 第 35–40 行。

只要发现任何不安全条目，`collect()` 就在第 77–81 行抛出异常。这个顺序很关键：

```text
检查全部候选项
→ 有符号链接则报错
→ 没有错误才打开 ZIP
→ 最后才 read_bytes()
```

项目选择的是“拒绝所有符号链接”，而不是判断某个链接现在是否恰好指向仓库内。这条规则更简单，也避免链接目标后来变化。仓库中的回归测试分别构造了指向项目外部的文件链接和目录链接，并要求 `build()` 抛出包含 `symbolic link` 的错误，见 [test_release_tools.py:29](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/tests/test_release_tools.py#L29) 第 29–53 行。项目自审文档也记录了旧实现曾把链接目标字节放入 ZIP 的原因，见 [self-audit-bundle-safety.md:5](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/examples/self-audit-bundle-safety.md#L5) 第 5–20 行。

边界也要说清楚：这是源码静态检查得到的结论。它能防止正常、静止项目树中的符号链接逃逸，但检查与第 99 行读取之间仍有时间窗口；若另一个进程恰好在打包期间替换文件，理论上仍存在竞态。更严格的成熟系统通常会打包不可变快照，或使用“不跟随链接”的文件描述符打开方式。项目自己的文档也只把它称为一条狭窄安全性质，而不是“整个项目绝对安全”，见 [self-audit-bundle-safety.md:39](https://github.com/weike-zhang/launch-github-project/blob/1dc4425/examples/self-audit-bundle-safety.md#L39)。

理解检查：先预测下面命令会不会输出内容，再在项目根目录只读执行它：

```bash
find . -type l -print
```

本轮观察到输出为空，说明当前检出的项目树里没有符号链接。假设它输出了 `docs/latest`，你应能预测：该路径会在第 53 或 62 行被记录，第 81 行报错，并且不会到达第 99 行读取文件字节。

检查过的文件：`grounded-ai-mentor/SKILL.md`、`references/teaching-protocol.md`、`build_release_bundle.py`、`test_release_tools.py`、`examples/self-audit-bundle-safety.md`、`README.zh-CN.md`、`launch-github-project/SKILL.md`。
