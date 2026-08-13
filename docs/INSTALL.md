# Installation

## Recommended: Agent Skills CLI

The public commands below become available after the authorized repository rename to `grounded-ai-tutor`. Until then, install from the current local checkout.

```bash
npx skills add weike-zhang/grounded-ai-tutor \
  --skill grounded-ai-tutor -g
```

Restart a host that discovers Skills only at startup, then test:

```text
Use $grounded-ai-tutor to explain an HTTP request without assuming prior knowledge.
```

Update or remove the installed Skill with:

```bash
npx skills update grounded-ai-tutor -g
npx skills remove grounded-ai-tutor -g
```

## Manual Codex installation

Clone the repository, then copy only the installable Skill folder:

```bash
git clone https://github.com/weike-zhang/grounded-ai-tutor.git
mkdir -p ~/.codex/skills
cp -R grounded-ai-tutor/skills/grounded-ai-tutor \
  ~/.codex/skills/grounded-ai-tutor
```

Restart Codex and invoke `$grounded-ai-tutor` explicitly for the first check.

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
rm -r ~/.codex/skills/grounded-ai-tutor
```

The learner-state directory inside a project is separate and must not be removed unless the learner explicitly asks to delete it.
