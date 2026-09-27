# Describe Response

## Purpose

> **Scope:** Consolidated descriptions produced when a request asks to describe a subject
> **Key items:** collection and consolidation, impersonal compact style, shortly length
> caps, inline delivery

This file defines the describe procedure and the response style it produces.

Follow it whenever the request asks to describe, summarize, or give an overview of a
subject.

## When This Applies

The describe task activates on requests such as "describe", "describe shortly", "make a
description", "summarize", "write a summary", "give an overview", or "short
description", including their equivalents declared in the matching `languages/` file.

The subject is whatever the request points at - the current session's work, a document,
a repository, a directory, or a concept explained in context.

Classify the request as Describe only when it asks for a description itself.

A request that uses "describe" to shape another task stays that task - "create a
document describing the API" is a Create task, not a Describe task.

A description produced for an inline response is not a document - encoding detection,
scope detection, and parameter resolution do not run.

## Collecting Content

Gather the facts from the subject itself - the files read, the actions taken, and the
request's context.

Consolidate the material by theme instead of retelling it chronologically.

A description states what the subject is, names its key elements, and closes with the
outcome or verification status.

Never invent content to fill a gap - mark missing facts per
`principles/authoring-rules.md`.

## Length

A plain describe request consolidates at its natural length while staying compact.

A "shortly", "brief", or "quick" request caps the response at ten sentences in total.

A large subject under a shortly request extends the cap to twenty sentences - a large
subject carries more than a handful of distinct facts, for example a whole repository or
a multi-part session.

Count every sentence and every list item toward the cap.

A bare label line ending with a colon, such as `Key elements:`, does not count.

## Response Style

Write in an impersonal voice - the subject or the work is the actor, never "I".

Replace first-person phrasing such as "I created" or "I derived" with "session
delivered", "work produced", or a passive form.

Drop articles where the sentence stays grammatical - "session created" instead of "the
session created".

Write short sentences, one sentence per paragraph, with a blank line between them.

Join related clauses with a comma - do not use semicolons.

Use a spaced hyphen (` - `) where prose needs a dash, never an em-dash or en-dash.

Use straight ASCII quotes and apostrophes.

Do not use emoji.

Write file paths, commands, tool names, and values in inline code.

Use bold or italics sparingly - a bolded lead-in term on a list item is the common case.

## Lists

Use `-` bullets.

Start every item with a lowercase letter.

End items without a trailing period or comma.

Keep the lead-in name short - one to three words - followed by a ` - ` explanation when
the item needs one.

## Output

Deliver the description as an inline response.

Write a file only when the request explicitly asks for one - a requested file becomes a
document task: the language baseline, filename rules, encoding contract, and delivery
steps of `process/document-workflow.md` apply to it.

Write the response in the language of the request.

## Example

Correct - impersonal, compact, capped, lowercase unpunctuated items:

```
Session delivered an ASCII diagram convention for panther-skill.

Measured invariants:

- **shared axis** - one column carries every `┬`, `│`, and `▼`
- **content** - prose centered, enumerations left-aligned at one space
- **edges** - `│` then `▼` between boxes, `▶` across a branch gap

Convention registered in `conventions/ascii-diagrams.md` and wired into `SKILL.md`.

All validators pass.
```

Incorrect - first person, semicolons, em-dashes, punctuated capital items:

```
I created a new convention; it covers the diagram style — boxes,
arrows — and I registered it.

- Shared Axis - the column is shared.
- Content - prose is centered.
```
