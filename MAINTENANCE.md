# Skill Maintenance

## Purpose

> **Scope:** Rules for extending, restructuring, and maintaining the panther-skill repository
> itself
> **Key items:** directory roles, file naming, registration contract, addition procedures,
> validation

These rules apply to the skill's own files, not to documents the skill produces.

Document production rules live in `principles/`, `process/`, `types/`, `languages/`, and
`conventions/`.

Prose and formatting style for the skill's files lives in `STYLE.md`.

## Directory Roles

| Directory      | Role                                                          |
|----------------|---------------------------------------------------------------|
| `principles/`  | Non-negotiable authoring invariants                           |
| `process/`     | Document-production workflow and checklists                   |
| `types/`       | Per-document-type deltas on top of the language baseline      |
| `languages/`   | Per-language self-contained style baselines, one per ISO code |
| `scopes/`      | Per-project-layout organization and registration rules        |
| `conventions/` | Cross-cutting encoding and Markdown dialect rules             |
| `templates/`   | Per-language document skeletons grouped by ISO code directory |
| `tools/`       | Canonical scripts: document production and skill maintenance  |
| `evals/`       | Behavioral regression prompts                                 |

Root files govern the repository itself: `SKILL.md` (router), `README.md`, `STYLE.md`,
`VERSIONING.md`, `MAINTENANCE.md`, `LICENSE`.

Keep rule files one level deep under their directory.

Do not nest subdirectories inside `types/`, `languages/`, `scopes/`, `conventions/`, `process/`,
or `principles/`.

A new top-level rule directory also needs its name added to `KNOWN_DIRS` in
`tools/check-references.py`, otherwise references to its files inside rule documents are not
checked.

`templates/` is the exception: it groups skeletons one level deep under per-language
directories (`templates/<code>/`).

## File Naming

Use lowercase kebab-case for rule files: `project-document.md`, `rules-document.md`.

Match the dominant word-count convention of the target directory.

When most existing filenames use two words, a new file uses at least two words even when one
word would do: `article-text.md` in `types/`, not `article.md`.

Language baselines are named `languages/<code>.md`, where `<code>` is the ISO 639-1 language
code.

Each language file carries YAML frontmatter with `code`, `name`, and `native-name` fields.

Localised templates are named `templates/<code>/<type>-template-<code>.md` - the language code
in the filename makes the variant self-describing.

Tools are named `tools/<verb>-<object>.py`, for example `detect-encoding.py` or
`format-table.py`.

Document-production tools are copied into working repositories under a `.tmp.` infix before
use.

Repository files use uppercase conventional names: `README.md`, `STYLE.md`, `VERSIONING.md`,
`MAINTENANCE.md`, `LICENSE`.

## New Rule Files

Every new topic file must include at minimum:

- H1 title
- `## Purpose` section
- One or more main content sections

Files over 300 lines must also include a `## Contents` table.

## Registration Contract

Register every new rule file in `SKILL.md` with a line saying what it covers and when to load
it, under the section matching its directory.

List every new template pair in the matching `types/<type>.md` file as a `**Templates**` bullet
list, see the Localised Resources rule in `STYLE.md`.

Mirror every layout change in the `README.md` directory tree.

Renumber every `## Contents` table affected by line shifts.

Keep `evals/evals.json` prompts in sync with capabilities that change.

## Adding A Language

1. Create `languages/<code>.md` with frontmatter (`code`, `name`, `native-name`) and a full
   style baseline modeled on `languages/en.md`.
2. Create `templates/<code>/` with one `<type>-template-<code>.md` per document type.
3. Register both in `SKILL.md` under the `languages/` and `templates/` sections.
4. Extend the `**Templates**` list in every file under `types/`.
5. Declare the language's activation phrases with their English equivalents and its per-type
   section names inside `languages/<code>.md` - keep `SKILL.md` and the other rule files in
   English only.
6. Update the `README.md` directory tree.

## Adding A Document Type

1. Create `types/<name>.md` following the existing type-file shape: Purpose blockquote, When To
   Use with a `**Templates**` list, Structure, Deltas From The Language Baseline, Section Names
   table.
2. Create `templates/en/<name>-template-en.md` and `templates/pl/<name>-template-pl.md`.
3. Register the type in `SKILL.md` under `types/` and add trigger phrases when needed.
4. Update the `README.md` directory tree.

## Adding A Scope

1. Create `scopes/<name>.md` following the scope-file shape: Purpose blockquote, Detection,
   Directory Roles or layout table, Conventions, Document Types In This Scope.
2. Register the scope in `SKILL.md` under the `scopes/` section and add trigger phrases when
   needed.
3. Extend the Scope Detection table in `process/document-workflow.md` with the scope's signals.
4. Update the `README.md` directory tree.

## Adding A Tool

1. Create `tools/<verb>-<object>.py`, standard library only unless the dependency is
   documented.
2. Classify it in `tools/README.md` as document-production (copied as `.tmp.`) or
   skill-maintenance (runs from this repository only).
3. Reference it from the `SKILL.md` `tools/` section and from the workflow step where it runs.

## Validation After Changes

Run the skill-maintenance tools after every structural change:

```text
python tools/validate-skill.py .
python tools/check-references.py .
```

Run `python tools/format-table.py <file>` on every file whose tables were touched.

Run `python tools/validate-document.py <file>` on every edited rule document.

Exercise the prompts in `evals/evals.json` after changes that alter behavior.

## Versioning

The skill version lives in `SKILL.md` frontmatter under `metadata.version` and follows
`VERSIONING.md`.

Bump it only on explicit user request, never as a side effect of a change.

## File Encoding

Preserve the existing line-ending style and encoding of every file edited in this repository.

Create new files in UTF-8 without BOM and with LF line endings.
