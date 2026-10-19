# Procedure Manual Title

## Purpose

What this manual governs and which audiences it serves.

For the human reader: how to use this manual as a reference.

For the operator or agent: which operation to run and when.

## Operating Modes

- **First Operation** - what it does, when it is selected.
- **Second Operation** - what it does, when it is selected.

## Decision Points

Before starting, the operator resolves each decision and records the answer.

**Question Name**

"Literal question wording presented to the user?"

- First option - recommended default
- Second option
- Let the user specify another answer.

## Roles and Locations

Logical roles map to concrete locations.

Resolve each role independently and preserve conventions the target already established.

| Role         | Location             | Required           |
|--------------|----------------------|--------------------|
| Role name    | `path/` or `FILE.md` | Yes or conditional |
| Another role | `other/path/`        | No                 |

## Procedures

### First Operation

1. First stage - what the operator does.
2. Second stage - what the operator does next.

### Second Operation

1. First stage - what the operator does.

## Validation

Confirm all of the following before finishing:

- [ ] Each required artifact exists.
- [ ] Each rule this manual defines is followed.

## Appendix

### Structure Tree

```
docs/
  GUIDELINES.md      (role: rules owner, existing)
  PROPOSED.md        (role: new owner, proposed)
```

### Template Library

```markdown
# Embedded Skeleton

A copy-ready template the operator instantiates.
```
