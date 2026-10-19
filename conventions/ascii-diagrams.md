# ASCII Diagrams

## Purpose

> **Scope:** Node-and-edge diagrams drawn with box-drawing characters inside untagged
> fenced blocks in documents created and edited with this skill
> **Key items:** fixed border columns, shared axis, centered boxes and prose lines,
> `┬`/`▼` vertical edges, gap-filling `▶` side branches, `┌`/`┬`/`┼`/`┐` fan-out
> junctions

This file defines how node-and-edge diagrams - process flows, pipelines, decision
paths, and component layouts are drawn with box-drawing characters.

Load it when a document contains or needs a diagram built from `┌ ─ ┐ │` and arrow
characters, or when the request asks to draw, fix, or extend such a diagram.

## When This Applies

The rule covers box-drawing node-and-edge diagrams inside untagged fenced blocks, from
vertical flows and horizontal chains to fan-outs and component layouts.

It does not cover directory trees, ` ```mermaid ` blocks, or art a document already drew
in plain ASCII - an existing `+`, `-`, `|` drawing keeps its own convention.

## Glyphs

- `┌ ─ ┐` and `└ ─ ┘` - box borders, `│` - box sides. A document that already frames
  its boxes with `╭ ╮ ╰ ╯` keeps the rounded corners.
- `┬` - the downward junction in the bottom border of a box that continues the flow.
- `│` and `▼` - a vertical edge: one connector row, then one arrowhead row.
- `─` and `▶` - a horizontal edge: dashes filling the gap, the head touching the target.
- `◀` - a horizontal edge running to the left.
- `┌ ┬ ┼ ┐` - a fan-out junction row: caps on the outermost drop columns, `┬` on each
  inner drop, `┼` where the source's own axis crosses.
- `┴ ├ ┤` - only when a diagram genuinely merges or crosses lines.

An existing diagram that already draws its arrowheads as `>`, `v`, or `^` keeps that
style - the geometry rules apply unchanged, only the glyph choice stays as found.

Never replace these characters with `+`, `-`, `|`, or `-->` approximations.

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

Every row of one box shares the same left and right border columns: each `│` side sits
exactly under its top corners, and the bottom corners close exactly under the sides.

A content or border row shifted even one column off its box is a defect - redraw the
box rather than leaving a drifted edge.

The interior width is the longest content line plus two - one space of padding on each
side at minimum.

Widen the box when a line does not fit - a label never touches, crowds, or overflows a
border, and padding is never stolen to squeeze a long line in.

Each box keeps its own width.

Do not stretch a narrow box to match a wider one.

## Content Alignment

Center every prose line inside the box - the node title and standalone note lines.

When the padding cannot split evenly, put the extra space on the right.

A label wrapped over several lines forms one block: indent every line to the same left
column, chosen so the longest line is centered.

Keep enumeration and reference lines left-aligned with exactly one leading space: dash
items, file paths, tool names, and the wrapped continuations of a list.

## Vertical Edges

Between two consecutive boxes draw exactly two rows: `│` on the axis, then `▼` on the
axis.

An edge label sits on the `│` row, one space after the bar, for example `│ Yes`.

A connector row ends after its last glyph - never pad it to the box width.

A diagram that preserves another convention draws the same two-row edge with its own
head glyph - `│` then `v`.

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

In a side-by-side chain the edge may leave the source box on any one content row - keep
the same row for every link in the chain.

## Fan-Out Junctions

When one node feeds several nodes laid out side by side, the source's vertical edge ends
in a junction row instead of a single arrowhead.

Draw the junction row directly under the source's last `│` row: `─` fills between the
glyphs, `┌` opens on the leftmost drop column, `┐` closes on the rightmost, `┬` marks
each inner drop column, and `┼` continues the source's axis.

The next row carries one arrowhead - `▼`, or the diagram's own head glyph - on every
drop column, directly above the target boxes' top borders.

Every drop column lands on the center column of the box it feeds - shift a target box or
re-space the junction row until the drops and the box centers match.

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

A fan-out - every drop and arrowhead lands on a target's center column:

```
         ┌─────────────┐
         │ Dispatcher  │
         └──────┬──────┘
                │
       ┌────────┼────────┐
       ▼        ▼        ▼
   ┌───────┐  ┌─────┐  ┌───────┐
   │ Queue │  │ Log │  │ Store │
   └───────┘  └─────┘  └───────┘
```

## Editing Existing Diagrams

Preserve an existing diagram's axis, box widths, and glyph style when the request adds
or changes a node.

Recompute the padding after changing a content line - a longer line widens its box and
moves both borders, and a wider box may shift the axis for every node.

Recompute the junction and drop columns after moving or resizing a box - every fan-out
drop still lands on its target's center.

Recenter the affected boxes and redraw the connectors that touched them.

Keep the diagram inside the document's width convention when one exists.

## Verification

Recount the columns before delivering the block.

Every `│` side edge sits exactly under its box's top corners, every bottom corner closes
exactly under a side edge, and both borders of a box carry the same dash count.

Every horizontal arrowhead touches its target's border, every vertical drop and fan-out
junction lands on a box center, and no label touches or overflows a border.
