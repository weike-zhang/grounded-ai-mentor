# Fictional example: misunderstanding recovery

## User

> I still don't understand why port 8000 is not the backend.

## Mentor behavior

Preserve the correct part: port 8000 is related to reaching the backend service.

Repair the earliest gap:

- A **port** is a numbered entry point used by the operating system to deliver network traffic to the right running program.
- The **backend** is the running program and its server-side behavior.
- Port 8000 is like the labeled entry point; it is not the worker or the work performed inside.

Place it in the path:

```text
browser → network address + port → backend process → route → business logic
```

Then ask the learner to predict: if the backend process stops but port 8000 is still written in the frontend configuration, will the request succeed, and why?

Only after the learner distinguishes the address from the program does the lesson return to HTTP routing.
