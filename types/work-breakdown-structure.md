# Work Breakdown Structure

## Purpose

> **Scope:** Hierarchical decompositions of project scope - the WBS and its
> dictionary.
>
> **Key items:** Decimal-coded outline, work packages, WBS dictionary, 100
> percent rule, RACI matrix.

## When To Use

Use for work breakdown structures and their dictionaries, Polish `struktura
podziału pracy` (SPP). Product breakdown structures follow the same shape.

**Templates:**

- `templates/en/work-breakdown-structure-template-en.md`
- `templates/pl/work-breakdown-structure-template-pl.md`

## Structure

1. H1 title - `# Work Breakdown Structure` or the project name with WBS.
2. Purpose - what scope the structure decomposes.
3. Structure - the numbered outline with decimal codes:
   - level 1 is the project
   - level 2 carries phases or major deliverables
   - work packages sit at the lowest level
4. Work Packages - the rules the lowest level must satisfy: assignable to one
   owner, estimable, typically eight to eighty hours of effort.
5. WBS Dictionary - one H3 per work package carrying the code, name,
   description, acceptance criteria, owner, estimate, and dependencies.
6. RACI Matrix - an optional table mapping work packages to team members.
7. Baseline note - which version forms the scope baseline.

## Deltas From The Language Baseline

- Renumber codes continuously after adding, removing, or moving elements - the
  numbered-chapter rule applies.
- The 100 percent rule: the structure covers all project work and no element
  appears in two places.
- A new WBS uses a numbered outline list. On edit, preserve an existing
  fenced-block or table layout.
- Dictionary entries reference codes, not titles - codes survive renumbering,
  titles do not.
- The scope baseline - scope statement, WBS, and dictionary - is frozen once
  approved. Changes go through change control only.
- Placement - conventionally `docs/WBS.md`.

## Section Names

| English             | Polish              |
|---------------------|---------------------|
| Structure           | Struktura           |
| Work Packages       | Pakiety robocze     |
| WBS Dictionary      | Słownik SPP         |
| Acceptance Criteria | Kryteria akceptacji |
| Owner               | Właściciel          |
| Estimate            | Szacunek            |
| Dependencies        | Zależności          |
| RACI Matrix         | Macierz RACI        |
| Baseline            | Baza                |
