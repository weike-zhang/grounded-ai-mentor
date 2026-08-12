<div align="center">
  <img src="assets/hero.png" alt="Grounded AI Mentor — learn computing and AI through real projects" width="100%">

# Grounded AI Mentor

**Learn computer science and AI through the systems you are actually building.**

[简体中文](README.zh-CN.md) · [How it works](#how-it-works) · [Evaluation](#evaluation) · [Privacy](PRIVACY.md)

</div>

Grounded AI Mentor is a zero-assumption Agent Skill for learning computing, software engineering, and AI. It finds the earliest missing concept, places it in the whole system, connects it to authorized project evidence, and asks for proportionate proof of understanding before moving on.

It is not a course dump, an answer bot, or permission to rewrite your project while you are trying to understand it.

## Why it is different

| A typical answer | Grounded AI Mentor |
| --- | --- |
| Uses familiar-looking terms without checking prerequisites | Defines each new term without hidden prerequisites |
| Gives an isolated explanation | Maps hardware → OS → network → app → data → AI |
| Invents a plausible relationship to your project | Cites authorized files, logs, commands, screenshots, or your statements |
| Treats explanation as mastery | Uses a small restate, prediction, observation, or transfer check |
| Saves context silently | Persists local learner state only with consent |

## Quick start

### Agent Skills-compatible clients

Copy `skills/grounded-ai-mentor/` into your client's skills directory, restart the client if required, and ask:

```text
Use $grounded-ai-mentor to explain what happens from clicking Login
to the database returning a result. Define every new term.
```

### Codex plugin package

This repository is also packaged as a skills-only Codex plugin. During local testing, add the repository through a Codex plugin marketplace or copy the bundled Skill into your Codex skills directory. See [docs/INSTALL.md](docs/INSTALL.md) for verified and manual paths.

No API key, backend, or telemetry is required by the Skill itself.

## Try these prompts

```text
Use $grounded-ai-mentor to help me understand this repository before I change it.
```

```text
I don't understand what an API is. Explain it from the user click to the saved data,
then give me one safe observation I can make in my project.
```

```text
Use $grounded-ai-mentor to diagnose this error. First inspect the evidence,
then teach me the whole request path that caused it.
```

## How it works

![Teaching flow](assets/teaching-flow.svg)

1. Route the request as explanation, diagnosis, implementation, or planning.
2. Start with existing evidence instead of an onboarding questionnaire.
3. Ask related questions only when a real decision point is reached.
4. Define the earliest missing prerequisite and place it in the system map.
5. Ground project claims in evidence or label the example generic.
6. Check understanding proportionately and preserve local state only with consent.

See [examples/project-grounded-session.md](examples/project-grounded-session.md) and [examples/misunderstanding-recovery.md](examples/misunderstanding-recovery.md).

## Privacy by architecture

The public repository contains a blank learner-profile template and fictional examples only. If a learner explicitly consents, private learning state belongs in:

```text
.grounded-ai-mentor/learner-profile.md
```

That path is ignored by default. The Skill supports viewing, correcting, exporting, and deleting the state. Run the bundled validator before sharing any profile:

```bash
python skills/grounded-ai-mentor/scripts/validate_state.py \
  .grounded-ai-mentor/learner-profile.md
```

Read [PRIVACY.md](PRIVACY.md) before enabling persistence.

## Evaluation

The evaluation suite includes positive and negative trigger prompts, multi-turn teaching scenarios, privacy and authorization cases, and a rubric for with-Skill versus without-Skill comparison.

```bash
python evals/validate_dataset.py
```

Published scores are accepted only with raw prompts, run conditions, model, date, and limitations. The first release evaluates observable teaching behavior; it does **not** claim proven long-term learning gains. See [evals/README.md](evals/README.md).

## Compatibility

| Surface | Status | Evidence |
| --- | --- | --- |
| Agent Skills folder format | Verified | Skill structure validation |
| Codex skills-only plugin | Verified locally | Plugin manifest validation |
| Codex live teaching behavior | Exploratory pair completed | One recorded pair; not a benchmark |
| Claude Code and other compatible clients | Unverified | Community testing welcome |

Compatibility labels are deliberately conservative.

## Repository map

```text
skills/grounded-ai-mentor/  # the installable Skill
examples/                   # fictional, reproducible teaching examples
evals/                      # prompts, rubric, runner guidance and results
assets/                     # mascot, hero and diagrams
docs/                       # installation and author notes
release/                    # v0.1.0 launch-ready copy
```

## Contributing

The most useful contribution is a reproducible teaching failure: an undefined term, an invented project claim, a premature action, or a case where the learner still cannot transfer the idea. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License and mascot

Code and documentation are released under the [MIT License](LICENSE).

The mascot is a user-provided asset. Its public modification and redistribution permission must be confirmed before the first public push; until then, the generated visual files are local release candidates, not licensed public assets. See [assets/ASSET-NOTICE.md](assets/ASSET-NOTICE.md).

Built by [Weike Zhang](https://github.com/weike-zhang).
