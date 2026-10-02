# Message Document

## Purpose

> **Scope:** Conventions for informal written communication - announcements, memos, notes to a
> team, and single-issue messages meant to be read once
> **Key items:** subject-first title, minimal ceremony, one clear ask or statement

A message document communicates one thing to its readers.

It is written to be read, not maintained - a message carries no document ceremony.

Typical shape: a subject title, an optional sender and audience line, a short body, and an
optional closing ask.

## When To Use

Use for announcements, memos, release or incident notes to a team, and single-issue messages.

For durable working drafts use `types/quick-note.md` instead.

For formal project communication with stakeholders use `types/status-report.md`.

**Templates**

- `templates/en/message-document-template-en.md`
- `templates/pl/message-document-template-pl.md`
- `templates/de/message-document-template-de.md`

## Structure

The canonical skeleton, adjusted to the request:

1. H1 title - the subject of the message, not the word "Message".
2. Sender and audience line - who writes and who is addressed, when it is not obvious.
3. Body - the statement or news, a few short paragraphs or a list.
4. Closing - the action expected from the reader, a deadline, or a contact.

## Deltas From The Language Baseline

- Write to the reader directly - first and second person are natural in messages.
- Keep the whole document short enough to read in one screen.
- No metadata ceremony - a message does not carry a version or a document information block.
- A message with a deadline or an ask puts it at the end, where the reader finishes.

## Section Names

| Section              | Requirement |
|----------------------|-------------|
| Background           | optional    |
| Details              | optional    |
| Action Required      | recommended |
| Next Steps           | optional    |
| Contact              | optional    |
| Document Information | unusual     |
| Version History      | unusual     |
| Contents             | unusual     |

Section names for other languages are declared in the matching `languages/<code>.md` file.
