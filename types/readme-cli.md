# CLI Tool README

## Purpose

> **Scope:** Conventions for the `README.md` of a command-line tool - a utility whose value is
> invoked through commands, subcommands, and flags
> **Key items:** install, commands table, options table, copy-pasteable examples

| Out of scope                    | See instead                   |
|---------------------------------|-------------------------------|
| General repository README       | `types/readme-general.md`     |
| Agent skill repository README   | `types/readme-skill.md`       |
| Software product README         | `types/readme-application.md` |
| Package and library README      | `types/readme-library.md`     |
| Documentation repository README | `types/readme-docs.md`        |
| Collection and monorepo README  | `types/readme-collection.md`  |

A CLI README serves a reader who wants to run commands now.

It leads with install, then the command surface, then real invocations.

## When To Use

Use for the root `README.md` of a command-line application, script, or developer tool whose
primary interface is a shell command.

For a larger product that also ships a CLI among other interfaces, prefer
`types/readme-application.md`.

**Templates**

- `templates/en/readme-cli-template-en.md`
- `templates/pl/readme-cli-template-pl.md`

## Structure

The canonical skeleton, adjusted to the request:

1. H1 title - the command name, optionally with a short tag line.
2. Short description - one line stating what the tool does.
3. Install - global and local install paths.
4. Commands - a table or list of subcommands and what each does.
5. Options - a table of flags with defaults and descriptions.
6. Examples - real invocations covering the common cases.
7. Configuration - config files and environment variables when the tool reads them.
8. License.

## Deltas From The Language Baseline

- Commands and Options use tables - command names and flags in inline code.
- Show the primary command first, then the rest.
- Examples are copy-pasteable and produce visible output - include expected output when it
  clarifies.
- A short demo (as text output or a linked recording) fits after the description when the
  project convention uses one.

## Section Names

- Overview
- Install
- Commands
- Options
- Examples
- Configuration
- License

Polish section names for this document type are declared in `languages/pl.md`.
