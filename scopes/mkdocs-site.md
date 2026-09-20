# MkDocs Site Layout

## Purpose

> **Scope:** Document work inside an MkDocs documentation site - a project that builds its
> documentation from Markdown pages in a `docs/` directory configured by `mkdocs.yml`
> **Key items:** `mkdocs.yml` nav registration, `docs/index.md` homepage, kebab-case pages,
> file-path URLs

An MkDocs site renders a `docs/` directory into a static documentation website.

Navigation is either listed explicitly in the `mkdocs.yml` `nav` key or generated from the
directory tree.

Load this file when the task creates or edits pages inside such a site.

## Detection

A repository matches this scope when it contains all of the following:

- an `mkdocs.yml` or `mkdocs.yaml` file, at the repository root or one level deep
- a `site_name` key inside that configuration file
- a `docs/` directory holding Markdown pages, with `docs/index.md` as the homepage

The configuration file is the strongest signal - the other two may be missing in a partially
set up project.

When a software project with a `docs/GUIDELINES.md` tree also carries `mkdocs.yml`, this scope
governs placement and registration while the guidelines document still governs project rules.

## Directory Roles

| Path                    | Role                                               |
|-------------------------|----------------------------------------------------|
| `mkdocs.yml`            | Site configuration and the `nav` page list         |
| `docs/`                 | Content pages, the site payload                    |
| `docs/index.md`         | Homepage served at the site root                   |
| `docs/<topic>/`         | Topic directory - its pages group in navigation    |
| `docs/<topic>/index.md` | Topic homepage, serves as the section landing page |
| `docs/` media           | Images and assets referenced by relative path      |

`mkdocs.yml` is build configuration, not a document - edit only the `nav` section for a
document task.

## Page Conventions

Author and edit content in the `.md` pages.

Page filenames use lowercase kebab-case, for example `retry-helpers.md` or
`installation-guide.md`.

This convention comes from the scope - the URL of a page derives from its file path, so hyphens
in the filename keep the URLs clean.

`index.md` serves as the homepage of its directory.

A page carrying YAML frontmatter follows `conventions/markdown-dialects.md` - preserve its keys.

## Nav Registration

When `mkdocs.yml` defines a `nav` key, adding a page requires registering it:

1. Create the `.md` page in `docs/` or in a topic subdirectory.
2. Add the page's path relative to `docs/` to the `nav` list, in the entry and position that
   define the section and the reading order.
3. Remove the entry when the page is removed.

When no `nav` key is defined, navigation is generated from the directory structure and no
registration is needed - placing the file is enough.

Never reorder unrelated `nav` entries, the nav order defines the site's reading order.

## Document Types In This Scope

| File or directory          | Type or handling                           |
|----------------------------|--------------------------------------------|
| Topic and guide pages      | `technical-document` type                  |
| Tutorials, narrative pages | `article-text` type                        |
| `docs/index.md`            | `readme-file` type - the site landing page |
| `mkdocs.yml`               | Build configuration - nav edits only       |
| `site/` directory          | Generated output - never edit              |

## Building

Running `mkdocs serve` or `mkdocs build` is out of scope unless the request asks for it.

Report added or removed `nav` entries in the delivery summary so the user can rebuild.
