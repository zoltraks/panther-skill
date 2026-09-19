# Unstructured Layout

## Purpose

> **Scope:** The default document scope - a project or directory with no defined organization of
> documents or document types
> **Key items:** request-driven placement, language-file naming, no registration side effects

This is the baseline scope.

It applies when no other scope's detection signals match, or when the task names a single file
or directory without a document structure.

Loading this file changes nothing about the base workflow - it documents the default explicitly
so every scope in `scopes/` is a file.

## Detection

This scope applies by default.

No detection signals are required - it is the fallback when `SKILL.md` frontmatter, Sphinx build
files, and other project markers are absent.

## Rules

Place a new file where the request names it.

When the request is silent on location, place the file in the working directory or alongside the
documents it relates to.

Name the file per the matching `languages/` file naming rules, type-conventional names such as
`README.md` or `CHANGELOG.md` stay allowed.

No registration, index, or navigation update follows a document change in this scope.

Apply `types/` files per document as usual - the absence of project organization does not change
how a single document is shaped.

## Document Types

Any document type may appear in an unstructured layout.

There is no fixed map - classify each document on its own, per `process/document-workflow.md`.
