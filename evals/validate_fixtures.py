#!/usr/bin/env python3
"""Validate the structure and release integrity of evaluation fixtures."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "README.md",
    "README.zh-CN.md",
    "LICENSE",
    "PRIVACY.md",
    "SECURITY.md",
    "skills/grounded-ai-tutor/SKILL.md",
    "skills/grounded-ai-tutor/agents/openai.yaml",
    "assets/social-preview.png",
    "assets/teaching-flow.svg",
    "examples/project-grounded-session.md",
    "tests/test_validate_state.py",
    "evals/results/project-grounded-comparison.md",
    "evals/results/public-install-v0.2.0.md",
    "evals/results/pilot/baseline-project-bundle-safety.md",
    "evals/results/pilot/with-skill-project-bundle-safety.md",
    "release/v0.2.0.json",
    "release/v0.2.0.md",
    "tests/test_public_materials.py",
]


def main() -> int:
    with (ROOT / "evals/trigger-prompts.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    scenarios = [
        json.loads(line)
        for line in (ROOT / "evals/scenarios.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    rubric = json.loads((ROOT / "evals/rubric.json").read_text(encoding="utf-8"))
    manifest = json.loads((ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    release_spec = json.loads((ROOT / "release/v0.2.0.json").read_text(encoding="utf-8"))
    release_page = (ROOT / "release/v0.2.0.md").read_text(encoding="utf-8")
    triggered = sum(row["should_trigger"] == "true" for row in rows)
    not_triggered = sum(row["should_trigger"] == "false" for row in rows)
    checks = {
        "trigger_prompt_count": len(rows) == 24,
        "trigger_balance": triggered == 12 and not_triggered == 12,
        "scenario_count": len(scenarios) == 8,
        "scenario_schema": all(
            {"id", "intent", "prompt", "required", "forbidden"} <= set(item)
            for item in scenarios
        ),
        "rubric_weights_sum_to_one": math.isclose(
            sum(item["weight"] for item in rubric["dimensions"]), 1.0, abs_tol=1e-9
        ),
        "required_release_files": all((ROOT / path).is_file() for path in REQUIRED_FILES),
        "release_version_alignment": (
            manifest["version"] == release_spec["version"] == "0.2.0"
            and f"v{release_spec['version']}" in release_page.splitlines()[0]
        ),
        "release_page_matches_spec": (
            release_spec["title"] in release_page.splitlines()[0]
            and release_spec["summary"] in release_page
            and release_spec["release_asset"] in release_page
            and all(command in release_page for command in release_spec["install_or_update"])
        ),
    }
    passed = sum(checks.values())
    result = {
        "suite": "grounded-ai-tutor-fixture-integrity",
        "version": "0.2.0",
        "checks": checks,
        "passed_checks": passed,
        "total_checks": len(checks),
        "all_passed": all(checks.values()),
        "interpretation": "Structure and release-integrity checks only; no model behavior or learning outcome is scored.",
    }
    output = ROOT / "evals/results/fixture-integrity.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
