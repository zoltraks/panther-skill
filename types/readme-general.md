# General README

## Purpose

> **Scope:** Conventions for repository and package `README.md` files with no more specific
> variant - the default README type and the entry point that orients a reader in the project
> **Key items:** title, purpose, contents, usage, license, conventional filename

| Out of scope                    | See instead                   |
|---------------------------------|-------------------------------|
| Agent skill repository README   | `types/readme-skill.md`       |
| Software product README         | `types/readme-application.md` |
| Package and library README      | `types/readme-library.md`     |
| Command-line tool README        | `types/readme-cli.md`         |
| Documentation repository README | `types/readme-docs.md`        |
| Collection and monorepo README  | `types/readme-collection.md`  |

A README is the first document a reader opens.

It answers three questions fast: what is this, how do I use it, where do I look next.

Typical shape: title, blockquote purpose, contents table, capability overview, usage table,
directory tree, license - like this skill's own `README.md`.

## When To Use

Use for the root `README.md` of a repository and for package-level READMEs in subdirectories
when no more specific README variant applies.

The detected scope selects the variant - see `process/document-workflow.md`.

When the scope gives no signal and the request does not name a variant, ask the user or fall
back to this general type.

**Templates**

- `templates/en/readme-general-template-en.md`
- `templates/pl/readme-general-template-pl.md`

The filename is always `README.md` - a type-conventional name that overrides the lowercase naming
rule.

## Structure

The canonical skeleton, adjusted to the request:

1. H1 title - the project name, optionally with a short tag line.
2. Purpose - a paragraph or blockquote stating what the project does.
3. Contents - table of sections for long READMEs.
4. Overview - what the project does and its main capabilities.
5. Usage - how to install, run, or invoke it.
6. Project layout - a directory tree in a plain fenced block when the structure matters.
7. License and credits.

## Deltas From The Language Baseline

- A blockquote purpose block is acceptable and common in READMEs.
- A directory tree in an untagged fenced block may use box-drawing characters.
- Trailing `#` comments on tree or listing lines align to a shared column per block - see
  `conventions/plain-text-comments.md`.
- A "when to use" table is a good fit for the usage section.
- Badges and HTML are allowed only when the repository's README convention already uses them -
  do not introduce them unasked.
- Keep the README honest: describe what exists, not what is planned, unless a section is clearly
  marked as planned.

## Section Names

- Contents
- Overview
- Installation
- Usage
- Project Layout
- Documentation
- License
- Credits

Polish section names for this document type are declared in `languages/pl.md`.
