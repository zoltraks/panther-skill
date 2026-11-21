# Nom de la compétence

> Une phrase qui dit ce que la compétence fait et quand elle est utilisée.

## Aperçu

Ce qu'est la compétence, ce qu'elle produit et pour quels environnements d'agents
elle est prévue.

## Fonctions de la compétence

- **Fonction une** - ce que la compétence fait à l'activation
- **Fonction deux** - ce que la compétence fait à l'activation

## Installation

```bash
git clone <url-du-depot> <repertoire-des-competences>/nom-competence
```

### Environnements d'agents

- Agent A - `.agent-a/skills/nom-competence/`
- Agent B - `.agent-b/skills/nom-competence/`
- Installation globale - `~/.config/<agent>/skills/nom-competence/`

## Utilisation

La compétence s'active quand une demande correspond à une clé de déclenchement
déclarée dans `SKILL.md`.

## Exemples de prompts

> Demande d'exemple qui active la compétence.

> Une autre demande d'exemple.

## Contenu

```
nom-competence/
├── SKILL.md    # Routage central
└── <rep>/      # fichiers de ressources
```

## Licence

Nom de la licence - voir `LICENSE`.
