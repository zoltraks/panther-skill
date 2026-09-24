# ASCII Diagrams

## Purpose

> **Scope:** Flow diagrams drawn with box-drawing characters inside untagged fenced
> blocks in documents created and edited with this skill
> **Key items:** shared axis, centered boxes, `┬`/`▼` vertical edges, gap-filling `▶`
> side branches, centered prose lines

This file defines how flow diagrams - process flows, pipelines, and decision paths - are
drawn with box-drawing characters.

Load it when a document contains or needs a diagram built from `┌ ─ ┐ │` and arrow
characters, or when the request asks to draw, fix, or extend such a diagram.

## When This Applies

The rule covers vertical flow diagrams inside untagged fenced blocks.

It does not cover directory trees, ` ```mermaid ` blocks, or art a document already drew
in plain ASCII - an existing `+`, `-`, `|` drawing keeps its own convention.

## Glyphs

- `┌ ─ ┐` and `└ ─ ┘` - box borders, `│` - box sides.
- `┬` - the downward junction in the bottom border of a box that continues the flow.
- `│` and `▼` - a vertical edge: one connector row, then one arrowhead row.
- `─` and `▶` - a horizontal edge: dashes filling the gap, the head touching the target.
- `◀` - a horizontal edge running to the left.
- `┴ ├ ┤ ┼` - only when a diagram genuinely merges or crosses lines.

Never replace these characters with `+`, `-`, `|`, `v`, or `-->` approximations.

## The Axis

All main-flow boxes share one vertical axis column.

Choose the axis once per diagram - a column that keeps the widest box inside the
document's width convention with a small left margin.

Center every main-flow box on the axis.

When the box width is odd, the box's middle column is the axis.

When the box width is even, the axis sits on either of the two middle columns - keep the
choice consistent within the diagram.

The bottom border of a box that continues the flow carries `┬` exactly on the axis.

A terminal box ends with a plain `└ ─ ┘` border, no tee.

## Boxes

A box is a top border, its content rows, and a bottom border - no empty padding rows.

The interior width is the longest content line plus two - one space of padding on each
side at minimum.

Each box keeps its own width - do not stretch a narrow box to match a wider one.

## Content Alignment

Center every prose line inside the box - the node title and standalone note lines.

When the padding cannot split evenly, put the extra space on the right.

Keep enumeration and reference lines left-aligned with exactly one leading space: dash
items, file paths, tool names, and the wrapped continuations of a list.

## Vertical Edges

Between two consecutive boxes draw exactly two rows: `│` on the axis, then `▼` on the
axis.

An edge label sits on the `│` row, one space after the bar, for example `│ Yes`.

A connector row ends after its last glyph - never pad it to the box width.

## Side Branches

A branch box sits to the right of its source box, both top borders on the same row.

The horizontal edge leaves the source box on its last content row: `─` fills the whole
gap and `▶` touches the target box's left border.

The branch label sits inside the gap on the row directly above the arrow, centered in
the gap with at least two spaces on each side.

A branch box that continues the flow may carry its own `┬` or side branch, a terminal
one ends with a plain bottom border.

Mirror the layout for a branch that leaves to the left: `◀` leads the dashes and touches
the target's right border.

## Example

Correct - one axis, centered prose, left-aligned lists, a labeled side branch:

```
     ┌─────────────────────┐
     │  Incoming Request   │
     └──────────┬──────────┘
                │
                ▼
   ┌────────────────────────┐        ┌─────────────────────┐
   │      Authorized?       │  Deny  │  Request Rejected   │
   │ check the access token │───────▶│ log and respond 403 │
   └────────────┬───────────┘        └─────────────────────┘
                │ Allow
                ▼
   ┌────────────────────────┐
   │     Handle Request     │
   │ - validate the payload │
   │ - call the backend     │
   └────────────────────────┘
```

Incorrect - drifting axis, left-aligned title, ASCII approximations, stretched boxes:

```
 ┌─────────────────────┐
 | Incoming Request   |
 +---------------------+
          |
          v
   ┌────────────────────────┐    -- Deny -->   ┌──────────────────┐
   │ Authorized?            │                  │ Request Rejected │
   └────────────────────────┘                  └──────────────────┘
```

## Editing Existing Diagrams

Preserve an existing diagram's axis, box widths, and glyph style when the request adds
or changes a node.

Recompute the padding after changing a content line - a longer line widens its box and
moves both borders, and a wider box may shift the axis for every node.

Recenter the affected boxes and redraw the connectors that touched them.

Keep the diagram inside the document's width convention when one exists.
