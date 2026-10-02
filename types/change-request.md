# Change Request

## Purpose

> **Scope:** Conventions for formal change request documents - a single proposed change to
> scope, schedule, budget, or baseline submitted for approval
> **Key items:** request metadata, justification, impact assessment, approval block

A change request asks a decision maker to approve one change.

It is a form, not an argument - each field exists so the approver can decide without a meeting.

Typical shape: a request header, the description of the change, the reason, the impact on the
baselines, and an approval block.

## When To Use

Use for scope, schedule, budget, and baseline change requests in governed projects.

For design alternatives under review use `types/proposal-document.md` - a decision already
taken belongs in `types/decision-record.md`, and the log of many requests in
`types/register-log.md`.

**Templates**

- `templates/en/change-request-template-en.md`
- `templates/pl/change-request-template-pl.md`
- `templates/de/change-request-template-de.md`

## Structure

The canonical skeleton, adjusted to the request:

1. H1 title - `# Change Request: <short title>` or the request ID.
2. Document Information - request ID, requester, date, and state.
3. Summary - one paragraph stating the change a reader can act on alone.
4. Description - what exactly changes, the current state and the target state.
5. Justification - why the change is needed, with the driver or trigger.
6. Impact - the effect on scope, schedule, budget, quality, and risk, one line each.
7. Alternatives - other ways to get the outcome, including doing nothing.
8. Approval - the decision block: approver, decision, date, conditions.

## Deltas From The Language Baseline

- One change per request - split combined requests into separate documents linked by ID.
- The state moves through `submitted`, `approved`, `rejected`, `deferred` - record the state in
  Document Information, never rewrite a decided request's description.
- Mark unknown fields `TBD` or `NOT SPECIFIED` - never invent impact figures.
- The approval block is filled by the approver - write `Pending` until the decision lands.
- Placement - conventionally `docs/change-requests/` or the register directory the project
  declares.

## Section Names

| Section              | Requirement |
|----------------------|-------------|
| Document Information | required    |
| Summary              | required    |
| Description          | required    |
| Justification        | recommended |
| Impact               | recommended |
| Alternatives         | optional    |
| Approval             | required    |

Section names for other languages are declared in the matching `languages/<code>.md` file.
