# JSON Parameter Exchange

## Purpose

> **Scope:** Emit and consume machine-readable parameter documents in place of, or alongside,
> the question surfaces in `process/document-workflow.md`
> **Key items:** emission trigger, diagnostic output, emitted document, parameter catalog,
> returned document, authority

This file defines how Panther exposes its intake questions as JSON and how it consumes JSON
answers.

## When To Emit

When the request asks for the questions, settings, or parameters "in JSON", "as JSON", or another
machine-readable format, emit a parameter document instead of the question prompts.

Detection and default resolution still run first: the document contains only the questions that
are actually pending in this session.

Emit the document where the request directs - inline in the response by default, inside a fenced
`json` block.

## Diagnostic Output

When the request names a debugging mode, a diagnostic mode, or asks for detailed or verbose
information, emit the parameter document for information purposes only.

The emission order is fixed: the JSON document first, then a text description of the pending
decisions, then the question prompts.

The question prompts still run - the emitted document does not replace the question flow.

Answers may still arrive as prompt selections, natural-language responses, or a returned document.

The same emission applies when diagnostics are implied: a malformed returned document, an
unresolved parameter conflict, or an intake validation failure may accompany the parameter
document and a text note, while the prompts proceed.

## Emitted Document

The document carries a `description`, context fields (`target`, `task`, `date`, `time`), and an
`intake` array.

- `target` - the document or directory the task centers on.
- `task` - the classified task: `create`, `edit`, `reformat`, `translate`, `discover`, `audit`,
  or `describe`.
- `date` - the current day in `YYYY-MM-DD` format.
- `time` - the local time in `hh:mm:ss` followed by the timezone offset, for example
  `13:45:21 GMT+2`.

Each parameter object keeps a fixed key order: `id`, `question`, `answer`, `description`, `type`,
`menu`, `default` - the `default` key is always the last key of the object.

- `id` - a stable kebab-case identifier for the parameter.
- `question` - the literal question wording presented to the answering side.
- `answer` - emitted as an empty string, or an empty array for `selection`, to be filled by the
  answering side.
- `description` - what the parameter controls and the detection evidence behind its default.
- `type` - `choice` for a single-option answer taken from `menu`, `selection` when multiple
  options may be chosen, or `text` for free input.
- `menu` - required for `choice` and `selection` types and omitted for `text`, letter-keyed (`A`,
  `B`, `C`, ...), and the recommended option label carries "(recommended)".
  A menu lists at most three candidate options plus a trailing `Cancel - abort the operation`
  entry, so it never exceeds four letters, and `Cancel` is never the `default`.
- `default` - the option letter or suggested text applied when the answer stays empty, and the
  array of pre-checked letters for `selection`.

The bypass options of a parameter gate, such as accepting every remaining default, do not become
`menu` entries - the `default` key and the returned document's "use defaults" semantics cover
them.

`Cancel` is a real menu entry, not a bypass - it emits at the last letter of every `choice` and
`selection` menu.

Format parameters such as `encoding` and `line-endings` emit before `document-type` in the
`intake` array, matching the question order in `process/document-workflow.md`.

The prose-layout parameters emit with the format group: `line-wrapping` and
`sentence-spacing` always emit when unresolved, `wrap-width` emits directly after
`line-wrapping` and only when the wrapping answer chooses a fixed width.

A `selection` parameter never accepts an empty `answer` - an empty selection re-asks the
question rather than advancing.

When a `choice` menu exceeds the four-letter cap in interactive questioning, the emitted
document still carries the full menu - the group-question split in
`process/document-workflow.md` is a prompt-side mechanism only.

`document-type` emits before `section-plan`, and `section-selection` or `section-format` follow
its answer - `plan-confirmation` always emits last.

```json
{
    "description": "Intake parameters for <target>",
    "target": "<document-or-directory>",
    "task": "create",
    "date": "2026-09-30",
    "time": "13:45:21 GMT+2",
    "intake": [
        {
            "id": "parameters-acceptance",
            "question": "Should the document use the default parameters or should they be configured?",
            "answer": "",
            "description": "Controls whether the resolved defaults apply as-is - each pending parameter carries its resolved default.",
            "type": "choice",
            "menu": {
                "A": "Accept defaults (recommended)",
                "B": "Configure the core parameters",
                "C": "Cancel - abort the operation"
            },
            "default": "A"
        },
        {
            "id": "readme-variant",
            "question": "Which README variant applies to this repository?",
            "answer": "",
            "description": "Selects the README type file - the detected scope gave no signal for a more specific variant.",
            "type": "choice",
            "menu": {
                "A": "readme-general (recommended)",
                "B": "readme-application",
                "C": "readme-cli",
                "D": "Cancel - abort the operation"
            },
            "default": "A"
        },
        {
            "id": "filename",
            "question": "What filename should the document use?",
            "answer": "",
            "description": "Free input - the suggested default follows the language file naming rules.",
            "type": "text",
            "default": "project_specification.md"
        }
    ]
}
```

## Parameter Catalog

Every pending question surface emits with a stable kebab-case `id`:

| Parameter                 | Type        | Surface                                                                     |
|---------------------------|-------------|-----------------------------------------------------------------------------|
| `parameters-acceptance`   | `choice`    | Accept defaults or configure in Parameter Resolution, document or translate |
| `document-type`           | `choice`    | Ambiguous type inference - the menu lists the candidate types               |
| `document-language`       | `choice`    | Language resolution when unclear - `en`, `pl`, or `de`                      |
| `document-scope`          | `choice`    | Emitted only when scope detection leaves a genuine choice                   |
| `filename`                | `text`      | Naming or output-path question - free input                                 |
| `encoding`                | `choice`    | Encoding confirmation or ambiguity per `conventions/file-encoding.md`       |
| `line-endings`            | `choice`    | LF, CRLF, or preserve the detected style                                    |
| `line-wrapping`           | `choice`    | Unwrapped logical lines or a fixed width per `conventions/prose-layout.md`  |
| `sentence-spacing`        | `choice`    | Packed sentences or a blank line between them                               |
| `wrap-width`              | `choice`    | Fixed-width limit - 60, 80, or 100 - only when wrapping was selected        |
| `delivery`                | `choice`    | Inline vs file for reports, descriptions, and translation output            |
| `readme-variant`          | `choice`    | README variant selection per `process/document-workflow.md`                 |
| `section-plan`            | `choice`    | Accept the recommended structure, select sections, or describe a format     |
| `section-selection`       | `selection` | Recommended and optional sections to include, recommended pre-checked       |
| `section-format`          | `text`      | Free-form structure description such as "plain without sections"            |
| `section-add`             | `selection` | Missing required or recommended sections to insert on a structure edit      |
| `plan-confirmation`       | `choice`    | Proceed, adjust, or cancel the described plan before executing              |
| `source-language`         | `choice`    | Translate - ambiguous source language                                       |
| `target-language`         | `choice`    | Translate - absent target language                                          |
| `translation-industry`    | `selection` | Glossary selection when ambiguous - several glossaries may apply            |
| `translation-fidelity`    | `choice`    | Faithful or adapted - emitted only when the request suggests adaptation     |
| `unsupported-pair`        | `choice`    | Proceed with language baselines only or stop                                |
| `derived-role`            | `choice`    | Derive - summary or supplement when the request leaves the role open        |
| `summary-tiers`           | `selection` | Derive - compression tiers per `process/derived-documents.md`               |
| `overwrite-confirmation`  | `choice`    | Whole-file overwrite and in-place translation overwrite                     |
| `fix-plan-approval`       | `choice`    | Approve the audit fix plan - approval converts it to an Edit task           |
| `maintenance-action`      | `choice`    | The maintenance menu - document work, adjust the skill, or session review   |
| `session-review-approval` | `choice`    | Approve the session-review findings report before applying changes          |
| `mode-selection`          | `choice`    | Document vs maintenance ambiguity and activation vs task ambiguity          |
| `source-resolution`       | `text`      | Translation audit with an unresolvable source - free input                  |

Thin-input clarifications emit as `text` or `choice` parameters as they arise - `text` when free
input is appropriate.

The convention confirmations in `principles/authoring-rules.md`, such as the ` -- ` form, and the
typography questions in `languages/` files emit through this catch-all.

## Returned Document

The answering side returns a document keeping a `response` key - either an array of entry objects
or a condensed object keyed by parameter `id`.

Each array entry requires only `id` and `answer` - an option letter for `choice`, an array of
letters for `selection`, or free text for `text`.

Other keys may be echoed or omitted.

In the condensed form, each key is a parameter `id` and each value is its `answer`.

An empty or missing `answer` - including an `id` absent from the condensed object - applies the
parameter's `default`.

Entries or keys with an unknown `id` are ignored.

Answering "use defaults" or "bypass" applies every `default` value.

A returned `answer` of `cancel` - the `Cancel` letter on a `choice` or `selection` parameter, or
the literal string on any parameter - stops the questioning and aborts the operation.

A returned document is accepted whenever it appears - on any question surface, on its own or
embedded inside a natural-language reply.

Answers are applied from the `response` value.

Natural language surrounding the document is treated as supplementary context, not as part of
the answers.

```json
{
    "response": [
        {
            "id": "parameters-acceptance",
            "answer": "A"
        },
        {
            "id": "readme-variant",
            "answer": "B"
        }
    ]
}
```

The same answers in the condensed form:

```json
{
    "response": {
        "parameters-acceptance": "A",
        "readme-variant": "B"
    }
}
```

## Authority

The JSON format is a presentation format, not an authority change.

Every gate still follows `process/document-workflow.md` and the matching procedure file: a
confirmation still waits for an answer, and returned documents answer the same questions the
prompts would have asked.

The once-per-session Skill Update Check is a session gate outside this exchange - it always asks
in text and never emits a parameter.

Maintenance mode emits little routine: `MAINTENANCE.md` and `STYLE.md` already fix its answers,
so the scheduled surfaces are the `maintenance-action` menu and the `session-review-approval`
gate, plus genuine ambiguities such as `mode-selection`.

An orchestrating agent may emit and consume these documents without human interaction, and every
automated decision is still recorded as answered through the exchange.
