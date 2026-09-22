# Library README

## Purpose

> **Scope:** Conventions for the `README.md` of a consumable package or library - a module a
> developer installs and imports into their own code
> **Key items:** short description, package-manager install, minimal usage example, API pointer

| Out of scope                    | See instead                   |
|---------------------------------|-------------------------------|
| General repository README       | `types/readme-general.md`     |
| Agent skill repository README   | `types/readme-skill.md`       |
| Software product README         | `types/readme-application.md` |
| Command-line tool README        | `types/readme-cli.md`         |
| Documentation repository README | `types/readme-docs.md`        |
| Collection and monorepo README  | `types/readme-collection.md`  |

A library README serves a reader evaluating whether to depend on the package.

It leads with the install command and the smallest working example - everything else is
secondary.

## When To Use

Use for the root `README.md` of a published or internal package: an npm module, a PyPI package,
a crate, a gem, or any library consumed through a package manager or an import.

**Templates**

- `templates/en/readme-library-template-en.md`
- `templates/pl/readme-library-template-pl.md`

## Structure

The canonical skeleton, adjusted to the request:

1. H1 title - the package name, matching the package manager name.
2. Short description - one line of plain text stating what the package does.
3. Long description - optional context paragraphs.
4. Install - the package manager command.
5. Usage - the minimal runnable example: import plus one real call.
6. API Reference - a link to full docs, or a summary table for small APIs.
7. Configuration - options when the package has them.
8. Contributing - a pointer to `CONTRIBUTING.md` or development setup.
9. License.

## Deltas From The Language Baseline

- The Usage example must be real and runnable - an example that references functions that no
  longer exist is the most common library README failure.
- Keep the README scannable, roughly 100 to 300 lines - move deep reference material into
  `docs/` and link to it.
- Badges and banners appear only when the repository's convention already uses them.
- A "why this library" section fits when the package replaces or improves on existing
  solutions.

## Section Names

- Install
- Usage
- API Reference
- Configuration
- Contributing
- License

Polish section names for this document type are declared in `languages/pl.md`.
