# Model comparison: misunderstanding recovery

Status: **one exploratory pair completed; not a benchmark**.

- Date: 2026-08-12
- Model: `gpt-5.6-sol`
- Client: Codex CLI `0.147.0-alpha.6.5`
- Scenario: learner still does not understand a port and asks for the earliest prerequisite plus a safe observation
- Conditions: read-only, ephemeral, same user scenario; baseline was instructed not to read the Skill, treatment was instructed to read `SKILL.md` and the directly referenced teaching protocol

| Observable criterion | Baseline | With Skill |
| --- | ---: | ---: |
| Identifies the earliest prerequisite instead of merely changing metaphor | 1/2 | 2/2 |
| Defines the prerequisite and port without hidden dependencies | 1/2 | 2/2 |
| Places the idea in an end-to-end system path | 1/2 | 2/2 |
| Labels generic examples and avoids invented project evidence | 1/2 | 2/2 |
| Provides a non-modifying observation | 2/2 | 2/2 |
| Requests a prediction, location, or transfer check | 1/2 | 2/2 |
| **Total** | **7/12 (58.3%)** | **12/12 (100%)** |

The baseline answer was already accurate and safe. The observed improvement was narrower: the Skill explicitly defined `process`, showed the operating-system path, labeled the example generic, and asked the learner to predict and locate output before continuing. One pair cannot establish reliability or long-term learning. Raw outputs remain in the ignored local `evals/results/runs/` directory.
