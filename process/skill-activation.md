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

A request that combines activation with a task is a task request - "use panther, write a
quick note" enters document mode directly and this procedure does not run.

When the request is ambiguous between bare activation and a task, ask - under JSON exchange the
question emits as the `mode-selection` `choice` parameter per `process/json-exchange.md`.

## Procedure

1. Run the once-per-session Skill Update Check from `SKILL.md` - the gate applies in
   every mode.
2. Confirm the router state - the loaded `SKILL.md` is the enabled state, re-read it when
   it may have changed during the session.
3. Answer with the enablement response below, then wait for the next request.

## Enablement Response

Open with one sentence confirming the skill is enabled for editorial support.

Follow with a compact capability list - one short item per family: create, edit,
reformat, translate, audit, describe, layout discovery, and skill maintenance.

Keep the response compact - an opening sentence, one list, and a closing line inviting
the task request.

Write the response in the language of the request.

## What Does Not Apply

- No task classification, parameter resolution, scope detection, or encoding detection
  runs - the request named no task.
- No rule files load beyond the router and this file - progressive disclosure stays lazy,
  the next request selects its own rule set.
- No file is written.

## Relation To The Modes

Enable mode is the standby state - it precedes document mode and maintenance mode.

A task-bearing request that follows enters document mode or maintenance mode per the mode
rules in `SKILL.md`, without repeating the update check this session.
