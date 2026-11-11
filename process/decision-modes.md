# Decision Modes

## Purpose

> **Scope:** The interaction-mode contract for every Panther operation - how question surfaces,
> gates, and gated actions resolve in each mode
> **Key items:** mode selection, the autonomous flag, resolution precedence, reporting
> flags, permission boundary

This file is the authoritative definition of the interaction modes named in `SKILL.md` and carried
by `process/skill-maintenance.md`, `process/session-review.md`, and `process/correct-document.md`.

Every procedure resolves its question surfaces through this matrix.

The session review keeps the shared two-flag review contract of `process/session-review.md` - the
`autonomous` and `verbose` semantics there and here are the same.

## Mode Selection

Classify the request first, then record the interaction mode once at intake and carry
it through the task.

- `autonomous`, `automatic`, `unattended`, `non-interactive`,
  or `fully autonomous` wording selects the autonomous mode.
  Panther keeps a single no-questions tier - `fully autonomous` resolves to the same `autonomous`
  mode, no stronger mode exists.
- `verbose`, `informational`, `diagnostic`,
  and `timing` are reporting flags that change what the task emits,
  never what it decides or is permitted to do,
  per `process/json-exchange.md` and `process/operation-timing.md`.
- Explicit parameter statements in the request outrank every detected or default resolution.
- A bare activation with no task stays informational standby in every mode - no question
  surfaces exist to resolve.

## The Matrix

| Mode                  | Question surfaces and gates                            | Missing inputs                 | Separately gated actions            |
|-----------------------|--------------------------------------------------------|--------------------------------|-------------------------------------|
| Interactive (default) | Ask at every surface per the governing procedure.      | Ask before dependent work.     | Seek the required permission.       |
| Autonomous            | Resolve to the recommended option, report each inline. | Ask only when no safe default. | Seek permission or skip and report. |

A gate is a point where the task cannot proceed without an answer - parameter resolution,
plan confirmation, apply confirmation - not every routine sub-step.

An interactive question is delivered through the host's own question mechanism - a dedicated ask
or question tool - whenever the host provides one.
A reply that ends by waiting on a choice carries a pending surface, and naming options in prose is
not asking them.
A question appends to the tail of the reply in prose where the host offers no question mechanism,
and may append under `verbose` where the explanation the mode adds belongs with the question.
Every appended question names its recommendation.
A question appended under `verbose` also states what the question decides and the consequences
each answer carries.

An interactive question lists at most four entries and ends with a cancel-class entry - `Cancel`,
`Pause`, `Skip`, `None`, `Break`, or `Stop` - which means no answer and pauses the operation for
the next user prompt.
Five or more candidates split the question into pages or a group question per
`process/document-workflow.md` - non-final pages end with `Next`,
the final page carries the cancel entry, and a page asks only after `Next` was selected.
A `Proceed` entry may replace the cancel entry,
accepting every recommendation and answering the current and remaining questions at once.
A canceled questionnaire resumes on `repeat` - the last question is re-asked and the task continues.
A `selection` answer mixing a no-answer entry with content entries warns and re-asks.

## Resolution Precedence

Resolve each surface in this order, and record which tier supplied the answer:

1. An explicit user choice or parameter statement.
2. The document's own detected conventions.
3. Evidence from detection - scope, encoding, layout, existing structure.
4. A documented Panther default.
5. Unresolved - ask, or record the surface `Cancel`-aborted.

Never manufacture a convention the document does not show,
and never normalize a document that carries its own.

## Autonomous Recording

Every autonomous resolution is reported inline with its surface name and the tier that supplied it,
the same record an answered question would leave.

The skill update check runs its gate normally - under an autonomous request its reported outcome is
applied per `SKILL.md` without a question surface.

## Reporting Flags

`verbose` adds the offered options and the rationale to every resolved surface and never changes a
selection or a gate.

`informational` arms the timing report alone,
while `diagnostic` and `timing` also emit the `process/json-exchange.md` parameter document for
every pending surface.

## Permission Boundary

No mode commits, pushes, or publishes, and no mode writes a file the request did not name.

An autonomous run reports partial coverage rather than claiming the surfaces it skipped.
