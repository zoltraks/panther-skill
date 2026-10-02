# Skill Maintenance

## Purpose

> **Scope:** Rules for extending, restructuring, and maintaining the panther-skill repository
> itself
> **Key items:** directory roles, file naming, registration contract, addition procedures,
> validation

These rules apply to the skill's own files, not to documents the skill produces.

Document production rules live in `principles/`, `process/`, `types/`, `languages/`, and
`conventions/`.

Prose and formatting style for the skill's files lives in `docs/STYLE.md`.

The intake procedure for requests that target the skill itself - mode selection and the
governing-file read set - lives in `process/skill-maintenance.md`.

## Directory Roles

| Directory       | Role                                                           |
|-----------------|----------------------------------------------------------------|
| `principles/`   | Non-negotiable authoring invariants                            |
| `process/`      | Document-production workflow and checklists                    |
| `types/`        | Per-document-type deltas on top of the language baseline       |
| `languages/`    | Per-language self-contained style baselines, one per ISO code  |
| `translations/` | Directional pair rules and per-industry translation glossaries |
| `scopes/`       | Per-project-layout organization and registration rules         |
| `conventions/`  | Cross-cutting encoding and Markdown dialect rules              |
| `templates/`    | Per-language document skeletons grouped by ISO code directory  |
| `scripts/`      | Canonical scripts: document production and skill maintenance   |
| `evals/`        | Behavioral regression prompts                                  |
| `docs/`         | Repository-governance documents for the skill itself           |

Root files govern the repository itself: `SKILL.md` (router), `AGENTS.md` (agent entry
point), `README.md`, `LICENSE`, plus the `docs/` governance documents - `docs/STYLE.md`,
`docs/VERSIONING.md`, `docs/MAINTENANCE.md`, `docs/SECURITY.md`, `docs/CONTRIBUTING.md`, and
the `docs/README.md` index.

`work/` is gitignored research scratch outside the rule corpus.

Its content must not be promoted into tracked files without provenance review.

Keep rule files one level deep under their directory.

Do not nest subdirectories inside `types/`, `languages/`, `scopes/`, `conventions/`,
`process/`, or `principles/`.

A new top-level rule directory also needs its name added to `KNOWN_DIRS` in
`scripts/check-references.py`, otherwise references to its files inside rule documents are not
checked.

`docs/` is a governance directory excluded from rule-document scanning, not a rule directory -
it stays out of `KNOWN_DIRS`.

`templates/` and `translations/` are the exceptions: `templates/` groups skeletons one
level deep under per-language directories (`templates/<code>/`), and `translations/`
groups direction files one level deep under per-pair directories
(`translations/<pair>/`).

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

Translation pair directories are named `translations/<pair>/` with ISO 639-1 codes
ordered source to target.

Translation files inside a pair directory are named `translations/<pair>/<pair>-<category>.md`.

Direction rules use `translations/<pair>/<pair>-general.md`.

Glossaries use a stable category slug shared by every pair directory (`software`, `project`,
`finance`, `legal`, `medical`, `electrical`, `construction`)
so the same subject keeps the same filename across languages.

Tools are named `scripts/<verb>-<object>.py`, for example `detect-encoding.py` or
`format-table.py`.

Document-production tools are copied into working repositories under a `.tmp.` infix before
use.

Repository files use uppercase conventional names: `README.md`, `AGENTS.md`, `LICENSE`, and the
governance documents under `docs/` - `STYLE.md`, `VERSIONING.md`, `MAINTENANCE.md`,
`SECURITY.md`, `CONTRIBUTING.md`, `README.md`.

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
list, see the Localised Resources rule in `docs/STYLE.md`.

Mirror every layout change in the `README.md` directory tree.

Renumber every `## Contents` table affected by line shifts and verify the result with
`scripts/check-contents.py`.

Keep `evals/evals.json` prompts in sync with capabilities that change.

## External Examples

A change request may supply example documents, file paths, or project names to illustrate the
requested behavior.

Never reference those supplied examples inside skill documents, scripts, templates, or evals -
external material may not be reachable later, and real names or paths do not belong in the rule
corpus.

Create the skill's own examples instead.

Keep them generic and anonymized - invented project names, placeholder paths, and synthetic
content that demonstrates the same point without depending on anything outside this repository.

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
   Use with a `**Templates**` list, Structure, Deltas From The Language Baseline, and a
   `## Section Names` requirement table marking each section `required`, `recommended`,
   `optional`, or `unusual` - `scripts/check-sections.py` reads this table.
2. Create `templates/<lang>/<name>-template-<lang>.md` for every language directory under
   `templates/`.
3. Register the type in `SKILL.md` under `types/` and add trigger phrases when needed - the
   `languages/<code>.md` activation tables carry the localized equivalents.
4. Add the type's localized section names to each `languages/<code>.md` section-name table so
   `check-sections.py --language` can match localized headings.
5. Update the `README.md` directory tree.

## Adding A Scope

1. Create `scopes/<name>.md` following the scope-file shape: Purpose blockquote, Detection,
   Directory Roles or layout table, Conventions, Document Types In This Scope.
2. Register the scope in `SKILL.md` under the `scopes/` section and add trigger phrases when
   needed.
3. Extend the Scope Detection table in `process/document-workflow.md` with the scope's signals.
4. Update the `README.md` directory tree.

## Adding A Tool

1. Create `scripts/<verb>-<object>.py`, standard library only unless the dependency is
   documented.
2. Keep it a self-contained single file - document-production tools are copied into working
   repositories under `.tmp.` names, where a shared helper module would not exist.
3. Under the `__main__` guard, reconfigure `sys.stdout` and `sys.stderr` with
   `errors="backslashreplace"`, and pass explicit `encoding=` and `errors=` to every
   `subprocess` text call - console and pipe output must survive legacy encodings.
4. Classify it in `scripts/README.md` as document-production (copied as `.tmp.`) or
   skill-maintenance (runs from this repository only).
5. Reference it from the `SKILL.md` `scripts/` section and from the workflow step where it runs.

## Adding A Translation Pair

1. Create `translations/<pair>/` with `<pair>-general.md` following the pair-file shape:
   Purpose blockquote, Loading Order, Style Adaptation, Locale Conventions, Vocabulary
   And Register, What Stays Untranslated, Terminology Resolution, Output Conventions.
2. Create the reverse pair directory `translations/<reverse-pair>/` with its own
   directional `general` file.
3. Register both pair directories in `SKILL.md` under the `translations/` section.
4. Update the `README.md` directory tree.

## Adding A Translation Glossary

1. Create `translations/<pair>/<pair>-<category>.md` following the glossary shape:
   Purpose blockquote, Domain Signals, Terminology, Context Forms, Calque Traps,
   Untranslated. The `<category>` slug must match the same subject's slug in every
   other pair directory.
2. Create the matching `translations/<reverse-pair>/<reverse-pair>-<category>.md` with
   its own directional tables and calque traps.
3. Register the category slug in `SKILL.md` under the `translations/` section.
4. Update the `README.md` directory tree.

## Validation After Changes

Run the skill-maintenance tools after every structural change:

```bash
python scripts/validate-skill.py .
python scripts/check-references.py .
python scripts/check-contents.py .
```

Run `python scripts/format-table.py <file>` on every file whose tables were touched.

Run `python scripts/validate-document.py <file>` on every edited rule document.

Exercise the prompts in `evals/evals.json` after changes that alter behavior.

The gate is manual by design: no CI pipeline or hook automation runs these checks, so the
maintainer runs the full suite before each commit.

## Style Self-Audit

Run the checkers over every Markdown file outside `work/`:

- `python scripts/split-sentences.py <file> --paragraphs --check` - every sentence must be its
  own paragraph, per `docs/STYLE.md`.
- `python scripts/wrap-prose.py <file> --check` - skill files wrap prose at 100 characters.
- `python scripts/format-table.py <file> --check`
- `python scripts/align-comments.py <file> --check`
- `python scripts/validate-document.py <file>`
- `python scripts/check-contents.py .` - Contents tables still anchor to real headings.

Skip `wrap-prose.py` on `languages/` and `templates/` files - produced documents never
hard-wrap.

The intentional "Incorrect" example block in `conventions/plain-text-comments.md` carries the
`<!-- align-comments: off -->` marker, so `align-comments.py --check` must pass clean on every
shipped file - an unmarked flag is a defect, not expected noise.

## Versioning

The skill version lives in `SKILL.md` frontmatter under `metadata.version` and follows
`docs/VERSIONING.md`.

Bump it only on explicit user request, never as a side effect of a change.

## File Encoding

Preserve the existing line-ending style and encoding of every file edited in this repository.

Create new files in UTF-8 without BOM and with LF line endings.
