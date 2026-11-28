# Skill Activation

## Purpose

Bare-activation standby procedure: a request that names Panther but no work.

## When This Applies

A phrase naming Panther ("use panther", "work on panther-skill") binds directly.

A generic phrase ("use skill", "use this skill")
binds only when context identifies Panther as the skill in play - otherwise ask which skill is meant
through the host's question tool and wait.

A request that also names a task is a task request and skips this procedure.

A named target, purpose qualifier, or mode without an operation stays here as standby,
never a mode-selection question.

## Procedure

On a bare `use`, follow `process/skill-update.md` when the request names `improvement`,
`development`, or `training`, or makes an explicit update request.
A request naming no mode uses the installed package.
Reuse this session's result for the checkout when available.
Continue with the installed package when the check cannot run.

1. Treat the loaded `SKILL.md` as the enabled state.
2. Print the enablement response in the request's language.
3. Ask any pending question through the host's question tool, then wait for the task.
   A JSON request for that question follows `process/json-exchange.md`.

## Enablement Response

One sentence confirms editorial support and names the version from `metadata.version`,
folding in a named mode ("enabled in timing mode").

One sentence describes the skill: plain-text-readable Markdown in English, Polish,
German, French, or Spanish.

| Operation | What it covers                                          |
|-----------|---------------------------------------------------------|
| Create    | New documents of every supported type                   |
| Edit      | Convention-preserving edits                             |
| Reformat  | Table, prose, comment, and character passes             |
| Translate | Between the five languages, or revise a translation     |
| Correct   | In-place correction, fidelity proposals, humanizing     |
| Audit     | Document and translation conformance                    |
| Describe  | Inline descriptions, summaries, briefs, and supplements |
| Discover  | Layout census and scope classification                  |
| Maintain  | Changes and session reviews of this skill               |

Close with a pointer to `process/operation-catalog.md` for the full list and an
invitation to name the task.

A target-scoped activation answers with one or two standby lines and no table.

## What Does Not Apply

- No task classification, parameter resolution, encoding detection, or target scan runs.
- No rule file loads beyond the router, this file, and an armed mode's own file.
- No file is written.

## Relation To The Modes

Enable mode is the standby state before document mode and maintenance mode.
