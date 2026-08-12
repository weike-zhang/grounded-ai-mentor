#!/usr/bin/env python3
"""Validate a local Grounded AI Mentor learner profile without echoing secrets."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REQUIRED_HEADINGS = (
    "## Consent",
    "## Confirmed information",
    "## Shared inferences to confirm",
    "## Unknowns that currently matter",
    "## Progress evidence",
)

SENSITIVE_PATTERNS = {
    "possible_api_key": re.compile(r"\b(?:sk|gh[opusr]|AKIA)[-_A-Za-z0-9]{12,}\b"),
    "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "email_address": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "phone_number": re.compile(r"(?<!\d)(?:\+?86[- ]?)?1[3-9]\d{9}(?!\d)"),
    "government_id_like": re.compile(r"(?<!\d)\d{17}[0-9Xx](?!\d)"),
}


def validate(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    missing = [heading for heading in REQUIRED_HEADINGS if heading not in text]
    findings: list[dict[str, object]] = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        for kind, pattern in SENSITIVE_PATTERNS.items():
            if pattern.search(line):
                findings.append({"line": line_no, "type": kind})
    consent_granted = bool(
        re.search(
            r"Permission to persist learning state:\s*(?:granted|yes|true|已授权|同意)",
            text,
            re.I,
        )
    )
    return {
        "path": str(path),
        "valid_structure": not missing,
        "missing_headings": missing,
        "consent_marked_granted": consent_granted,
        "sensitive_findings": findings,
        "safe_to_share": not missing and not findings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    if not args.profile.is_file():
        parser.error(f"profile not found: {args.profile}")
    result = validate(args.profile)
    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Structure: {'PASS' if result['valid_structure'] else 'FAIL'}")
        print(f"Consent marked granted: {result['consent_marked_granted']}")
        print(f"Sensitive findings: {len(result['sensitive_findings'])}")
        print(f"Safe to share: {result['safe_to_share']}")
    return 0 if result["safe_to_share"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
