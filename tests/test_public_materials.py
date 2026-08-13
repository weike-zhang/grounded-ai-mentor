from __future__ import annotations

import json
import struct
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INSTALL_COMMAND = (
    "npx skills add weike-zhang/grounded-ai-tutor \\\n"
    "  --skill grounded-ai-tutor -g"
)


class PublicMaterialsTests(unittest.TestCase):
    def read(self, relative: str) -> str:
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_first_use_precedes_example_and_teaching_protocol(self):
        english = self.read("README.md")
        chinese = self.read("README.zh-CN.md")

        self.assertLess(
            english.index("## When an explanation skips a step"),
            english.index("## Use your project when it helps"),
        )
        self.assertLess(
            english.index("## Use your project when it helps"),
            english.index("## How it teaches"),
        )
        self.assertLess(
            chinese.index("## 解释跳步了怎么办？"),
            chinese.index("## 需要时，再结合自己的项目"),
        )
        self.assertLess(
            chinese.index("## 需要时，再结合自己的项目"),
            chinese.index("## 它怎样陪你学"),
        )

    def test_bilingual_readmes_share_the_verified_install_command(self):
        for relative in (
            "README.md",
            "README.zh-CN.md",
            "docs/INSTALL.md",
            "docs/INSTALL.zh-CN.md",
        ):
            self.assertIn(INSTALL_COMMAND, self.read(relative), relative)

    def test_tutor_identity_precedes_optional_project_grounding(self):
        english = self.read("README.md")
        chinese = self.read("README.zh-CN.md")
        manifest = json.loads(self.read(".codex-plugin/plugin.json"))
        skill = self.read("skills/grounded-ai-tutor/SKILL.md")

        self.assertIn("A real project can make the lesson more concrete", english)
        self.assertIn("真实项目可以让解释更具体，但不是使用前提", chinese)
        self.assertIn("only when they improve the lesson", skill)
        self.assertEqual(manifest["name"], "grounded-ai-tutor")
        self.assertEqual(manifest["interface"]["displayName"], "Grounded AI Tutor")
        for text in (english, chinese):
            self.assertNotIn("Grounded AI Mentor", text)
            self.assertNotIn("grounded-ai-mentor", text)
            self.assertNotIn("awaits the repository rename", text)
            self.assertNotIn("等待远程仓库改名", text)
        self.assertIn("evals/results/public-install-v0.2.0.md", english)
        self.assertIn("evals/results/public-install-v0.2.0.md", chinese)

    def test_bilingual_comparisons_keep_the_evidence_limit_nearby(self):
        english = self.read("README.md")
        chinese = self.read("README.zh-CN.md")

        self.assertIn("two answers to one prompt", english)
        self.assertIn("not a benchmark", english)
        self.assertIn("did not make the answer clearly more accurate", english)
        self.assertIn("不是基准测试", chinese)
        self.assertIn("没有表现出实质性的准确性优势", chinese)

    def test_social_preview_uses_github_recommended_dimensions(self):
        data = (ROOT / "assets/social-preview.png").read_bytes()
        self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
        width, height = struct.unpack(">II", data[16:24])
        self.assertEqual((width, height), (1280, 640))

    def test_release_spec_matches_manifest_and_generated_page(self):
        manifest = json.loads(self.read(".codex-plugin/plugin.json"))
        spec = json.loads(self.read("release/v0.2.0.json"))
        page = self.read("release/v0.2.0.md")

        self.assertEqual(manifest["version"], spec["version"])
        self.assertIn(f"v{spec['version']}", page.splitlines()[0])
        self.assertIn(spec["title"], page.splitlines()[0])
        self.assertIn(spec["summary"], page)
        for command in spec["install_or_update"]:
            self.assertIn(command, page)
        self.assertIn(spec["release_asset"], page)

    def test_english_readme_uses_questions_a_learner_would_ask(self):
        english = self.read("README.md")

        self.assertIn("## Start where the explanation lost you", english)
        self.assertIn("You mentioned processes and sockets", english)
        self.assertIn("something safe I can check on my computer", english)
        self.assertIn("shows the few files and steps", english)
        self.assertIn("one quick way to check that you understood it", english)

        stale_phrases = [
            "repairs that layer",
            "Return to the earliest missing prerequisite",
            "locate-the-parts check",
            "Start with the concept that lost you",
            "trace a compact path through the evidence",
            "one proportionate check of understanding",
            "places it in the hardware",
            "grounds project claims",
            "proportionate restate",
        ]
        for phrase in stale_phrases:
            self.assertNotIn(phrase, english)

    def test_english_visuals_explain_the_learning_result_in_plain_words(self):
        source = self.read("scripts/build_visuals.py")
        flow = self.read("assets/teaching-flow.svg")

        self.assertIn("Explains why programs need ports", source)
        self.assertIn("Find what the learner missed", flow)
        self.assertIn("Check understanding", flow)
        for phrase in (
            "First repairs",
            "Predicts before, locates after",
            "2. Evidence",
            "3. Foundation",
            "restate, predict",
            "observe, transfer",
        ):
            self.assertNotIn(phrase, source + flow)


if __name__ == "__main__":
    unittest.main()
