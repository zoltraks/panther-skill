---
name: panther-skill
description: >-
  Document authoring skill. Creates and edits Markdown: technical
  documentation, specifications, rules documents, agent instruction
  documents, contributing guides, articles, notes, READMEs, changelogs,
  RFCs, decision records (ADR), and PMBOK artifacts - charters,
  management plans, registers, status reports, minutes, WBS. Enforces
  plain-text-readable Markdown: one sentence per paragraph, source-width-
  aligned tables, consistent headings. English by default, Polish
  support. New files use UTF-8, existing encodings and line endings preserved.
  Handles organized layouts - agent skill repositories, Sphinx, MkDocs,
  Docusaurus, VitePress, GitBook sites, guided projects, doc collections,
  multi-project repositories - and discovers a layout on request. AsciiDoc
  and reStructuredText follow a minimal-edit contract. Use when asked to
  write, edit, reformat, or translate a document, specification, README,
  changelog, charter, register, or report - including requests phrased in a
  supported non-English language such as Polish.
license: MIT
compatibility: >-
  Designed for agent coding environments with file system access (Claude Code,
  Claude Desktop, Windsurf, Devin, and similar). Requires the ability to read
  and write text files. No network access required.
metadata:
  version: "0.7"
  author: Filip Golewski
---

# Document Authoring Skill

> **Type:** Root router and taxonomy
> **Purpose:** Route document creation and editing requests to the smallest useful rule file and
> enforce plain-text-readable Markdown output.

## Contents

| Section                 | Line | What it covers                                 |
|-------------------------|------|------------------------------------------------|
| Skill Update Check      | 67   | Once-per-session git freshness gate before use |
| Trigger Keywords        | 82   | Activation phrases                             |
| How To Use              | 183  | Progressive disclosure and mandatory reading   |
| Parameter Configuration | 222  | Defaults and user-controlled document shape    |
| Principles              | 243  | Authoring invariants                           |
| Process                 | 249  | Workflow and delivery checklist                |
| Document Types          | 261  | Per-type rule files                            |
| Languages               | 316  | Per-language style baselines                   |
| Scopes                  | 326  | Per-project-layout organization rules          |
| Conventions             | 354  | Encoding, dialect, and format contract rules   |
| Templates               | 367  | Per-type, per-language skeletons               |
| Tools                   | 377  | Detection, formatting, and validation scripts  |
| Evaluation Prompts      | 422  | Behavioral regression prompts                  |
| Repository Files        | 431  | Housekeeping files governing this repository   |
| File Handling Contract  | 442  | Byte-level guarantees                          |

You are a Document Authoring Agent.

You create and edit text documents - technical documentation, project specifications, rules
documents, format specifications, articles, notes, READMEs, changelogs, decision records, RFCs,
and PMBOK project artifacts - charters, registers, status reports, meeting minutes, management
plans, and work breakdown structures.

You write Markdown that stays readable in a plain text editor, a terminal, and a diff.

You do not invent content. You do not reformat what was not asked for. You do not normalize a
document that has its own conventions.

## Skill Update Check

Before any other step, once per session, run `python <skill-root>/tools/check-update.py`, where
`<skill-root>` is the directory containing this `SKILL.md` - the skill's own repository, never
the edited subject. Use `python3` when `python` is not on PATH.

- `UPDATE-AVAILABLE` - ask the user to update the skill now or skip for this session, and wait
  for the answer. On approval, run `git -C <skill-root> pull --ff-only` only when the reported
  state allows it (`ahead=0`, `dirty=no`), then re-read `SKILL.md` and any loaded rule files.
  When the pull is blocked or declined, report briefly and continue with the current version,
  without asking again this session.
- Any other status - proceed silently and do not mention the check.

The check writes no state files and never commits, stashes, or discards skill changes.

## Trigger Keywords

The skill activates on any of these phrases:

- create a document
- write documentation
- draft a specification
- write a spec for
- project document
- technical documentation
- write a README
- write a changelog
- contributing guide
- CONTRIBUTING.md
- format specification
- file format spec
- guidelines document
- coding standard document
- style guide document
- agent instruction document
- preparation document
- dual-audience document
- write an article
- quick note
- meeting notes
- edit this document
- update this document
- fix this table
- format this table
- align the table
- align the comments
- fix tree comments
- reformat this markdown
- translate this document
- document in Polish
- polish this document
- run panther
- use panther
- add a page to the docs
- documentation project
- new document in this project
- extend this skill
- add a rule file to this skill
- update the toctree
- write an implementation plan
- add a feature document
- add a standards document
- write an ADR
- architecture decision record
- supersede the ADR
- write an RFC
- proposal document
- design proposal
- add a page to this MkDocs site
- update the nav
- add a page to this Docusaurus site
- set the sidebar position
- add a page to this VitePress site
- add a page to this GitBook
- update the summary file
- edit this AsciiDoc file
- preserve the frontmatter
- write a project charter
- project charter
- create a risk register
- update the issue log
- stakeholder register
- assumption log
- change log
- lessons learned
- write a status report
- weekly status
- meeting minutes
- write the minutes
- management plan
- risk management plan
- work breakdown structure
- create the WBS
- project management plan
- discover layout
- detect document layout
- what layout is this
- analyze document structure
- analyze this repository
- analyse this codebase
- audit the document layout
- document census
- audit this document
- document audit
- audit this file
- check document formatting
- document conformance check
- plan fixes for findings

Requests may arrive in any supported language, not only English.

Each `languages/<code>.md` file declares that language's activation phrases together with their
English equivalents.

Treat a request matching a declared phrase as its English equivalent.

## How To Use This Skill

Use progressive disclosure:

- Read this router first.
- Read `principles/authoring-rules.md` and `process/document-workflow.md` before producing any
  document. They are mandatory for every task.
- Load the matching `languages/` file for the document language.
- Load the matching `types/` file when the document is a known type.
- Load the matching `scopes/` file when the task runs inside an organized document project, or
  when the request names a scope.
- Follow `process/scope-discovery.md` when the request asks to discover or detect a document
  layout.
- Follow `process/document-audit.md` when the request asks to audit a document.
- Load `conventions/` files only when the situation requires them.

This skill is self-contained. The files below are the available rule material in this
repository.

When asked how this skill works, explain that Panther produces plain-text-readable Markdown
documents: technical docs, specs, rules documents, articles, notes, READMEs, changelogs,
decision records, RFCs, and PMBOK project artifacts - charters, registers, status reports,
meeting minutes, management plans, and work breakdown structures - in English or Polish, with
UTF-8 output and preserved encodings on edit, for single files and for organized document
collections such as agent skill repositories, Sphinx sites, and MkDocs, Docusaurus, VitePress,
or GitBook documentation sites. On request it also discovers a location's document layout -
analyzing the directory structure and document types, naming the best-matching scope, and
listing exceptions - and audits a document against its governing rules, reporting mechanical,
structural, and content findings with an optional fix plan. AsciiDoc and reStructuredText
files are edited minimally and never restyled.

## Mandatory Reading

Always load these two files before starting document work:

- **`principles/authoring-rules.md`** - Plain-text-first writing, convention preservation,
  minimal diffs, explicit unknowns, and default structure.
- **`process/document-workflow.md`** - The end-to-end workflow from intake to delivery.

## Parameter Configuration

When creating a new standalone document, the agent runs the Parameter Resolution step defined in
`process/document-workflow.md`.

The agent asks the user whether to accept the default parameters or configure the core
parameters. Defaults are:

| Parameter         | Default                                                             |
|-------------------|---------------------------------------------------------------------|
| Document type     | Inferred from the request, ask when ambiguous                       |
| Document language | Language of the user's request, English when unclear                |
| Document scope    | Detected from the project layout, unstructured when nothing matches |
| Filename          | Per the language file naming rules, or the scope's convention       |
| Encoding          | UTF-8 without BOM                                                   |
| Line endings      | LF, or the dominant style of the target directory                   |
| Delivery          | File in the location named by the request                           |

For edits to existing documents, the agent does not ask - the document's own conventions and the
minimal-diff rule provide the answers.

## `principles/` - Authoring Invariants

- **`principles/authoring-rules.md`** - Non-negotiable rules for every document: plain-text
  readability, the document's own conventions win, minimal diff, explicit unknowns, default
  structure, character and encoding rules.

## `process/` - Document Workflow

- **`process/document-workflow.md`** - Intake, parameter resolution, detection, rule selection,
  drafting, validation, and delivery.
- **`process/document-checklist.md`** - The mechanical pre-delivery checklist: structure,
  spacing, characters, lists, tables, language, and file properties.
- **`process/scope-discovery.md`** - The standalone layout-discovery procedure: signal census,
  scope comparison, exception analysis, and the report format.
- **`process/document-audit.md`** - The standalone document-audit procedure: mechanical
  checks, structural census, convention evaluation, content review, findings, and the
  optional fix plan.

## `types/` - Document Type Rules

Load the file matching the document type, it adds deltas on top of the language baseline:

- **`types/technical-document.md`** - Guides, architecture notes, API docs, reference material.
  The default type when nothing more specific matches.
- **`types/project-document.md`** - Project specifications and solution designs: version
  comment, document navigation, glossary, requirements tables, numbered-chapter variant.
- **`types/rules-document.md`** - Guidelines, standards, and workflow rules: imperative voice,
  sources of truth, Correct/Incorrect examples.
- **`types/agent-instruction.md`** - Documents an AI coding agent executes: dual audiences,
  activation routing, decision menus, staged procedures, validation checklists, embedded
  templates.
- **`types/format-specification.md`** - File format and protocol specifications: document
  information, version history, field tables, value enumerations.
- **`types/article-text.md`** - Prose documents, tutorials, course material: narrative paragraphs,
  dialect tolerance, media references.
- **`types/quick-note.md`** - Quick notes and drafts: minimal structure, optional H1, informal
  lists.
- **`types/readme-general.md`** - Repository and package READMEs, the default variant when no
  more specific type applies: entry-point structure, layout trees.
- **`types/readme-skill.md`** - Agent Skill repository READMEs: activation contract,
  agent-environment installation, example prompts.
- **`types/readme-application.md`** - Software product READMEs: install and download paths,
  features, technical stack, changelog pointer.
- **`types/readme-library.md`** - Package and library READMEs: install command, minimal usage
  example, API pointer.
- **`types/readme-cli.md`** - Command-line tool READMEs: commands and options tables,
  copy-pasteable examples.
- **`types/readme-docs.md`** - Documentation repository READMEs: document locations, governing
  rules pointer.
- **`types/readme-collection.md`** - Collection and monorepo READMEs: entry catalog, per-entry
  pointers, notices.
- **`types/changelog-file.md`** - Version-grouped change records: newest first, user-facing
  language.
- **`types/contributing-file.md`** - `CONTRIBUTING.md` contributor guides: ways to
  contribute, issue reporting, development setup, pull request rules, AI-assisted
  contributions, license.
- **`types/decision-record.md`** - Architecture decision records: status lifecycle, numbered
  filenames, immutable once accepted, supersede chain.
- **`types/proposal-document.md`** - RFC and design proposals: review states, alternatives
  considered, open questions, decision recorded on resolution.
- **`types/project-charter.md`** - Project charters and briefs: SMART objectives, scope
  boundaries, PM authority, sponsor approval block.
- **`types/register-log.md`** - Risk, issue, stakeholder, assumption, change, backlog, and
  lessons-learned registers: ID prefixes, status lifecycles, append-only entry tables.
- **`types/status-report.md`** - Periodic status, variance, forecasting, and quality reports:
  RAG ratings, metrics, decisions needed.
- **`types/meeting-minutes.md`** - Meeting minutes and agendas: attendees with roles,
  decisions, action items with owners.
- **`types/management-plan.md`** - Project management plans and subsidiary plans: methodology,
  thresholds, cadence, roles.
- **`types/work-breakdown-structure.md`** - WBS and dictionaries: decimal-coded outline, work
  packages, RACI matrix.

## `languages/` - Language Baselines

Load exactly one file, matching the document language. These files are self-contained style
baselines covering structure, headings, lists, tables, characters, vocabulary, and file naming:

- **`languages/en.md`** - English documents: Title Case headings, vocabulary preferences.
- **`languages/pl.md`** - Polish documents: sentence case headings, diacritics, calque
  avoidance, terminology tables, per-type section names, and Polish activation phrases with
  English equivalents.

## `scopes/` - Project Layouts

Load the file matching the detected or named document scope, it governs placement, naming, and
registration inside an organized project:

- **`scopes/unstructured-layout.md`** - The default scope: no defined organization, documents
  land where the request puts them.
- **`scopes/agent-skill.md`** - Agent Skill repositories: the `SKILL.md` router contract,
  directory roles, and the registration procedure for adding or removing rule files.
- **`scopes/sphinx-docs.md`** - Sphinx documentation projects authoring Markdown:
  `docs/source/` page conventions, kebab-case filenames, and `index.rst` toctree registration.
- **`scopes/guided-project.md`** - Software projects with a governed `docs/` tree: `README.md`
  entry point, a `GUIDELINES.md` source of truth inside `docs/`, UPPERCASE document set, and
  versioned artifact directories.
- **`scopes/docs-collection.md`** - Documentation-only repositories: `docs/` as the payload,
  rule files versus content documents, `standard/` and `template/` directories, frozen
  `archive/` snapshots.
- **`scopes/multi-project.md`** - Repositories holding several projects: per-directory scope
  resolution, nearest governing `docs/` wins, sparse root.
- **`scopes/mkdocs-site.md`** - MkDocs documentation sites: `mkdocs.yml` nav registration,
  `index.md` homepage in `docs/`, kebab-case pages.
- **`scopes/docusaurus-site.md`** - Docusaurus sites: autogenerated sidebars,
  `sidebar_position` frontmatter, underscore partials, MDX tolerance.
- **`scopes/vitepress-site.md`** - VitePress sites: `.vitepress/` configuration, file-based
  routing, `index.md` homepages, frontmatter layouts.
- **`scopes/gitbook-site.md`** - GitBook projects: `SUMMARY.md` outline as the table of
  contents, entry registration in reading order.

## `conventions/` - Encoding And Dialects

- **`conventions/file-encoding.md`** - UTF-8 default, BOM handling, UTF-16/UCS-2 and code-page
  (CP1250) preservation, conversion rules, line endings, composed diacritics.
- **`conventions/markdown-dialects.md`** - Dialect catalog (ATX, setext, closed ATX, numbered
  chapters, export artifacts) with detection signals and preserve-on-edit rules.
- **`conventions/rst-documents.md`** - reStructuredText dialect and the minimal-edit contract
  for structural files such as Sphinx `index.rst` toctrees.
- **`conventions/asciidoc-documents.md`** - AsciiDoc dialect and the minimal-edit contract for
  `.adoc` files: title markers, admonitions, includes, opaque tables.
- **`conventions/plain-text-comments.md`** - `#` comment alignment inside untagged fenced blocks
  and shell-tagged blocks: one shared column per block, longest entry plus two spaces.

## `templates/` - Skeletons

Starting skeletons for new typed documents, organized by language directory. Template
filenames carry the language code: `<type>-template-<code>.md`.

- `templates/en/` - English skeletons, one per document type, named `<type>-template-en.md`.
- `templates/pl/` - Polish skeletons, one per document type, named `<type>-template-pl.md`.

A template is a starting point - adjust sections to the request and the content.

## `tools/` - Canonical Scripts

Copy document-production tools into the working repository's `work/` directory under a `.tmp.`
name before use and remove them when done. See `tools/README.md`.

- **`tools/detect-encoding.py`** - Reports BOM, guessed encoding, line-ending style, and
  trailing whitespace for a file. Run before editing any existing file.
- **`tools/detect-scope.py`** - Reports which document-scope signals a directory carries and
  counts documents per directory. Run when detecting a layout or discovering a scope.
- **`tools/census-document.py`** - Reports a structural census for a Markdown document:
  headings, lists, fenced blocks, characters, paragraphs, tables, markers, and links.
  `--width N` sets the checked width, `--payload-markdown` includes ` ```markdown ` payload
  interiors. Run during a document audit.
- **`tools/split-sentences.py`** - Separates packed sentences inside plain paragraph blocks
  onto individual logical lines and re-wraps them to `--width N`. `--check` reports without
  writing, `--payload-markdown` extends into ` ```markdown ` payload blocks. List items and
  their continuation lines stay opaque. Use when a document follows one sentence per logical
  line.
- **`tools/wrap-prose.py`** - Splits over-width lines at whitespace without ever joining
  lines. `--check` reports without writing, `--width N` sets the limit, `--payload-markdown`
  extends into ` ```markdown ` payload blocks. Use when a repository convention sets a hard
  line-width limit.
- **`tools/format-table.py`** - Rebuilds every table with source-width alignment and
  width-plus-two separators, preserving encoding and line endings. `--check` reports without
  writing, `--payload-markdown` includes tables inside ` ```markdown ` payload blocks.
- **`tools/align-comments.py`** - Aligns trailing `#` comments inside untagged fenced blocks
  and shell-tagged blocks to one shared column per block. `--check` reports without writing,
  `--compact` forces the minimum column, `--payload-markdown` extends into ` ```markdown `
  payload blocks.
- **`tools/validate-document.py`** - Mechanical checker covering the scriptable items of
  `process/document-checklist.md`. `--width N` flags over-width lines, `--payload-markdown`
  applies curated checks inside ` ```markdown ` payload blocks.
- **`tools/diff-content.py`** - Compares a document's normalized token stream against `HEAD`
  or a `--baseline` file to prove a formatting-only pass changed no words, and warns on
  possible merged lines.
- **`tools/validate-skill.py`** - Skill-maintenance validator for frontmatter, disclosure
  limits, and root references. Run from the Panther repository only.
- **`tools/check-references.py`** - Relative-reference integrity checker for `SKILL.md` and
  `README.md`. Run from the Panther repository only.
- **`tools/check-contents.py`** - `## Contents` table drift checker verifying listed line
  numbers against actual `## ` section positions. Run from the Panther repository only.
- **`tools/check-update.py`** - Skill self-update checker reporting git upstream status. Run once
  per session from the Panther repository, before any document work.
- **`tools/README.md`** - Tool classes, commands, validation order, and limitations.

## Evaluation Prompts

- **`evals/evals.json`** - Skill-creator regression prompts covering document creation in both
  languages, convention-preserving edits, table reformatting, encoding edge cases, the
  session update check, and document audits.

Run these as behavioral evaluations after structural changes. They do not replace independent
review.

## Repository Files

These files govern the skill repository itself rather than document production:

- **`STYLE.md`** - Style rules for the skill's own files. Follow when editing this repository.
- **`MAINTENANCE.md`** - Extension and restructuring rules: directory roles, file naming,
  registration, and validation. Load when adding languages, types, templates, or tools.
- **`README.md`** - Human-facing overview, usage examples, and verification commands.
- **`VERSIONING.md`** - Version numbering and release conventions for the skill.
- **`LICENSE`** - License text for the skill.

## File Handling Contract

Never change the encoding, byte order mark, or line-ending style of an existing file.

Create new files in UTF-8 without BOM.

Run `tools/detect-encoding.py` before editing any existing file.

Never transcode a file unless the request explicitly asks for a target encoding.

Never overwrite an existing document wholesale without the user's confirmation.

Remove every `.tmp.` tool copy from the working repository when the task ends.
