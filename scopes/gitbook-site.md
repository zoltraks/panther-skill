# GitBook Site Layout

## Purpose

> **Scope:** Document work inside a GitBook project - a documentation space whose pages are
> listed in a `SUMMARY.md` outline that defines the reading order
> **Key items:** `SUMMARY.md` as the table of contents, `.gitbook.yaml` configuration, outline
> registration, relative page links

A GitBook project keeps its content as Markdown pages and its navigation as an outline file.

The `SUMMARY.md` file is the canonical table of contents - a page appears in navigation only
when the outline lists it.

Load this file when the task creates or edits pages inside such a project.

## Detection

A repository matches this scope when it contains all of the following:

- a `SUMMARY.md` file at the root containing a Markdown link outline of the project's pages
- optionally a `.gitbook.yaml` configuration file or a `book.json` file

The outline file is the strongest signal - a `SUMMARY.md` made of internal page links and
heading groups is a GitBook table of contents.

## Directory Roles

| Path            | Role                                             |
|-----------------|--------------------------------------------------|
| `SUMMARY.md`    | Canonical table of contents and reading order    |
| `<page>.md`     | Content pages at any path the outline references |
| `.gitbook.yaml` | Configuration - root, structure, and plugins     |
| `book.json`     | Legacy configuration file                        |

`SUMMARY.md` is a navigation document, not a content page - edit it only for entry changes, the
same contract Sphinx projects apply to `index.rst` toctrees.

## Page Conventions

Page filenames and directory structure follow the paths already used in the outline - new pages
follow the dominant naming style of the outline's existing entries.

A page carries YAML frontmatter, follow `conventions/markdown-dialects.md` - preserve its keys.

Pages link to each other with relative Markdown links, keep links consistent with the outline's
paths.

## Outline Registration

Adding a page requires registering it in `SUMMARY.md`:

1. Create the `.md` page at the path the outline structure suggests.
2. Add a `- [Page title](page-path.md)` entry in the position that defines the reading order.
3. Use a `## Section` or `# Part` heading line above a group of entries when the page starts a
   new group, matching the outline's existing group style.
4. Remove the entry when the page is removed.

The outline order is the reading order - place the entry where the page belongs, never
re-sort unrelated entries.

A page missing from the outline still renders when visited directly, but stays invisible in
navigation - report unlisted pages as exceptions when discovered.

## Document Types In This Scope

| File or directory            | Type or handling                             |
|------------------------------|----------------------------------------------|
| Content pages                | `technical-document` type                    |
| Tutorials, guides            | `article-text` type                          |
| `SUMMARY.md`                 | Navigation document - governed by this scope |
| `.gitbook.yaml`, `book.json` | Build configuration - edit only when asked   |

## Building

Running GitBook builds or synchronizing with the GitBook cloud is out of scope unless the
request asks for it.

Report added or removed outline entries in the delivery summary.
