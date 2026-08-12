#!/usr/bin/env python3
"""Validate Grounded AI Mentor fixtures and produce an auditable score."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "README.md", "README.zh-CN.md", "LICENSE", "PRIVACY.md", "SECURITY.md",
    "skills/grounded-ai-mentor/SKILL.md", "skills/grounded-ai-mentor/agents/openai.yaml",
    "assets/hero.png", "assets/teaching-flow.svg", "examples/project-grounded-session.md",
]


def main() -> int:
    with (ROOT / "evals/trigger-prompts.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    scenarios = [json.loads(line) for line in (ROOT / "evals/scenarios.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    rubric = json.loads((ROOT / "evals/rubric.json").read_text(encoding="utf-8"))
    triggered = sum(row["should_trigger"] == "true" for row in rows)
    not_triggered = sum(row["should_trigger"] == "false" for row in rows)
    files_ok = all((ROOT / path).is_file() for path in REQUIRED_FILES)
    weights_ok = math.isclose(
        sum(item["weight"] for item in rubric["dimensions"]), 1.0, abs_tol=1e-9
    )
    scenario_keys_ok = all({"id", "intent", "prompt", "required", "forbidden"} <= set(item) for item in scenarios)
    checks = {
        "trigger_prompt_count": len(rows) == 24,
        "trigger_balance": triggered == 12 and not_triggered == 12,
        "scenario_count": len(scenarios) == 8,
        "scenario_schema": scenario_keys_ok,
        "rubric_weights_sum_to_one": weights_ok,
        "required_release_files": files_ok,
    }
    passed = sum(checks.values())
    result = {
        "suite": "grounded-ai-mentor",
        "version": "0.1.0",
        "checks": checks,
        "score": round(100 * passed / len(checks), 2),
        "interpretation": "fixture coverage only; not a claim of model teaching quality",
    }
    output = ROOT / "evals/results/deterministic.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
