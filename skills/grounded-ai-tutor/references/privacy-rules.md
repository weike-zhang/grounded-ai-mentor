# Learner-state privacy rules

## Default

Do not create persistent learner state unless the learner explicitly agrees. A useful conversation does not require a profile.

## Store only when useful

Eligible information is stable and useful to future teaching: preferred language, learning outcome, authorized project paths, demonstrated understanding, learning preferences, constraints the learner volunteered, and progress evidence.

Do not store passwords, API keys, tokens, contact details, government identifiers, exact addresses, financial accounts, health data, private customer data, or unrelated personal details.

## Separate certainty

- **Confirmed**: directly stated or demonstrated by the learner.
- **Shared inference**: a tentative interpretation shown to the learner.
- **Unknown**: information that matters but is not known.

Never promote an inference to a confirmed fact silently.

## Local storage

Use `.grounded-ai-tutor/learner-profile.md`. Add `.grounded-ai-tutor/` to the project ignore file before storing state. Avoid global profiles unless the user specifically asks for one and understands its scope.

## User control

On request:

- show the full stored profile;
- explain why each field is useful;
- correct or remove individual entries;
- export it to a user-selected local path;
- delete the state file and report what was removed.

Public examples must be fictional and clearly labeled.
