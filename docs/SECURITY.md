# Security Policy

## Purpose

> **Scope:** Vulnerability disclosure channel and response expectations for the panther-skill
> repository
> **Key items:** GitHub Issues reporting, update-path trust boundary, supported versions

This file defines how to report a security defect in the skill repository itself - the `SKILL.md`
router, the rule corpus, and the `scripts/` tooling.

It does not cover documents produced by the skill.

## Supported Versions

The skill is versioned in `SKILL.md` under `metadata.version` and distributed as a Git clone.

Only the latest declared version on the default branch is supported.

## Reporting A Vulnerability

Report defects through GitHub Issues at
`https://github.com/zoltraks/panther-skill/issues`.

Include:

- The affected file or script and the skill version from `metadata.version`.
- A reproduction path or a concrete example of the defect.
- The impact you believe it carries.

Do not file a public issue for defects that expose user secrets or private repository content
before contacting the maintainer through the repository profile.

This is a single-maintainer project.

There is no guaranteed response SLA, but security reports take priority over feature work.

## Update-Path Trust Boundary

The once-per-session update check in `SKILL.md` offers `git pull --ff-only` from the configured
upstream.

The pull path applies no cryptographic verification of merged content.

The `tip_sha` and `tip_date` details in the update verdicts identify the incoming upstream tip
commit, which serves as the review anchor for deciding whether to pull.

Approve updates only from upstreams you trust, and review `git log HEAD..@{u}` diffs before
pulling when unsure.

## Accepted Posture

The update path deliberately relies on `--ff-only` pulls, dirty-tree and diverged refusal, the
verdict's `incoming_*` and `changed_scripts`/`changed_skill` review payload, and explicit
per-session user approval rather than signed commits or tags.

Commit-hash anchoring per `docs/VERSIONING.md` is the integrity anchor consumers verify
against.

The regression gate is intentionally manual - no CI pipeline or hook automation runs it, per
`docs/MAINTENANCE.md`.

These postures are standing accepted decisions, revisited at each audit.
