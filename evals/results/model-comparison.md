# Pilot comparison: misunderstanding recovery

Status: **one transparent pilot pair; not a benchmark**.

- Date: 2026-08-12
- Model: `gpt-5.6-sol`
- Client: Codex CLI `0.147.0-alpha.6.5`
- Scenario: a learner still does not understand a port and asks for the earliest prerequisite plus a safe observation
- Exact user prompt: `我还是不明白什么是端口。请不要换一个花哨比喻，回到最早的前置概念并让我做一个安全观察。`
- Conditions: read-only and ephemeral; the baseline did not read the Skill, while the treatment read `SKILL.md` and its teaching protocol

## Published outputs

- [Baseline response](pilot/baseline-misunderstanding.md)
- [Response with Grounded AI Mentor](pilot/with-skill-misunderstanding.md)

## What was observed

| Behavior | Baseline | With Skill |
| --- | --- | --- |
| Earliest prerequisite | Introduces concurrent programs before the port definition | Explicitly names the running-process concept as the earliest gap |
| System path | Explains IP, operating system and program routing | Opens with a compact end-to-end path, then expands it |
| Generic evidence | Uses a clearly hypothetical command output | Explicitly labels the service map as a generic example |
| Understanding check | Requests a real read-only observation | Requests a prediction before the observation and a locate-the-parts check afterward |
| Safety | Accurate and read-only | Accurate and read-only |

The baseline was already useful, accurate and safe. The narrower observed difference was that the Skill made the prerequisite, system path, evidence label and prediction step more explicit. One pair cannot establish reliability, compatibility across hosts or long-term learning gains.
