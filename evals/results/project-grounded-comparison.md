# Exploratory comparison: real-project bundle safety

Status: **one transparent project-grounded pair; not a benchmark**.

- Date: 2026-08-13
- Runtime: isolated Codex subagents using the same inherited session model; exact deployment identifier was not exposed
- Scenario: explain why a real release-bundle implementation must handle symlinks before reading file bytes
- Project evidence: the current `launch-github-project` bundle builder, regression tests and self-audit case
- Conditions: read-only and ephemeral; the baseline did not load Grounded AI Tutor, while the treatment loaded `SKILL.md` and `teaching-protocol.md`
- Sanitization: machine-specific checkout paths were replaced with repository-relative links and commands

## Published outputs

- [Baseline response](pilot/baseline-project-bundle-safety.md)
- [Response with Grounded AI Tutor](pilot/with-skill-project-bundle-safety.md)

## Exact sanitized prompt

```text
请查看真实项目 launch-github-project。我不明白为什么发布 ZIP 在读取文件之前
必须处理符号链接。请从我最早缺失的前置概念开始，结合当前代码解释一次文件
怎样进入 ZIP、当前实现怎样阻止仓库内路径读到仓库外内容。涉及项目的结论请引用
精确文件和行号，最后给我一个安全的预测或只读观察来检查我是否理解。
```

## What was observed

| Behavior | Baseline | With Skill |
| --- | --- | --- |
| Earliest prerequisite | Explicitly distinguishes a path from file content | Explicitly distinguishes a path from the bytes ultimately read |
| System path | Explains archive name versus source bytes | Opens with a compact operating-system → Python → ZIP path |
| Project evidence | Cites implementation, tests and self-audit lines | Cites implementation, tests and self-audit lines |
| Understanding check | Predicts whether an external-target link reaches `read_bytes()` | Predicts the exact collection and failure stage before `read_bytes()` |
| Limitations | Identifies the remaining scan/read race | Identifies the same remaining race and stronger snapshot/open options |
| Safety | Read-only and accurate | Read-only and accurate |

The baseline was already unusually complete, grounded and pedagogically structured. The Skill response made the compact system path and check-before-read sequence more visually explicit, but this pair does not show a material accuracy or safety advantage. Its value is narrower: it demonstrates that the Skill can operate on real files without inventing project relationships.

One pair cannot establish reliable triggering, learning transfer, compatibility across hosts or long-term learning gains. A future evaluation needs multiple unfamiliar repositories, repeated runs, blinded scoring and actual learner responses.
