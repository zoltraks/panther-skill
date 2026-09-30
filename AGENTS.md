# Agent Instructions

## Purpose

> **Scope:** Agent-facing entry point for authoring and maintaining this skill repository.
> **Key items:** governing documents, boundaries, local workspace, validation, improvement.

This repository is the Panther skill, an Agent Skills package for authoring and editing
plain-text-readable Markdown documents in English, Polish, or German.

`SKILL.md` is the runtime router read by agents that use the skill.

This file is the entry point for agents that modify the skill.

## Governing Documents

| Document               | Owns                                                                |
|------------------------|---------------------------------------------------------------------|
| `docs/CONTRIBUTING.md` | Issue reporting, development setup, pull-request and AI policy      |
| `docs/STYLE.md`        | Prose, tables, headings, and encoding for the skill's own documents |
| `docs/MAINTENANCE.md`  | Directory roles, file naming, registration, validation procedures   |
| `docs/VERSIONING.md`   | Version format, bump rules, and release anchoring                   |
| `docs/SECURITY.md`     | Vulnerability reporting path and the update-path trust boundary     |
| `docs/README.md`       | Index of the repository-governance documents under `docs/`          |

Keep each rule in its owning document and link to it instead of duplicating it.

## Boundaries

- The skill is a routed instruction set: Markdown content becomes agent instructions, so
  content integrity issues are security issues - follow `docs/SECURITY.md` for them.
- Maintenance-mode work on this repository follows `process/skill-maintenance.md` - the
  document-production machinery in `process/document-workflow.md` does not apply to the
  skill's own files.
- Keep `SKILL.md` lean: it routes to resources and must stay below 500 lines.
- Register every new or renamed resource in `SKILL.md` and mirror it in the `README.md`
  tree, per `docs/MAINTENANCE.md`.
- Follow `docs/STYLE.md` for every shipped file: H1 plus Purpose, one sentence per
  paragraph, prose wrapped at 100 characters, tables aligned by source width.
- Never embed example files, paths, or project names supplied with a request - create
  anonymized skill-owned examples instead, per `docs/MAINTENANCE.md`.
- Keep `evals/evals.json` in sync when a change alters skill behavior.
- Never bump `metadata.version` as a side effect of a change - the skill version moves only
  on an explicit request, per `docs/VERSIONING.md`.
- Do not claim validation that did not run.
- Never commit automatically.

## Local Workspace

Research scratch and other local working artifacts live in the gitignored `work/` directory.

Shipped skill files never depend on workspace content - document-production tools are copied
into the working repository under a `.tmp.` infix and removed after use, per `scripts/README.md`.

## Validation

Run the skill-maintenance suite from `docs/MAINTENANCE.md` after structural changes:

```
python scripts/validate-skill.py .
python scripts/check-references.py .
python scripts/check-contents.py .
python scripts/test-scripts.py
git diff --check
```

Run `python scripts/validate-document.py <file>` and the style self-audit checkers listed in
`docs/MAINTENANCE.md` on every edited rule document, and `python scripts/format-table.py <file>`
on every file whose tables were touched.

Changes that alter skill behavior also exercise the regression prompts in `evals/evals.json`.

## Skill Improvement

Structural, naming, registration, or layout changes follow the procedures in
`docs/MAINTENANCE.md` and the intake procedure in `process/skill-maintenance.md`.
