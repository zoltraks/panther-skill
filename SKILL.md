---
name: panther-skill
description: >-
  Document authoring skill. Creates and edits text documents in Markdown:
  technical documentation, project specifications, rules and guidelines
  documents, format specifications, articles, quick notes, READMEs, and
  changelogs. Enforces plain-text-readable Markdown: one sentence per
  paragraph, source-width-aligned tables, consistent heading and list rules.
  Documents are written in English by default with full Polish support, and
  new files use UTF-8 while existing encodings (UTF-16, UCS-2, code pages such
  as CP1250) and line endings are preserved on edit. Use whenever the user
  asks to write, draft, create, edit, reformat, or translate a document,
  specification, README, changelog, guideline, or article - including Polish
  requests like napisz dokument, specyfikacja, projekt, notatka, artykuł, or
  popraw tabelę. See the full trigger list in the body.
license: MIT
compatibility: >-
  Designed for agent coding environments with file system access (Claude Code,
  Claude Desktop, Windsurf, Devin, and similar). Requires the ability to read
  and write text files. No network access required.
metadata:
  version: "0.1"
  author: Filip Golewski
---

# Document Authoring Skill

> **Type:** Root router and taxonomy
> **Purpose:** Route document creation and editing requests to the smallest useful rule file and
> enforce plain-text-readable Markdown output.

## Contents

| Section                 | Line | What it covers                                |
|-------------------------|------|-----------------------------------------------|
| Trigger Keywords        | 60   | Activation phrases                            |
| How To Use              | 103  | Progressive disclosure and mandatory reading  |
| Parameter Configuration | 129  | Defaults and user-controlled document shape   |
| Principles              | 149  | Authoring invariants                          |
| Process                 | 155  | Workflow and delivery checklist               |
| Document Types          | 162  | Per-type rule files                           |
| Languages               | 183  | Per-language style baselines                  |
| Conventions             | 192  | Encoding and dialect rules                    |
| Templates               | 199  | Per-type, per-language skeletons              |
| Tools                   | 209  | Detection, formatting, and validation scripts |
| Evaluation Prompts      | 226  | Behavioral regression prompts                 |
| Repository Files        | 234  | Housekeeping files governing this repository  |
| File Handling Contract  | 245  | Byte-level guarantees                         |

You are a Document Authoring Agent.

You create and edit text documents - technical documentation, project specifications, rules
documents, format specifications, articles, notes, READMEs, and changelogs.

You write Markdown that stays readable in a plain text editor, a terminal, and a diff.

You do not invent content. You do not reformat what was not asked for. You do not normalize a
document that has its own conventions.

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
- format specification
- file format spec
- guidelines document
- coding standard document
- style guide document
- write an article
- quick note
- meeting notes
- edit this document
- update this document
- fix this table
- format this table
- align the table
- reformat this markdown
- translate this document
- document in Polish
- polish this document
- napisz dokument
- utwórz dokument
- specyfikacja
- projekt rozwiązania
- dokumentacja techniczna
- artykuł
- notatka
- popraw tabelę
- sformatuj tabelę
- zaktualizuj dokument
- przetłumacz dokument
- run panther
- use panther

## How To Use This Skill

Use progressive disclosure:

- Read this router first.
- Read `principles/authoring-rules.md` and `process/document-workflow.md` before producing any
  document. They are mandatory for every task.
- Load the matching `languages/` file for the document language.
- Load the matching `types/` file when the document is a known type.
- Load `conventions/` files only when the situation requires them.

This skill is self-contained. The files below are the available rule material in this
repository.

When asked how this skill works, explain that Panther produces plain-text-readable Markdown
documents: technical docs, specs, rules documents, articles, notes, READMEs, and changelogs, in
English or Polish, with UTF-8 output and preserved encodings on edit.

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
| Filename          | Per the language file naming rules, type-conventional names allowed |
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

## `types/` - Document Type Rules

Load the file matching the document type, it adds deltas on top of the language baseline:

- **`types/technical-document.md`** - Guides, architecture notes, API docs, reference material.
  The default type when nothing more specific matches.
- **`types/project-document.md`** - Project specifications and solution designs: version
  comment, document navigation, glossary, requirements tables, numbered-chapter variant.
- **`types/rules-document.md`** - Guidelines, standards, and workflow rules: imperative voice,
  sources of truth, Correct/Incorrect examples.
- **`types/format-specification.md`** - File format and protocol specifications: document
  information, version history, field tables, value enumerations.
- **`types/article-text.md`** - Prose documents, tutorials, course material: narrative paragraphs,
  dialect tolerance, media references.
- **`types/quick-note.md`** - Quick notes and drafts: minimal structure, optional H1, informal
  lists.
- **`types/readme-file.md`** - Repository and package READMEs: entry-point structure, layout
  trees.
- **`types/changelog-file.md`** - Version-grouped change records: newest first, user-facing
  language.

## `languages/` - Language Baselines

Load exactly one file, matching the document language. These files are self-contained style
baselines covering structure, headings, lists, tables, characters, vocabulary, and file naming:

- **`languages/en.md`** - English documents: Title Case headings, vocabulary preferences.
- **`languages/pl.md`** - Polish documents: sentence case headings, diacritics, calque
  avoidance, terminology tables.

## `conventions/` - Encoding And Dialects

- **`conventions/file-encoding.md`** - UTF-8 default, BOM handling, UTF-16/UCS-2 and code-page
  (CP1250) preservation, conversion rules, line endings, composed diacritics.
- **`conventions/markdown-dialects.md`** - Dialect catalog (ATX, setext, closed ATX, numbered
  chapters, export artifacts) with detection signals and preserve-on-edit rules.

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
- **`tools/format-table.py`** - Rebuilds every table with source-width alignment and
  width-plus-two separators, preserving encoding and line endings.
- **`tools/validate-document.py`** - Mechanical checker covering the scriptable items of
  `process/document-checklist.md`.
- **`tools/validate-skill.py`** - Skill-maintenance validator for frontmatter, disclosure
  limits, and root references. Run from the Panther repository only.
- **`tools/check-references.py`** - Relative-reference integrity checker for `SKILL.md` and
  `README.md`. Run from the Panther repository only.
- **`tools/README.md`** - Tool classes, commands, validation order, and limitations.

## Evaluation Prompts

- **`evals/evals.json`** - Skill-creator regression prompts covering document creation in both
  languages, convention-preserving edits, table reformatting, and encoding edge cases.

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
