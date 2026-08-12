# Installation

## Manual Agent Skills installation

Copy `skills/grounded-ai-mentor/` into the skills directory used by your client. Keep the folder name `grounded-ai-mentor`, restart the client if it discovers Skills only at startup, then explicitly test:

```text
Use $grounded-ai-mentor to explain what an HTTP request is without assuming prior knowledge.
```

## Codex local Skill

For a user-scoped manual installation:

```bash
mkdir -p ~/.codex/skills
cp -R skills/grounded-ai-mentor ~/.codex/skills/grounded-ai-mentor
```

Restart Codex and invoke `$grounded-ai-mentor` explicitly for the first check.

## Codex plugin authoring package

The repository root contains `.codex-plugin/plugin.json`. A Codex marketplace can point at this repository or a local checkout. Plugin installation surfaces change over time; follow current official Codex plugin documentation when publishing a marketplace entry.

## Validate the package

From the repository root:

```bash
python /path/to/skill-creator/scripts/quick_validate.py skills/grounded-ai-mentor
python /path/to/plugin-creator/scripts/validate_plugin.py .
python evals/validate_dataset.py
```

## Uninstall

Remove only the installed Skill folder:

```bash
rm -r ~/.codex/skills/grounded-ai-mentor
```

Review the exact path before deleting. The learner-state directory inside a project is separate and must not be removed unless the learner asks to delete it.
