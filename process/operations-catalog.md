# Operations Catalog

## Purpose

> **Scope:** Response contract for requests that ask for the skill's complete list of
> operations
> **Key items:** catalog triggers, canonical operations table, inline delivery, no caps

This file defines the answer produced when the request asks what operations the skill
performs or assists with.

Follow it when the request says "list all operations", "show all capabilities", "what
operations can this skill perform", "list everything this skill can do", or an
equivalent declared in the `languages/` files.

## When This Applies

The request names the skill and asks for the complete list of its operations.

A partial question - "can panther translate documents" - is not a catalog request.

Answer it directly instead of reproducing the table.

The catalog is a query surface, not a document task - no parameter resolution, scope
detection, or encoding detection runs.

When the catalog request is the session's first action, the once-per-session Skill
Update Check from `SKILL.md` runs first.

When it follows an activation or another task, the check is not repeated.

## The Catalog

Answer with the operations table below, reproduced inline and re-aligned to source
width when the request's language changes the cell text.

| Family    | Operation                | What it covers                                                                  |
|-----------|--------------------------|---------------------------------------------------------------------------------|
| Create    | technical document       | guides, architecture notes, API docs, reference material                        |
| Create    | project document         | specifications and solution designs                                             |
| Create    | rules document           | guidelines, standards, workflow rules                                           |
| Create    | agent instruction        | documents an AI agent executes                                                  |
| Create    | engineering standard     | coding standards by stack                                                       |
| Create    | format specification     | file format and protocol specifications                                         |
| Create    | article                  | prose, tutorials, course material                                               |
| Create    | quick note               | notes and drafts                                                                |
| Create    | message                  | announcements, memos, single-issue messages                                     |
| Create    | daily plan               | single-day planning documents                                                   |
| Create    | readme                   | repository READMEs: general, skill, application, library, cli, docs, collection |
| Create    | changelog                | version-grouped change records                                                  |
| Create    | contributing guide       | CONTRIBUTING.md contributor guides                                              |
| Create    | decision record          | architecture decision records with status lifecycle                             |
| Create    | proposal                 | RFCs and design proposals                                                       |
| Create    | project charter          | charters and project briefs                                                     |
| Create    | change request           | formal change requests to a governed baseline                                   |
| Create    | register or log          | risk, issue, stakeholder, assumption, change, backlog, lessons-learned          |
| Create    | status report            | periodic status, variance, and quality reports                                  |
| Create    | meeting minutes          | minutes and agendas                                                             |
| Create    | management plan          | management and subsidiary plans                                                 |
| Create    | work breakdown structure | WBS outlines and dictionaries                                                   |
| Edit      | document edit            | in-place edits honoring the document's own conventions                          |
| Edit      | section insertion        | sections added at canonical positions per type                                  |
| Revise    | translation revision     | minimal-diff corrections to an existing translation                             |
| Reformat  | table formatting         | source-width table alignment                                                    |
| Reformat  | comment alignment        | shared `#` comment column per plain-text block                                  |
| Reformat  | sentence splitting       | one sentence per logical line                                                   |
| Reformat  | prose reflow             | wrap, unwrap, and justify passes                                                |
| Reformat  | character normalization  | typographic characters to ASCII                                                 |
| Reformat  | safe replace             | word-boundary find and replace                                                  |
| Reformat  | dialect edits            | AsciiDoc and reStructuredText minimal edits                                     |
| Translate | english to polish        | en-pl direction rules and glossaries                                            |
| Translate | polish to english        | pl-en direction rules and glossaries                                            |
| Translate | english to german        | en-de direction rules and glossaries                                            |
| Translate | german to english        | de-en direction rules and glossaries                                            |
| Translate | polish to german         | pl-de direction rules and glossaries                                            |
| Translate | german to polish         | de-pl direction rules and glossaries                                            |
| Audit     | document audit           | findings with an optional fix plan                                              |
| Audit     | translation audit        | fidelity verdict against the source                                             |
| Audit     | polish lint              | calque and prose findings                                                       |
| Describe  | describe                 | consolidated inline descriptions, capped or floored                             |
| Derive    | summary or brief         | compression-tier documents derived from a source                                |
| Derive    | supplement               | documents continuing a parent's numbering                                       |
| Discover  | layout discovery         | document-layout census and scope classification                                 |
| Maintain  | skill adjustment         | changes to this skill repository                                                |
| Maintain  | session review           | session lessons harvested into the rule corpus                                  |
| Enable    | enablement               | bare-activation standby with version and operations table                       |
| Enable    | self-update check        | once-per-session upstream check                                                 |
| Enable    | operations catalog       | this table                                                                      |

## Response

Deliver the catalog inline.

Write the response in the language of the request - family and operation names render
in that language while the `Family` column keeps its canonical grouping.

Close with one line inviting a task request.

## What Does Not Apply

- No task classification or parameter resolution runs - the request named a query.
- No rule files beyond the router and this file load - the catalog table is canonical
  and is not rebuilt by rescanning the repository.
- The caps and floors of `process/describe-response.md` do not apply - the catalog is
  a table, not a consolidated description.
- No file is written and no target is surveyed.
