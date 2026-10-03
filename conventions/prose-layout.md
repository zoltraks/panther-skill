# Prose Layout

## Purpose

> **Scope:** The named prose-formatting conventions for Markdown documents - how sentences sit
> on lines and how blank lines separate them - with detection signals, the no-assumed-default
> rule, and the intake parameters that resolve the layout of a new document
> **Key items:** flowing, separated, bounded, justified conventions, per-element detection,
> mixed-document handling, layout parameters, tooling map

Documents differ in how prose sits on lines.

This file names the conventions the skill recognizes, defines how each is detected, and maps
them to the tools and intake parameters that produce them.

The core rule: never assume a layout - detect it on existing documents, resolve it through
parameters on new ones.

## The Conventions

The layout model has two axes.

The wrap axis decides whether a sentence may break across lines: `unwrapped` sentences never
break, `fixed-width` sentences break at a character limit, `justified` breaks like fixed-width
but stretches inter-word spacing to flush the right margin.

The spacing axis decides how sentences separate: `packed` sentences share one paragraph block,
`separated` sentences carry one blank line between them.

Four named conventions cover the combinations seen in real documents:

| Convention  | Wrapping    | Spacing   | Definition                                                            |
|-------------|-------------|-----------|-----------------------------------------------------------------------|
| `flowing`   | unwrapped   | packed    | Sentences start lines, short sentences may share one line up to ~80   |
| `separated` | unwrapped   | separated | One blank line between every sentence                                 |
| `bounded`   | fixed-width | separated | Lines wrap at a declared width, blank lines between sentence blocks   |
| `justified` | fixed-width | separated | Like bounded, with inter-word spacing stretched to flush both margins |

`separated` is the produced-document default - the `languages/` baselines define it.

`bounded` is the convention the skill's own rule files use, wrapped at 100 characters.

A plain wrapped paragraph - `fixed-width` lines, `packed` sentences, no blank lines between
them - is a bounded variant written without sentence spacing.

Treat it as `bounded, packed`.

`justified` is rare: the source reads like typeset text, every line except the last of a block
padded to the same width.

## Flowing

Sentences are never broken across lines.

Every sentence starts on its own line, but short sentences may share a line when their combined
length stays within about 80 characters.

In the rendered view the paragraph reads as continuous prose.

The line breaks are a source convenience only.

```markdown
The service polls the queue. It retries on failure.
Each attempt is logged with its correlation id, its delay, and the final verdict for
that delivery.
```

## Separated

Every sentence is its own paragraph, separated from the next by one blank line.

Sentences are never broken across lines - the editor wraps on display.

```markdown
The service polls the queue.

It retries on failure.

Each attempt is logged with its correlation id, its delay, and the final verdict for
that delivery.
```

## Bounded

Prose wraps at a declared character limit - 60, 80, 100, or 120 are typical.

Blank lines separate the sentence blocks, so each block holds one sentence or one thought.

```markdown
The service polls the queue and retries on failure. Each attempt is logged with its
correlation id, its delay, and the final verdict for that delivery attempt outcome.
```

## Justified

Lines wrap at a width and inter-word spacing stretches so both edges of the block sit flush.

The last line of a block is never stretched.

```markdown
The  service  polls  the  queue  and  retries  on  failure.  Each  attempt  is  logged
with  its  correlation  id,  its  delay,  and  the  final  verdict  for  the  delivery.
```

`justified` layout is preserved on edit and produced on explicit request - see the tooling map.

## Detection

Detect the layout before editing an existing document - never assume one.

`scripts/census-document.py` reports the raw signals: the wrap convention and continuation
lines per element type, multi-sentence lines, and blank-line runs.

| Convention  | Signals                                                                              |
|-------------|--------------------------------------------------------------------------------------|
| `flowing`   | Unwrapped lines, sentences start lines, shared lines hold several short sentences    |
| `separated` | Unwrapped lines, one sentence per paragraph block, blank line between every sentence |
| `bounded`   | Lines cluster below a fixed width, continuation lines common, spaced sentence blocks |
| `justified` | Lines at exactly one width, inter-word spacing varies to fill the right margin       |

Evaluate each element type separately - paragraphs, list items, and blockquotes may follow
different conventions inside one document, per the element-level rule in
`conventions/markdown-dialects.md`.

A `bounded` document and a `justified` document can look alike at a glance.

The variable inter-word spacing is the distinguishing signal.

## Mixed Documents

When a document mixes conventions, report the inconsistency.

Adopt the dominant convention - the one used more often and most appropriate to the document's
content - for the content the task adds or touches.

Suggest normalizing the document to one convention, but normalize only when the request
explicitly covers the conversion.

## New Documents

The layout of a new document resolves through the intake parameters in
`process/document-workflow.md`: `line-wrapping`, `sentence-spacing`, and `wrap-width`.

The recommended answer produces `separated`, matching the `languages/` baselines.

A scope rule document or a request may also name the layout directly - an explicit request
overrides the parameter defaults.

## Tooling Map

- `scripts/split-sentences.py` - separates packed sentences onto individual logical lines:
  `--paragraphs` produces `separated`, `--flow` produces `flowing`.
- `scripts/reflow-prose.py --wrap --width N` - produces the `bounded` wrap axis, and
  `--unwrap` joins wrapped continuations back to unwrapped lines.
- `scripts/reflow-prose.py --justify --width N` - produces `justified`.
- `scripts/census-document.py` - reports the detection signals above, including a prose-layout
  classification per element type.

Conversion between conventions runs only on explicit request.

A request to produce `justified` on a new document applies `reflow-prose.py --justify` after
drafting, or writes the spacing directly.
