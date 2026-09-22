# Document Workflow

## Purpose

> **Scope:** The end-to-end workflow for creating and editing documents with this skill
> **Key items:** intake, parameter resolution, detection, rule selection, drafting, validation,
> delivery

This file defines the required workflow.

Follow it for every document task, whether the result is a new file, an edit to an existing file,
a reformatting, or a translation.

## Intake

Classify the request into one primary task:

| Task      | Trigger example                                    | Rule source                    |
|-----------|----------------------------------------------------|--------------------------------|
| Create    | "write a spec", "create a README", "draft a note"  | language file + type file      |
| Edit      | "add a section", "update the glossary"             | document's own conventions win |
| Reformat  | "fix this table", "align the columns"              | language file table rules      |
| Translate | "translate this doc to Polish"                     | target language file           |
| Discover  | "discover layout", "detect document layout"        | scope discovery procedure      |
| Audit     | "audit this document", "check document formatting" | document audit procedure       |

A request may combine tasks.

Apply the union of the required rule files.

An approved fix plan from an audit becomes an Edit task.

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

Copy `tools/detect-encoding.py` into the working repository under a `.tmp.` name first, see
`tools/README.md`.

The report gives the byte order mark, the guessed encoding, the line-ending style, and the
trailing-whitespace count.

Then identify the Markdown dialect of the document per `conventions/markdown-dialects.md`.

Dialect signals include heading style, section numbering, list markers, table shape, and embedded
HTML artifacts.

Identify embedded payload documents the same way - ` ```markdown ` fenced blocks that carry
complete documents are separate dialect regions with their own conventions.

When the task involves reformatting or wrapping, check the repository's own style rules for a
hard line-width limit before touching the document - a `STYLE.md` or equivalent guideline
overrides the no-hard-wrap default of the language files.

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
visible structure - the census reports every scope's signals at once, see `tools/README.md`.

When the request asks to discover or detect the document layout itself, follow
`process/scope-discovery.md` - that procedure produces a full report, not just a scope name.

## Rule Selection

Load rule files in this order:

1. **`languages/<lang>.md`** - mandatory for every document. `<lang>` is the ISO 639-1 language
   code (`en`, `pl`). Load the file matching the document language, never both at once.
2. **`types/<type>.md`** - load when the document matches a known type. The type file adds deltas
   on top of the language file.
3. **`scopes/<scope>.md`** - load when scope detection matches a project layout, or when the
   request names a scope. The scope file governs placement, filename conventions, and
   registration side effects, it never replaces the language baseline for prose style, and the
   document's own conventions still win on edit.
4. **`conventions/file-encoding.md`** - load when the document encoding is not UTF-8, when the request
   involves encoding or code pages, or when detection reports an unexpected result.
5. **`conventions/markdown-dialects.md`** - load when the document uses a non-default dialect or
   when the request involves reformatting.
6. **`conventions/rst-documents.md`** - load when the task touches an `.rst` file or when a scope
   file delegates to it.
7. **`conventions/asciidoc-documents.md`** - load when the task touches an `.adoc` file or when
   a scope file delegates to it.

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
`tools/split-sentences.py` separates packed sentences onto individual logical lines,
`tools/wrap-prose.py --width N` wraps prose and never joins lines, `tools/format-table.py`
realigns tables.

Pass `--payload-markdown` to the payload-aware tools only when the request covers embedded
payload documents - payload content stays opaque otherwise.

## Validation

Before delivering, run the checks from `process/document-checklist.md`:

- Mechanical self-review of the written content.
- `tools/split-sentences.py --check` when the request covered packed sentences.
- `tools/format-table.py --check` on the file when it contains tables.
- `tools/wrap-prose.py --check --width N` when the document follows a width convention.
- `tools/validate-document.py` on the file, with `--payload-markdown` when the document embeds
  ` ```markdown ` payload blocks.
- `tools/diff-content.py` after any formatting-only pass - the token stream must be identical
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
