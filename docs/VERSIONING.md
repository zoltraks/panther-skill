# Skill Versioning Policy

This document defines the versioning rules for the `panther-skill` Agent Skill.

## Format

Versions use a three-part decimal format: `<major>.<minor>.<patch>`.

- `major` - the outer digit, rolls the whole minor-patch space
- `minor` - the middle digit, rolls the patch space
- `patch` - the innermost digit, the counter incremented by every release

## Increment Rules

Every release increments the version - no distinction is made between minor and major
changes.

1. **Increment patch by 1** for each release.

2. **Patch rolls at 9 without resetting**. When a release lands on a version whose patch is
   already 9, increment the minor digit by 1 and keep the patch at 9.

3. **Minor and patch at 9 roll to major**. When both the minor digit and the patch digit
   are 9, increment the major digit by 1 and reset minor and patch to 0.

   | Before | After  | Reason                                    |
   |--------|--------|-------------------------------------------|
   | 1.0.0  | 1.0.1  | patch + 1                                 |
   | 1.0.9  | 1.1.9  | patch at ceiling - minor + 1, patch stays |
   | 1.9.9  | 2.0.0  | both at ceiling - major + 1, lower reset  |
   | 9.9.9  | 10.0.0 | both at ceiling - major + 1, lower reset  |

## When To Bump

A bump is applied when the user asks for it.

Whenever maintenance changes any document that is part of the skill, propose a version
bump in the delivery report - the proposal names the current version and the next version
the increment rules produce.

The bump itself happens only on an explicit request or an accepted proposal - never as an
unannounced side effect.

## Release Anchors

Panther does not tag releases.

The commit that bumps `metadata.version` is the release anchor - its hash is the named state
consumers pin or revert to, since the version alone lives only in frontmatter text.

Record the bump commit's short hash in release notes or issues when a consumer needs to pin a
specific release.

## Terminology

The word `version` in this file always means the skill version recorded in `SKILL.md`
frontmatter.

Documents produced by the skill may carry their own version markers,
such as a version comment or a Version History section, defined by the matching `types/` file.

Those document versions belong to the produced document, not to the skill.

## Where Version Is Recorded

The version lives in `SKILL.md` frontmatter under `metadata.version`:

```yaml
---
name: panther-skill
metadata:
  version: "X.Y.Z"
---
```

This follows the [Agent Skills specification](https://agentskills.io/specification) `metadata` field
convention, keeping the skill compatible with Anthropic Claude and other spec-compliant agents.
