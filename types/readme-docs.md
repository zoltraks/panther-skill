# Documentation Repository README

## Purpose

> **Scope:** Conventions for the `README.md` of a documentation-only repository or a
> documentation site project - a repository whose payload is documents, not code
> **Key items:** what the documents cover, where they live, governing rules pointer

| Out of scope                   | See instead                   |
|--------------------------------|-------------------------------|
| General repository README      | `types/readme-general.md`     |
| Agent skill repository README  | `types/readme-skill.md`       |
| Software product README        | `types/readme-application.md` |
| Package and library README     | `types/readme-library.md`     |
| Command-line tool README       | `types/readme-cli.md`         |
| Collection and monorepo README | `types/readme-collection.md`  |

A documentation repository README is a map, not a manual.

It states what the documents cover, where they live, and which files govern the work.

## When To Use

Use for the root `README.md` of a repository whose content is documentation: a docs
collection, a standards repository, a knowledge base, or a documentation site project.

Also use it for a site landing page such as `docs/index.md` when the scope's page conventions
call for an entry-point document.

**Templates**

- `templates/en/readme-docs-template-en.md`
- `templates/pl/readme-docs-template-pl.md`

## Structure

The canonical skeleton, adjusted to the request:

1. H1 title - the repository or documentation set name.
2. Purpose - a paragraph stating what the documents cover.
3. Documentation - where the documents live and how they are organized.
4. Project Guidelines - a pointer to the governing rules document when one exists.
5. Repository Layout - the top-level structure when it helps navigation.
6. License.

## Deltas From The Language Baseline

- Point at the governing rules document, for example `docs/GUIDELINES.md`, instead of restating
  its rules.
- State clearly which files carry working rules and which are content or reference material.
- No install or usage sections unless the repository ships tooling - a docs README stays short.
- Keep links to documents relative and verified.

## Section Names

- Overview
- Documentation
- Project Guidelines
- Repository Layout
- License

Polish section names for this document type are declared in `languages/pl.md`.
