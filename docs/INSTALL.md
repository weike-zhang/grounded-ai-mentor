# Installation

## Recommended: Agent Skills CLI

```bash
npx skills add weike-zhang/grounded-ai-mentor \
  --skill grounded-ai-mentor -g
```

Restart a host that discovers Skills only at startup, then test:

```text
Use $grounded-ai-mentor to explain an HTTP request without assuming prior knowledge.
```

Update or remove the installed Skill with:

```bash
npx skills update grounded-ai-mentor -g
npx skills remove grounded-ai-mentor -g
```

## Manual Codex installation

Clone the repository, then copy only the installable Skill folder:

```bash
git clone https://github.com/weike-zhang/grounded-ai-mentor.git
mkdir -p ~/.codex/skills
cp -R grounded-ai-mentor/skills/grounded-ai-mentor \
  ~/.codex/skills/grounded-ai-mentor
```

Restart Codex and invoke `$grounded-ai-mentor` explicitly for the first check.

## Validate a checkout

From the repository root:

```bash
python -m unittest discover -s tests -v
python evals/validate_fixtures.py
```

The tests cover learner-state consent and sensitive-pattern semantics. The fixture command validates release structure; neither command scores model behavior or grants permission to persist or share learner state.

## Manual uninstall

If the Skill was copied manually, review the exact path and remove only the installed Skill folder:

```bash
rm -r ~/.codex/skills/grounded-ai-mentor
```

The learner-state directory inside a project is separate and must not be removed unless the learner explicitly asks to delete it.
