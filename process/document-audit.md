# Document Audit

## Purpose

> **Scope:** The standalone procedure for auditing a single document against its governing
> rules
> **Key items:** mechanical checks, structural census, convention evaluation, content review,
> findings, fix plan, report

An audit answers "how well does this document follow the rules that govern it".

It is analysis only - it changes nothing in the audited location.

Use it when the request asks to audit, check, review, or assess a document's formatting,
structure, conformance, or content quality.

## Target Resolution

The target is the document named by the request.

When the request names none, the target is the file the request centers on.

Markdown documents get the full procedure.

Other formats get a limited census - encoding and characters only - reported with a `Note`
finding that coverage was partial.

## Governing Rules

Read the target repository's own rule documents first.

Candidates are `README.md`, `AGENTS.md`, and rule files the repository declares, such as
`GUIDELINES.md`, `STYLE.md`, or `TABLE.md` inside a docs tree.

The document's own conventions win over skill defaults.

Where the repository is silent, the matching `languages/` baseline and `types/` file supply
the defaults.

Directories the repository marks frozen or excluded stay out of scope unless the request
names them - an `archive/` tree is the common case.

## Mechanical Checks

Copy the document-production tools into the working repository as `.tmp.` copies, see
`tools/README.md` and the File Handling Contract in `principles/authoring-rules.md`.

Run them on the target:

```text
python detect-encoding.tmp.py <file>
python validate-document.tmp.py <file>
python wrap-prose.tmp.py <file> --check --width <convention-or-100>
python format-table.tmp.py <file> --check
```

Add `--payload-markdown` to `validate-document.py` and `format-table.py` when the document
carries ` ```markdown ` payload blocks.

The width comes from the repository's own convention - 100 when it declares none.

Record every `PASS`, `WARN`, and `FAIL` for the report.

## Structural Census

Copy `tools/census-document.py` as `census-document.tmp.py` and run it on the target.

```text
python census-document.tmp.py <file> --width <convention-or-100>
```

The output lists heading counts and violations, list markers, fenced blocks and payloads,
special characters, paragraph shape, tables, task markers, and internal links.

Add `--payload-markdown` when the request covers payload interiors.

## Convention Evaluation

Compare the mechanical results and the census against the governing rules.

Distinguish a violation from an in-document convention.

A rule broken once is a violation.

A rule broken systematically and consistently - em-dashes everywhere, paired short sentences
throughout - is a convention the document adopted.

Report conventions as `Minor` or `Note` findings that name the diverging rule.

Never normalize them silently.

## Content Review

Read the document for content quality after the mechanical pass.

Report only observations with line evidence - never taste judgments:

- clarity - vague instructions, undefined terms on first use, ambiguous references
- completeness - sections the document type expects but the document lacks, empty headings,
  unfilled placeholders
- consistency - contradictory statements, version numbers that disagree between sections
- redundancy - the same statement repeated across sections

The review is best-effort - report what surfaces, do not grade every sentence.

## Findings

Structure every finding the same way:

| Column          | Content                                          |
|-----------------|--------------------------------------------------|
| ID              | `FINDING-001`, `FINDING-002`, ...                |
| Severity        | `Critical`, `Major`, `Minor`, or `Note`          |
| Finding         | one sentence naming the problem                  |
| Evidence / Rule | line references plus the rule source that judges |

Number findings `FINDING-001` style by default.

Use the compact `F-01` style when the request or the report context prefers short IDs.

Never mix the two styles in one report.

Severity levels:

- `Critical` - the document is broken or unusable, for example wrong encoding or unreadable
  content
- `Major` - a clear rule violation, for example a missing H1 or a dead internal link
- `Minor` - a style divergence from a stated or default rule
- `Note` - an observation or usability gap, for example no Contents section in a very long
  document

## Fix Plan

Produce a Fix Plan section only when the request asks for one.

Map every finding to a fix:

| Column       | Content                                      |
|--------------|----------------------------------------------|
| Finding      | the finding ID                               |
| Action       | the concrete edit that resolves it           |
| Scope        | the lines or sections the edit touches       |
| Verification | the tool or check that re-proves conformance |

Order the plan by severity - `Critical` first, `Note` last.

Note explicitly that executing the plan is an Edit task the user must approve.

The audit never applies fixes itself.

## Report

Deliver the report inline unless the request asks for a file.

A file goes to the location the request names - a conventional name such as
`docs/report/AUDIT-1.0.md` is allowed when the target carries a report tree.

Structure every report the same way:

1. **Verdict** - the conformance summary and whether the document is clean, divergent, or
   broken.
2. **Document Facts** - path, scope, type, language, encoding, line endings, size.
3. **Mechanical Results** - every tool run and its `PASS`, `WARN`, or `FAIL`.
4. **Structural Census** - the census numbers that matter.
5. **Findings** - the findings table.
6. **Content Review** - the evidence-based observations.
7. **Fix Plan** - present only when requested.
8. **Limitations** - what was not checked and why.

## Non-Goals

An audit does not modify the audited location.

It performs no registration or index updates - those belong to document tasks.

It is not a security review, code audit, or production-readiness assessment - those belong to
lens-skill.

It does not re-ask after a declined fix plan, and it never applies the plan it writes.
