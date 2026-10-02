# Application README

## Purpose

> **Scope:** Conventions for the `README.md` of a software product - an application, service,
> tool, or system a user installs, runs, or deploys
> **Key items:** install and download paths, features, technical stack, repository structure,
> changelog pointer

| Out of scope                    | See instead                  |
|---------------------------------|------------------------------|
| General repository README       | `types/readme-general.md`    |
| Agent skill repository README   | `types/readme-skill.md`      |
| Package and library README      | `types/readme-library.md`    |
| Command-line tool README        | `types/readme-cli.md`        |
| Documentation repository README | `types/readme-docs.md`       |
| Collection and monorepo README  | `types/readme-collection.md` |

An application README serves a reader who wants to run the product.

It leads with what the product does, how to get it, and how to start it - then points to deeper
documentation instead of duplicating it.

## When To Use

Use for the root `README.md` of a software project that builds or ships a runnable artifact:

desktop and server applications, services, emulators, tools with a deployment story.

For a consumable package or importable module, prefer `types/readme-library.md`.

For a pure command-line utility, prefer `types/readme-cli.md`.

**Templates**

- `templates/en/readme-application-template-en.md`
- `templates/pl/readme-application-template-pl.md`
- `templates/de/readme-application-template-de.md`

## Structure

The canonical skeleton, adjusted to the request:

1. H1 title - the product name, optionally with a short tag line.
2. Banner - an ASCII banner or badges, only when the project convention uses them.
3. Version comment - an optional `<!-- Version: ... -->` comment when the project uses one.
4. Overview - what the product does and the problem it solves.
5. Download or Installation - binaries table or build steps, per platform when needed.
6. Project Status - development phase or maturity when relevant.
7. Features and Technical Stack - capabilities and the technologies behind them.
8. Usage or Quick Start - the shortest path to a running product.
9. Configuration - parameter tables mapping CLI, environment, and config sources.
10. Repository Structure - the top-level directory layout.
11. Documentation - pointers to manuals, concepts, and guidelines.
12. Changelog - a pointer to the change history.
13. License and credits.

## Deltas From The Language Baseline

- A Download section may use a table mapping version, platform, and file.
- A Configuration section may use a table mapping each parameter across its CLI flag,
  environment variable, config key, and default.
- Point at `CHANGELOG.md`, manuals, and guidelines documents - do not duplicate their content.
- An ASCII banner or badges appear only when the project's convention already uses them.
- Keep run instructions copy-pasteable and ordered from prerequisites to first run.

## Section Names

| Section              | Requirement |
|----------------------|-------------|
| Contents             | optional    |
| Overview             | recommended |
| Download             | optional    |
| Installation         | recommended |
| Project Status       | optional    |
| Technical Stack      | optional    |
| Features             | recommended |
| Quick Start          | recommended |
| Usage                | recommended |
| Configuration        | optional    |
| Repository Structure | optional    |
| Documentation        | optional    |
| Changelog            | optional    |
| License              | recommended |
| Credits              | optional    |

Section names for other languages are declared in the matching `languages/<code>.md` file.
