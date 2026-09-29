# Document Workflow

## Purpose

> **Scope:** The end-to-end workflow for creating and editing documents with this skill
> **Key items:** intake, parameter resolution, detection, rule selection, drafting, validation,
> delivery

This file defines the required workflow.

Follow it for every document task, whether the result is a new file, an edit to an existing file,
a reformatting, or a translation.

## Intake

A request whose target is the Panther repository itself is a maintenance task - follow
`process/skill-maintenance.md` instead of this workflow.

Classify the request into one primary task:

| Task      | Trigger example                                    | Rule source                    |
|-----------|----------------------------------------------------|--------------------------------|
| Create    | "write a spec", "create a README", "draft a note"  | language file + type file      |
| Edit      | "add a section", "update the glossary"             | document's own conventions win |
| Reformat  | "fix this table", "unwrap the document"            | language file + convention set |
| Translate | "translate this doc to Polish"                     | translate procedure            |
| Discover  | "discover layout", "detect document layout"        | scope discovery procedure      |
| Audit     | "audit this document", "check document formatting" | document audit procedure       |
| Describe  | "describe this", "summarize the session"           | describe-response procedure    |

A request may combine tasks.

Apply the union of the required rule files.

An approved fix plan from an audit becomes an Edit task.

A describe task produces an inline response, not a document - a file is written only when
the request explicitly asks for one.

Identify the target file or the intended output location before writing anything.

Read the whole target document when editing, conventions are detected from the document itself.

## Parameter Resolution

When creating a new standalone document, confirm the parameters before writing.

Ask the user whether to accept the defaults or configure the core parameters.

| Parameter         | Default                                                             |
|-------------------|---------------------------------------------------------------------|
| Document type     | Inferred from the request, ask when ambiguous                       |
| Document language | Language of the user's request, English when unclear                |
| Document scope    | Detected from the project layout, unstructured when nothing matches |
| Filename          | Per the language file naming rules, or the scope's convention       |
| Encoding          | UTF-8 without BOM                                                   |
| Line endings      | LF, or the dominant style of the target directory                   |
| Delivery          | File in the location named by the request                           |

If the user accepts the defaults or says "bypass", proceed immediately.

If the user chooses to configure, ask only the unresolved parameter questions.

README documents resolve their variant through the detected scope's Document Types table -
`types/readme-general.md` is the fallback.

When the scope gives no signal and the request does not name a variant, ask the user which
README variant applies.

For edits to existing documents, do not ask.

The existing document's conventions and the minimal-diff rule provide the answers.

Type-conventional names such as `README.md`, `CHANGELOG.md`, `SPECIFICATION.md`,
`CHARTER.md`, or `WBS.md` are allowed even though the default naming rule is
lowercase with underscores.

Conventional names in other languages are declared in the matching `languages/` file.

## Detection

For every existing file involved in the task, run the detection tool before editing:

```text
python detect-encoding.tmp.py <file>
```

Copy `scripts/detect-encoding.py` into the working repository under a `.tmp.` name first, see
`scripts/README.md`.

The report gives the byte order mark, the guessed encoding, the line-ending style, and the
trailing-whitespace count.

Then identify the Markdown dialect of the document per `conventions/markdown-dialects.md`.

Dialect signals include heading style, section numbering, list markers, table shape, and embedded
HTML artifacts.

Identify embedded payload documents the same way - ` ```markdown ` fenced blocks that carry
complete documents are separate dialect regions with their own conventions.

Before planning changes, gather every convention the document currently follows and record them
as the working set for the edit:

- encoding, byte order mark, and line-ending style (from `detect-encoding.py`)
- Markdown dialect, heading style, and section numbering
- sentence layout - paragraph-per-sentence, sentence-per-line, or packed
- wrap convention - unwrapped logical lines or a fixed width, with the dominant width
- quote and apostrophe style, list markers, table alignment
- version markers or contents tables the document maintains
- embedded payload regions and their own interior conventions

The document's own observed conventions are authoritative for edits.

Repository rule documents such as `STYLE.md` or `GUIDELINES.md` declare the convention for new
files and break ties when the document is mixed or ambiguous.

When the observed convention conflicts with a declared rule, report the conflict instead of
silently normalizing the document.

Converting between wrapped and logical-line layout is itself a convention change - apply it only
when the request explicitly covers it, using `scripts/reflow-prose.py`.

## Scope Detection

When the task touches a project or repository, detect the document scope before selecting rules:

| Signal                                                                        | Scope                 |
|-------------------------------------------------------------------------------|-----------------------|
| `SKILL.md` at the root with `name` and `description` frontmatter              | `agent-skill`         |
| `conf.py` with `master_doc`, `index.rst` toctree, Sphinx Makefile             | `sphinx-docs`         |
| `mkdocs.yml` with `site_name`, `docs/` with `index.md`                        | `mkdocs-site`         |
| `docusaurus.config.js`, `docs/` or `website/docs/` content tree               | `docusaurus-site`     |
| `.vitepress/` directory with a config file                                    | `vitepress-site`      |
| `.gitbook.yaml` or a `SUMMARY.md` page outline                                | `gitbook-site`        |
| `docs/GUIDELINES.md` plus a `README.md` entry point, software project present | `guided-project`      |
| `docs/GUIDELINES.md` in a documents-only repository                           | `docs-collection`     |
| Several top-level project directories, sparse root documentation              | `multi-project`       |
| The request names a scope                                                     | The named scope       |
| Nothing matches                                                               | `unstructured-layout` |

A site-generator configuration file is a stronger signal than `docs/GUIDELINES.md` - a repository
with both `mkdocs.yml` and `docs/GUIDELINES.md` follows the site scope for placement and
registration, while the guidelines document still governs the project's own rules.

The scope describes how documents are organized in the project - where new documents go, which
naming convention applies, and which registration or index files must be updated when a document
is added, moved, or removed.

In a multi-project repository, detection runs per directory - the scope of the subproject that
contains the target file applies.

Load the matching `scopes/<scope>.md` file when a scope is detected or named.

The `unstructured-layout` scope is the default and needs no signals.

Run `python detect-scope.tmp.py <dir>` on the target when the layout is not obvious from the
visible structure - the census reports every scope's signals at once, see `scripts/README.md`.

When the request asks to discover or detect the document layout itself, follow
`process/scope-discovery.md` - that procedure produces a full report, not just a scope name.

## Rule Selection

Load rule files in this order:

1. **`languages/<lang>.md`** - mandatory for every document. `<lang>` is the ISO 639-1 language
   code (`en`, `pl`, `de`). Load the file matching the document language, never more than one
   at once.
2. **`types/<type>.md`** - load when the document matches a known type. The type file adds deltas
   on top of the language file.
3. **`scopes/<scope>.md`** - load when scope detection matches a project layout, or when the
   request names a scope. The scope file governs placement, filename conventions, and
   registration side effects, it never replaces the language baseline for prose style, and the
   document's own conventions still win on edit.
4. **`conventions/file-encoding.md`** - load when the document encoding is not UTF-8, when
   the request involves encoding or code pages, or when detection reports an unexpected
   result.
5. **`conventions/markdown-dialects.md`** - load when the document uses a non-default dialect or
   when the request involves reformatting.
6. **`conventions/rst-documents.md`** - load when the task touches an `.rst` file or when a scope
   file delegates to it.
7. **`conventions/asciidoc-documents.md`** - load when the task touches an `.adoc` file or when
   a scope file delegates to it.

On a Translate task the selection shifts: `languages/<lang>.md` is the target language,
and `process/translate-document.md` defines the procedure - it loads
`translations/<pair>/<pair>-general.md` and the matching industry glossaries on top of
the target baseline.

For a simple document, the language file alone may suffice.

Language files are self-contained baselines and stay the single source of truth for their
language.

## Drafting And Editing

For a new typed document, start from the matching `templates/<lang>/<type>-template-<lang>.md`
skeleton.

A template is a starting point, not a cage - add, remove, or rename sections when the request or
the content requires it.

For an edit, work inside the document's existing conventions.

Keep the minimal-diff rule: touch only what the request covers.

The detected scope decides the target directory for new documents, overrides the filename
convention when it defines one, and lists the registration steps that follow adding, moving, or
removing a document.

Apply the language file rules to the content you write even inside a dialect document - sentence
shape, vocabulary, and terminology still follow the language rules.

For a requested reformatting, prefer the dedicated tools over hand edits:

`scripts/split-sentences.py` separates packed sentences onto individual logical lines,
`scripts/reflow-prose.py --wrap --width N` wraps prose and `--unwrap` joins wrapped
continuations back into logical lines,
`scripts/format-table.py` realigns tables,
`scripts/align-comments.py` aligns `#` comments inside plain-text and shell blocks.

Pass `--payload-markdown` to the payload-aware tools only when the request covers embedded
payload documents - payload content stays opaque otherwise.

## Editing Governed Documents

A governed document defines a set other parts of itself enumerate - canonical files, section
names, rule owners, or options.

Re-verify the target before planning a multi-part edit when time passed or the file may have
changed - re-read it or check its version marker and `git status`, never rely on an earlier
read.

When the change adds, removes, or renames a member of a governed set, first inventory every
place the document enumerates that set - tables, bullet lists, decision menus, checklists,
procedures, and embedded examples - then update all of them in one pass.

When renaming a section or file the document references by name, search the whole document
for the old name before and after the rename and update every reference.

Renumber ordered lists after inserting or removing items.

Apply edits that share anchor context sequentially - when an edit fails because the anchor
text no longer matches, re-read the region and retry with the current text.

Keep embedded ` ```markdown ` templates consistent with the normative text they implement.

A verification search that finds no match confirms absence - it is not a failure.

## Validation

Before delivering, run the checks from `process/document-checklist.md`:

- Mechanical self-review of the written content.
- `scripts/split-sentences.py --check` when the request covered packed sentences.
- `scripts/format-table.py --check` on the file when it contains tables.
- `scripts/align-comments.py --check` when the document contains plain-text blocks with `#`
  comments.
- `scripts/reflow-prose.py --wrap --check --width N` when the document follows a width
  convention, `scripts/reflow-prose.py --unwrap --check` when it keeps logical lines.
- `scripts/validate-document.py` on the file, with `--payload-markdown` when the document embeds
  ` ```markdown ` payload blocks.
- `scripts/diff-content.py` after any formatting-only pass - the token stream must be identical
  to the pre-edit baseline, and every merged-line warning must be reviewed.
- Legitimate sentence joins and deliberate reflows produce expected merged-line warnings.
- `git diff --check` when working inside a repository.

A failing check must be fixed or explicitly reported to the user with a reason.

## Delivery

Never overwrite an existing document without the user's confirmation when the change replaces the
whole file.

In-place edits that follow the request do not need confirmation.

When finished, report the file path, the scope detected, the conventions applied, every
registration or index file updated, and any checks that were skipped or failed.

Remove every copied `.tmp.` script from the working repository.
