# Contributing

Contributions should improve a reproducible teaching behavior rather than add more generic content.

Useful contributions include:

- a prompt that should or should not trigger the Skill;
- an example where a term was introduced without a prerequisite;
- a project-specific claim without evidence;
- a privacy or authorization failure;
- a misunderstanding-recovery case;
- a compatibility result with the host, version and raw prompt recorded.

Before opening a pull request:

1. Remove personal, company, customer and credential data.
2. Add or update the smallest relevant Eval case.
3. Run `python evals/validate_fixtures.py`.
4. Run the Skill and plugin validators described in `docs/INSTALL.md`.
5. Explain what behavior changed and what evidence supports it.

Do not submit full copyrighted course material or private conversation histories.
