# Evaluation

This repository separates release integrity from model behavior. Neither proves long-term learning outcomes.

## Fixture integrity

```bash
python evals/validate_fixtures.py
```

The script checks the shape and balance of 24 trigger fixtures, eight scenario fixtures, rubric weights and required release files. It reports checks passed, not a performance percentage. It does not invoke a model or test whether the Skill actually triggers.

## Model behavior

Model comparisons must record the exact model, client version, date, prompt, full sanitized output, scoring method and failure notes. Compare the same scenario with and without the Skill.

Current status: transparent exploratory pairs and their limitations are published in [results/model-comparison.md](results/model-comparison.md). The project-grounded pair uses exact repository files; neither pair is a benchmark, compatibility claim or evidence of long-term learning.

A future benchmark should run all eight scenarios in both conditions with repeated trials, publish sanitized raw outputs, report failures and avoid converting one successful example into a broad product claim.
