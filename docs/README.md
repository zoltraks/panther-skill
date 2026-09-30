# Governance Documents

## Purpose

> **Scope:** Index of the repository-governance documents under `docs/`.
> **Key items:** style, maintenance, versioning, contributing, security.

These documents govern the Panther repository itself, not the documents the skill produces.

| File                               | Owns                                                                  |
|------------------------------------|-----------------------------------------------------------------------|
| [STYLE.md](STYLE.md)               | Prose, tables, headings, and encoding for the skill's own documents   |
| [MAINTENANCE.md](MAINTENANCE.md)   | Directory roles, file naming, registration, and validation procedures |
| [VERSIONING.md](VERSIONING.md)     | Version format, bump rules, and release anchoring                     |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Issue reporting, development setup, pull-request and AI policy        |
| [SECURITY.md](SECURITY.md)         | Vulnerability reporting path and the update-path trust boundary       |

`AGENTS.md` at the root is the agent-facing entry point and summarizes the same contract.

Root `docs/` holds repository governance only - it is unrelated to the `docs/` trees the
skill writes or audits inside subject repositories.
