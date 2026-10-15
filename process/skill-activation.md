# Skill Activation

## Purpose

> **Scope:** Enablement procedure for requests that activate the skill without naming a
> task
> **Key items:** bare activation, session update check, enablement response, mode hand-off

This file defines the intake for a request that names the skill but no work.

Follow it when the request is a bare activation phrase - "use skill", "use panther", "run
panther", "use this skill", "activate the skill" - or an equivalent declared in the
`languages/` files.

## When This Applies

A bare activation names the skill and nothing else - no document to produce, edit,
reformat, translate, audit, or describe, and no maintenance request.

An activation may also name a working target - a repository, directory, or document
collection - while still naming no operation: "use panther on the docs repository",
"work on the project".

Naming a target is not a task, so the request stays in enable mode with the target held
as context for the next request.

A purpose qualifier such as "for editorial purposes" is not a task either - it names a
mode, not an operation, and the request stays in enable mode.

A request that combines activation with a task is a task request - "use panther, write a
quick note" enters document mode directly and this procedure does not run.

Ambiguity asks are rare - `mode-selection` fires only when the request mixes genuinely
conflicting signals, such as an activation phrase joined to an operation verb whose
object is missing.

A named target without a named operation resolves to standby, never to a mode-selection
question.

A target whose own agent-facing rules define bare-request behavior confirms the same
answer without any scan.

Under JSON exchange a genuine ambiguity emits as the `mode-selection` `choice`
parameter per `process/json-exchange.md`.

## Procedure

1. Run the once-per-session Skill Update Check from `SKILL.md` - the gate applies in
   every mode.
2. Confirm the router state - the loaded `SKILL.md` is the enabled state, re-read it when
   it may have changed during the session.
3. Answer with the enablement response below, then wait for the next request.

## Enablement Response

Open with one sentence confirming the skill is enabled for editorial support.

Follow with a compact capability list - one short item per family: create, edit,
reformat, translate, audit, describe, derive, layout discovery, and skill maintenance.

Keep the response compact - an opening sentence, one list, and a closing line inviting
the task request.

A target-scoped activation answers with a minimal standby instead: one or two lines
confirming the skill is enabled on the named target, then the wait begins - no
capability list.

The standby never scans or surveys the target to infer the intended task - guessing
intent from the repository's state is analysis the request did not ask for.

The reply confirms enablement and waits for the next request, or asks what to do.

A read-only survey with proposed work belongs in the reply only when the request names
that operation itself - "take a look around" asks for the survey, a purpose qualifier
does not.

A diagnostic flag folds into the opening sentence - "enabled in diagnostic mode" - and
adds no intake-state preamble, since a bare activation has no pending surface to report.

Write the response in the language of the request.

## What Does Not Apply

- No task classification, parameter resolution, scope detection, or encoding detection
  runs - the request named no task.
- No read or scan of the named target runs - a bare activation does not open the target
  to guess the task.
- No rule files load beyond the router and this file - progressive disclosure stays lazy,
  the next request selects its own rule set.
- A diagnostic or verbose flag adds `process/json-exchange.md` to the loaded set and
  nothing else - no scan of the target runs and no document-mode files load, and no
  parameter document emits while no question surface is pending.
- No file is written - a proposed change waits for a request that names the operation
  and confirms it.

## Relation To The Modes

Enable mode is the standby state - it precedes document mode and maintenance mode.

A task-bearing request that follows enters document mode or maintenance mode per the mode
rules in `SKILL.md`, without repeating the update check this session.
