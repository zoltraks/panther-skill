# Project Document

## Purpose

> **Scope:** Conventions for technical project documents - project specifications and solution
> designs that are the primary source of truth for implementation
> **Key items:** version comment, document navigation, glossary, goals, requirements tables,
> numbered chapters variant

A project document describes how a system should be built and how it should behave.

Typical titles: `Project Specification`.

## When To Use

Use for project specifications, solution designs, and architecture documents that define a
system's structure, requirements, and conventions.

**Templates**

- `templates/en/project-document-template-en.md`
- `templates/pl/project-document-template-pl.md`

## Structure

The canonical skeleton, adjusted to the request:

1. H1 title - plain document title (`# Project Specification`).
2. Version comment - an HTML comment line recording version, date, and author.
3. Document navigation - optional table mapping sections to contents for large documents.
4. Glossary and abbreviations - tables defining domain terms before they are used.
5. Vision, goals, non-goals.
6. Architecture and components.
7. Requirements - functional and non-functional, with identifiers.
8. Implementation phases, testing strategy, conventions.

### Version Comment

Place an HTML comment with document metadata directly below the H1:

```markdown
<!-- Version: 0.1.0 | Date: 2026-01-15 | Author: Name -->
```

Update the version and date on every content change.

### Document Navigation

For long documents, add a `Document Navigation` section after the
purpose or version block.

The table maps top-level sections to their contents so a reader can locate a component without
reading linearly.

Use a `→` prefix in the section column for subsection rows.

## Requirements And Decision Tables

Use identifier columns for requirements (`F-01`, `N-01`), decisions (`A-01`), and use cases
(`C-01`).

Keep one sentence per table cell, put the long explanation in prose below the table.

Define the priority legend (for example `Must Have`, `Should Have`, `Won't Have`) before the first
requirements table that uses it.

Requirements may be grouped under H3 milestone headings (`Milestone 1: ...`)
instead of one flat table.

Use cases may get one H3 subsection each (`### C-01 Product synchronization`) with a bold
`**Mechanisms used:**` line listing the features it
exercises.

## Deltas From The Language Baseline

- Section numbering is optional. If used, number chapters and subsections (`1`, `1.1`) and keep
  the numbering continuous after any change. Both the numbered variant (`# 1 Basic
  Information`) and the unnumbered variant occur in real documents - follow the request or the
  existing convention.
- A metadata table with an empty header row may replace the version comment when the document
  uses that convention - the Polish variant is declared in `languages/pl.md`.

- The glossary table defines terms before first use, keep it early in the document.

## PMBOK Artifact Mapping

When documenting a project with PMBOK 7, map its artifacts to the Panther types:

| PMBOK artifact                                 | Panther handling                                                |
|------------------------------------------------|-----------------------------------------------------------------|
| Business case, business need                   | `proposal-document` type - benefits and financial justification |
| Project charter, project brief                 | `project-charter` type                                          |
| Vision statement, roadmap                      | `project-document` type                                         |
| Requirements documentation, activity list      | `project-document` type - requirement tables                    |
| Team charter                                   | `rules-document` type                                           |
| Management plans                               | `management-plan` type                                          |
| Logs and registers                             | `register-log` type                                             |
| Status, variance, forecasting, quality reports | `status-report` type                                            |
| Meeting agendas and minutes                    | `meeting-minutes` type                                          |
| WBS and WBS dictionary                         | `work-breakdown-structure` type                                 |
| Baselines                                      | Frozen artifacts - change control only, never informally edited |
| Contracts, MOU, SLA                            | Verbatim legal text - preserve, never restyle                   |
| Visual data artifacts                          | Out of scope - generated visuals, not text documents            |

Boundary rule: architectural decisions go to `decision-record`, scope and budget changes go to
the change log per `register-log`, and meeting decisions go to `meeting-minutes`.

## Section Names

- Document Purpose
- Document Navigation
- Glossary
- Abbreviations
- Vision
- Goals
- Non-Goals
- Quality Requirements
- System Architecture
- Component Diagram
- Functional Reqs
- Non-Functional Reqs
- Use Cases
- Design Decisions
- Implementation Phases
- Testing Strategy
- Naming Conventions
- Version Control
- Documentation

Polish section names for this document type are declared in `languages/pl.md`.
