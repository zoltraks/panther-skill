# Panther - Document Authoring Skill

> Plain-text-readable Markdown documents - technical documentation, project specifications,
> rules documents, format specifications, articles, notes, READMEs, and changelogs, in English
> or Polish.
>
> [Versioning Policy](./VERSIONING.md)

## Contents

| Section             | Line | What it covers                             |
|---------------------|------|--------------------------------------------|
| Overview            | 26   | What Panther is and what it produces       |
| What The Skill Does | 50   | Authoring purpose and workflow             |
| Installation        | 109  | How to add Panther to an agent environment |
| Usage               | 171  | How agents activate and run the skill      |
| Example Prompts     | 182  | Phrases the skill activates on             |
| Workflow Diagrams   | 216  | ASCII and Mermaid diagrams of the pipeline |
| Core Principles     | 341  | Convention preservation and minimal diffs  |
| When To Use         | 352  | Supported requests and exclusions          |
| What's Inside       | 389  | Rule files, templates, tools, and evals    |
| Verification        | 484  | Skill-maintenance checks                   |
| License             | 491  | License for the skill itself               |
| Credits             | 497  | Methodology and example sources            |

## Overview

Panther is a document authoring process packaged as an agent skill.

It guides an AI coding agent through creating or editing a Markdown document with consistent,
plain-text-readable conventions: one sentence per paragraph, source-width-aligned tables, and
language-appropriate style rules.

Documents are written in English by default, with full Polish support, and new files use UTF-8.

The skill detects and preserves the encoding, line endings, and Markdown dialect of existing
documents - a file in UTF-16 or a legacy code page stays that way after an edit.

Supported types cover technical documentation, project specifications, rules documents, agent
instruction documents, contributing guides, format specifications, articles, notes, READMEs,
changelogs, decision records, RFCs, and PMBOK artifacts - charters, registers, status reports,
meeting minutes, management plans, and work breakdown structures.

Supported project layouts cover agent skill repositories, Sphinx, MkDocs, Docusaurus,
VitePress, GitBook sites, guided projects, documentation collections, and multi-project
repositories.

AsciiDoc and reStructuredText documents follow a minimal-edit contract.

## What The Skill Does

When you ask for a document, the agent loads the skill and performs the following:

**Checks for updates**

Once per session, the agent runs a git self-update check on the skill's own repository and offers
to pull incoming commits before starting, when the skill lives in a git clone.

**Resolves parameters**

For a new document it confirms the type, language, filename, and encoding, with sensible
defaults. For an edit it skips the questions and follows the document's own conventions.

**Detects the document's conventions**

Encoding, byte order mark, line-ending style, and Markdown dialect (standard ATX, setext
headings, numbered chapters, export artifacts) are detected before any write.

**Detects the document scope**

When the task runs inside a project, its document layout is classified - an agent skill
repository, a Sphinx documentation project, or the unstructured default - and the matching
scope file governs where new documents go, how they are named, and which index files are
updated.

**Selects the smallest rule set**

One language baseline plus one document-type file, loaded only when the document is a known
type, plus a scope file when the project layout is organized. A simple note needs far less
machinery than a project specification.

**Writes to the baseline**

Every language file covers structure, headings, lists, characters, tables, vocabulary, and file
naming. English uses Title Case headings, Polish uses sentence case, and each language carries
its own terminology guidance.

**Validates mechanically**

Tables are formatted by script, not by hand. A document validator checks structure, spacing,
characters, and table alignment before delivery.

**Discovers document layouts**

Separately, when you ask to "discover layout" or "detect document layout", the agent analyzes a
directory or repository: it censuses layout signals and document types, compares them with
every defined scope, names the best match, and lists exceptions - missing expected directories
or documents no scope covers. The report is delivered inline, and a file is written only when
asked.

**Audits documents**

Separately, when you ask to "audit this document" or "check document formatting", the agent
follows `process/document-audit.md`: it runs mechanical checks and a structural census with
`tools/census-document.py`, evaluates the document against its governing rules, and reports
findings with an optional fix plan. An audit is analysis only - it changes nothing in the
document.

## Installation

Panther is a filesystem-based skill.

Agents load it by reading the directory and activating `SKILL.md` when a request matches a
trigger phrase.

Clone the repository into the agent's skills directory:

```bash
git clone https://github.com/zoltraks/panther-skill.git
```

### Agent Environments

**Devin and Windsurf**

Project skills live under `.devin/skills/`, `.windsurf/skills/`, or `.agents/skills/`:

```
your-project/
└── .devin/
    └── skills/
        └── panther-skill/
```

For a global install across all projects, use `~/.config/devin/skills/panther-skill/` instead.

**Claude Code**

Project skills live under `.claude/skills/`:

```
your-project/
└── .claude/
    └── skills/
        └── panther-skill/
```

For a personal install across all projects, use `~/.claude/skills/panther-skill/` instead.

**Other Agents**

Agents that follow the shared skills convention load project skills from `.agents/skills/`:

```
your-project/
└── .agents/
    └── skills/
        └── panther-skill/
```

### Updating

Once per session the skill checks its own git upstream and offers to pull incoming commits.

To update by hand, pull the clone wherever it was installed:

```bash
git -C <skills-dir>/panther-skill pull --ff-only
```

## Usage

Panther activates when a request matches any trigger phrase declared in `SKILL.md`.

Examples include "write a README", "draft a specification", "format this table", "quick note",
"write an ADR", "audit this document", and "run panther".

The skill performs an update check, resolves parameters, detects conventions and scope, selects
rule files, drafts the document, validates it mechanically, and delivers the file with preserved
encoding and line endings.

## Example Prompts

**New project specification**
> Write a project specification for a Go order-tracking service. Cover goals, non-goals,
> glossary, functional requirements, and design decisions.

**Architecture decision record**
> Write an ADR in docs/adr/ deciding between RabbitMQ and a Postgres-backed queue for the
> event pipeline. Include decision drivers, both options, and the consequences.

**Project risk register**
> Create a risk register for the payments migration project in docs/registers/. Define the
> probability and impact scales, then seed it with three risks - each with an owner and a
> response strategy.

**Article in Polish**
> Write a short article in Polish about the ring buffer, with a usage example in an embedded
> system.

**Convention-preserving edit**
> Add a new functional requirement and use case to this numbered-chapter project document.

**Table reformatting**
> Fix the formatting of the tables in this document so they align in plain text.

**Quick note**
> Take a quick planning note in Polish - three discussion points and two open items.

**New page in a documentation project**
> Add a page documenting the retry helpers to this Sphinx documentation project.

**Document audit**
> Audit this document's formatting against its governing rules and report the findings.

## Workflow Diagrams

The diagrams show the authoring pipeline for document tasks.

Layout discovery and document audits follow their own standalone procedures in
`process/scope-discovery.md` and `process/document-audit.md`.

### ASCII Diagram

```
         ┌──────────────────────────┐
         │   User Request Arrives   │
         │ (e.g., "write a README") │
         └────────────┬─────────────┘
                      │
                      ▼
      ┌───────────────────────────────┐       ┌───────────────────────┐
      │     Trigger Phrase Match?     │  No   │ Not a Panther request │
      │ (SKILL.md activation phrases) │──────▶│  Skill not activated  │
      └───────────────┬───────────────┘       └───────────────────────┘
                      │ Yes
                      ▼
          ┌───────────────────────┐
          │ Session Update Check  │
          │ tools/check-update.py │
          └───────────┬───────────┘
                      │
                      ▼
      ┌───────────────────────────────┐
      │     Load Mandatory Files      │
      │ principles/authoring-rules.md │
      │ process/document-workflow.md  │
      └───────────────┬───────────────┘
                      │
                      ▼
   ┌────────────────────────────────────┐
   │           Classify Task            │
   │ create, edit, reformat, translate, │
   │ discover, audit                    │
   └──────────────────┬─────────────────┘
                      │
                      ▼
        ┌───────────────────────────┐
        │   Parameter Resolution    │
        │ - type                    │
        │ - language                │
        │ - scope                   │
        │ - filename                │
        │ - encoding / line endings │
        └─────────────┬─────────────┘
                      │
                      ▼
     ┌──────────────────────────────────┐
     │   Detect Document Conventions    │
     │ tools/detect-encoding.py         │
     │ conventions/markdown-dialects.md │
     └────────────────┬─────────────────┘
                      │
                      ▼
      ┌───────────────────────────────┐
      │ Detect Project Layout (Scope) │
      │ tools/detect-scope.py         │
      │ scopes/<scope>.md             │
      └───────────────┬───────────────┘
                      │
                      ▼
          ┌───────────────────────┐
          │    Select Rule Set    │
          │ - language baseline   │
          │ - document type rules │
          │ - scope rules         │
          └───────────┬───────────┘
                      │
                      ▼
  ┌───────────────────────────────────────┐
  │            Draft Document             │
  │ - templates/<lang>/<type>-template.md │
  │ - minimal diff for edits              │
  └───────────────────┬───────────────────┘
                      │
                      ▼
       ┌────────────────────────────┐
       │   Mechanical Validation    │
       │ tools/format-table.py      │
       │ tools/wrap-prose.py        │
       │ tools/validate-document.py │
       │ tools/diff-content.py      │
       └──────────────┬─────────────┘
                      │
                      ▼
   ┌────────────────────────────────────┐
   │              Delivery              │
   │ - write file                       │
   │ - preserve encoding & line endings │
   └────────────────────────────────────┘
```

### Mermaid Diagram

```mermaid
flowchart TD

    A[User Request<br/>e.g., 'write a README'] --> B{Trigger Phrase Match?}
    B -->|Yes| C[Session Update Check<br/>tools/check-update.py]
    C --> D[Load Mandatory Files<br/>principles/authoring-rules.md<br/>process/document-workflow.md]

    D --> D2[Classify Task<br/>create, edit, reformat,<br/>translate, discover, audit]

    D2 --> E[Parameter Resolution<br/>type, language, scope,<br/>filename, encoding, line endings]

    E --> F[Detect Document Conventions<br/>tools/detect-encoding.py<br/>conventions/markdown-dialects.md]

    F --> G[Detect Project Layout (Scope)<br/>tools/detect-scope.py<br/>scopes/<scope>.md]

    G --> H[Select Rule Set<br/>language baseline<br/>document type rules<br/>scope rules]

    H --> I[Draft Document<br/>templates/<lang>/<type>-template.md<br/>minimal diff for edits]

    I --> J[Mechanical Validation<br/>tools/format-table.py<br/>tools/wrap-prose.py<br/>tools/validate-document.py<br/>tools/diff-content.py]

    J --> K[Delivery<br/>write file<br/>preserve encoding & line endings]

    B -->|No| Z[Not a Panther request<br/>Skill not activated]
```

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

| Situation                                        | Use this skill?                          |
|--------------------------------------------------|------------------------------------------|
| "Write a spec for this service"                  | **Yes**                                  |
| "Create a README for this repo"                  | **Yes**                                  |
| "Draft a Polish article about sound design"      | **Yes**                                  |
| "Update the glossary in this spec"               | **Yes** - preserves document conventions |
| "Update this agent instruction document"         | **Yes** - dual-audience conventions      |
| "Write a CONTRIBUTING.md"                        | **Yes** - contributor-guide conventions  |
| "Fix the tables in this document"                | **Yes** - script-formatted tables        |
| "Translate this document to Polish"              | **Yes** - language baseline switch       |
| "Edit this CP1250-encoded document"              | **Yes** - encoding preserved             |
| "Take a quick note"                              | **Yes** - minimal-structure note         |
| "Add a page to this Sphinx docs project"         | **Yes** - toctree registration           |
| "Add a page to this MkDocs site"                 | **Yes** - `nav` registration             |
| "Add a page to this Docusaurus site"             | **Yes** - sidebar and frontmatter        |
| "Add a page to this VitePress site"              | **Yes** - file-based routing             |
| "Add a page to this GitBook project"             | **Yes** - `SUMMARY` outline registration |
| "Write an ADR for this technology choice"        | **Yes** - status lifecycle, numbering    |
| "Draft an RFC for the new service"               | **Yes** - review states, open questions  |
| "Edit this AsciiDoc file"                        | **Yes** - minimal-edit contract          |
| "Add a rule file to this skill repository"       | **Yes** - `SKILL.md` registration        |
| "Write an implementation plan for this release"  | **Yes** - versioned `docs/plan/` entry   |
| "Add a standard to this documentation repo"      | **Yes** - `docs/standard/` conventions   |
| "Write the project charter for this initiative"  | **Yes** - SMART objectives, approval     |
| "Create a risk register for this project"        | **Yes** - append-only entry table        |
| "Write our weekly status report"                 | **Yes** - RAG ratings, decisions needed  |
| "Write up the steering committee minutes"        | **Yes** - decisions and action items     |
| "Create the WBS for phase one"                   | **Yes** - decimal codes, dictionary      |
| "Draft the risk management plan"                 | **Yes** - thresholds and cadence         |
| "What document layout does this repo use?"       | **Yes** - scope discovery report         |
| "Audit this document"                            | **Yes** - findings and optional fix plan |
| "Check this document's formatting"               | **Yes** - audit procedure                |
| "Write code for this feature"                    | No - this skill writes documents         |
| "Review this document for technical correctness" | No - authoring skill, not an auditor     |

## What's Inside

```
panther-skill/
├── SKILL.md                         # Root router - load this first
├── STYLE.md                         # Document style rules for all files in this skill
├── MAINTENANCE.md                   # Skill extension and restructuring rules
├── VERSIONING.md                    # Skill versioning policy
├── principles/
│   └── authoring-rules.md           # Plain-text-first, convention preservation, minimal diff
├── process/
│   ├── document-workflow.md         # Intake, detection, rule selection, validation, delivery
│   ├── document-checklist.md        # Mechanical pre-delivery checklist
│   ├── document-audit.md            # Standalone audit procedure: findings and fix plan
│   └── scope-discovery.md           # Standalone layout-discovery procedure and report format
├── types/
│   ├── technical-document.md        # Guides, architecture notes, reference material
│   ├── project-document.md          # Specifications: version comment, glossary, requirement IDs
│   ├── rules-document.md            # Guidelines and standards: imperative rules, examples
│   ├── agent-instruction.md         # Agent-executable docs: dual audience, decision menus
│   ├── format-specification.md      # Format specs: version history, field tables
│   ├── article-text.md              # Prose documents: narrative, dialect tolerance
│   ├── quick-note.md                # Quick notes: minimal structure
│   ├── readme-general.md            # Default repository README variant
│   ├── readme-skill.md              # Agent skill repository READMEs
│   ├── readme-application.md        # Software product READMEs
│   ├── readme-library.md            # Package and library READMEs
│   ├── readme-cli.md                # Command-line tool READMEs
│   ├── readme-docs.md               # Documentation repository READMEs
│   ├── readme-collection.md         # Collection and monorepo READMEs
│   ├── changelog-file.md            # Version-grouped change records
│   ├── contributing-file.md         # CONTRIBUTING.md guides: PR rules, AI-assisted policy
│   ├── decision-record.md           # ADRs: status lifecycle, numbered records
│   ├── proposal-document.md         # RFCs: review states, open questions
│   ├── project-charter.md           # Charters: SMART objectives, approval block
│   ├── register-log.md              # Registers and logs: entry tables, lifecycles
│   ├── status-report.md             # Status reports: RAG ratings, decisions needed
│   ├── meeting-minutes.md           # Minutes: attendees, decisions, action items
│   ├── management-plan.md           # Management plans: thresholds, cadence, roles
│   └── work-breakdown-structure.md  # WBS: decimal outline, dictionary, RACI
├── languages/
│   ├── en.md                        # English baseline: Title Case, vocabulary
│   └── pl.md                        # Polish baseline: style, section names, activation phrases
├── scopes/
│   ├── unstructured-layout.md       # Default scope: no defined organization
│   ├── agent-skill.md               # Skill repositories: router contract, registration
│   ├── sphinx-docs.md               # Sphinx Markdown docs: toctree registration
│   ├── guided-project.md            # Governed docs/ trees: GUIDELINES, versioned artifacts
│   ├── docs-collection.md           # Documentation-only repositories
│   ├── multi-project.md             # Several projects per repository, per-dir scope
│   ├── mkdocs-site.md               # MkDocs sites: nav registration
│   ├── docusaurus-site.md           # Docusaurus sites: sidebars, frontmatter
│   ├── vitepress-site.md            # VitePress sites: file-based routing
│   └── gitbook-site.md              # GitBook projects: SUMMARY.md registration
├── conventions/
│   ├── file-encoding.md             # UTF-8 default, UTF-16/UCS-2, code pages, line endings
│   ├── markdown-dialects.md         # ATX, setext, numbered chapters, frontmatter, payloads
│   ├── rst-documents.md             # reStructuredText minimal-edit contract
│   ├── asciidoc-documents.md        # AsciiDoc minimal-edit contract
│   ├── plain-text-comments.md       # Trailing comment alignment in plain-text blocks
│   └── ascii-diagrams.md            # Box-drawing flow diagram rules
├── templates/
│   ├── en/                          # Twenty-four English skeletons, <type>-template-en.md
│   └── pl/                          # Twenty-four Polish skeletons, <type>-template-pl.md
├── tools/
│   ├── detect-encoding.py           # BOM, encoding, and line-ending detection
│   ├── detect-scope.py              # Document-scope signal census
│   ├── census-document.py           # Structural document census for audits
│   ├── wrap-prose.py                # Split-only line wrapper for width conventions
│   ├── format-table.py              # Source-width table formatter
│   ├── align-comments.py            # Plain-text block comment aligner
│   ├── validate-document.py         # Mechanical document checker
│   ├── diff-content.py              # Token-stream content-integrity diff
│   ├── validate-skill.py            # Skill metadata and disclosure validator
│   ├── check-references.py          # Root reference integrity checker
│   ├── check-contents.py            # Contents-table line-number drift checker
│   ├── check-update.py              # Git upstream self-update checker for the skill repo
│   └── README.md                    # Tool classes, commands, and limits
└── evals/
    └── evals.json                   # Behavioral regression prompts
```

Document-production tools are copied into the working repository under a `.tmp.` name, run
against the document, and removed afterward.

Skill-maintenance tools run from this repository only.

`SKILL.md` is the router and taxonomy for the whole skill.

`principles/authoring-rules.md` and `process/document-workflow.md` are mandatory reading for
every document task.

Type rules, language baselines, scope rules, encoding conventions, templates, and tools load
only as the workflow requires them.

## Verification

- Run `python tools/validate-skill.py .`, `python tools/check-references.py .`, and
  `python tools/check-contents.py .` after changing `SKILL.md`, `README.md`, or file layout.
- Exercise the regression prompts in `evals/evals.json` after structural changes.
- Run `python tools/validate-document.py <file>` on any document the skill produces.

## License

MIT - see [LICENSE](./LICENSE).

---

## Credits

Built by Filip Golewski.

Made at **KWAS #42**, a meeting at ATARI MUZEUM in Poznań, on 19 September 2026.

If you use this skill in a project, a link back is appreciated but not required.
