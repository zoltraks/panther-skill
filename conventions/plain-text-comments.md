# Plain-Text Comments

## Purpose

> **Scope:** Comment alignment inside fenced plain-text and shell blocks in documents created
> and edited with this skill
> **Key items:** shared comment column, dominant column, longest entry plus two spaces,
> compacting, per-block scope, `align-comments.py`

This file defines how `#` comments are placed inside directory trees, file listings, console
output, and shell snippets.

Load it when a document contains a fenced block whose lines carry trailing `#` comments, or
when the request asks to align, fix, or add such comments.

## When This Applies

The rule covers untagged fenced blocks - directory trees, file listings, diagrams, console
output, and other plain text.

It also covers blocks tagged `bash`, `sh`, `zsh`, `shell`, `console`, or `shellsession`, where
`#` is the comment character.

Every other tagged code block stays opaque - the rule does not guess at comment syntax for
programming or data languages.

## The Rule

Every commented line in the same fenced block starts its comment at the same column.

When most comments in a block already share a column, keep that column and align the
outliers to it - do not move the majority.

When no column is established, set the comment column from the longest entry in the block:
the comment begins exactly two spaces after the end of that entry.

Pad every shorter entry so its comment reaches the shared column.

Keep comment text short - a list of key items, not a full description.

Re-confirm or recompute the column and re-pad the block after adding, removing, or renaming
an entry.

Compacting the column left to the minimum - two spaces after the longest entry - is allowed
on request.

The rule applies per block: different fenced blocks may use different comment columns.

## Example

Correct - one shared column, longest entry keeps a two-space gap:

```
├── src/                          # Application sources
│   ├── main.py                   # Entry point
│   └── config.py                 # Settings loader
└── docs/                         # Documentation
    └── long-document-name.md     # Specification
```

Incorrect - comments drift to different columns:

```
├── src/                   # Application sources
│   ├── main.py        # Entry point
│   └── config.py                  # Settings loader
└── docs/  # Documentation
```

## Edge Cases

A standalone comment line - a `#` with no entry text before it - is not an entry and stays
untouched.

Inside shell-tagged blocks, a `#` comment is recognized only when preceded by at least two
spaces.

A single-space `#` is assumed to be inline content such as a quoted string and stays
untouched.

A `#` inside the comment text itself is part of the comment and never affects alignment.

## Reformatting

Use `tools/align-comments.py` to check and fix comment columns instead of counting by hand.

Copy it into the working repository as `align-comments.tmp.py`, run it on the document, and
remove the copy afterward - see `tools/README.md`.

Run `--check` to report misaligned comments without writing.

Run `--compact` to move every block's column to the minimum instead of keeping an
established one.
