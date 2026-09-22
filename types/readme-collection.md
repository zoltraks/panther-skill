# Collection README

## Purpose

> **Scope:** Conventions for the `README.md` of a repository that is a catalog of independent
> entries - a skill collection, a monorepo root, an examples showcase, or a package family
> **Key items:** collection description, entry catalog, per-entry pointers, notices

| Out of scope                    | See instead                   |
|---------------------------------|-------------------------------|
| General repository README       | `types/readme-general.md`     |
| Agent skill repository README   | `types/readme-skill.md`       |
| Software product README         | `types/readme-application.md` |
| Package and library README      | `types/readme-library.md`     |
| Command-line tool README        | `types/readme-cli.md`         |
| Documentation repository README | `types/readme-docs.md`        |

A collection README is an index with a spine.

It explains what the collection is, lists every entry with a one-line description, and routes
the reader to each entry's own documentation.

## When To Use

Use for the root `README.md` of a repository whose value is the set of things it contains:
a collection of skills or plugins, a monorepo holding several projects, an examples or
templates showcase.

Each entry's own `README.md` carries its details - the collection README links to them instead
of duplicating them.

**Templates**

- `templates/en/readme-collection-template-en.md`
- `templates/pl/readme-collection-template-pl.md`

## Structure

The canonical skeleton, adjusted to the request:

1. H1 title - the collection name.
2. Note or About block - what the collection is and who maintains it.
3. Contents - a catalog of entries, each with its path and a one-line description.
4. Usage - how to install, consume, or contribute entries.
5. Notices - disclaimers, third-party notices, or per-entry licensing differences.
6. License and credits.

## Deltas From The Language Baseline

- The Contents catalog uses a list or table of entries with paths in inline code - one line
  per entry, never a prose paragraph per entry.
- Per-entry detail lives in the entry's own README - the collection README links, it does not
  repeat.
- When entries carry different licenses or statuses, a Notices section states the split plainly.
- Groups of entries may get their own subsection when the catalog has natural categories.

## Section Names

- Overview
- About This Repository
- Contents
- Usage
- Notices
- License
- Credits

Polish section names for this document type are declared in `languages/pl.md`.
