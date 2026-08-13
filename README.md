<div align="center">
  <img src="assets/mascot-transparent.png" alt="Grounded AI Tutor flame mascot" width="132">

# Grounded AI Tutor

**An AI tutor that starts from what you know and explains the step you're missing.**

[简体中文](README.zh-CN.md) · [When an explanation skips a step](#when-an-explanation-skips-a-step) · [Use your project](#use-your-project-when-it-helps) · [Evidence](#evidence-and-compatibility) · [Privacy](PRIVACY.md)

</div>

You ask what a port is. The answer starts using words such as protocol, process, and socket before explaining them. Now you have three more questions and still do not understand the first one.

Grounded AI Tutor teaches computing, software, websites, data, cloud systems, and AI without assuming a technical background. It goes back to the first idea the explanation skipped, explains that missing step, and checks your understanding before moving on.

A real project can make the lesson more concrete, but it is not required. The Skill uses files, logs and pages only when you allow it and when they help answer the question. Otherwise it uses a clearly labeled generic example.

## When an explanation skips a step

A learner asked what a port was. The first answer used "process" and "socket," which caused two new problems. They asked:

```text
I still don't understand what a port is. You mentioned processes and sockets,
but I don't know what those mean either. Please start earlier and give me
something safe I can check on my computer.
```

![The same port question compared as a regular answer and with Grounded AI Tutor](assets/before-after.png)

The regular answer was already correct and safe. With the Skill, the response first explained why a computer needs a way to send incoming data to the right program. It then asked the learner to predict what a read-only command would show and to identify the program and port in the result.

Read the [complete first answer](evals/results/pilot/baseline-misunderstanding.md), [answer with the Skill](evals/results/pilot/with-skill-misunderstanding.md), and [comparison notes](evals/results/model-comparison.md). These are two answers to one prompt. This is not a benchmark and does not prove that people will learn better over time.

## Start where the explanation lost you

On 2026-08-13, this command worked in a new empty test project.

Install it with the Agent Skills CLI:

```bash
npx skills add weike-zhang/grounded-ai-tutor \
  --skill grounded-ai-tutor -g
```

Then use this prompt in an app that supports Agent Skills:

```text
Use $grounded-ai-tutor to explain what a port is.

I don't have a technical background. If you need a term I haven't learned,
explain it first. Before moving on, give me one safe way to check that I
understood.
```

The response should start with the first missing idea, explain each new term before using it, and give one quick way to check that you understood it.

See [docs/INSTALL.md](docs/INSTALL.md) to install it by hand in Codex, check the install, update it, or remove it.

## Use your project when it helps

```text
Use $grounded-ai-tutor to help me understand this project.

I clicked Login. Show me where the data goes and what each part does.
Explain each new term when you first use it. Point to the file, log, or page
that supports each claim about this project. Do not change code yet.
```

When project files are available, the response shows the few files and steps that connect the click to the result. If it cannot confirm a connection, it says so instead of guessing how the project works.

Another test asks about a real ZIP bug. It uses the ZIP builder and the test that stops the bug from returning. Both answers were useful. The Skill showed the path through the code more clearly, but it did not make the answer clearly more accurate. Read the [comparison using project files](evals/results/project-grounded-comparison.md). This limit matters when judging the result.

## What it changes for you

| What happens now | What Grounded AI Tutor does |
| --- | --- |
| One explanation introduces several unfamiliar terms | Finds the first idea you missed and explains it before adding more terms |
| You ask about one idea but the answer jumps ahead | Goes back to the step where the explanation lost you |
| You want to connect an idea to your own work | Uses only the project files you allow it to read, and only when they make the idea clearer |
| AI says "your project probably works like this" | For each claim about your project, points to the file, log, page, or fact you gave it |
| No project material is needed or available | Uses a generic example and labels it as generic |
| You understood the words but cannot use the idea | Asks you to predict a result or find the relevant part in a safe command output |

The goal is not a longer answer. It is to find where your understanding first broke and help you use the idea on your own.

## How it teaches

1. It first checks whether you want to learn, find a problem, change code, or make a study plan. This stops a learning question from turning into a code change.
2. It starts with what you already shared instead of asking you to rate your technical background.
3. It finds the first missing idea and shows where it fits in the computer, network, app, data, or AI system.
4. For claims about your project, it points to the file, log, screen, or fact you gave it. It says when it cannot find proof.
5. It asks one short question or gives one safe check before moving on.
6. It saves learning notes on your computer only when you clearly agree.

![Grounded AI Tutor teaching flow](assets/teaching-flow.svg)

## What it will not do

- It will not change a project or live system just because you asked to learn.
- It will not make up the tools a project uses, how its files connect, or what users did.
- It will not claim that a general example is true for your project.
- It will not save personal learning information without your permission.

## Evidence and compatibility

[![Release](https://img.shields.io/github/v/release/weike-zhang/grounded-ai-tutor)](https://github.com/weike-zhang/grounded-ai-tutor/releases)
[![Validate](https://github.com/weike-zhang/grounded-ai-tutor/actions/workflows/validate.yml/badge.svg)](https://github.com/weike-zhang/grounded-ai-tutor/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-F24B22.svg)](LICENSE)

| What was tested | Status | Proof |
| --- | --- | --- |
| Skill files | Checked | Skill check and GitHub Actions |
| Skills CLI install | Checked from the public repository | [Test from a new empty folder](evals/results/public-install-v0.2.0.md) |
| Codex plugin file | Checked on this computer | Plugin file check |
| Teaching results | Early test only | Two complete pairs; one uses exact project files |
| Other tools that support Agent Skills | Not tested | Reports with the tool name and version are welcome |

Check that the release files are complete:

```bash
python evals/validate_fixtures.py
```

These checks confirm that the example files have the required parts. They do not measure teaching quality. See [evals/README.md](evals/README.md) for the planned repeated tests.

## Privacy

The public repository contains no private user project or real learner profile. Examples are made up, and the tests use only public repository files. The Skill may create a real profile only if the learner clearly agrees. It saves the profile at:

```text
.grounded-ai-tutor/learner-profile.md
```

Git ignores that path by default. Learners can view, correct, export, or delete their profile. Run this check after saving a profile or before sharing it:

```bash
python skills/grounded-ai-tutor/scripts/validate_state.py \
  .grounded-ai-tutor/learner-profile.md
```

A clean scan means that the file has the expected parts and no known private-data pattern was found. It does not give anyone permission to save or share the profile. Both actions still need clear approval.

Read [PRIVACY.md](PRIVACY.md) before asking the Skill to save a profile.

## Contributing and license

The most useful contribution is a teaching problem someone else can repeat: an unexplained term, a made-up claim about a project, an unwanted action, or a case where the learner still cannot make the next judgment. See [CONTRIBUTING.md](CONTRIBUTING.md).

Code and documentation use the [MIT License](LICENSE). The project author has confirmed the right to publish and redistribute the mascot as part of Grounded AI Tutor. Mascot-derived visuals are not separately licensed under MIT for reuse outside this project; see [assets/ASSET-NOTICE.md](assets/ASSET-NOTICE.md).

Built by [Weike Zhang](https://github.com/weike-zhang).
