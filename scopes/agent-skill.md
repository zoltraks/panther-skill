# Agent Skill Layout

## Purpose

> **Scope:** Document work inside an Agent Skill repository - a directory that contains a
> `SKILL.md` router and bundled resource files
> **Key items:** router contract, directory roles, registration procedure, kebab-case naming

An Agent Skill is a documented collection of rule files, scripts, and templates that an agent
loads progressively.

The layout follows the Agent Skills specification and the `skill-creator` conventions.

Load this file when the task creates, edits, or restructures documents inside a skill
repository, including the Panther repository itself.

## Detection

A repository matches this scope when it contains a `SKILL.md` file at its root with YAML
frontmatter carrying `name` and `description` fields.

The `name` field conventionally matches the directory name.

## Directory Roles

The specification requires only `SKILL.md`.

Optional directories seen in real skills:

| Directory     | Role                                                     |
|---------------|----------------------------------------------------------|
| `scripts/`    | Executable code for deterministic or repetitive tasks    |
| `references/` | Documentation loaded into context as needed              |
| `assets/`     | Files used in output such as templates, icons, and fonts |
| `agents/`     | Prompt files for delegated subagent roles                |
| `evals/`      | Behavioral regression prompts, usually `evals.json`      |
| `tools/`      | Canonical scripts with their own `README.md`             |
| `templates/`  | Skeletons for produced artifacts                         |

Skills may define their own taxonomy on top, for example `principles/`, `process/`, `types/`,
`languages/`, `conventions/`, `scopes/`, `assessment/`, `synthesis/`, or `translation/`.

The skill's own governing files describe its specific taxonomy and cascade - read them when
working inside that skill (see Governing Files).

## The Router Contract

`SKILL.md` is the root router of the skill, not a prose document.

It registers every rule file with a line saying what the file covers and when to load it, under
the section matching the file's directory.

It stays under 500 lines and carries a `## Contents` table when longer files require navigation.

Its frontmatter follows the Agent Skills specification: `name` uses lowercase letters, digits,
and single hyphens, `description` stays under 1024 characters and carries the trigger phrases.

When a rule file is added, removed, or renamed, update its registration line in `SKILL.md`.

Mirror layout changes in the `README.md` directory tree when one exists.

Renumber every `## Contents` table affected by line shifts.

Keep `evals/evals.json` prompts in sync with capabilities that change.

## Governing Files

Before editing inside a skill repository, read its governing documents in order:

1. `SKILL.md` - the router: taxonomy, registration entries, and activation contract.
2. The maintenance document, conventionally `MAINTENANCE.md` - directory roles, naming rules,
   and the per-kind addition procedures.
3. The style document, conventionally `STYLE.md` - prose and formatting rules for the skill's
   own files.
4. The versioning document, conventionally `VERSIONING.md` - version field location and bump
   policy.
5. `tools/README.md` when the skill ships tools - tool classes and command conventions.

The skill's own maintenance document defines its registration cascade - follow it.

When no maintenance document exists, apply the procedure in Adding Or Removing A Document.

## Consistency Sets

One resource is typically enumerated in several places at once: the `SKILL.md` registry, the
`README.md` directory tree, `## Contents` tables, language or translation files, and
`evals/evals.json`.

Update every enumeration in a single pass - the governed-set inventory rules of
`process/document-workflow.md` apply to skill files the same way they apply to governed
documents.

`## Contents` entries carry approximate line numbers, so renumber them when sections move
significantly.

Verify a renumbered table against `grep -n '^## ' <file>` or with the skill's contents checker
when it provides one, for example `tools/check-contents.py` in the Panther repository.

Untracked scratch directories such as `work/` are not rule material - never register them, and
keep them out of reference checks and audits.

## Document Types In This Scope

| File                                          | Handling                                                            |
|-----------------------------------------------|---------------------------------------------------------------------|
| `SKILL.md`                                    | Router document - governed by this scope's contract                 |
| `README.md`                                   | `readme-skill` type                                                 |
| Rule and topic files                          | `technical-document`, `rules-document`, or `agent-instruction` type |
| `MAINTENANCE.md`, `STYLE.md`, `VERSIONING.md` | `rules-document` type                                               |
| `CONTRIBUTING.md`                             | `contributing-file` type                                            |
| `LICENSE`                                     | Verbatim legal text - preserve, never restyle                       |
| `evals.json`, scripts                         | Data and code - not documents                                       |
| `templates/` skeletons                        | Payload artifacts - style follows the skill's rules                 |

## Naming

Use lowercase kebab-case for new rule files, for example `project-document.md`.

Match the dominant word-count convention of the target directory - when most filenames use two
words, a new file uses at least two words even when one would do.

This naming rule comes from the scope, it overrides the `languages/` file default for rule
files inside the skill.

## Adding Or Removing A Document

1. Create or remove the file in the directory matching its role.
2. Register or remove its line in `SKILL.md` under the matching directory section.
3. Update the `README.md` directory tree when the layout changed.
4. Renumber `## Contents` tables affected by line shifts - see Consistency Sets.
5. Sync `evals/evals.json` when behavior changed.
6. Run the skill's own validators when it defines them, for example
   `tools/validate-skill.py .`, `tools/check-references.py .`, and `tools/check-contents.py .`
   in the Panther repository.
