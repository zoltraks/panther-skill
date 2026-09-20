# Decision Record

## Purpose

> **Scope:** Conventions for architecture decision records - short documents that capture a
> single design decision, its context, and its consequences
> **Key items:** status lifecycle, numbered file naming, immutable once accepted, supersede
> chain

A decision record explains why one architectural choice was made and what it implies.

Code shows what was built, the record explains why it was built that way.

Typical shape: a numbered file with a status block, a context statement, the options considered,
the chosen outcome, and its consequences - following the MADR convention.

## When To Use

Use for architecture decision records, technology selection records, and any single-decision
document future maintainers will consult.

Do not use for implementation plans or design proposals that cover several decisions - use
`types/proposal-document.md` for those.

Meeting decisions belong in `types/meeting-minutes.md`, and scope or budget change requests
belong in the change log per `types/register-log.md`.

**Templates**

- `templates/en/decision-record-template-en.md`
- `templates/pl/decision-record-template-pl.md`

## Structure

The canonical skeleton, adjusted to the request:

1. H1 title - `# ADR-NNNN: Short Title` naming the solved problem and the solution.
2. Status block - a metadata list directly below the H1 with Status, Date, and Deciders.
3. Context and Problem Statement - the forces that motivate the decision.
4. Decision Drivers - the concerns that matter for choosing, one bullet each.
5. Considered Options - the candidate solutions, one bullet each.
6. Decision Outcome - the chosen option and the justification.
7. Consequences - positive and negative effects, one bullet each.
8. Pros and Cons of the Options - one H3 per option, optional.
9. Links - related records, tickets, and references.

## Status Lifecycle

A record moves through a small set of states, recorded in the Status block:

- `proposed` - drafted, not yet binding.
- `accepted` - the decision is in force.
- `rejected` - the option was considered and declined.
- `deprecated` - the decision still stands but is being phased out.
- `superseded by ADR-NNNN` - replaced by a newer record.

Accepted records are immutable except for two edits: fixing an error, and changing the Status
line to `deprecated` or `superseded by ADR-NNNN`.

To change a decision, write a new record with the next free number, link it in the old record's
Status line, and leave the old body untouched.

## Numbering And Placement

Records live in a dedicated directory, conventionally `docs/adr/`.

Filenames follow `NNNN-kebab-case-title.md`, for example `0007-use-postgres-queue.md`.

`NNNN` is a consecutive four-digit number - take the next free number, never reuse the number of
a deleted record, and never renumber existing records.

The numbering convention comes from the type, the detected scope may relocate the directory or
adjust the naming - the scope wins for placement.

## Deltas From The Language Baseline

- One decision per record - split multi-part decisions into chained records linked through the
  Links section.
- The status block is metadata, not prose - keep it as a short bulleted list, the
  sentence-per-paragraph rule does not apply to it.
- Keep the Decision Outcome to a small number of sentences, put the option analysis in the Pros
  and Cons section instead.
- Write the justification so a reader who was not present can evaluate the trade-off, name the
  drivers the chosen option satisfies.
- Prefer `TBD` in the status block over inventing a date or a decider the request did not
  provide.

## Section Names

| English                  | Polish                 |
|--------------------------|------------------------|
| Status                   | Stan                   |
| Context                  | Kontekst               |
| Decision Drivers         | Czynniki decyzyjne     |
| Considered Options       | Rozważane opcje        |
| Decision Outcome         | Wynik decyzji          |
| Consequences             | Konsekwencje           |
| Positive Consequences    | Konsekwencje pozytywne |
| Negative Consequences    | Konsekwencje negatywne |
| Pros and Cons of Options | Zalety i wady opcji    |
| Links                    | Linki                  |
| Supersedes               | Zastępuje              |
