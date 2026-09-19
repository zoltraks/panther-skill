# Sphinx Documentation Layout

## Purpose

> **Scope:** Document work inside a Sphinx documentation project that authors its content in
> Markdown
> **Key items:** `docs/source/` pages, `index.rst` toctrees, kebab-case filenames, setext
> dialects, minimal `.rst` edits

A Sphinx project builds HTML documentation from source files.

Some projects author the content pages in Markdown while the navigation and configuration stay
in reStructuredText and Python.

Load this file when the task works inside such a documentation project.

## Detection

A repository matches this scope when it contains a Sphinx build configuration:

- `conf.py` setting `master_doc`, usually inside `docs/source/` or `doc/source/`
- an `index.rst` file containing a `.. toctree::` directive
- a `Makefile` or `make.bat` wrapping `sphinx-build`
- a `requirements.txt` listing `sphinx`

Any two of these signals are enough - `conf.py` plus `index.rst` is the strongest pair.

## Directory Roles

| Path                   | Role                                                 |
|------------------------|------------------------------------------------------|
| `docs/`                | Documentation root - `Makefile`, `requirements.txt`  |
| `docs/source/`         | Source pages - `conf.py`, `index.rst`, topic files   |
| `docs/source/<dir>/`   | Topic group - its own `index.rst` toctree plus pages |
| `docs/media/`          | Images and other binary assets referenced by pages   |
| `docs/source/_static/` | Static files copied into the build                   |
| `docs/build/`          | Generated output - never edit                        |

`conf.py`, `Makefile`, and `requirements.txt` are build files, not documents - do not edit them
for a document task.

## Page Conventions

Author and edit content in the `.md` pages only.

Page filenames use lowercase kebab-case, for example `base-text.md` or `attribute-command.md`.

This naming convention comes from the scope - it overrides the `languages/` file default for
pages inside the project.

The dominant dialect is setext headings (`Title` underlined with `=`, sections with `-`), with
closed ATX headings such as `### Name ###` appearing in some topic groups.

Detect the page's own dialect per `conventions/markdown-dialects.md` and preserve it - pages in
one project may mix dialects.

New pages follow the dominant dialect of the surrounding pages in the same directory.

## Toctree Registration

Adding a page requires registering it:

1. Create the `.md` page in `docs/source/` or in a topic subdirectory.
2. Add the filename without extension to the `.. toctree::` list in `index.rst`, or in the
   subdirectory's own `index.rst` for a topic-group page.
3. Place the entry in the thematic group it belongs to - toctree order defines the reading
   order of the built documentation.

Removing a page requires removing its toctree entry in the same file.

Edit `.rst` files only for these structural entries - the full contract lives in
`conventions/rst-documents.md`.

## Document Types In This Scope

| File                            | Type or handling                           |
|---------------------------------|--------------------------------------------|
| `index.rst`, sub-indexes        | Navigation - governed by this scope        |
| Topic and API pages             | `technical-document` type                  |
| Narrative guides, book chapters | `article-text` type                        |
| Standards pages                 | `rules-document` type                      |
| `license.md`                    | Verbatim legal text - preserve, no restyle |
| `conf.py`, `Makefile`, media    | Build files and assets - not documents     |

## Building

Running `sphinx-build` or `make html` is out of scope unless the request asks for it.

Report added or removed toctree entries in the delivery summary so the user can rebuild.
