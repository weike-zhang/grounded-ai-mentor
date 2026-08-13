<div align="center">
  <img src="assets/mascot-transparent.png" alt="Grounded AI Tutor 火焰角色" width="132">

# Grounded AI Tutor

**从你已经理解的地方开始，把缺的那一步讲明白。**

[English](README.md) · [解释跳步了怎么办](#解释跳步了怎么办) · [结合自己的项目](#需要时再结合自己的项目) · [证据与兼容性](#证据与兼容性) · [隐私](PRIVACY.md)

</div>

你问的是“端口是什么”，回答却直接讲起协议、进程和套接字。结果多了三个陌生词，原来的问题还是没听懂。

Grounded AI Tutor 是一个不预设技术基础的 AI 教学 Skill，目前覆盖计算机、软件工程、Web、数据、云和 AI。它会找到解释跳过的第一个前置概念，先补上这一层，再确认你能不能把它用到下一个问题里。

真实项目可以让解释更具体，但不是使用前提。只有得到允许，而且项目材料确实有助于回答时，它才会读取文件、日志或页面；其他时候使用明确标注的通用例子。

## 解释跳步了怎么办？

案例中的学习者已经听过“端口”的解释，但仍然不明白，于是提出：

```text
我还是不明白什么是端口。请不要换一个花哨比喻，
回到最早的前置概念并让我做一个安全观察。
```

![同一个端口问题在普通回答与 Grounded AI Tutor 中的学习过程对照](assets/before-after.zh-CN.png)

普通回答本身已经准确、安全。启用 Skill 后，回答先补上“电脑会同时运行多个程序，收到的数据必须交给正确程序”这一层，再解释端口；运行只读命令前先让学习者预测，运行后再请他从结果中找出程序和端口。

你可以查看[完整的基线回答](evals/results/pilot/baseline-misunderstanding.md)、[启用 Skill 后的回答](evals/results/pilot/with-skill-misunderstanding.md)和[对照说明](evals/results/model-comparison.md)。这只是一组公开的探索性案例，不是基准测试，也不能证明长期学习效果。

## 从卡住的那个概念开始

下面的公网安装命令已于 2026-08-13 从干净临时项目验证。

使用 Agent Skills CLI 安装：

```bash
npx skills add weike-zhang/grounded-ai-tutor \
  --skill grounded-ai-tutor -g
```

然后把这段话交给支持 Agent Skills 的客户端：

```text
使用 $grounded-ai-tutor 给我解释什么是端口。

假设我没有技术基础。如果解释依赖了我可能不知道的概念，
请先从那里讲起。继续下一个概念前，给我一种安全的方法，
让我确认自己是不是真的理解了。
```

回答应该从第一个缺失的前置概念开始，先定义再使用新术语，并安排一次不过量的理解检查。

Codex 手动安装、校验、更新和卸载方式见 [docs/INSTALL.zh-CN.md](docs/INSTALL.zh-CN.md)。

## 需要时，再结合自己的项目

```text
使用 $grounded-ai-tutor 帮我看懂这个项目。

请从“用户点击登录”开始，告诉我数据经过了哪些地方。
第一次出现的技术词，先解释它是什么、解决什么问题。
结合项目时请指出依据；先不要修改代码。
```

项目材料可用时，回答应该沿它能检查的证据画出一条紧凑路径。如果某个关系无法确认，它应该直接说明，不用看起来合理的架构补空白。

第二组只读对照直接使用真实发布打包器、回归测试和已经记录的安全缺陷。两组回答都很强；启用 Skill 后系统路径更直观，但没有表现出实质性的准确性优势。完整材料见[真实项目证据对照](evals/results/project-grounded-comparison.md)。如实公开这个限制也是证据标准的一部分。

## 它具体会怎么帮你

| 你遇到的情况 | Grounded AI Tutor 的做法 |
| --- | --- |
| 一个解释里连续出现很多陌生词 | 找到你第一次跟不上的概念，先补这一层，不继续堆术语 |
| 问一个概念，回答却连续跳步 | 回到最早缺失的前置概念，不继续堆新词 |
| 想把概念对应到自己的工作 | 项目证据确实有帮助时，才读取你允许查看的材料 |
| AI 说“你的项目应该是这样” | 指出结论来自哪个文件、日志、页面或你的明确陈述 |
| 不需要或没有项目材料 | 使用通用例子，并明确说明它不是你的项目事实 |
| 听完感觉懂了，但还不会用 | 让你做一次安全的预测、观察或定位，确认自己能判断 |

它不是为了把每个回答写得更长，而是要停在理解第一次断掉的那一层，让你补上之后能自己做出下一个判断。

## 它怎样陪你学

1. 先判断你现在要的是理解、诊断、修改还是学习规划，不把“给我讲明白”擅自变成改代码。
2. 先利用你已经提供的材料开始解释，不在开头让你填写一整套技术背景问卷。
3. 找到你第一次跟不上的概念，把它放回“硬件—操作系统—网络—应用—数据—AI”的完整路径。
4. 涉及真实项目时，引用文件、日志、界面状态或你的明确陈述；证据不足就如实说明。
5. 对重要内容安排一次适度的复述、预测、观察或迁移练习，不把“听过”当成“会用”。
6. 只有得到明确同意，才会在本地保存学习状态。

![Grounded AI Tutor 中文教学流程](assets/teaching-flow.zh-CN.svg)

## 它不会替你做的决定

- 不会因为你想学习，就擅自修改项目或生产环境；
- 不会编造看起来合理的技术栈、文件关系、用户或业务结果；
- 不会把通用示例写成已经在你项目中确认的事实；
- 不会未经同意保存个人学习信息。

## 证据与兼容性

[![Release](https://img.shields.io/github/v/release/weike-zhang/grounded-ai-tutor)](https://github.com/weike-zhang/grounded-ai-tutor/releases)
[![Validate](https://github.com/weike-zhang/grounded-ai-tutor/actions/workflows/validate.yml/badge.svg)](https://github.com/weike-zhang/grounded-ai-tutor/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-F24B22.svg)](LICENSE)

| 使用方式 | 状态 | 证据 |
| --- | --- | --- |
| Skill 结构 | 已验证 | Skill 验证器和 CI |
| Skills CLI 发现 | 公网已验证 | [干净临时项目验证](evals/results/public-install-v0.2.0.md) |
| Codex 插件清单 | 本地已验证 | 清单校验通过 |
| 实际教学行为 | 仅探索性案例 | 两组完整对照，其中一组使用真实项目文件 |
| 其他 Agent Skills 客户端 | 未验证 | 欢迎提交兼容性报告 |

运行发布材料完整性检查：

```bash
python evals/validate_fixtures.py
```

这项检查只验证夹具结构和必要文件，不输出模型能力百分比。重复运行方案见 [evals/README.md](evals/README.md)。

## 隐私

公开仓库不包含用户的私有项目或真实学习画像；示例使用虚构材料，评估只引用可公开的仓库文件。只有得到你的明确同意，Skill 才可以在当前项目中创建：

```text
.grounded-ai-tutor/learner-profile.md
```

该目录默认被 Git 忽略。你可以随时查看、纠正、导出或删除其中的内容。持久化或评估是否可分享之前运行：

```bash
python skills/grounded-ai-tutor/scripts/validate_state.py \
  .grounded-ai-tutor/learner-profile.md
```

扫描通过只表示结构有效、且没有命中已配置的敏感信息规则；它不代表已经获得持久化或分享授权，这两个动作仍需学习者明确同意。

启用学习状态保存前，请阅读 [PRIVACY.md](PRIVACY.md)。

## 贡献与许可

最有价值的贡献是可复现的教学失败：哪个词没有定义、哪段项目关系被编造、哪次操作执行得太早，或者解释结束后学习者仍然不会判断。参见 [CONTRIBUTING.md](CONTRIBUTING.md)。

代码和文档使用 [MIT License](LICENSE)。项目作者已经确认火焰角色可以作为 Grounded AI Tutor 的一部分公开和再分发；角色衍生视觉不随 MIT 许可单独授权给项目外使用。详见 [assets/ASSET-NOTICE.md](assets/ASSET-NOTICE.md)。

Built by [Weike Zhang](https://github.com/weike-zhang)。
