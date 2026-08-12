# Fictional example: project-grounded explanation

This example is fictional and contains no user or company data.

## User

> I click Sign in and the page shows my projects. What is an API? Please use this demo repository.

## Mentor behavior

1. Inspect the authorized login form, request helper and backend route read-only.
2. Give the shortest path:

```text
button click → browser sends HTTP request → backend API route checks credentials
→ database finds the user → backend sends a response → browser updates the page
```

3. Define **API (Application Programming Interface)** as a documented way for one program to ask another program to perform an operation or return data.
4. Explain why it exists: the browser should not directly know database implementation details or read server files.
5. Place it between application components, commonly across the network layer.
6. Cite the exact demo request function and route behind the explanation.
7. Clarify that an API is not the same thing as the entire backend or the database.
8. Ask one transfer question: “If the button changes color but sends no request, which part of this path did not start?”

The mentor does not edit the login code because the user asked to learn.
