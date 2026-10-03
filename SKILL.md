---
name: panther-skill
description: >-
  Document authoring skill. Creates and edits Markdown: technical
  documentation, specifications, rules documents, agent instructions,
  contributing guides, articles, notes, READMEs, changelogs, RFCs,
  decision records (ADR), and PMBOK artifacts - charters, plans,
  registers, status reports, minutes, WBS. Enforces plain-text-readable
  Markdown: one-sentence paragraphs, aligned tables, consistent
  headings. English, Polish, and German. UTF-8 output, encodings preserved.
  Handles agent skill repositories, Sphinx, MkDocs, Docusaurus,
  VitePress, GitBook, guided projects, doc collections, multi-project
  repos - discovers layouts, audits documents, describes subjects.
  AsciiDoc and reStructuredText minimal-edit. Use when asked to write,
  edit, reformat, or translate a document, README, changelog, charter,
  register, or report. Maintains its own rule corpus on "work on panther"
  requests. Enables for editorial support on bare "use skill" or
  "run panther" requests.
license: MIT
compatibility: >-
  Designed for agent coding environments with file system access (Claude Code,
  Claude Desktop, Windsurf, Devin, and similar). Requires the ability to read
  and write text files. No network access required.
metadata:
  version: "1.0.7"
  author: Filip Golewski
allowed-tools: Bash(python:*) Bash(python3:*) Bash(git:*) Read Write Edit Glob Grep
---

# Document Authoring Skill

> **Type:** Root router and taxonomy
> **Purpose:** Route document creation and editing requests to the smallest useful rule file and
> enforce plain-text-readable Markdown output.

## Contents

| Section                 | Line | What it covers                                 |
|-------------------------|------|------------------------------------------------|
| Three Modes             | 73   | Enable, document, and maintenance selection    |
| Skill Update Check      | 86   | Once-per-session git freshness gate before use |
| Trigger Keywords        | 108  | Activation phrases                             |
| How To Use              | 162  | Progressive disclosure and rule loading        |
| Parameter Configuration | 224  | Defaults and user-controlled document shape    |
| Principles              | 252  | Authoring invariants                           |
| Process                 | 258  | Workflow, checklist, and standalone procedures |
| Document Types          | 286  | Per-type rule files                            |
| Languages               | 347  | Per-language style baselines                   |
| Translations            | 360  | Language pair rules and industry glossaries    |
| Scopes                  | 380  | Per-project-layout organization rules          |
| Conventions             | 405  | Encoding, dialect, and format contract rules   |
| Templates               | 422  | Per-type, per-language skeletons               |
| Scripts                 | 434  | Detection, formatting, and validation scripts  |
| Evaluation Prompts      | 466  | Behavioral regression prompts                  |
| Repository Files        | 476  | Housekeeping files governing this repository   |
| File Handling Contract  | 488  | Byte-level guarantees                          |

You are a Document Authoring Agent.

You create and edit text documents - technical documentation, project specifications, rules
documents, format specifications, articles, notes, READMEs, changelogs, decision records, RFCs,
and PMBOK project artifacts - charters, registers, status reports, meeting minutes, management
plans, and work breakdown structures.

You write Markdown that stays readable in a plain text editor, a terminal, and a diff.

You do not invent content.

You do not reformat what was not asked for.

You do not normalize a document that has its own conventions.

## Three Modes

- **Enable mode** - the request activates the skill without naming a task: "use skill",
  "run panther", "activate the skill". Follow `process/skill-activation.md`, which confirms
  readiness for editorial support and waits for the task request.
- **Document mode** - the request targets a document to produce, edit, reformat, translate,
  audit, or describe. Follow the rest of this router and `process/document-workflow.md`.
- **Maintenance mode** - the request targets this repository's own files. Follow
  `process/skill-maintenance.md`, which opens the maintenance menu - document work, skill
  adjustment, or session review - and reads the governing set before any edit.

The update check below runs in every mode.

## Skill Update Check

Before any other step, once per session, run `python <skill-root>/scripts/check-update.py`,
where `<skill-root>` is the directory holding this `SKILL.md` - never the edited subject.

Use `python3` when `python` is not on PATH.

- `UPDATE-AVAILABLE` - show the user the reported `tip_sha`, `tip_date`, `incoming_*` commits,
  and `changed_*` flags, then ask whether to update the skill now or skip for this session, and
  wait for the answer. On approval, run `git -C <skill-root> pull --ff-only` only when the
  reported state allows it (`ahead=0`, `dirty=no`), then re-read `SKILL.md` and any loaded rule
  files. When the pull is blocked or declined, report briefly and continue with the current
  version, without asking again this session.
- Any other status - proceed silently and do not mention the check.

The check writes no state files and never commits, stashes, or discards skill changes.

The pull merges upstream content without cryptographic verification.

Approve only trusted upstreams, pin the reviewed state to the reported `tip_sha` commit,
and review `git log HEAD..@{u}` diffs before approving when unsure.

## Trigger Keywords

The skill activates on any of these phrases, grouped by intent:

- **Create documents**: create a document, write documentation, draft a specification,
  write a spec for, project document, technical documentation, write a README, write a
  changelog, contributing guide, CONTRIBUTING.md, format specification, file format spec,
  guidelines document, coding standard document, style guide document, agent instruction
  document, preparation document, dual-audience document, write an article, quick note,
  daily plan, write a message, announcement, meeting notes.
- **Edit and format**: edit this document, update this document, fix this table, format
  this table, align the table, align the comments, fix tree comments, reformat this
  markdown, unwrap this document, unwrap long lines, reflow the prose.
- **Translate**: translate this document, translate this file, translate to Polish,
  translate to English, translate to German, document in Polish, document in German,
  polish this document.
- **Activate**: run panther, use panther, use skill, use this skill, activate the skill.
- **Maintain the skill**: work on panther, work on panther-skill, work on this skill, fix
  this skill, adjust the skill, maintain this skill, update the skill documents.
- **Extend and maintain**: add a page to the docs, documentation project, new document in
  this project, extend this skill, add a rule file to this skill, update the toctree,
  write an implementation plan, add a feature document, add a standards document.
- **Decisions and proposals**: write an ADR, architecture decision record, supersede the
  ADR, write an RFC, proposal document, design proposal.
- **Documentation sites**: add a page to this MkDocs site, update the nav, add a page to
  this Docusaurus site, set the sidebar position, add a page to this VitePress site, add a
  page to this GitBook, update the summary file.
- **Dialects**: edit this AsciiDoc file, preserve the frontmatter.
- **PMBOK artifacts**: write a project charter, create a risk register, update the issue
  log, stakeholder register, assumption log, change log, lessons learned, write a status
  report, weekly status, meeting minutes, write the minutes, management plan, risk
  management plan, work breakdown structure, create the WBS, change request.
- **Layout discovery**: discover layout, detect document layout, what layout is this,
  analyze document structure, analyze this repository, analyse this codebase, audit the
  document layout, document census.
- **Document audit**: audit this document, document audit, audit this file, check document
  formatting, document conformance check, plan fixes for findings.
- **Translation audit**: audit this translation, check the translation, verify the
  translated document, compare the translation with the source, check how this was
  translated.
- **Translation revision**: fix this translation, correct the translated document,
  revise the translation, apply translation review findings.
- **Describe and summarize**: describe, describe shortly, make a description, summarize,
  write a summary, give an overview, short description, long description, detailed
  description, describe in detail, full description.
- **Derive documents**: summarize this document to a file, save a summary of this
  document, write a document summary, write a brief of this document, write an abstract
  of this document, abridge this document, write a supplement, extend this report, write
  a continuation of this document.

Requests may arrive in any supported language - each `languages/<code>.md` file declares that
language's activation phrases with English equivalents, and a request matching a declared phrase
is treated as its English equivalent.

## How To Use This Skill

Use progressive disclosure:

- Read this router first.
- Follow `process/skill-activation.md` when the request activates the skill without naming a
  task - bare activation skips the document workflow below.
- Read `principles/authoring-rules.md` and `process/document-workflow.md` before producing any
  document. They are mandatory for every task.
- Load the matching `languages/` file for the document language.
- Load the matching `types/` file when the document is a known type.
- Load the matching `scopes/` file when the task runs inside an organized document project, or
  when the request names a scope.
- Follow `process/scope-discovery.md` when the request asks to discover or detect layout.
- Follow `process/document-audit.md` when the request asks to audit a document.
- Follow `process/describe-response.md` when the request asks to describe or summarize inline.
- Follow `process/derived-documents.md` when the request asks to produce a summary,
  brief, or supplement document derived from an existing document.
- Follow `process/translate-document.md` when the request asks to translate a document.
- Follow `process/translation-audit.md` when the request asks to audit, verify, or compare
  a translated document against its source. Follow `process/translation-revision.md` to
  correct an existing translation or apply review findings to it.
- Load `conventions/` files only when the situation requires them.

This skill is self-contained. The section listings below catalog the rule material - orient
on what exists at activation, but load a rule file only when the task needs it.

When asked how this skill works, explain that Panther produces plain-text-readable Markdown
documents in English, Polish, or German - UTF-8 output, preserved encodings - for single
files and organized collections such as skill repositories and documentation sites.

On request it discovers a location's document layout - signals, best-matching scope,
exceptions - and audits a document against its governing rules, reporting mechanical,
structural, and content findings with an optional fix plan.

On describe or summarize requests it produces consolidated inline descriptions - impersonal,
compact, capped for "shortly" and floored at one hundred sentences for long requests.

On derivation requests it produces documents derived from an existing one - summaries and
briefs at declared compression tiers, supplements continuing the source's numbering.

On translate requests it renders a document into the target language in a single pass with
the pair's style adaptation and matching glossaries, preserving structure, code, and
identifiers - an adapted translation may compress and reorder, with every delta reported.

On translation-audit requests it maps a rendered document against its source - verifying the
structure map, untranslated elements, and terminology concordance, then reporting a fidelity
verdict.

On translation-revision requests it corrects an existing translation - aligning findings with
source passages and applying minimal-diff fixes and same-class sweeps.

AsciiDoc and reStructuredText files are edited minimally and never restyled.

On "work on panther-skill" requests it presents the maintenance menu - document work, skill
adjustment, or session review - then maintains its own rule corpus: it reads the governing
set and applies `docs/MAINTENANCE.md` instead of the document workflow.

On bare activation - "use skill", "run panther", or an equivalent - it enables for editorial
support: the update check runs, the router is the loaded state, and a compact capability list
answers the request. The next task request enters document or maintenance mode normally.

## Parameter Configuration

When creating a new standalone document, the agent runs the Parameter Resolution step in
`process/document-workflow.md` - it asks whether to accept or configure the core parameters.

Defaults are:

| Parameter         | Default                                                             |
|-------------------|---------------------------------------------------------------------|
| Document type     | Inferred from the request, ask when ambiguous                       |
| Document language | Language of the user's request, English when unclear                |
| Document scope    | Detected from the project layout, unstructured when nothing matches |
| Filename          | Per the language file naming rules, or the scope's convention       |
| Encoding          | UTF-8 without BOM                                                   |
| Line endings      | LF, or the dominant style of the target directory                   |
| Delivery          | File in the location named by the request                           |

Every question offers at most four answers - up to three candidates guessed from detection
evidence plus `Cancel`, which aborts the task.

Format questions are asked before the document-type question, which is always its own surface.

A section-plan question then selects the required, recommended, and optional sections.

Before executing, the agent describes the plan and asks to proceed, adjust, or cancel.

For edits to existing documents, the document's own conventions and the minimal-diff rule answer.

## `principles/` - Authoring Invariants

- **`principles/authoring-rules.md`** - Non-negotiable rules for every document: plain-text
  readability, the document's own conventions win, minimal diff, explicit unknowns, default
  structure, character and encoding rules.

## `process/` - Document Workflow

- **`process/document-workflow.md`** - Intake, parameter resolution, detection, rule selection,
  section plan, plan confirmation, drafting, validation, and delivery.
- **`process/document-checklist.md`** - The mechanical pre-delivery checklist: structure,
  spacing, characters, lists, tables, language, and file properties.
- **`process/scope-discovery.md`** - The standalone layout-discovery procedure: signal census,
  scope comparison, exception analysis, report format.
- **`process/document-audit.md`** - The standalone document-audit procedure: mechanical checks,
  section check, convention evaluation, content review, findings, and the optional fix plan.
- **`process/describe-response.md`** - The standalone describe procedure: consolidation,
  shortly caps and long-description floors, impersonal response style, inline delivery.
- **`process/derived-documents.md`** - The standalone derive procedure: derivation
  contract, compression tiers, supplement continuation, naming, and freshness rules.
- **`process/translate-document.md`** - The standalone translate procedure: pair
  resolution, industry glossaries, single-pass rendering, adapted fidelity, output conventions.
- **`process/translation-audit.md`** - The standalone translation-audit procedure: structure
  map, untranslated-set verification, terminology concordance, fidelity class, report format.
- **`process/translation-revision.md`** - The standalone translation-revision procedure:
  passage alignment, issue classes, minimal-diff correction of an existing translation.
- **`process/json-exchange.md`** - JSON parameter documents for intake question surfaces.
- **`process/skill-maintenance.md`** - The maintenance-mode procedure: the intake menu,
  governing set, skipped document machinery, and validation for work on this repository.
- **`process/session-review.md`** - The session-review procedure: gather the session's
  lessons, report findings for approval, apply and validate approved rule changes.
- **`process/skill-activation.md`** - The enable-mode procedure: bare-activation intake, the
  readiness response, and the hand-off to document or maintenance mode.

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
- **`types/quick-note.md`** - Quick notes and drafts: minimal structure, informal lists.
- **`types/message-document.md`** - Announcements, memos, and single-issue messages:
  subject-first title, minimal ceremony, one clear ask.
- **`types/daily-plan.md`** - Single-day planning documents: date-first title, priorities,
  scheduled blocks, carry-over.
- **`types/readme-general.md`** - Repository and package READMEs, the default variant when no
  more specific type applies: entry-point structure, layout trees.
- **`types/readme-skill.md`** - Agent Skill repository READMEs: activation contract,
  agent-environment installation, example prompts.
- **`types/readme-application.md`** - Software product READMEs: install and download paths,
  features, technical stack, changelog pointer.
- **`types/readme-library.md`** - Package and library READMEs: install command, minimal usage
  example, API pointer.
- **`types/readme-cli.md`** - Command-line tool READMEs: commands/options tables, examples.
- **`types/readme-docs.md`** - Documentation-repo READMEs: document locations, rules pointer.
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
- **`types/change-request.md`** - Formal change requests to a governed baseline: request
  metadata, justification, impact assessment, approval block.
- **`types/register-log.md`** - Risk, issue, stakeholder, assumption, change, backlog, and
  lessons-learned registers: ID prefixes, status lifecycles, append-only entry tables.
- **`types/status-report.md`** - Periodic status, variance, forecasting, and quality reports:
  RAG ratings, metrics, decisions needed.
- **`types/meeting-minutes.md`** - Meeting minutes and agendas: attendees with roles,
  decisions, action items with owners.
- **`types/management-plan.md`** - Management and subsidiary plans: methodology, cadence, roles.
- **`types/work-breakdown-structure.md`** - WBS and dictionaries: decimal-coded outline, work
  packages, RACI matrix.
- **`types/summary-document.md`** - Summaries, briefs, and abstracts derived from an
  existing document: declared source, compression tiers, carried verdict.
- **`types/supplement-document.md`** - Supplements extending an existing document:
  continued ID sequences, extended matrices, updated conclusions.

## `languages/` - Language Baselines

Load exactly one file, matching the document language - self-contained style baselines covering
structure, headings, lists, tables, characters, vocabulary, and file naming:

- **`languages/en.md`** - English documents: Title Case headings, vocabulary preferences.
- **`languages/pl.md`** - Polish documents: sentence case headings, diacritics, calque
  avoidance, terminology tables, per-type section names, and Polish activation phrases with
  English equivalents.
- **`languages/de.md`** - German documents: sentence case headings with noun
  capitalization, umlauts, Denglish calque avoidance, terminology tables, per-type section
  names, and German activation phrases with English equivalents.

## `translations/` - Language Pairs And Glossaries

Load on translate tasks per `process/translate-document.md`, and on translation-audit
tasks per `process/translation-audit.md`: the direction's
`translations/<pair>/<pair>-general.md`, then the pair's `<pair>-style.md` when it
exists, then every matching `<pair>-<category>.md`:

- **`translations/en-pl/`** - English to Polish direction rules and glossaries.
- **`translations/pl-en/`** - Polish to English direction rules and glossaries.
- **`translations/en-de/`** - English to German direction rules and glossaries.
- **`translations/de-en/`** - German to English direction rules and glossaries.
- **`translations/pl-de/`** - Polish to German direction rules and glossaries.
- **`translations/de-pl/`** - German to Polish direction rules and glossaries.
- Category slugs shared by every pair directory: `general`, `style`, `software`,
  `project`, `finance`, `legal`, `medical`, `electrical`, `construction`.

A `<pair>-style.md` file carries sentence-level adaptation rules - aspect, voice, actor verbs,
verb choice, fixed idioms, hedged verdicts - and loads between the direction contract and the
glossaries.

## `scopes/` - Project Layouts

Load the file matching the detected or named document scope, it governs placement, naming, and
registration inside an organized project:

- **`scopes/unstructured-layout.md`** - The default scope - documents land where requested.
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
- **`scopes/multi-project.md`** - Several projects per repo - nearest governing `docs/` wins.
- **`scopes/mkdocs-site.md`** - MkDocs documentation sites: `mkdocs.yml` nav registration,
  `index.md` homepage in `docs/`, kebab-case pages.
- **`scopes/docusaurus-site.md`** - Docusaurus sites: autogenerated sidebars,
  `sidebar_position` frontmatter, underscore partials, MDX tolerance.
- **`scopes/vitepress-site.md`** - VitePress sites: `.vitepress/` config, file-based routing.
- **`scopes/gitbook-site.md`** - GitBook projects: `SUMMARY.md` outline as the table of
  contents, entry registration in reading order.

## `conventions/` - Encoding And Dialects

- **`conventions/file-encoding.md`** - UTF-8 default, BOM handling, UTF-16/UCS-2 and code-page
  (CP1250) preservation, conversion rules, line endings, composed diacritics.
- **`conventions/markdown-dialects.md`** - Dialect catalog (ATX, setext, closed ATX, numbered
  chapters, export artifacts) with detection signals and preserve-on-edit rules.
- **`conventions/rst-documents.md`** - reStructuredText dialect and the minimal-edit contract.
- **`conventions/asciidoc-documents.md`** - AsciiDoc dialect and the minimal-edit contract for
  `.adoc` files: title markers, admonitions, includes, opaque tables.
- **`conventions/plain-text-comments.md`** - `#` comment alignment inside untagged fenced blocks
  and shell-tagged blocks: one shared column per block, longest entry plus two spaces.
- **`conventions/ascii-diagrams.md`** - Box-drawing flow diagrams: one shared axis, centered
  boxes and prose lines, `┬`/`▼` vertical edges, gap-filling `▶` side branches.
- **`conventions/prose-layout.md`** - Prose-layout conventions `flowing`, `separated`,
  `bounded`, `justified`: detection signals, the no-assumed-default and mixed-document
  rules, the `line-wrapping`/`sentence-spacing`/`wrap-width` parameters, and the tooling map.

## `templates/` - Skeletons

Starting skeletons for new typed documents, organized by language directory.

Template filenames carry the language code: `<type>-template-<code>.md`.

- `templates/en/` - English skeletons, one per document type, named `<type>-template-en.md`.
- `templates/pl/` - Polish skeletons, one per document type, named `<type>-template-pl.md`.
- `templates/de/` - German skeletons, one per document type, named `<type>-template-de.md`.

A template is a starting point - adjust sections to the request and the content.

## `scripts/` - Canonical Scripts

Copy document-production tools into the working repository's `work/` directory under a `.tmp.` name
before use and remove them when done.

See `scripts/README.md`.

- **`scripts/detect-encoding.py`** - BOM, guessed encoding, line endings, trailing whitespace.
- **`scripts/detect-scope.py`** - Document-scope signals and per-directory document counts.
- **`scripts/census-document.py`** - Structural census: headings, lists, fences, paragraphs,
  tables, and a per-element prose-layout classification.
- **`scripts/split-sentences.py`** - Split packed sentences onto logical lines, one
  sentence per paragraph with `--paragraphs`, or repack blocks into the `flowing`
  layout with `--flow`, re-wrap to `--width N` in default mode.
- **`scripts/reflow-prose.py`** - Prose reflow: `--wrap` splits over-width lines at
  whitespace, `--unwrap` joins wrapped continuations into logical lines, `--justify`
  stretches inter-word spacing to flush both edges of a block.
- **`scripts/wrap-prose.py`** - Deprecated split-only wrapper, superseded by
  `reflow-prose.py --wrap`, kept for documents that already reference it.
- **`scripts/format-table.py`** - Rebuild tables with source-width alignment.
- **`scripts/align-comments.py`** - Align trailing `#` comments to one column per block.
- **`scripts/validate-document.py`** - Mechanical checker for `process/document-checklist.md`.
- **`scripts/diff-content.py`** - Prove a formatting-only pass changed no words vs `HEAD`.
- **`scripts/check-sections.py`** - Section conformance check against a type's required,
  recommended, optional, and unusual vocabulary, localized aliases included.
- **`scripts/validate-skill.py`** - Panther-repo frontmatter, disclosure, root-reference checks.
- **`scripts/check-references.py`** - Panther-repo relative-reference integrity checker.
- **`scripts/check-contents.py`** - Panther-repo `## Contents` line-number drift checker.
- **`scripts/check-update.py`** - Git upstream self-update checker, once per session.
- **`scripts/test-scripts.py`** - Smoke harness exercising every tool's non-mutating path.
- **`scripts/README.md`** - Tool classes, commands, flags, validation order, limitations.

## Evaluation Prompts

- **`evals/evals.json`** - Skill-creator regression prompts covering document creation in
  all supported languages, convention-preserving edits, table reformatting, encoding edge
  cases, the session update check, bare activation, and document audits.

Run these as behavioral evaluations after structural changes.

They do not replace independent review.

## Repository Files

These files govern the skill repository itself rather than document production:

- **`AGENTS.md`** - Agent-facing entry point for repository authoring and maintenance.
- **`README.md`** - Human-facing overview, usage examples, and verification commands.
- **`docs/STYLE.md`** - Style rules for the skill's own files.
- **`docs/MAINTENANCE.md`** - Extension rules: directory roles, naming, registration, validation.
- **`docs/VERSIONING.md`** - Version numbering and release conventions for the skill.
- **`docs/CONTRIBUTING.md`** - Issue reporting, development setup, and pull-request rules.
- **`docs/SECURITY.md`** - Vulnerability disclosure channel and update-path trust boundary.

## File Handling Contract

Never change the encoding, byte order mark, or line-ending style of an existing file.

Create new files in UTF-8 without BOM.

Run `scripts/detect-encoding.py` before editing any existing file.

Never transcode a file unless the request explicitly asks for a target encoding.

Never overwrite an existing document wholesale without the user's confirmation.

Remove every `.tmp.` tool copy from the working repository when the task ends.
