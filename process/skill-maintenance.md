# Skill Maintenance Mode

## Purpose

> **Scope:** Procedure for requests that target the panther-skill repository itself
> **Key items:** mode distinction, governing set, skipped document machinery, validation

This file defines the intake and execution rules for changes to the skill's own files.

Follow it when the request asks to adjust, extend, fix, or review the skill repository -
`SKILL.md`, the rule corpus, scripts, templates, evals, or the repository documents.

## Mode Distinction

Panther runs in three modes:

- **Enable mode** - the request activates the skill without naming a task. Follow
  `process/skill-activation.md`.
- **Document mode** - the request targets a document the skill produces or edits: a
  specification, README, register, translation, audit, or description. Follow the router in
  `SKILL.md` and `process/document-workflow.md`.
- **Maintenance mode** - the request targets this repository's own files. Follow this file.

A bare activation request has no target and takes enable mode.

For every other request the target decides the mode, not the trigger phrase.

"Work on panther-skill" phrasing signals the start of adjustment, extension, or fixing of the
skill's documents - expect the following requests in the same session to stay in this mode.

A request to extend another skill repository follows `scopes/agent-skill.md` through document
mode instead.

When the target is ambiguous, ask which mode applies - under JSON exchange the question emits as
the `mode-selection` `choice` parameter per `process/json-exchange.md`.

A request naming another repository or directory and no operation is not mode ambiguity - it is
enable mode scoped to that target per `process/skill-activation.md`.

The ask stays reserved for signals that genuinely conflict, such as a request that could read as
document work on a file or as a change to this repository.

## Intake Menu

Every "work on panther-skill" trigger opens the maintenance menu - an informational list of
the three directions this mode offers:

- **Document work** - use the skill to create or work on a document the user names.
  The request then leaves maintenance mode and follows `process/document-workflow.md`, the
  session update check already ran.
- **Adjust the skill** - the user describes a behavior change or new rules. Continue under
  this file: read the governing set in Intake, then apply the change.
- **Improve the skill from this session** - review the session's conversation, gather the
  lessons, and land them in the rule corpus. Follow `process/session-review.md`.

The list is informational - present it, then wait for the user's pick.

A task named in the same request counts as the selection: present the menu, then proceed
treating the named task as the chosen direction - document work goes to option 1, skill
changes to option 2.

Under JSON exchange the menu emits as the `maintenance-action` `choice` parameter per
`process/json-exchange.md`.

## Intake

1. Run the once-per-session Skill Update Check from `SKILL.md` - the same gate applies in
   every mode.
2. Read the governing set below in full before planning any edit.
3. Read in full every additional rule file the change touches or contradicts - the governing
   set defines the process, the corpus defines the content.
4. Inventory the consistency sets the change affects: the `SKILL.md` registry lines, the
   `README.md` directory tree, every `## Contents` table, the language-file activation
   phrases, and `evals/evals.json` (see `scopes/agent-skill.md` Consistency Sets).

## Governing Set

Read these files completely before starting maintenance work:

1. `SKILL.md` - the router: taxonomy, registrations, trigger phrases, update check.
2. `docs/MAINTENANCE.md` - directory roles, file naming, the registration contract, per-kind
   addition procedures, validation, encoding.
3. `docs/STYLE.md` - prose and formatting rules for the skill's own files.
4. `docs/VERSIONING.md` - the version field location and the bump-only-on-request policy.
5. `docs/CONTRIBUTING.md` - contribution rules, including AI-assisted contributions.
6. `docs/SECURITY.md` - the update-path trust boundary and accepted postures.
7. `README.md` - the human-facing overview and the directory tree that mirrors the layout.
8. `AGENTS.md` - the agent-facing entry point summarizing the same contract.
9. `scripts/README.md` - tool classes, commands, and limitations.

`work/` is untracked scratch and is never part of the governing set.

Later maintenance requests in the same session reuse this reading - re-read a file before
editing it when time passed or it may have changed, per the governed-document rule in
`process/document-workflow.md`.

## What Does Not Apply

Document-mode machinery is skipped for the skill's own files:

- No parameter-resolution questions - `docs/MAINTENANCE.md` and `docs/STYLE.md` already fix
  the answers.
- No `languages/` baseline, `types/` delta, or `templates/` skeleton - skill files follow
  `docs/STYLE.md`, which wraps prose at 100 characters instead of the produced-document
  baselines.
- No scope detection - the repository is the `agent-skill` scope by definition.
- No `.tmp.` tool copies - document-production tools run directly from `scripts/` here.

## Applicable Rules

The change follows `docs/MAINTENANCE.md`: directory roles, kebab-case naming, the registration
contract, the per-kind addition procedures, the external-example anonymization rule, and the
file-encoding rules.

Prose follows `docs/STYLE.md`.

Bump the skill version only on explicit request, per `docs/VERSIONING.md` - when the change
touched any skill document, propose the bump in the delivery report, naming the current
and next version.

## Validation

After the change, run the suite from `docs/MAINTENANCE.md`:

- `scripts/validate-skill.py`, `scripts/check-references.py`, `scripts/check-contents.py`.
- `scripts/format-table.py`, `scripts/align-comments.py`, `scripts/split-sentences.py`,
  `scripts/reflow-prose.py`, and `scripts/validate-document.py` on every touched file.
- `evals/evals.json` stays in sync with behavior changes.
- `git diff --check` before reporting.

The gate is manual - report every check that was skipped or failed.

## Relation To The Agent-Skill Scope

`scopes/agent-skill.md` is the generic contract for document work inside any skill
repository, loaded through document mode.

This file is the Panther-specific intake procedure.

When the request targets this repository, maintenance mode applies and takes precedence over
document-mode routing, whatever trigger phrase arrived.
