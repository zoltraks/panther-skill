# Project Document

## Purpose

> **Scope:** Conventions for technical project documents - project specifications and solution
> designs that are the primary source of truth for implementation
> **Key items:** version comment, document navigation, glossary, goals, requirements tables,
> numbered chapters variant

A project document describes how a system should be built and how it should behave.

Typical titles: `Project Specification`, `Projekt rozwiązania`, `Specyfikacja Projektu`.

## When To Use

Use for project specifications, solution designs, and architecture documents that define a
system's structure, requirements, and conventions.

**Templates**

- `templates/en/project-document-template-en.md`
- `templates/pl/project-document-template-pl.md`

## Structure

The canonical skeleton, adjusted to the request:

1. H1 title - plain document title (`# Project Specification`, `# Specyfikacja Projektu`).
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

For long documents, add a `Document Navigation` (PL: `Nawigacja dokumentu`) section after the
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

Requirements may be grouped under H3 milestone headings (`Kamień milowy I: ...`,
`Milestone 1: ...`) instead of one flat table.

Use cases may get one H3 subsection each (`### C-01 Product synchronization`) with a bold
`**Mechanisms used:**` (PL: `**Wykorzystywane mechanizmy:**`) line listing the features it
exercises.

## Deltas From The Language Baseline

- Section numbering is optional. If used, number chapters and subsections (`1`, `1.1`) and keep
  the numbering continuous after any change. Both the numbered variant (`# 1 Podstawowe
  informacje`) and the unnumbered variant occur in real documents - follow the request or the
  existing convention.
- A metadata table with an empty header row may replace the version comment when the document
  uses the Polish project convention:

```markdown
|                |                          |
|----------------|--------------------------|
| Nazwa projektu | Data Integration Service |
| Wersja         | 1.0.7                    |
```

- The glossary table defines terms before first use, keep it early in the document.

## Section Names

| English               | Polish                    |
|-----------------------|---------------------------|
| Document Purpose      | Cel dokumentu             |
| Document Navigation   | Nawigacja dokumentu       |
| Glossary              | Słownik pojęć             |
| Abbreviations         | Skróty                    |
| Vision                | Wizja                     |
| Goals                 | Cele                      |
| Non-Goals             | Cele wykluczone           |
| Quality Requirements  | Wymagania jakościowe      |
| System Architecture   | Architektura systemu      |
| Component Diagram     | Diagram komponentów       |
| Functional Reqs       | Wymagania funkcjonalne    |
| Non-Functional Reqs   | Wymagania niefunkcjonalne |
| Use Cases             | Przypadki użycia          |
| Design Decisions      | Decyzje architektoniczne  |
| Implementation Phases | Fazy realizacji           |
| Testing Strategy      | Strategia testowania      |
| Naming Conventions    | Konwencje nazewnicze      |
| Version Control       | Kontrola wersji           |
| Documentation         | Dokumentacja              |
