# GitHub Contribution Agent

This is a human-approved scout for meaningful open-source contributions that fit MateehUllah's AI, backend, and data-engineering profile.

## Safety policy

The agent finds and ranks issues only. It does not create branches, push code, comment on issues, or open pull requests. Before any contribution:

1. Read the repository's `CONTRIBUTING.md` and code of conduct.
2. Confirm the issue is open, unassigned, and not already covered by a pull request.
3. Reproduce the problem.
4. Propose a short plan and get human approval.
5. Make a focused change with tests.
6. Run formatting, linting, type checks, and tests.
7. Review the complete diff.
8. Ask for final approval before pushing or opening a PR.

Avoid typo-only changes, generated README spam, duplicate work, inactive repositories, and changes made only to increase the contribution count.

## Run it

Requirements: Python 3.11+ and an authenticated [GitHub CLI](https://cli.github.com/).

```bash
python github-agent/agent.py
```

The shortlist is printed and saved to `github-agent-candidates.json`. Adjust search queries and scoring rules in `config.json`.

## Recommended next phase

After the scout proves reliable, add an analyzer that fetches the issue, comments, contribution guide, open PRs, test commands, and recent maintainer activity. Keep both PR creation and public comments behind explicit human approval.
