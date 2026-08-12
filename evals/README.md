# Evaluation

This suite is intentionally small and inspectable. It measures release claims that can be observed locally; it does not prove long-term learning outcomes.

## Deterministic validation

```bash
python evals/validate_dataset.py
```

It checks 24 trigger prompts (12 expected to trigger, 12 expected not to), eight scenario fixtures, rubric weights, required public files, and the privacy-state validator. The score is a fixture coverage score, not a model quality score.

## Model comparison

For a model run, record the exact model, client version, date, prompt, raw output, rubric score, and failure notes. Compare the same fixtures with and without the Skill. Keep the raw outputs private if they contain project material; publish only redacted excerpts and aggregate scores.

Current status: deterministic fixture validation is runnable. One exploratory model pair and its limitations are recorded in `results/model-comparison.md`; it is not a benchmark or evidence of long-term learning.
