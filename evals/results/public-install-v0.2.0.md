# Public install verification for v0.2.0

Date: 2026-08-13. Repository: `weike-zhang/grounded-ai-tutor`. Scope: public default branch after the repository rename, tested from a temporary clean project.

```bash
npx -y skills@latest add weike-zhang/grounded-ai-tutor \
  --agent codex --skill grounded-ai-tutor --copy -y
```

The Skills CLI cloned the public repository, found one Skill named `grounded-ai-tutor` and copied it to `.agents/skills/grounded-ai-tutor`. The installed `SKILL.md` was present after the command completed.

This verifies public repository discovery and installation. It does not score teaching behavior, prove learning outcomes or establish compatibility with other Agent Skills hosts.
