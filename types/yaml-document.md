# YAML Document

## Purpose

> **Scope:** Conventions for YAML documents - configuration files, specifications, pipelines,
> and manifests written in the YAML data language rather than Markdown
> **Key items:** two-space indentation, minimal quoting, comment placement, key ordering,
> minimal-diff edits, scalar pitfall awareness

A YAML document is a data file, not a prose document.

The Markdown conventions of the language baseline - headings, sentence-per-paragraph prose,
source-width tables - do not apply inside one.

What carries over is the skill's core contract: plain-text readability, encoding and
line-ending preservation, minimal diffs, and no invented content.

## When To Use

Use for `.yaml` and `.yml` files: configuration files, OpenAPI and AsyncAPI specifications,
CI/CD pipelines, container manifests, Ansible playbooks, and similar data documents.

For a Markdown document that carries a YAML frontmatter block the file stays a Markdown
document - `conventions/markdown-dialects.md` governs the frontmatter payload, while this
file governs documents that are themselves YAML.

**Templates**

- `templates/en/yaml-document-template-en.md`
- `templates/pl/yaml-document-template-pl.md`
- `templates/de/yaml-document-template-de.md`

## Document Shape

A new YAML document starts directly with data - there is no title and no prose preamble.

An optional header comment block names the file's purpose:

```yaml
# Application configuration for the example-service component.
# Owner: platform team.
```

A document-start marker `---` is optional for a single-document file and required between the
documents of a multi-document stream.

Keep top-level keys in a deliberate order - by domain grouping or by the order the consuming
tool documents - and explain non-obvious values with comments.

## Syntax Rules

Author new YAML files with these conventions:

- Two spaces per indentation level, never tabs.
- Mappings as `key: value`, sequences as `- item` at the parent key's indentation.
- Prefer unquoted scalars, quote only when the value would otherwise parse wrong.
- Quote scalars containing `: ` or ` #`, scalars starting with indicator characters (`*`,
  `&`, `!`, `%`, `@`, `` ` ``), values with leading or trailing spaces, and values that read
  as another type - `y`, `n`, `on`, `off`, `null`, `~`, and numbers such as `1.10` that must
  stay strings.
- Canonical booleans `true` and `false` - avoid `yes`/`no`/`on`/`off` even though YAML 1.1
  accepts them.
- Null as `null` or an empty value, following the file's own convention.
- Multi-line strings through block scalars: `|` literal keeps line breaks, `>` folded joins
  them - pick deliberately, never accidentally.
- Comments start with `# ` after at least one space, and full-line comments sit at the
  indentation of the block they describe.
- Anchors (`&name`), aliases (`*name`), and merge keys (`<<`) are allowed where the consuming
  tool supports them - add a short comment when a merge hides keys.
- A single trailing newline, no trailing whitespace, UTF-8 without BOM for new files - the
  general contract in `conventions/file-encoding.md`.

## Editing Existing Files

On edit the document's own conventions win - the minimal-edit contract applies:

- Preserve the file's indentation width, quoting style, comment alignment, blank-line
  grouping, and key order - never re-indent or re-sort on an edit request.
- Preserve existing anchors, aliases, merge keys, tags, and document markers verbatim.
- Insert new keys where the file's existing order suggests them, matching the surrounding
  style - not blindly at the end, and never reordering existing keys.
- Quote a new value only when the syntax requires it or the file's conventions do so.
- Never strip comments, and never rewrite comments the request did not name.

## Validation

The mechanical battery from `process/document-checklist.md` targets Markdown structure and
does not run against `.yaml` files.

File-level guarantees still hold: encoding, byte order mark, line endings, trailing
whitespace, and a final newline - `scripts/detect-encoding.py` applies as usual.

Python's standard library ships no YAML parser, so syntax validation is the author's
responsibility: check indentation consistency, every `key:` followed by a space or a line
end, and the scalar pitfalls listed above.

When a PyYAML installation happens to be available, an ad-hoc parse
(`python -c "import yaml,sys; yaml.safe_load(open(sys.argv[1], encoding='utf-8'))" file.yaml`)
verifies syntax before delivery - an option, never a requirement, and it must not swallow
errors silently.

Schema validation - whether keys satisfy an OpenAPI, Kubernetes, or pipeline contract - stays
out of scope for this skill.

## Deltas From The Language Baseline

- Prose rules do not apply: no headings, no sentence-per-paragraph, no Markdown tables or
  lists - the syntax rules above replace them.
- Comments are the only prose inside the file: write them in the document's language and
  keep them free of semicolons when they form full sentences.
- Section planning does not apply: a YAML file's structure is its key layout, resolved with
  the request rather than a section-name table.
- Unknown values are never invented - leave an explicit `TBD` placeholder or an empty key
  the request names, per `principles/authoring-rules.md`.

## Section Names

A YAML document carries no Markdown headings, so no section vocabulary exists.

The section set is open - headings inside a `.yaml` file come from its data, not from
document structure:

| Section              | Requirement |
|----------------------|-------------|
| Document Information | unusual     |
| Version History      | unusual     |
| Contents             | unusual     |

Section names for other languages are declared in the matching `languages/<code>.md` file.
