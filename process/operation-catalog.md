# Operations Catalog

## Purpose

> **Scope:** Response contract for requests that ask for the skill's complete list of operations
>
> **Key items:** catalog triggers, canonical operations table, inline delivery, no caps

This file defines the answer produced when the request asks what operations the skill
performs or assists with.

Follow it when the request says "list all operations", "show all capabilities",
"what operations can this skill perform", "list everything this skill can do",
or an equivalent declared in the `languages/` files.

## When This Applies

The request names the skill and asks for the complete list of its operations.

A partial question - "can panther translate documents" - is not a catalog request.

Answer it directly instead of reproducing the table.

The catalog is a query surface, not a document task - no parameter resolution, scope detection,
or encoding detection runs.

When it follows an activation or another task, the check is not repeated.

## The Catalog

Answer with the operations table below, reproduced inline and re-aligned to source width when the
request's language changes the cell text.

| Operation                | Family    | What it covers                                                                  |
|--------------------------|-----------|---------------------------------------------------------------------------------|
| technical document       | Create    | guides, architecture notes, API docs, reference material                        |
| project document         | Create    | specifications and solution designs                                             |
| rules document           | Create    | guidelines, standards, workflow rules                                           |
| agent instruction        | Create    | documents an AI agent executes                                                  |
| engineering standard     | Create    | coding standards by stack                                                       |
| format specification     | Create    | file format and protocol specifications                                         |
| article                  | Create    | prose, tutorials, course material                                               |
| quick note               | Create    | notes and drafts                                                                |
| message                  | Create    | announcements, memos, single-issue messages                                     |
| daily plan               | Create    | single-day planning documents                                                   |
| readme                   | Create    | repository READMEs: general, skill, application, library, cli, docs, collection |
| changelog                | Create    | version-grouped change records                                                  |
| contributing guide       | Create    | CONTRIBUTING.md contributor guides                                              |
| decision record          | Create    | architecture decision records with status lifecycle                             |
| proposal                 | Create    | RFCs and design proposals                                                       |
| project charter          | Create    | charters and project briefs                                                     |
| change request           | Create    | formal change requests to a governed baseline                                   |
| register or log          | Create    | risk, issue, stakeholder, assumption, change, backlog, lessons-learned          |
| status report            | Create    | periodic status, variance, and quality reports                                  |
| meeting minutes          | Create    | minutes and agendas                                                             |
| management plan          | Create    | management and subsidiary plans                                                 |
| work breakdown structure | Create    | WBS outlines and dictionaries                                                   |
| document edit            | Edit      | in-place edits honoring the document's own conventions                          |
| section insertion        | Edit      | sections added at canonical positions per type                                  |
| translation revision     | Revise    | minimal-diff corrections to an existing translation                             |
| document correction      | Correct   | in-place formatting, structure, grammar, style, and typo fixes                  |
| fidelity proposals       | Correct   | translation-fidelity findings proposed for approval, never applied              |
| voice rewrite            | Humanize  | fact-preserving revision so the document reads human-authored                   |
| scout decomposition      | Humanize  | parallel region drafts merged serially for large documents                      |
| table formatting         | Reformat  | source-width table alignment                                                    |
| comment alignment        | Reformat  | shared `#` comment column per plain-text block                                  |
| sentence splitting       | Reformat  | one sentence per logical line                                                   |
| prose reflow             | Reformat  | wrap, unwrap, and justify passes                                                |
| character normalization  | Reformat  | typographic characters to ASCII                                                 |
| safe replace             | Reformat  | word-boundary find and replace                                                  |
| dialect edits            | Reformat  | AsciiDoc and reStructuredText minimal edits                                     |
| yaml documents           | Edit      | `.yaml`/`.yml` files per `types/yaml-document.md`                               |
| english to polish        | Translate | en-pl direction rules and glossaries                                            |
| polish to english        | Translate | pl-en direction rules and glossaries                                            |
| english to german        | Translate | en-de direction rules and glossaries                                            |
| german to english        | Translate | de-en direction rules and glossaries                                            |
| polish to german         | Translate | pl-de direction rules and glossaries                                            |
| german to polish         | Translate | de-pl direction rules and glossaries                                            |
| english to french        | Translate | en-fr direction rules and glossaries                                            |
| french to english        | Translate | fr-en direction rules and glossaries                                            |
| english to spanish       | Translate | en-es direction rules and glossaries                                            |
| spanish to english       | Translate | es-en direction rules and glossaries                                            |
| document audit           | Audit     | findings with an optional fix plan                                              |
| translation audit        | Audit     | fidelity verdict against the source                                             |
| polish lint              | Audit     | calque and prose findings                                                       |
| describe                 | Describe  | consolidated inline descriptions, capped or floored                             |
| summary or brief         | Derive    | compression-tier documents derived from a source                                |
| supplement               | Derive    | documents continuing a parent's numbering                                       |
| layout discovery         | Discover  | document-layout census and scope classification                                 |
| skill adjustment         | Maintain  | changes to this skill repository                                                |
| session review           | Maintain  | session lessons harvested into the rule corpus                                  |
| enablement               | Enable    | bare-activation standby with version and operations table                       |
| self-update check        | Enable    | upstream check on working modes or explicit request                             |
| operations catalog       | Enable    | this table                                                                      |

## Response

Deliver the catalog inline.

Write the response in the language of the request - family and operation names render in that
language while the `Family` column keeps its canonical grouping.

Close with one line inviting a task request.

## What Does Not Apply

- No task classification or parameter resolution runs - the request named a query.
- No rule files beyond the router and this file load.
  The catalog table is canonical and is not rebuilt by rescanning the repository.
- The caps and floors of `process/describe-response.md` do not apply. The catalog is a table,
  not a consolidated description.
- No file is written and no target is surveyed.
