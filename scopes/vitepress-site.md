# VitePress Site Layout

## Purpose

> **Scope:** Document work inside a VitePress documentation site - a Vue-based static site
> generator configured by a `.vitepress/` directory with file-based routing
> **Key items:** `.vitepress/` config, file-based routing, `index.md` homepages, frontmatter
> `layout` values, `srcDir` relocation

A VitePress site compiles every Markdown file into a page at the same path.

Navigation, sidebars, and the theme are configured inside the reserved `.vitepress/` directory.

Load this file when the task creates or edits pages inside such a site.

## Detection

A repository matches this scope when it contains all of the following:

- a `.vitepress/` directory, typically inside `docs/` or at the repository root
- a configuration file inside it, `config.js`, `config.ts`, or `config.mts`

The `.vitepress/` directory is the strongest signal - when it is nested, for example
`docs/.vitepress/`, the containing directory is the site's project root.

## Directory Roles

| Path                       | Role                                        |
|----------------------------|---------------------------------------------|
| `<root>/.vitepress/`       | Configuration, theme, and cache - see below |
| `<root>/*.md`              | Content pages, routed by file path          |
| `<root>/index.md`          | Site homepage served at the root path       |
| `<root>/<topic>/index.md`  | Topic homepage served at the topic path     |
| `<root>/.vitepress/cache/` | Dev-server cache - never edit, never commit |
| `<root>/.vitepress/dist/`  | Build output - never edit                   |

Inside `.vitepress/`, only `config.*` and the `theme/` directory are editable source - treat
everything else as generated.

The source directory may be relocated with the `srcDir` config option - read the config before
placing a new page, content may live in `src/` or another configured directory.

## Page Conventions

Page filenames use lowercase kebab-case, `index.md` serves as the homepage of its directory.

Routing is file-based - `docs/guide/getting-started.md` becomes the page at
`/guide/getting-started.html`, so hyphenated filenames keep the URLs clean.

A page carries YAML frontmatter, follow `conventions/markdown-dialects.md` - preserve its keys.

Frontmatter keys the generator reads:

- `title` - the page title and the `<title>` tag.
- `description` - the page meta description.
- `layout` - `doc` by default, `home` for the frontmatter-driven homepage, `page` for
  unstyled pages.
- `layout: home` pages carry a `hero` block and a `features` list in frontmatter - treat both
  as metadata and edit values only, never restructure.

Home pages are an exception to the prose rules - their visible content is generated from the
frontmatter, so the template shape is the convention to follow.

## Registration

No registration is needed - routing derives from the file tree, placing the file publishes the
page.

The navbar and sidebar are configured in the `theme` section of `.vitepress/config.*` - edit
them only when the task explicitly asks, and add the entry in the position the existing order
suggests.

## Document Types In This Scope

| File or directory            | Type or handling                           |
|------------------------------|--------------------------------------------|
| Doc pages                    | `technical-document` type                  |
| Tutorials, guides            | `article-text` type                        |
| `index.md` homepage          | `readme-file` type or home frontmatter     |
| `.vitepress/config.*`        | Build configuration - edit only when asked |
| `.vitepress/cache/`, `dist/` | Generated output - never edit              |

## Building

Running `vitepress dev` or `vitepress build` is out of scope unless the request asks for it.

Report navbar and sidebar entries changed in the delivery summary so the user can rebuild.
