# Guided Project Layout

## Purpose

> **Scope:** Document work inside a software project whose `docs/` tree is governed by an
> explicit guidelines document
> **Key items:** README entry point, `docs/GUIDELINES.md` source of truth, UPPERCASE document
> set, versioned artifact directories, agent read boundaries

A guided project is a software repository that carries a governed documentation tree.

A root `README.md` serves as the entry point and delegates project rules to a guidelines file,
conventionally `docs/GUIDELINES.md`.

Load this file when the task creates or edits documents inside such a project.

## Detection

A repository matches this scope when it contains all of the following:

- a software project - source directories, build manifests such as `Cargo.toml`, `*.sln`, or
  `package.json`
- a guidelines document, conventionally `docs/GUIDELINES.md`, named as the source of truth
- a root `README.md` that points to the guidelines for project rules

Secondary signals: a set of UPPERCASE conventional documents in `docs/` such as `ALWAYS.md`,
`COPYRIGHTS.md`, `CONCEPT.md`, `SPECIFICATION.md`, `VERSIONING.md`, `REFACTORING.md`, and
versioned artifact directories such as `docs/feature/`, `docs/change/`, `docs/plan/`,
`docs/refactoring/`, or `docs/report/`.

When `docs/GUIDELINES.md` exists but no software project does, check `scopes/docs-collection.md`
instead.

## Sources Of Truth

The project defines its own rule hierarchy - read the guidelines document before writing.

Typical chain: `README.md` points to `docs/GUIDELINES.md`, which names the authoritative
specification and mandatory reads such as `COPYRIGHTS.md` or a pre-work checklist in
`ALWAYS.md`.

Project rules outrank the skill's defaults for that repository - a guidelines document may set
its own changelog format, section conventions, or filename rules.

## Directory Roles

| Path                          | Role                                                     |
|-------------------------------|----------------------------------------------------------|
| `README.md`                   | Entry point and project overview                         |
| `CHANGELOG.md`, `LICENSE.md`  | Conventional root files                                  |
| `docs/<NAME>.md`              | UPPERCASE project documents - rules, specs, plans        |
| `docs/feature/<version>/`     | Feature specifications grouped by release version        |
| `docs/change/<version>/`      | Change descriptions grouped by release version           |
| `docs/plan/<version>/`        | Implementation plans grouped by release version          |
| `docs/refactoring/<version>/` | Refactoring assessments and proposals by version         |
| `docs/report/<date>/`         | Status reports grouped by date                           |
| `docs/standard/`              | Reusable per-stack engineering standards                 |
| `docs/template/`              | Document skeletons for the project's recurring artifacts |
| `docs/reference/`             | External format or domain reference material             |
| `docs/archive/`               | Frozen document snapshots - never edit                   |
| `work/`                       | Temporary files, ignored by version control              |

The exact directory set varies per project - the guidelines document is authoritative.

Projects may also carry payload collections outside `docs/`, for example a knowledge base under
`example/data/` - those follow their own conventions, not this scope's.

## Working Rules

Read only what the task needs.

Guided projects often restrict agent exploration - do not read files under versioned artifact
directories such as `docs/feature/`, `docs/plan/`, `docs/refactoring/`, or `docs/report/`
unless the task or the guidelines explicitly call for them.

Place temporary scripts in the project's `work/` directory when it declares one.

Many projects require documentation updates to precede implementation - check the guidelines
when a task mixes code and documents.

Documents carrying a version comment such as `<!-- Version: X.Y | Date: ... -->` have it
updated on every change, per the project's own versioning rules.

Never bump version numbers unless the request explicitly asks for it.

## Naming

UPPERCASE conventional names are used for the governed document set in `docs/`:
`GUIDELINES.md`, `SPECIFICATION.md`, `ARCHITECTURE.md`, `TESTING.md`, `DEPLOYMENT.md`,
`WORKFLOW.md`, `REFERENCES.md`, `COPYRIGHTS.md`, `CONCEPT.md`, `PREPARATION.md`, `PLAN.md`,
`BENCHMARK.md`, `IGNORE.md`.

Versioned artifact files use lowercase kebab-case inside the version directory, for example
`docs/feature/0.1.8/knowledge-library.md`.

Implementation plans carry the `-implementation` suffix, for example
`docs/plan/0.1.5/code-quality-issues-implementation.md` derived from `code-quality-issues.md`.

Refactoring artifacts come in `ASSESSMENT` and `PROPOSAL` pairs per version.

These conventions come from the scope - they override the `languages/` file default inside this
project.

## Document Types In This Scope

| File or directory                                                                                | Type or handling                                        |
|--------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| `GUIDELINES.md`, `ALWAYS.md`, `IGNORE.md`, `WORKFLOW.md`, `standard/`                            | `rules-document` type                                   |
| `CONCEPT.md`, `SPECIFICATION.md`, `ARCHITECTURE.md`, `PROJECT.md`, `TESTING.md`, `DEPLOYMENT.md` | `technical-document` or `project-document` type         |
| `docs/feature/`, `docs/change/` docs                                                             | `technical-document` type - feature and change speclets |
| `docs/plan/` docs                                                                                | `technical-document` type - implementation plans        |
| `docs/refactoring/` pairs                                                                        | `project-document` type - assessments and proposals     |
| `docs/report/` status files                                                                      | `quick-note` or `technical-document` type               |
| `docs/template/` skeletons                                                                       | Payload artifacts - keep placeholder conventions        |
| `docs/archive/`                                                                                  | Frozen snapshots - never edit                           |
| `CHANGELOG.md`                                                                                   | `changelog-file` type                                   |
| `COPYRIGHTS.md`, `LICENSE.md`                                                                    | Verbatim legal text - preserve, never restyle           |
| `README.md`                                                                                      | `readme-file` type                                      |
