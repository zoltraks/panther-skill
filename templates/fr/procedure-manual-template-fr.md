# Titre du manuel de procédures

## Objet

Ce que ce manuel régit et quels publics il sert.

Pour le lecteur humain : comment ce manuel sert de référence.

Pour l'opérateur ou l'agent : quelle opération exécuter et quand.

## Modes de fonctionnement

- **Première opération** - ce qu'elle fait, quand elle est choisie.
- **Deuxième opération** - ce qu'elle fait, quand elle est choisie.

## Points de décision

Avant de commencer, l'opérateur décide chaque point et consigne la réponse.

**Nom de la question**

"Question littérale présentée à l'utilisateur ?"

- Première option - valeur par défaut recommandée
- Deuxième option
- L'utilisateur peut donner une autre réponse.

## Rôles et emplacements

Les rôles logiques sont affectés à des emplacements concrets.

Chaque rôle se résout indépendamment, et les conventions déjà établies dans la cible
sont préservées.

| Rôle        | Emplacement               | Requis              |
|-------------|---------------------------|---------------------|
| Nom du rôle | `chemin/` ou `FICHIER.md` | Oui ou conditionnel |
| Autre rôle  | `autre/chemin/`           | Non                 |

## Procédures

### Première opération

1. Première étape - ce que fait l'opérateur.
2. Deuxième étape - ce que fait ensuite l'opérateur.

### Deuxième opération

1. Première étape - ce que fait l'opérateur.

## Validation

Confirmez tous les points suivants avant de conclure :

- [ ] Chaque artefact requis existe.
- [ ] Chaque règle définie dans ce manuel est respectée.

## Annexe

### Arbre de structure

```
docs/
  DIRECTIVES.md      (rôle : détenteur de règles, existant)
  PROPOSITION.md     (rôle : nouveau détenteur, proposé)
```

### Bibliothèque de modèles

```markdown
# Squelette incorporé

Un modèle prêt à copier que l'opérateur remplit.
```
