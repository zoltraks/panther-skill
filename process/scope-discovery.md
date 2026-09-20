# Scope Discovery

## Purpose

> **Scope:** The standalone procedure for discovering the document layout of a directory or
> repository
> **Key items:** signal census, scope comparison, document type census, exceptions, report

Discovery answers "which scope describes this location best".

It is analysis only - it changes nothing in the analyzed location.

Use it when the request asks to discover, detect, or identify the document layout or scope of a
location, or to analyze its document structure.

## Target Resolution

The target is the directory or repository named by the request.

When the request names none, the target is the working directory or the repository root.

## Signal Census

Copy `tools/detect-scope.py` into the working repository as `detect-scope.tmp.py`, see
`tools/README.md`.

Run it on the target:

```text
python detect-scope.tmp.py <target>
```

The output lists which detection signals each scope expects and which are present, plus a
document census of the location.

When the target declares a temporary-file directory (for example `work/` in its guidelines or
`.gitignore`) that does not exist yet, create it for the `.tmp.` copy instead of falling back
to the repository root.

Remove the `.tmp.` copy when the analysis is done.

## Scope Comparison

Compare the census with the `## Detection` section of every `scopes/` file.

The best match is the scope whose signals are present.

Report a partial match as partial - name the scope and the missing signals.

When several scopes match partially, name the closest and say why - never guess silently.

`unstructured-layout` is the verdict when nothing matches.

In a multi-project repository, produce a verdict per project directory, not one for the whole
repository - run the census on each project directory that carries its own `docs/` or `README.md`.

## Document Type Census

Classify the observed documents against the `types/` files and the winning scope's Document
Types map.

Work from file names and the scope's map - do not read files under directories the target's
rules mark as restricted, for example versioned artifact directories in a guided project.

Note documents that no type covers - they are exceptions to report, not new types to invent.

## Declared Elements

Compare the census with elements the target declares but does not carry.

Read the target's governing documents and `.gitignore` for declared directories and files - a
temporary `work/` directory, expected `docs/` subdirectories, named index files.

Report declared-but-absent elements under Exceptions.

## Consistency Scan

Scan the visible document set for drift and report findings under Exceptions:

- version comments that disagree with the version directory holding the file
- the newest artifact version ahead of or behind the version named by `README.md` or
  `CHANGELOG.md`
- stale absolute paths and contradictory figures between documents

The scan is best-effort - report what surfaces, do not audit every file.

## Exception Analysis

Report deviations in both directions:

- Expected elements missing, for example a guided project without `docs/report/` or a skill
  without `evals/`.
- Present elements no scope covers, for example undocumented subtrees, non-document artifacts
  such as API specifications and configs, or directories outside the scope's map.
- Convention conflicts, for example mixed dialects or naming styles inside one document set.

## Report

Deliver the report inline unless the request asks for a file.

A file goes to the location the request names - a conventional name such as `LAYOUT.md` is
allowed.

Structure every report the same way:

1. **Verdict** - the best-match scope, the basis, and whether the match is full, partial, or
   closest.
2. **Signals** - matched and missing signals per candidate scope.
3. **Document Types** - observed documents mapped to types.
4. **Exceptions** - missing expected elements, uncovered extras, conflicts.
5. **Rule Selection** - the `scopes/` and `types/` files that would govern document work here.

## Non-Goals

Discovery does not modify the analyzed location.

It performs no registration or index updates - those belong to document tasks.

It does not validate or fix documents - report findings only.
