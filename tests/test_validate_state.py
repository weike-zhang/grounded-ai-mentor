from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "grounded-ai-mentor" / "scripts" / "validate_state.py"
TEMPLATE = (
    ROOT
    / "skills"
    / "grounded-ai-mentor"
    / "references"
    / "learner-profile-template.md"
)


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_state", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validator = load_validator()


class ValidateStateTests(unittest.TestCase):
    def test_blank_template_is_not_authorized_for_persistence(self):
        result = validator.validate(TEMPLATE)

        self.assertTrue(result["valid_structure"])
        self.assertFalse(result["consent_marked_granted"])
        self.assertTrue(result["contains_no_detected_sensitive_data"])
        self.assertFalse(result["valid_for_persistence"])
        self.assertNotIn("safe_to_share", result)

    def test_explicit_consent_allows_clean_profile_to_persist(self):
        with tempfile.TemporaryDirectory() as directory:
            profile = Path(directory) / "learner-profile.md"
            text = TEMPLATE.read_text(encoding="utf-8").replace(
                "Permission to persist learning state: not granted",
                "Permission to persist learning state: granted",
            )
            profile.write_text(text, encoding="utf-8")

            result = validator.validate(profile)

            self.assertTrue(result["consent_marked_granted"])
            self.assertTrue(result["valid_for_persistence"])

    def test_sensitive_data_blocks_persistence_without_echoing_value(self):
        with tempfile.TemporaryDirectory() as directory:
            profile = Path(directory) / "learner-profile.md"
            secret = "person" + "@" + "example.com"
            profile.write_text(
                TEMPLATE.read_text(encoding="utf-8")
                .replace(
                    "Permission to persist learning state: not granted",
                    "Permission to persist learning state: granted",
                )
                .replace("- Preferred name and language:", f"- Preferred name and language: {secret}"),
                encoding="utf-8",
            )

            result = validator.validate(profile)

            self.assertFalse(result["contains_no_detected_sensitive_data"])
            self.assertFalse(result["valid_for_persistence"])
            self.assertNotIn(secret, str(result))


if __name__ == "__main__":
    unittest.main()
