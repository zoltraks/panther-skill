# Multi-Project Layout

## Purpose

> **Scope:** Document work inside a repository that holds several projects, each with its own
> documentation structure
> **Key items:** per-directory scope resolution, nearest governing `docs/` wins, sparse root,
> independent project conventions

A multi-project repository groups several projects under one root.

Each project directory may carry its own `docs/` tree, `README.md`, and conventions - or no
documentation at all.

Load this file when the task works inside such a repository.

## Detection

A repository matches this scope when it contains several top-level directories that each look
like an independent project - own sources, build files, `docs/`, or `README.md` - while the
root itself stays sparse.

The root typically holds a minimal `README.md` and cross-project material such as shared
format specifications in a root `docs/`.

## Scope Resolution

Resolve the scope per directory, not per repository.

Each project directory may independently match another scope - for example a subproject with
`docs/GUIDELINES.md` and versioned artifact directories matches `scopes/guided-project.md`.

The governing documents nearest to the file being written win: a subproject's own `docs/` rules
override anything at the repository root.

A subproject with no documentation structure falls back to `scopes/unstructured-layout.md`.

The root level follows `scopes/unstructured-layout.md` unless it matches a scope of its own.

## Working Rules

Never mix conventions across project boundaries - each project may follow its own document and
code style, and the nearest one applies.

Check for a guidelines document in the target subproject before writing, the same way a
standalone project would be checked.

Root-level documents cover cross-project concerns such as shared specifications and entry
links - place a document there only when it serves more than one subproject.

A new `README.md` or `docs/` inside one subproject does not change the conventions of its
siblings.

## Document Types In This Scope

| Location                 | Handling                                            |
|--------------------------|-----------------------------------------------------|
| Root `README.md`         | `readme-file` type - often minimal link lists       |
| Root `docs/` documents   | Per-document classification, cross-project material |
| Subproject documents     | Per the subproject's own detected scope             |
| Undocumented subprojects | `unstructured-layout` rules                         |
