# Humanize Document

## Purpose

> **Scope:** Standalone procedure for rewriting a document so its style, structure, and
> voice read human-authored while every fact stays intact
> **Key items:** hard invariants, deletion pass, meta collapse, passage rewrites, voice
> sweeps, scout decomposition, verification

This file defines the humanize operation: the agent revises an existing document so it
reads like a person wrote it over time rather than generated in one pass.

Follow it when the request asks to humanize a document, make it read like a human wrote
it, remove the generated voice, or an equivalent declared in the `languages/` files.

The operation changes how a document reads, never what it says.

It differs from Correct (`process/correct-document.md`), which fixes detected
violations, and from Edit, which applies a named scoped change - humanize revises voice
and pacing deliberately and may leave the document formally less uniform.

## Hard Invariants

These bounds hold for every passage the procedure touches.

- Every technical fact, requirement, decision, default, endpoint, error code, and
  identifier keeps its meaning and its name.
- Normative vocabulary (`must`, `should`, `may` and language equivalents) survives
  rewording - a rule may be rephrased, never weakened or dropped.
- Fact tables stay byte-identical: requirement, decision, open-point, reference,
  error-code, option, and traceability rows are content, not prose style.
- Cross-reference numbering resolves exactly as before - rename headings by phrase, not
  by number, and keep identifier-bearing headings prefixed.
- No fabricated provenance: no invented meetings, authors, dates, or "we discussed"
  claims that supply history the document never had.
- The register stays technical - human does not mean casual, jokey, or sloppy.
- The document never mentions its own revision - no "made more human" remarks.
- Encoding, line endings, fenced payloads, and the document's own Markdown dialect are
  preserved.

## Passes

Apply the passes in order, skipping a pass the request narrows away.

### Deletion Pass

Delete self-referential sections outright: change summaries narrating the document's
own revision, self-audit checklists, and thin pointer sections that carry no
specification content.

Leave no placeholder - a deleted section simply stops existing, and only references
pointing at it are reworded or dropped.

### Meta Collapse

Compress passages where the document discusses its own authority, versioning, or
division of ownership into a declared keep-set, typically three sentences: the
normative-vocabulary rule, the status of proposed values, and one sentence naming the
authoritative artifacts.

Cut hedged restatements of the same claims - keep each substance once.

### Passage Rewrites

Rewrite the named patterns a generated document reveals:

- Abstract openings become problem-first: one concrete sentence of the problem, then
  the shape of the solution, then the trust model.
- Roadmap sentences that only summarize the table of contents are deleted.
- Dense limitation lists become one short paragraph plus at most five bullets, in the
  voice of someone naming what they deliberately did not build.
- Table lead-ins that restate the table are replaced by one plain sentence carrying the
  core point, letting the table hold the detail.
- Hard mechanisms keep their detail but breathe: shorter paragraphs, one "the reason
  is" explanation, and one concrete failure walk-through.
- Example blocks get lead-ins that say what to notice, not what the schema already
  shows.

### Voice Sweeps

Run the sweeps document-wide after the named rewrites.

- Spaced-hyphen or dash asides in running prose fall to a declared cap (typically five),
  definitional `term - description` entries and table cells stay.
- Possession personification ("owns", "is responsible for" overuse) is reduced to the
  few places it is genuinely clearest, and concrete verbs carry the rest.
- Repeated epistemological hedging ("proposed, not measured", "never claims") is
  deduplicated - each substance survives once.
- Sentence length varies deliberately: short declaratives land at load-bearing points,
  and one or two sentences may stay slightly awkward where the constraint is tangled.
- Uniform bullet parallelism breaks in a few lists - fragments and full sentences mix,
  one list may end on a sentence.
- A small fixed budget of first-person-plural asides (typically three to six) lands at
  real decision points, declarative rather than hedgy.
- A small budget of deliberate inconsistencies (mixed cross-reference forms, one
  "e.g." among "for example", an italic table note) leaves the professional whole
  intact.
- A few headings shift from noun phrases to questions or verb phrases where natural,
  numbering and identifier prefixes never move.

## Scout Decomposition

Documents too large for a reliable single pass - a guideline is roughly two thousand
lines - split into disjoint regions handled by parallel scouts (subagents).

- Split on top-level boundaries such as chapters, never mid-section.
- Each scout receives the invariants, its assigned passes, its region's heading
  boundaries, and a scratch output path.
- Scouts draft the complete revised region to scratch files - they never edit the live
  document concurrently.
- The orchestrator merges regions serially in document order, verifying each seam.
- A global reconciliation pass follows the merge: scouts regress document-wide
  constraints, so every sweep count, character inventory, and invariant diff re-runs
  against the merged whole - this step is mandatory, not optional.

## Mechanical Techniques

- Target packed sentences with `census-document.py` packed outliers, then split the
  worst offenders (four or more sentences) with `split-sentences.py` - never reformat
  every multi-sentence line indiscriminately.
- Packed sentences inside a list item transform manually into a multi-paragraph item:
  continuation lines indent to the item's content column, the marker is never
  duplicated, and a blank line separates the item from its sibling.
- Apply bulk single-site edits with `apply-pairs.py`, which asserts each literal pair
  occurs exactly once rather than trusting a global replace.
- Prove fact integrity with `diff-identifiers.py` before and after: identifier sets
  must be identical, and count deltas must trace to intended deletions only.
- Prove table sanctity with a diff of `^|` rows between the original and the result -
  only intended table changes may appear.

## Verification And Report

Run the mechanical battery on the result: layout-appropriate reflow check, table
alignment, language lint, and consistency check.

Residuals previously accepted stay accepted - a humanize pass does not reopen them.

Read every rewritten region against the original for factual drift before delivering.

Report inline with at most ten bullets naming the kinds of changes - style categories
only, never a section-by-section changelog.
