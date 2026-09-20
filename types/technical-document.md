# Technical Document

## Purpose

> **Scope:** Conventions for general technical documentation - guides, how-tos, architecture
> notes, API descriptions, and reference material
> **Key items:** purpose-first structure, progressive detail, example blocks

A technical document explains a system, a feature, or a procedure to a technical reader.

This is the default type for documentation that does not match a more specific type.

## When To Use

Use for developer guides, architecture overviews, setup instructions, API documentation, and
reference material.

**Templates**

- `templates/en/technical-document-template-en.md`
- `templates/pl/technical-document-template-pl.md`

## Structure

The canonical skeleton, adjusted to the request:

1. H1 title - the topic, not the document kind.
2. Purpose - one paragraph stating what the document covers.
3. Overview or context - what the reader needs to know first.
4. Main content sections - H2 topics, H3 subtopics, ordered from general to specific.
5. Examples - fenced blocks with language tags.

## Deltas From The Language Baseline

- Order sections from what the reader needs first to what they need last.
- Put commands, file paths, and identifiers in inline code, put runnable commands in fenced
  `bash` or `text` blocks.
- Prefer a table for enumerations of options, parameters, or fields.
- Keep each section self-contained enough to be found by search, do not rely on pronouns that
  resolve only in earlier sections.

## Diataxis Mapping

Documentation organized per the Diataxis framework maps onto this skill's types:

| Diataxis kind                                    | Panther handling                                |
|--------------------------------------------------|-------------------------------------------------|
| Tutorial - learning-oriented lesson              | `article-text` type                             |
| How-to guide - task-oriented, problem-first      | `technical-document` with a steps-first Usage   |
| Reference - information-oriented, dry facts      | `technical-document` with reference tables      |
| Explanation - understanding-oriented, discursive | `technical-document` overview or `article-text` |

When a project organizes docs into Diataxis quadrants - `docs/tutorials/`, `docs/how-to/`,
`docs/reference/`, `docs/explanation/` - place a new document in the directory matching its
kind and follow the dominant style of that directory.

## Section Names

- Purpose
- Overview
- Prerequisites
- Configuration
- Usage
- Examples
- Troubleshooting
- Limitations
- References

Polish section names for this document type are declared in `languages/pl.md`.
