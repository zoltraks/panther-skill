# Contributing to Panther

Thank you for your interest in contributing to Panther.

This document explains how to report issues, set up the project, and submit changes.

## Ways To Contribute

- Report bugs and request features through the issue tracker.
- Improve documentation and rule files.
- Submit code changes through pull requests.

## Reporting Issues

Search the existing issues before opening a new one.

File one issue per problem.

Include the version, environment, reproducible steps, and the expected versus actual behavior.

Report security vulnerabilities through the private channel in [SECURITY.md](./SECURITY.md).

Do not file them in the public issue tracker.

## Development Setup

```bash
git clone git@github.com:zoltraks/panther-skill.git
cd panther-skill
python3 scripts/validate-skill.py .
python3 scripts/test-scripts.py
```

The skill has no dependencies beyond `python3` and `git` - everything else is documentation.

## Pull Requests

- Keep each pull request focused on a single change.
- Follow [STYLE.md](./STYLE.md) for document and prose conventions.
- Follow [MAINTENANCE.md](./MAINTENANCE.md) for naming, registration, and layout rules.
- Run `python3 scripts/test-scripts.py` before submitting - it covers all three validators.
- The project runs no CI by design, so this local gate is the only regression check.
- Bump the skill version only on request - `VERSIONING.md` reserves bumps for explicit asks.
- Review goes through the maintainer, with a second reviewer per `README.md`.
- Keep `work/` research scratch out of tracked content - replace copied examples with links
  instead.
- Never embed references to external example files, paths, or names supplied in a request -
  contribute anonymized skill-owned examples instead, per [MAINTENANCE.md](./MAINTENANCE.md).

## AI-Assisted Contributions

Disclose when a report or change was produced with AI assistance.

Record meaningful AI involvement in the pull request description or a commit trailer such as
`Co-Authored-By`, so provenance stays traceable.

Trailers are expected only when meaningful AI involvement occurred.

Verify every AI-generated finding yourself before reporting it.

Do not paste raw AI output into an issue or pull request.

You must understand and own the code you submit.

AI-assisted changes follow the same style, testing, and licensing rules as other contributions.

## License

By contributing, you agree that your contributions are licensed under the MIT License.

See [LICENSE](../LICENSE).
