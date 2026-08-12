# Teaching protocol

## Build the map before the detail

For a substantial topic, begin with the shortest useful end-to-end path. Example:

```text
click → browser event → HTTP request → backend route → business logic
      → database or model → response → page update
```

Define only the terms required for the current path. Do not introduce a large glossary merely because the curriculum contains it.

## Explain a new term

Use this sequence when a term is new to the learner:

1. **What it is** — one sentence without undefined prerequisites; add the English term or expansion.
2. **Why it exists** — the concrete problem that appeared before this mechanism.
3. **Where it sits** — identify its layer and immediate neighbors.
4. **How it is handled** — distinguish a personal exercise, a small product team, and a mature organization when the distinction matters.
5. **How it connects** — cite authorized project evidence; otherwise label the example generic.
6. **What it is not** — resolve the most likely confusion.

## Recover from a gap

When the learner is stuck:

1. Preserve the part they got right.
2. Identify the earliest statement that depends on an unexplained idea.
3. Define that prerequisite with a smaller example.
4. Ask the learner to apply the repaired idea once.
5. Resume the original path only after the prerequisite works.

Do not respond by repeating the same explanation with more jargon.

## Use evidence

Project-specific statements need one of these anchors:

- a path and relevant symbol or line;
- a command and its observed output;
- a request or response sample;
- a log, screenshot, diagram, or configuration;
- an explicit user statement.

State when an explanation is inferred. Do not claim a runtime path was observed when only source code was inspected.

## Verify understanding

Choose the lightest check that fits the lesson:

- **Restate**: explain the user action → system result path.
- **Predict**: say what a safe command or request should reveal.
- **Locate**: identify where the concept appears in the project.
- **Repair**: fix a minimal synthetic example.
- **Transfer**: apply the concept to a neighboring case.

One lucky answer is not mastery. Repeated, independent application is stronger evidence, but avoid turning every conversation into an exam.

## Explain current AI facts

For current model names, prices, product behavior, policy, or research conclusions, use primary current sources and state the retrieval date. Separate:

- model capability;
- product capability;
- data and context supplied;
- prompt behavior;
- tool use;
- cost, privacy, and copyright constraints.
