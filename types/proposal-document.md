# Proposal Document

## Purpose

> **Scope:** Conventions for request-for-comments and design proposal documents - proposals
> circulated for review before implementation starts
> **Key items:** review status lifecycle, metadata header, alternatives considered, open
> questions, decision recorded on resolution

A proposal document argues for a change before any code is written.

It exists to collect feedback, surface trade-offs, and reach a decision - the implementation
follows a different document.

Typical shape: a metadata block, a summary readable on its own, background, the proposal,
alternatives, risks, open questions, and a decision section filled when the review concludes.

## When To Use

Use for RFCs, design proposals, feature proposals, and engineering briefs that precede
implementation.

Use `types/decision-record.md` instead when the decision is already made and only needs
recording.

Use `types/project-document.md` instead when the document is the durable specification the
implementation will follow.

**Templates**

- `templates/en/proposal-document-template-en.md`
- `templates/pl/proposal-document-template-pl.md`

## Structure

The canonical skeleton, adjusted to the request:

1. H1 title - `# RFC: Title` or `# Proposal: Title`.
2. Metadata block - a list directly below the H1 with Status, Author, Reviewers, Created, and
   Updated dates.
3. Summary - a short paragraph a stakeholder can read without the rest.
4. Background and Context - the history and the problem, with evidence.
5. Proposal - the detailed design, one H2 topic per component of the change.
6. Alternatives Considered - one H3 per alternative with the reason it was rejected.
7. Risks and Mitigations - what could go wrong and how the design answers it.
8. Open Questions - each phrased as a single question with an owner and a `TBD` marker.
9. Decision - the resolution and its rationale, marked `NOT SPECIFIED` until the review
   concludes.

## Status Lifecycle

A proposal moves through review states, recorded in the metadata block:

- `draft` - being written, not yet circulated.
- `in review` - circulated for feedback.
- `accepted` - approved, implementation may start.
- `rejected` - declined, with the reason recorded in the Decision section.
- `superseded` - replaced by a newer proposal, linked from the Decision section.

Accepted and rejected proposals are historical records - do not modify them substantially
afterward, record follow-up work in a `decision-record` or an implementation document instead.

## Deltas From The Language Baseline

- The metadata block is metadata, not prose - keep it as a short bulleted list, the
  sentence-per-paragraph rule does not apply to it.
- Mark every unresolved point in Open Questions with `TBD` and an owner, never invent an answer
  the review has not produced.
- Keep the Decision section `NOT SPECIFIED` until resolution - a proposal without a decision
  section is still valid while in review.
- Alternatives must state the rejection reason in one sentence, put the detailed comparison in
  the alternative's own subsection.
- Write the Summary last and place it first, a reader who cannot compress the proposal into one
  paragraph signals the scope is too wide.
- File naming follows the language baseline or the scope's convention, `docs/rfcs/` or
  `docs/proposals/` are conventional placement directories when the project defines one.

## Section Names

| English                 | Polish                   |
|-------------------------|--------------------------|
| Status                  | Stan                     |
| Summary                 | Podsumowanie             |
| Background              | Tło                      |
| Proposal                | Propozycja               |
| Alternatives Considered | Rozważane alternatywy    |
| Risks and Mitigations   | Ryzyka i środki zaradcze |
| Open Questions          | Otwarte pytania          |
| Decision                | Decyzja                  |
| Reviewers               | Recenzenci               |
