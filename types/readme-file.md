# README Document

## Purpose

> **Scope:** Conventions for repository and package `README.md` files - the entry point that
> orients a reader in the project
> **Key items:** title, purpose, contents, usage, license, conventional filename

A README is the first document a reader opens.

It answers three questions fast: what is this, how do I use it, where do I look next.

Typical shape: title, blockquote purpose, contents table, capability overview, usage table,
directory tree, license - like this skill's own `README.md`.

## When To Use

Use for the root `README.md` of a repository and for package-level READMEs in subdirectories.

**Templates**

- `templates/en/readme-file-template-en.md`
- `templates/pl/readme-file-template-pl.md`

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
