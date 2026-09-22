# Skill Name

> One sentence stating what the skill does and when to use it.

## Overview

What the skill is, what it produces, and which agent environments it targets.

## What The Skill Does

- **Capability one** - what the skill does when triggered
- **Capability two** - what the skill does when triggered

## Installation

```bash
git clone <repository-url> <skills-dir>/skill-name
```

### Agent Environments

- Agent A - `.agent-a/skills/skill-name/`
- Agent B - `.agent-b/skills/skill-name/`
- Global install - `~/.config/<agent>/skills/skill-name/`

## Usage

The skill activates when a request matches a trigger phrase declared in `SKILL.md`.

## Example Prompts

> Example request that activates the skill.

> Another example request.

## What's Inside

```
skill-name/
├── SKILL.md    # Root router
└── <dir>/      # Resource files
```

## License

License name - see `LICENSE`.
