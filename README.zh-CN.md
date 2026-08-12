<div align="center">
  <img src="assets/mascot-transparent.png" alt="Grounded AI Mentor 火焰角色" width="132">

# Grounded AI Mentor

**沿着眼前的真实项目学懂计算机与 AI，不跳过隐藏前提，也不编造项目关系。**

[![Release](https://img.shields.io/github/v/release/weike-zhang/grounded-ai-mentor)](https://github.com/weike-zhang/grounded-ai-mentor/releases)
[![Validate](https://github.com/weike-zhang/grounded-ai-mentor/actions/workflows/validate.yml/badge.svg)](https://github.com/weike-zhang/grounded-ai-mentor/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-F24B22.svg)](LICENSE)

[English](README.md) · [工作原理](#工作原理) · [证据状态](#证据状态) · [隐私](PRIVACY.md)

</div>

Grounded AI Mentor 面向已经在使用 AI 做项目、同时希望真正理解底层系统的人。它会找到最早缺失的概念，使用经过授权的项目证据建立关联，并在继续之前确认学习者是否能够使用这个概念。

## 安装并立即尝试

使用 Agent Skills CLI 安装：

```bash
npx skills add weike-zhang/grounded-ai-mentor \
  --skill grounded-ai-mentor -g
```

然后输入：

```text
使用 $grounded-ai-mentor，从点击登录按钮开始解释到数据库返回结果。
第一次出现的技术词要先定义；涉及我项目的结论必须引用真实证据。
```

Codex 手动安装、校验、更新和卸载方式见 [docs/INSTALL.zh-CN.md](docs/INSTALL.zh-CN.md)。

## 一次教学中会发生什么变化

![基线回答与 Grounded AI Mentor 回答的探索性对照](assets/before-after.zh-CN.png)

公开的探索性案例中，基线回答本身已经准确且安全。启用 Skill 后，以下行为变得更明确：

- 先指出最早缺失的前置概念，再定义用户问的词；
- 先展示最短的端到端系统路径；
- 把通用示例明确标成通用示例；
- 在安全观察前先要求学习者做预测。

可以阅读[完整脱敏输出与限制](evals/results/model-comparison.md)。一组案例不是基准测试，也不能证明长期学习效果。

## 工作原理

![Grounded AI Mentor 中文教学流程](assets/teaching-flow.zh-CN.svg)

1. 判断当前是学习、诊断、改动还是规划。
2. 先使用已有证据，不在开头启动问卷。
3. 找到最早缺失的前置概念，并放进系统地图。
4. 项目结论必须来自文件、日志、界面状态或用户明确陈述。
5. 使用一次适度的复述、预测、观察或迁移任务验证理解。
6. 只有得到明确同意才保存本地学习状态。

Skill 不会把学习请求擅自变成代码修改，不会编造看起来合理的项目架构，也不会静默保存个人上下文。

## 证据状态

| 使用方式 | 状态 | 证据 |
| --- | --- | --- |
| Skill 结构 | 已验证 | Skill 验证器和 CI |
| Skills CLI 发现 | 已验证 | 2026-08-12 在线发现仓库中的 Skill |
| Codex 插件清单 | 本地已验证 | 清单校验通过 |
| 实际教学行为 | 仅探索性案例 | 一组完整的基线/Skill 输出 |
| 其他 Agent Skills 客户端 | 未验证 | 欢迎提交兼容性报告 |

运行发布材料完整性检查：

```bash
python evals/validate_fixtures.py
```

这项检查只验证夹具结构和必要文件，不输出模型能力百分比。重复运行方案见 [evals/README.md](evals/README.md)。

## 隐私架构

公开仓库只包含虚构案例和空白学习画像模板。只有获得明确同意时，才可以在项目中创建：

```text
.grounded-ai-mentor/learner-profile.md
```

该目录默认被 Git 忽略。学习者可以查看、纠正、导出或删除状态。分享前运行：

```bash
python skills/grounded-ai-mentor/scripts/validate_state.py \
  .grounded-ai-mentor/learner-profile.md
```

启用持久化前请阅读 [PRIVACY.md](PRIVACY.md)。

## 贡献与许可

最有价值的贡献是可复现的教学失败：未定义术语、编造项目证据、过早执行操作，或学习者仍无法迁移使用的案例。参见 [CONTRIBUTING.md](CONTRIBUTING.md)。

代码和文档使用 [MIT License](LICENSE)。项目作者已经确认火焰角色可以作为 Grounded AI Mentor 的一部分公开和再分发；角色衍生视觉不随 MIT 许可单独授权给项目外使用。详见 [assets/ASSET-NOTICE.md](assets/ASSET-NOTICE.md)。

Built by [Weike Zhang](https://github.com/weike-zhang)。
