# Exploratory comparisons

Two complete sanitized pairs are published:

- [Misunderstanding recovery](#pilot-1-misunderstanding-recovery): a generic port explanation that tests prerequisite repair.
- [Real-project bundle safety](project-grounded-comparison.md): a file-grounded explanation that cites a live repository's implementation, tests and remaining limitation.

Neither pair is a benchmark or proof of learning gains.

## Pilot 1: misunderstanding recovery

Status: **one transparent pilot pair; not a benchmark**.

- Date: 2026-08-12
- Model: `gpt-5.6-sol`
- Client: Codex CLI `0.147.0-alpha.6.5`
- Scenario: a learner still does not understand a port and asks for the earliest prerequisite plus a safe observation
- Exact user prompt: `我还是不明白什么是端口。请不要换一个花哨比喻，回到最早的前置概念并让我做一个安全观察。`
- Conditions: read-only and ephemeral; the baseline did not read the Skill, while the treatment read `SKILL.md` and its teaching protocol

## Published outputs

- [Baseline response](pilot/baseline-misunderstanding.md)
- [Response with Grounded AI Tutor](pilot/with-skill-misunderstanding.md)

## What was observed

| Behavior | Baseline | With Skill |
| --- | --- | --- |
| Earliest prerequisite | Introduces concurrent programs before the port definition | Explicitly names the running-process concept as the earliest gap |
| System path | Explains IP, operating system and program routing | Opens with a compact end-to-end path, then expands it |
| Generic evidence | Uses a clearly hypothetical command output | Explicitly labels the service map as a generic example |
| Understanding check | Requests a real read-only observation | Requests a prediction before the observation and a locate-the-parts check afterward |
| Safety | Accurate and read-only | Accurate and read-only |

The baseline was already useful, accurate and safe. The narrower observed difference was that the Skill made the prerequisite, system path, evidence label and prediction step more explicit. One pair cannot establish reliability, compatibility across hosts or long-term learning gains.

## Pilot 2: real-project evidence

The second pair asks both conditions to explain a symlink path-escape repair in `launch-github-project` using exact code and test evidence. Both responses were accurate, grounded and explicit about a remaining scan/read race. The Skill response made the compact system path and check-before-read sequence more visual, but did not show a material accuracy or safety advantage over this strong baseline.

Read the [complete method, outputs and limitations](project-grounded-comparison.md). This pair demonstrates a real project-evidence path; it still does not establish reliable learning transfer or long-term outcomes.
