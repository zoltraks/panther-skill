# Register Or Log

## Purpose

> **Scope:** Living project documents that track evolving information as entry
> tables - registers and logs.
>
> **Key items:** ID prefixes, status lifecycles, scoring definitions,
> append-only entries, one owner per entry.

## When To Use

Use for the PMBOK register and log family:

- risk register
- issue log
- stakeholder register
- assumption log
- change log
- backlog
- lessons learned register

A project change log tracks change requests and their decisions. It is a
different document from `types/changelog-file.md`, which records release
history.

**Templates:**

- `templates/en/register-log-template-en.md`
- `templates/pl/register-log-template-pl.md`

## Kinds

Each register kind has its own ID prefix and column set. The document's own
conventions always win on edit.

| Kind                     | ID prefix | Typical columns                                                                         |
|--------------------------|-----------|-----------------------------------------------------------------------------------------|
| Risk register            | R         | description, category, probability, impact, score, response, owner, status, review date |
| Issue log                | I         | description, priority, owner, raised date, due date, status                             |
| Stakeholder register     | S         | name, role, contact, interest, influence, current engagement, desired engagement        |
| Assumption log           | A         | assumption or constraint, type, validated by, validation date, status                   |
| Change log               | C         | description, submitted by, date, impact, decision, authority                            |
| Backlog                  | B         | item, priority, estimate, status                                                        |
| Lessons learned register | LL        | category, what happened, recommendation, owner                                          |

## Structure

1. H1 title - `# Risk Register`, `# Issue Log`, `# Rejestr ryzyk`, and the other
   register names.
2. Purpose - one paragraph stating what the register tracks.
3. Scoring definitions - probability and impact scale tables sit above the
   first register table in scored registers, agreed once per document.
4. The register table - one row per entry, the ID column first.
5. Notes - any project-specific conventions below the table.

## Deltas From The Language Baseline

- Registers are append-only. Close an entry by changing its status, never by
  deleting the row.
- IDs are stable and sequential. A deleted entry's number is never reused.
- The document's own column set and ID prefixes win on edit. Prefixes are
  per-document, not global - an `A-01` assumption and an `A-01` decision in
  another file do not collide.
- Risk statements use cause-and-effect form - "If X happens, then Y".
- Status lifecycles follow the kind:
  - Risk - identified, assessed, response planned, closed.
  - Issue - open, in progress, resolved, closed.
  - Change - submitted, approved, rejected, deferred.
  - Assumption - open, validated, invalidated.
- Every entry carries exactly one owner.
- The table is the payload. Keep the prose minimal.
- One register per kind, in its own file - `docs/registers/risk-register.md`,
  `docs/registers/issue-log.md`, kebab-case names.

## Section Names

| English             | Polish               |
|---------------------|----------------------|
| Purpose             | Przeznaczenie        |
| Scoring Definitions | Definicje skali      |
| Probability         | Prawdopodobieństwo   |
| Impact              | Skutek               |
| Score               | Wynik                |
| Response Strategy   | Strategia reagowania |
| Owner               | Właściciel           |
| Status              | Stan                 |
| Review Date         | Data przeglądu       |
| Raised Date         | Data zgłoszenia      |
| Due Date            | Termin               |
| Resolution          | Rozwiązanie          |
| Priority            | Priorytet            |
| Description         | Opis                 |
| Category            | Kategoria            |
| Assumption          | Założenie            |
| Constraint          | Ograniczenie         |
| Validated By        | Zweryfikowane przez  |
| Submitted By        | Zgłoszone przez      |
| Decision            | Decyzja              |
| Authority           | Organ decyzyjny      |
| Recommendation      | Rekomendacja         |
