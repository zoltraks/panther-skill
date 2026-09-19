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

| Task      | Trigger example                                   | Rule source                    |
|-----------|---------------------------------------------------|--------------------------------|
| Create    | "write a spec", "create a README", "draft a note" | language file + type file      |
| Edit      | "add a section", "update the glossary"            | document's own conventions win |
| Reformat  | "fix this table", "align the columns"             | language file table rules      |
| Translate | "translate this doc to Polish"                    | target language file           |

A request may combine tasks.

Apply the union of the required rule files.

Identify the target file or the intended output location before writing anything.

Read the whole target document when editing, conventions are detected from the document itself.

## Parameter Resolution

When creating a new standalone document, confirm the parameters before writing.

Ask the user whether to accept the defaults or configure the core parameters.

| Parameter         | Default                                                             |
|-------------------|---------------------------------------------------------------------|
| Document type     | Inferred from the request, ask when ambiguous                       |
| Document language | Language of the user's request, English when unclear                |
| Filename          | Per the language file naming rules, type-conventional names allowed |
| Encoding          | UTF-8 without BOM                                                   |
| Line endings      | LF, or the dominant style of the target directory                   |
| Delivery          | File in the location named by the request                           |

If the user accepts the defaults or says "bypass", proceed immediately.

If the user chooses to configure, ask only the unresolved parameter questions.

For edits to existing documents, do not ask.

The existing document's conventions and the minimal-diff rule provide the answers.

Type-conventional names such as `README.md`, `CHANGELOG.md`, `SPECIFICATION.md`, or
`SPECYFIKACJA.md` are allowed even though the default naming rule is lowercase with underscores.

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

## Rule Selection

Load rule files in this order:

1. **`languages/<lang>.md`** - mandatory for every document. Load the file matching the document
   language, never both at once.
2. **`types/<type>.md`** - load when the document matches a known type. The type file adds deltas
   on top of the language file.
3. **`conventions/file-encoding.md`** - load when the document encoding is not UTF-8, when the request
   involves encoding or code pages, or when detection reports an unexpected result.
4. **`conventions/markdown-dialects.md`** - load when the document uses a non-default dialect or
   when the request involves reformatting.

For a simple document, the language file alone may suffice.

Language files are self-contained baselines and stay the single source of truth for their
language.

## Drafting And Editing

For a new typed document, start from the matching `templates/<lang>/` skeleton.

A template is a starting point, not a cage - add, remove, or rename sections when the request or
the content requires it.

For an edit, work inside the document's existing conventions.

Keep the minimal-diff rule: touch only what the request covers.

Apply the language file rules to the content you write even inside a dialect document - sentence
shape, vocabulary, and terminology still follow the language rules.

## Validation

Before delivering, run the checks from `process/document-checklist.md`:

- Mechanical self-review of the written content.
- `tools/format-table.py` on the file when it contains tables.
- `tools/validate-document.py` on the file.
- `git diff --check` when working inside a repository.

A failing check must be fixed or explicitly reported to the user with a reason.

## Delivery

Never overwrite an existing document without the user's confirmation when the change replaces the
whole file.

In-place edits that follow the request do not need confirmation.

When finished, report the file path, the conventions detected and applied, and any checks that
were skipped or failed.

Remove every copied `.tmp.` script from the working repository.
