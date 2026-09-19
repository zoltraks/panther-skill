# Panther - Document Authoring Skill

> Plain-text-readable Markdown documents - technical documentation, project specifications,
> rules documents, format specifications, articles, notes, READMEs, and changelogs, in English
> or Polish.
>
> [Versioning Policy](./VERSIONING.md)

## Contents

| Section             | Line | What it covers                            |
|---------------------|------|-------------------------------------------|
| What The Skill Does | 33   | Authoring purpose and workflow            |
| Core Principles     | 63   | Convention preservation and minimal diffs |
| When To Use         | 74   | Supported requests and exclusions         |
| Example Prompts     | 89   | Phrases the skill activates on            |
| What's Inside       | 107  | Rule files, templates, tools, and evals   |
| Verification        | 154  | Skill-maintenance checks                  |
| License             | 161  | License for the skill itself              |
| Credits             | 167  | Methodology and example sources           |

Panther is a document authoring process packaged as an agent skill.

It guides an AI coding agent through creating or editing a Markdown document with consistent,
plain-text-readable conventions: one sentence per paragraph, source-width-aligned tables, and
language-appropriate style rules.

Documents are written in English by default, with full Polish support, and new files use UTF-8.

The skill detects and preserves the encoding, line endings, and Markdown dialect of existing
documents - a file in UTF-16 or a legacy code page stays that way after an edit.

## What The Skill Does

When you ask for a document, the agent loads the skill and performs the following:

**Resolves parameters**

For a new document it confirms the type, language, filename, and encoding, with sensible
defaults. For an edit it skips the questions and follows the document's own conventions.

**Detects the document's conventions**

Encoding, byte order mark, line-ending style, and Markdown dialect (standard ATX, setext
headings, numbered chapters, export artifacts) are detected before any write.

**Selects the smallest rule set**

One language baseline plus one document-type file, loaded only when the document is a known
type. A simple note needs far less machinery than a project specification.

**Writes to the baseline**

Every language file covers structure, headings, lists, characters, tables, vocabulary, and file
naming. English uses Title Case headings, Polish uses sentence case, and each language carries
its own terminology guidance.

**Validates mechanically**

Tables are formatted by script, not by hand. A document validator checks structure, spacing,
characters, and table alignment before delivery.

## Core Principles

- **Plain text first** - the source must read well in a console before any renderer touches it.
- **The document's own conventions win** - existing dialects, numbering, encodings, and naming
  are preserved on edit.
- **Minimal diff** - changes stay inside the scope of the request.
- **Explicit unknowns** - missing information is marked `NOT SPECIFIED` or `TBD`, never
  invented.
- **One language file per document** - the matching `languages/` file is the authoritative style
  source.

## When To Use This Skill

| Situation                                         | Use this skill?                          |
|---------------------------------------------------|------------------------------------------|
| "Write a spec for this service"                   | **Yes**                                  |
| "Create a README for this repo"                   | **Yes**                                  |
| "Draft a Polish article about POKEY sound design" | **Yes**                                  |
| "Update the glossary in this spec"                | **Yes** - preserves document conventions |
| "Fix the tables in this document"                 | **Yes** - script-formatted tables        |
| "Translate this document to Polish"               | **Yes** - language baseline switch       |
| "Edit this CP1250-encoded document"               | **Yes** - encoding preserved             |
| "Take a quick note"                               | **Yes** - minimal-structure note         |
| "Write code for this feature"                     | No - this skill writes documents         |
| "Review this document for technical correctness"  | No - authoring skill, not an auditor     |

## Example Prompts

**New project specification**
> Write a project specification for a Go order-tracking service. Cover goals, non-goals,
> glossary, functional requirements, and design decisions.

**Polish article**
> Napisz artykuł o buforze cyklicznym z przykładem w systemie wbudowanym.

**Convention-preserving edit**
> Add a new functional requirement and use case to this numbered-chapter project document.

**Table reformatting**
> Fix the formatting of the tables in this document so they align in plain text.

**Quick note**
> Zapisz notatkę z planowania - trzy punkty i dwie pozycje otwarte.

## What's Inside

```
panther-skill/
├── SKILL.md                      # Root router - load this first
├── STYLE.md                      # Document style rules for all files in this skill
├── MAINTENANCE.md                # Skill extension and restructuring rules
├── VERSIONING.md                 # Skill versioning policy
├── principles/
│   └── authoring-rules.md        # Plain-text-first, convention preservation, minimal diff
├── process/
│   ├── document-workflow.md      # Intake, detection, rule selection, validation, delivery
│   └── document-checklist.md     # Mechanical pre-delivery checklist
├── types/
│   ├── technical-document.md     # Guides, architecture notes, reference material
│   ├── project-document.md       # Specifications: version comment, glossary, requirement IDs
│   ├── rules-document.md         # Guidelines and standards: imperative rules, examples
│   ├── format-specification.md   # Format specs: version history, field tables
│   ├── article-text.md           # Prose documents: narrative, dialect tolerance
│   ├── quick-note.md             # Quick notes: minimal structure
│   ├── readme-file.md            # Repository READMEs
│   └── changelog-file.md         # Version-grouped change records
├── languages/
│   ├── en.md                     # English baseline: Title Case, vocabulary
│   └── pl.md                     # Polish baseline: sentence case, diacritics, calques
├── conventions/
│   ├── file-encoding.md          # UTF-8 default, UTF-16/UCS-2, code pages, line endings
│   └── markdown-dialects.md      # ATX, setext, numbered chapters, export artifacts
├── templates/
│   ├── en/                       # Eight English skeletons, <type>-template-en.md
│   └── pl/                       # Eight Polish skeletons, <type>-template-pl.md
├── tools/
│   ├── detect-encoding.py        # BOM, encoding, and line-ending detection
│   ├── format-table.py           # Source-width table formatter
│   ├── validate-document.py      # Mechanical document checker
│   ├── validate-skill.py         # Skill metadata and disclosure validator
│   ├── check-references.py       # Root reference integrity checker
│   └── README.md                 # Tool classes, commands, and limits
└── evals/
    └── evals.json                # Behavioral regression prompts
```

Document-production tools are copied into the working repository under a `.tmp.` name, run
against the document, and removed afterward.

Skill-maintenance tools run from this repository only.

## Verification

- Run `python tools/validate-skill.py .` and `python tools/check-references.py .` after changing
  `SKILL.md`, `README.md`, or file layout.
- Exercise the regression prompts in `evals/evals.json` after structural changes.
- Run `python tools/validate-document.py <file>` on any document the skill produces.

## License

MIT - see [LICENSE](./LICENSE).

---

## Credits

Built by Filip Golewski.

Made at **KWAS #42**, a meeting at ATARI MUZEUM in Poznań, on 19 September 2026.

If you use this skill in a project, a link back is appreciated but not required.
