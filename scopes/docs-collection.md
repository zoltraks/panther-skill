# Documentation Collection Layout

## Purpose

> **Scope:** Document work inside a repository whose entire content is documents - a
> documentation project with no software underneath
> **Key items:** `docs/` as the payload, rule files versus content documents, `standard/` and
> `template/` directories, frozen `archive/` snapshots

A documentation collection is a repository where `docs/` is the product, not an appendix.

The repository hosts standards, templates, and reference documents intended for reuse across
other projects.

Load this file when the task works inside such a repository.

## Detection

A repository matches this scope when it contains all of the following:

- documents as the payload - little or no source code, no software project manifests
- a guidelines document, conventionally `docs/GUIDELINES.md`, that declares the repository a
  documentation project
- typically `docs/standard/`, `docs/template/`, or `docs/archive/` directories

When a software project is present alongside the `docs/` tree, use
`scopes/guided-project.md` instead.

## Rules Versus Content

The repository distinguishes governing files from content documents.

Only the entry `README.md` and the guidelines document contain rules for working in the
repository - read them first.

Every other file is content: it documents practices for other projects and does not govern this
repository.

Do not treat a content document's internal rules as repository conventions.

## Directory Roles

| Path                 | Role                                                             |
|----------------------|------------------------------------------------------------------|
| `README.md`          | Entry point, points to the guidelines document                   |
| `docs/GUIDELINES.md` | Source of truth for working in the repository                    |
| `docs/<NAME>.md`     | UPPERCASE documents - style rules, preparation notes, benchmarks |
| `docs/standard/`     | Per-stack engineering standards, `<stack>-development.md`        |
| `docs/template/`     | Document skeletons for reuse in other projects                   |
| `docs/reference/`    | Domain or format reference material                              |
| `docs/archive/`      | Frozen snapshots of earlier document versions - never edit       |

## Working Rules

New standards go to `docs/standard/` named `<stack>-development.md` in kebab-case.

New templates go to `docs/template/` using the conventional document name they skeleton, for
example `CHANGELOG.md` or `REFACTORING.md`.

Archived documents are frozen - an archive entry keeps a versioned name such as
`PREPARATION-1.2.md`, and language variants carry a suffix such as `-PL`.

Content documents follow the repository's own style documents when it defines them, for example
`STYLE.md` and `TABLE.md` for prose and table formatting.

## Document Types In This Scope

| File or directory                             | Type or handling                                 |
|-----------------------------------------------|--------------------------------------------------|
| `docs/standard/` documents                    | `rules-document` type - imperative standards     |
| `docs/adr/` records                           | `decision-record` type - numbered decisions      |
| `docs/rfcs/`, `docs/proposals/` docs          | `proposal-document` type                         |
| `docs/registers/` docs                        | `register-log` type - living entry tables        |
| `docs/reports/` docs                          | `status-report` type - periodic health reports   |
| `docs/minutes/` docs                          | `meeting-minutes` type - dated meeting records   |
| `docs/template/` documents                    | Payload skeletons - keep placeholder conventions |
| `docs/archive/` documents                     | Frozen snapshots - never edit                    |
| `STYLE.md`, `TABLE.md`                        | `rules-document` type                            |
| `PREPARATION.md`, `BENCHMARK.md`, `ALWAYS.md` | `technical-document` type                        |
| `README.md`                                   | `readme-file` type                               |
