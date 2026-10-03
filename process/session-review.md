# Session Review

## Purpose

> **Scope:** Procedure for improving the skill from the current session's history
> **Key items:** session gather, findings, approval gate, rule-file application, validation

This file defines the improvement path of maintenance mode: the agent reviews what happened
in this conversation, extracts the lessons worth keeping, and lands them in the rule corpus.

Follow it when the user picks the session-review option of the maintenance menu, or when the
request explicitly asks to improve the skill from this session.

## Procedure

### Gather

Read the session's conversation history.

List what failed, surprised, or needed a workaround, and every assumption the session made -
validated or broken.

Verify real state before recording a lesson: re-check files, rerun commands, confirm the
reported behavior - no guessed findings.

### Findings

Map each durable lesson to the rule file or files it belongs in.

A lesson about produced documents goes to `languages/`, `types/`, `principles/`, or the
matching `conventions/` file.

A lesson about the workflow goes to `process/`, a lesson about a tool goes to
`scripts/README.md` or the tool itself.

Drop lessons already covered by existing rules - the findings list names gaps, not
repetitions.

The external-example anonymization rule from `docs/MAINTENANCE.md` applies: findings describe
the lesson with skill-owned examples, never with names or paths the session supplied.

### Approval

Report the findings and the proposed changes per rule file.

Ask for approval before editing - under JSON exchange the gate emits as the
`session-review-approval` `choice` parameter per `process/json-exchange.md`.

The gate offers `Apply` (recommended), `Adjust`, and `Cancel`.

`Adjust` accepts a free-text correction to the findings or the proposal and re-presents the
report.

### Apply

On approval, edit the named rule files per `docs/MAINTENANCE.md` and `docs/STYLE.md`.

Apply the registration contract when the change adds, removes, or renames a resource.

`SKILL.md`, the `README.md` directory tree, `## Contents` tables, and `evals/evals.json`
move together.

### Validate

Run the skill-maintenance suite from `docs/MAINTENANCE.md` after the edits and report every
check that ran, failed, or was skipped.

## What Does Not Apply

- No document-mode machinery runs - parameter resolution, scope detection, and the language
  baseline cascade do not apply to skill files.
- No separate findings log is kept - findings land directly in the rule files they correct.
- The session's concrete task output is not part of the review - the review extracts
  transferable rules, not a report of the work itself.

## Relation To Maintenance Mode

This file is a path inside maintenance mode, not a mode of its own.

The maintenance menu in `process/skill-maintenance.md` routes to it, and the governing set
read happens under that intake.
