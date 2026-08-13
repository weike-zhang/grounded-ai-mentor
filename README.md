<div align="center">
  <img src="assets/mascot-transparent.png" alt="Grounded AI Mentor flame mascot" width="132">

# Grounded AI Mentor

**Let AI do more than build your project—make it explain the project to you.**

[简体中文](README.zh-CN.md) · [Install and try](#install-and-try-it) · [How it teaches](#how-it-teaches) · [Evidence](#evidence-and-compatibility) · [Privacy](PRIVACY.md)

</div>

You can already use AI to build pages, connect APIs and deploy services. But when something breaks or a critical path needs changing, you may still be unsure where the problem lives or what the change could affect.

Grounded AI Mentor is an Agent Skill for people building projects with AI. It reads only the code, logs and pages you allow, starts at the first concept you lost track of and connects abstract terms to the real project in front of you.

When the project does not support a claim, the Skill says so. It does not present a generic answer as a fact about your codebase.

## You may be stuck here

- AI-generated code runs, but you do not feel safe changing it yourself.
- When an error appears, your only move is to paste more logs back into AI.
- You have seen terms such as API, port, database and model, but cannot connect them into one path.
- An explanation feels clear in the moment, yet you cannot use it on the next problem.
- You want to learn computing and AI without putting your current project aside for months of prerequisite courses.

This Skill does not merely make AI answers longer. It starts where you are actually stuck, helps you understand and verify one part of the project, then decides what dependency comes next.

## What it changes for you

| What happens now | What Grounded AI Mentor does |
| --- | --- |
| One explanation introduces several unfamiliar terms | Finds the first concept you lost and repairs that layer before adding more vocabulary |
| You want to know how a feature really works | Traces the path from the user's action through code, requests, services and data |
| AI says “your project probably works like this” | Points to the file, log, page or explicit statement behind each project-specific claim |
| The available material cannot confirm something | Labels it as general knowledge or inference instead of pretending it is a project fact |
| You understood the explanation but cannot apply it | Uses one safe prediction, observation or locate-the-parts check to test your judgment |

The goal is not to help you memorize more terms. It is to help you describe how a feature moves through the system, know where to look for evidence, separate confirmed facts from guesses and make a safe observation before changing the project.

## See one public example

The learner had already heard an explanation of a port but still did not understand it. They asked:

```text
I still do not understand what a port is. Do not switch to a fancy analogy.
Return to the earliest missing prerequisite and give me one safe observation.
```

![The same port question compared as a regular answer and with Grounded AI Mentor](assets/before-after.png)

The regular answer was already accurate and safe. With the Skill, the response first repaired the idea that a computer runs several programs and must route incoming data to the right one. It then asked for a prediction before a read-only command and a locate-the-parts check afterward.

Read the [complete baseline](evals/results/pilot/baseline-misunderstanding.md), [response with the Skill](evals/results/pilot/with-skill-misunderstanding.md) and [comparison notes](evals/results/model-comparison.md). This is one exploratory pair, not a benchmark or proof of long-term learning gains.

A second read-only comparison uses a real release-bundle implementation, regression tests and a documented security failure. Both responses were strong; the Skill made the system path more explicit but showed no material accuracy advantage. Read the [project-grounded comparison](evals/results/project-grounded-comparison.md). Publishing this limit is part of the evidence standard.

## Install and try it

Install with the open Agent Skills CLI:

```bash
npx skills add weike-zhang/grounded-ai-mentor \
  --skill grounded-ai-mentor -g
```

Then give this prompt to a client that supports Agent Skills:

```text
Use $grounded-ai-mentor to help me understand this project.

Start when the user clicks Login and show me every place the data travels.
When a technical term first appears, explain what it is and why it exists.
Point to the evidence behind project-specific claims. Do not change code yet.
```

See [docs/INSTALL.md](docs/INSTALL.md) for manual Codex installation, validation, update and uninstall paths.

## How it teaches

1. It distinguishes understanding, diagnosis, implementation and learning plans, so “help me understand” does not silently become a code change.
2. It starts from material already available instead of opening with a technical-background questionnaire.
3. It finds the first missing concept and places it in the hardware → operating system → network → application → data → AI path.
4. It grounds project claims in files, logs, UI state or explicit user statements and says when evidence is missing.
5. It uses one proportionate restate, prediction, observation or transfer exercise instead of treating “heard it” as “can use it.”
6. It saves local learner state only with explicit consent.

![Grounded AI Mentor teaching flow](assets/teaching-flow.svg)

## Decisions it will not make for you

- It will not modify a project or production system merely because you asked to learn.
- It will not invent a plausible stack, file relationship, user or business result.
- It will not present a generic example as a confirmed fact about your project.
- It will not save personal learning information without consent.

## Evidence and compatibility

[![Release](https://img.shields.io/github/v/release/weike-zhang/grounded-ai-mentor)](https://github.com/weike-zhang/grounded-ai-mentor/releases)
[![Validate](https://github.com/weike-zhang/grounded-ai-mentor/actions/workflows/validate.yml/badge.svg)](https://github.com/weike-zhang/grounded-ai-mentor/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-F24B22.svg)](LICENSE)

| Surface | Status | Evidence |
| --- | --- | --- |
| Skill structure | Verified | Skill validator and CI |
| Skills CLI discovery | Verified | Repository discovery on 2026-08-12 |
| Codex plugin manifest | Verified locally | Manifest validation |
| Live teaching behavior | Exploratory only | Two complete pairs; one uses exact project files |
| Other Agent Skills hosts | Unverified | Community compatibility reports welcome |

Run the release-integrity checks:

```bash
python evals/validate_fixtures.py
```

These checks validate fixture structure and required files. They deliberately do not output a model-quality percentage. See [evals/README.md](evals/README.md) for the planned repeated evaluation design.

## Privacy

The public repository contains no private user project or real learner profile. Examples are fictional, and evaluations cite only publicly available repository files. A real profile may be created only with explicit consent at:

```text
.grounded-ai-mentor/learner-profile.md
```

That path is ignored by default. Learners can view, correct, export or delete their state. Scan a profile after saving it or before reviewing whether it is suitable to share:

```bash
python skills/grounded-ai-mentor/scripts/validate_state.py \
  .grounded-ai-mentor/learner-profile.md
```

A clean scan reports only that the structure passed and no configured sensitive-data pattern was detected. It does not grant permission to persist or share the profile; both actions still require explicit authorization.

Read [PRIVACY.md](PRIVACY.md) before enabling persistence.

## Contributing and license

The most useful contribution is a reproducible teaching failure: an undefined term, invented project evidence, premature action or a case where the learner still cannot make the next judgment. See [CONTRIBUTING.md](CONTRIBUTING.md).

Code and documentation use the [MIT License](LICENSE). The project author has confirmed the right to publish and redistribute the mascot as part of Grounded AI Mentor. Mascot-derived visuals are not separately licensed under MIT for reuse outside this project; see [assets/ASSET-NOTICE.md](assets/ASSET-NOTICE.md).

Built by [Weike Zhang](https://github.com/weike-zhang).
