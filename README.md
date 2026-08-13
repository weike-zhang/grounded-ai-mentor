<div align="center">
  <img src="assets/mascot-transparent.png" alt="Grounded AI Tutor flame mascot" width="132">

# Grounded AI Tutor

**An AI tutor that starts from what you know and explains the step you're missing.**

[简体中文](README.zh-CN.md) · [When an explanation skips a step](#when-an-explanation-skips-a-step) · [Use your project](#use-your-project-when-it-helps) · [Evidence](#evidence-and-compatibility) · [Privacy](PRIVACY.md)

</div>

You ask what a port is. The answer starts talking about protocols, processes and sockets. Now you have three more questions and still do not understand the first one.

Grounded AI Tutor teaches computing, software engineering, web systems, data, cloud and AI without assuming a technical background. It finds the earliest concept the explanation skipped, repairs that layer and checks whether you can use the idea before moving on.

A real project can make the lesson more concrete, but it is not required. The Skill uses files, logs and pages only when you allow it and when they help answer the question. Otherwise it uses a clearly labeled generic example.

## When an explanation skips a step

The learner had already heard an explanation of a port but still did not understand it. They asked:

```text
I still do not understand what a port is. Do not switch to a fancy analogy.
Return to the earliest missing prerequisite and give me one safe observation.
```

![The same port question compared as a regular answer and with Grounded AI Tutor](assets/before-after.png)

The regular answer was already accurate and safe. With the Skill, the response first repaired the idea that a computer runs several programs and must route incoming data to the right one. It then asked for a prediction before a read-only command and a locate-the-parts check afterward.

Read the [complete baseline](evals/results/pilot/baseline-misunderstanding.md), [response with the Skill](evals/results/pilot/with-skill-misunderstanding.md) and [comparison notes](evals/results/model-comparison.md). This is one exploratory pair, not a benchmark or proof of long-term learning gains.

## Start with the concept that lost you

The public install command below becomes available after the authorized remote rename to `grounded-ai-tutor`; use the current local checkout until then.

Install with the open Agent Skills CLI:

```bash
npx skills add weike-zhang/grounded-ai-tutor \
  --skill grounded-ai-tutor -g
```

Then give this prompt to a client that supports Agent Skills:

```text
Use $grounded-ai-tutor to explain what a port is.

Assume I have no technical background. If the explanation depends on a
concept I may not know, start there. Give me one safe way to check whether
I understood it before moving on.
```

The response should begin at the first missing prerequisite, define new terms before using them and include one proportionate check of understanding.

See [docs/INSTALL.md](docs/INSTALL.md) for manual Codex installation, validation, update and uninstall paths.

## Use your project when it helps

```text
Use $grounded-ai-tutor to help me understand this project.

Start when the user clicks Login and show me where the data travels.
Define each technical term when it first appears and point to the project
evidence behind specific claims. Do not change code yet.
```

When project material is available, the response should trace a compact path through the evidence it can inspect. If a relationship cannot be confirmed, it should say so instead of filling the gap with a plausible architecture.

A second read-only comparison uses a real release-bundle implementation, regression tests and a documented security failure. Both responses were strong; the Skill made the system path more explicit but showed no material accuracy advantage. Read the [project-grounded comparison](evals/results/project-grounded-comparison.md). Publishing this limit is part of the evidence standard.

## What it changes for you

| What happens now | What Grounded AI Tutor does |
| --- | --- |
| One explanation introduces several unfamiliar terms | Finds the first concept you lost and repairs that layer before adding more vocabulary |
| You ask about a concept but the answer jumps ahead | Returns to the earliest missing prerequisite before adding more terms |
| You want to connect an idea to your own work | Uses authorized project evidence when it makes the relationship clearer |
| AI says “your project probably works like this” | Points to the file, log, page or explicit statement behind each project-specific claim |
| No project material is needed or available | Uses a generic example and labels it as generic |
| You understood the explanation but cannot apply it | Uses one safe prediction, observation or locate-the-parts check to test your judgment |

The Skill is not trying to make every answer longer. It is trying to stop at the layer where understanding first broke, then give you enough evidence to make the next judgment yourself.

## How it teaches

1. It distinguishes understanding, diagnosis, implementation and learning plans, so “help me understand” does not silently become a code change.
2. It starts from material already available instead of opening with a technical-background questionnaire.
3. It finds the first missing concept and places it in the hardware → operating system → network → application → data → AI path.
4. It grounds project claims in files, logs, UI state or explicit user statements and says when evidence is missing.
5. It uses one proportionate restate, prediction, observation or transfer exercise instead of treating “heard it” as “can use it.”
6. It saves local learner state only with explicit consent.

![Grounded AI Tutor teaching flow](assets/teaching-flow.svg)

## Decisions it will not make for you

- It will not modify a project or production system merely because you asked to learn.
- It will not invent a plausible stack, file relationship, user or business result.
- It will not present a generic example as a confirmed fact about your project.
- It will not save personal learning information without consent.

## Evidence and compatibility

[![Release](https://img.shields.io/github/v/release/weike-zhang/grounded-ai-tutor)](https://github.com/weike-zhang/grounded-ai-tutor/releases)
[![Validate](https://github.com/weike-zhang/grounded-ai-tutor/actions/workflows/validate.yml/badge.svg)](https://github.com/weike-zhang/grounded-ai-tutor/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-F24B22.svg)](LICENSE)

| Surface | Status | Evidence |
| --- | --- | --- |
| Skill structure | Verified | Skill validator and CI |
| Skills CLI discovery | Partially verified | Local checkout verified; public discovery awaits the repository rename |
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
.grounded-ai-tutor/learner-profile.md
```

That path is ignored by default. Learners can view, correct, export or delete their state. Scan a profile after saving it or before reviewing whether it is suitable to share:

```bash
python skills/grounded-ai-tutor/scripts/validate_state.py \
  .grounded-ai-tutor/learner-profile.md
```

A clean scan reports only that the structure passed and no configured sensitive-data pattern was detected. It does not grant permission to persist or share the profile; both actions still require explicit authorization.

Read [PRIVACY.md](PRIVACY.md) before enabling persistence.

## Contributing and license

The most useful contribution is a reproducible teaching failure: an undefined term, invented project evidence, premature action or a case where the learner still cannot make the next judgment. See [CONTRIBUTING.md](CONTRIBUTING.md).

Code and documentation use the [MIT License](LICENSE). The project author has confirmed the right to publish and redistribute the mascot as part of Grounded AI Tutor. Mascot-derived visuals are not separately licensed under MIT for reuse outside this project; see [assets/ASSET-NOTICE.md](assets/ASSET-NOTICE.md).

Built by [Weike Zhang](https://github.com/weike-zhang).
