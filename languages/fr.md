---
code: fr
name: French
native-name: français
---

# Style et formatage des documents Markdown

## Objet

Ce document définit le style du texte et les règles de formatage des documents Markdown
rédigés en français.

Il s'applique à toute la documentation de projet, y compris les directives, les normes,
les modèles, les notes et les documents de référence.

Il s'adresse aux outils de génération de contenu et aux agents IA, tout en restant
lisible par des humains.

Les règles décrites ci-dessous s'appliquent également à ce document lui-même.

## Sommaire

| Section                               | Ligne | Contenu                                             |
|---------------------------------------|-------|-----------------------------------------------------|
| Structure du document                 | 48    | Titre, objet et plan du document                    |
| Titres                                | 67    | Casse et qualificatifs                              |
| Numérotation des sections             | 101   | Règles de numérotation des sections                 |
| Règles du sommaire                    | 117   | Quand insérer un sommaire                           |
| Paragraphes et phrases                | 135   | Construction des phrases et des paragraphes         |
| Retour à la ligne                     | 150   | Lignes logiques et sauts de ligne forcés            |
| Listes                                | 184   | Puces, numérotation et espacements                  |
| Lignes vides et espacements           | 210   | Règles d'espacement                                 |
| Blocs de code                         | 224   | Délimiteurs, marqueurs de langage et code en ligne  |
| Mise en forme en ligne                | 242   | Guillemets, gras et italique                        |
| Points-virgules                       | 266   | Interdiction du point-virgule dans le texte         |
| Caractères spéciaux                   | 292   | Caractères de cadres et emoji                       |
| Vocabulaire français                  | 301   | Termes préférés et calques                          |
| Noms de sections par type de document | 336   | Noms de sections et éléments des types              |
| Particularités typographiques         | 684   | Numérotation des chapitres et pseudo-titres         |
| Tableaux                              | 704   | Alignement selon le texte source                    |
| Noms de fichiers                      | 845   | Nommage des nouveaux fichiers de documentation      |
| Exemple                               | 860   | Exemple correct et exemple incorrect                |
| Maintenance des fichiers              | 894   | Encodage et fins de ligne                           |
| Question de mise à jour               | 906   | Formulation française de la question de mise à jour |
| Phrases d'activation                  | 914   | Phrases françaises et équivalents anglais           |

## Structure du document

Utilisez le même plan dans chaque document.

- Un titre H1 (`#`) en tête de fichier, un seul par document, concis et descriptif.
- Une section d'objet ou de but, un paragraphe qui dit ce que le document couvre.
- Des sections principales au niveau H2 (`##`), des sous-sections au niveau H3 (`###`).

Les sections **Informations du document**et**Historique des versions** sont optionnelles.

N'ajoutez pas ces sections à un document existant.

Ne les insérez pas non plus dans un nouveau document,
sauf si la commande de création l'exige explicitement.

Si le document les contient déjà, mettez-les à jour à chaque modification de contenu.

N'utilisez pas de titres de niveau H4 ou plus profond.

## Titres

Écrivez les noms de sections et de sous-sections avec une majuscule en tête et suivez pour
les autres mots la casse française normale.

N'appliquez pas la casse de titre anglaise, qui met une majuscule à chaque mot.

Les noms propres, les sigles et les noms de technologies gardent leur orthographe,
par exemple "Formatage XML", "Intégration avec Microsoft Fabric", "Couche gold dans le Lakehouse".

Gardez les noms de sections courts.

Ne mettez pas de qualificatifs entre parenthèses dans les noms de sections.

Les qualificatifs comme "obligatoire" ou "ne pas répéter" vont dans le corps de la section.

Ne terminez pas un titre par un signe de ponctuation.

### Correct

```markdown
## Étendue des données sources

### Formatage XML
```

### Incorrect

```markdown
## Étendue Des Données Sources

### Formatage XML (obligatoire):
```

## Numérotation des sections

Ne numérotez pas les sections par défaut.

L'absence de numérotation simplifie la réorganisation d'un document,
parce que le déplacement d'une section n'exige pas de renuméroter les autres.

Si le document édité contient déjà une numérotation des sections,
conservez-la et respectez l'ordre correct des numéros.

Après l'ajout, la suppression ou le déplacement d'une section, renumérotez les sections
de façon que les numéros restent continus et suivent l'ordre du document.

Le numéro d'une sous-section reprend le numéro de la section parente,
par exemple `3.1.` sous la section `3.`.

## Règles du sommaire

N'ajoutez pas de sommaire par défaut.

N'insérez un sommaire que sur demande et seulement
si les sections du document sont numérotées.

Un fichier de référence de plus de 300 lignes peut contenir un sommaire même sans
numérotation des sections.

Placez-le au début du document, immédiatement après la section optionnelle
Informations du document et la section optionnelle Historique des versions.

Si ces sections sont absentes, le sommaire est la première section
après le titre H1.

Mettez à jour le sommaire après chaque changement de la structure du document.

## Paragraphes et phrases

Écrivez des phrases courtes.

Pour les descriptions techniques, utilisez une phrase par paragraphe.

Cette disposition reste lisible dans les éditeurs de texte, dans le terminal et dans
les diffs de versions.

Séparez chaque phrase par une ligne vide.

Une phrase peut contenir plusieurs parties liées si elles expriment une même pensée.

Ne tassez pas des pensées sans lien dans un long paragraphe.

## Retour à la ligne

Ne coupez pas le texte à une largeur de colonne fixe.

Chaque phrase occupe une ligne logique.

Une phrase peut être longue quand la pensée est longue,
l'éditeur ou le navigateur coupe le texte à l'affichage.

N'insérez un saut de ligne forcé que lorsque le contenu source l'exige,
par exemple dans un bloc de code ou un diagramme.

Pour un document existant, sa propre convention de coupure l'emporte sur cette règle.

Détectez si le document coupe la prose à une largeur fixe ou s'il garde des lignes
logiques, conservez cette convention et ne la changez que lorsque la commande la couvre.

Les règles du dépôt, comme un `STYLE.md` exigeant des lignes d'au plus 100 caractères,
fixent la convention pour les nouveaux fichiers et tranchent les cas ambigus.

Utilisez `scripts/reflow-prose.py --wrap --width N` pour appliquer une largeur fixe
et `scripts/reflow-prose.py --unwrap` pour réunir les lignes coupées en lignes logiques.

Le mode wrap ne fait que couper les lignes, le mode unwrap ne fait que les réunir,
et tous deux laissent intactes les tables, les blocs de code et les blocs de code indentés.

La mise en page d'un document produit suit `conventions/prose-layout.md` - cette base
décrit la convention `separated`, et les paramètres d'accueil `line-wrapping`,
`sentence-spacing` et `wrap-width` peuvent choisir `flowing`,
`bounded` ou `justified` à la création.

La détection de la mise en page d'un document existant suit `conventions/prose-layout.md`
et ne présume jamais d'une convention par défaut.

## Listes

Utilisez le tiret (`-`) pour les items à puces.

Ne numérotez pas les items de liste par défaut.

Utilisez une numérotation pour des étapes exécutées en séquence,
quand le document édité l'emploie déjà dans la liste concernée ou quand la commande
de modification l'exige explicitement.

Si la liste est numérotée, gardez les numéros continus après l'ajout ou la suppression
d'items.

Insérez une ligne vide avant la liste et une ligne vide après.

N'insérez pas de lignes vides entre des items courts.

Insérez une ligne vide entre des items longs ou contenant plusieurs phrases.

Insérez une ligne vide entre un item parent et sa sous-liste.

Indentez la sous-liste au niveau de l'item parent.

Écrivez les listes de tâches sous la forme `- [ ]` pour un item ouvert et `- [x]` pour
un item terminé.

## Lignes vides et espacements

Insérez une ligne vide entre les paragraphes.

Insérez une ligne vide avant et après une liste.

Insérez une ligne vide avant et après un bloc de code.

Insérez une ligne vide avant et après une table.

Ne laissez pas plusieurs lignes vides consécutives.

Ne laissez pas d'espaces en fin de ligne.

## Blocs de code

Délimitez chaque bloc de code par trois backticks.

N'indiquez le marqueur de langage que lorsque le bloc contient du code dans un langage
de programmation, de balisage ou de données.

Les blocs de texte brut, de prompts, de sorties console ou stdout, d'arborescences de
répertoires, de diagrammes ou de tables restent sans marqueur - `text` et `txt` comptent
aussi comme marqueurs, et un document qui les emploie de façon cohérente garde sa convention.

Ne laissez pas de ligne vide en première ou en dernière position à l'intérieur du bloc.

Gardez les blocs de code concis et liés au sujet décrit.

Écrivez les noms de fichiers et de répertoires, les commandes, les noms de colonnes et
les valeurs en code en ligne, par exemple `docs/directives`, `SELECT`, `Fact_Sales`.

## Mise en forme en ligne

Pour le texte normal, utilisez les caractères de base sans variantes typographiques.

Utilisez le guillemet double ASCII droit (`"`)
au lieu des variantes typographiques comme les guillemets français.

Utilisez l'apostrophe ASCII droite (`'`) au lieu de l'apostrophe typographique.

La typographie française place une espace devant les signes de ponctuation doubles
(`;`, `?`, `!`, `:`) et à l'intérieur des guillemets.

Dans la source Markdown, utilisez une espace ordinaire et jamais une espace insécable
ou fine insécable, car ces caractères restent invisibles dans un éditeur de texte brut.

Si le document édité suit de façon cohérente une autre convention,
conservez la convention de ce document.

Écrivez les définitions de termes en gras sous la forme **Terme** : définition.

Employez l'italique avec parcimonie.

N'abusez pas des marques de mise en forme.

## Points-virgules

N'utilisez pas le point-virgule dans le texte suivi.

Reliez deux propositions étroitement liées par une virgule.

Quand les propositions expriment des pensées distinctes, divisez-les en phrases séparées.

La règle ne s'applique pas aux blocs de code, au code en ligne ni aux chemins de fichiers.

### Correct

```markdown
Les données brutes arrivent dans la couche `bronze`, la couche `silver` contient les données nettoyées.

Le nom porte le sens, le commentaire porte la justification.
```

### Incorrect

```markdown
Les données brutes arrivent dans la couche `bronze` ; la couche `silver` contient les données nettoyées.

Le nom porte le sens ; le commentaire porte la justification.
```

## Caractères spéciaux

Les caractères de dessin de cadres sont autorisés dans les blocs de code, les diagrammes
et les schémas.

Ne remplacez pas les caractères de cadres par `+`, `-` ou d'autres approximations ASCII.

N'utilisez pas d'emoji sauf si c'est explicitement demandé.

## Vocabulaire français

Écrivez un français correct et évitez les calques aléatoires de l'anglais.

N'accolez pas de terminaisons françaises à des mots anglais
quand un équivalent français naturel existe.

| Au lieu de       | Utilisez                |
|------------------|-------------------------|
| updater          | mettre à jour           |
| fixer            | corriger                |
| customiser       | personnaliser           |
| downloader       | télécharger             |
| uploader         | téléverser              |
| challenger       | remettre en question    |
| reviewer         | relire                  |
| merger           | fusionner               |
| syncer           | synchroniser            |
| sauver           | enregistrer             |
| le status report | le rapport d'avancement |
| le deadline      | la date limite          |
| scheduler        | planifier               |

Les noms propres établis, les noms de produits et les termes d'architecture gardent leur
forme d'origine, par exemple Microsoft Fabric, Lakehouse, Warehouse, Power BI, Workspace.

Les termes techniques établis comme emprunts restent également inchangés, par exemple
commit, pull request, merge, branch, repository, pipeline, cache, backend, frontend,
framework et endpoint.

Écrivez les noms techniques issus du système source exactement comme ils y apparaissent.

Dans les titres d'exemples, utilisez les noms de sections français,
par exemple "Contenu d'exemple", "Correct" et "Incorrect".

## Noms de sections par type de document

Les noms de sections françaises sont déclarés exclusivement dans cette section.

Les fichiers dans `types/` ne nomment que les noms anglais.

Choisissez le nom de section français selon le type de document dans la table suivante.

| Type de document         | Section anglaise                   | Section française                      |
|--------------------------|------------------------------------|----------------------------------------|
| agent-instruction        | Purpose                            | Objet                                  |
| agent-instruction        | Audiences                          | Publics                                |
| agent-instruction        | Use Cases                          | Cas d'utilisation                      |
| agent-instruction        | Decision Points                    | Points de décision                     |
| agent-instruction        | Procedures                         | Procédures                             |
| agent-instruction        | Validation                         | Validation                             |
| agent-instruction        | Example Content                    | Contenu d'exemple                      |
| agent-instruction        | Best Practices                     | Bonnes pratiques                       |
| agent-instruction        | References                         | Références                             |
| article-text             | Introduction                       | Introduction                           |
| article-text             | Summary                            | Résumé                                 |
| article-text             | Further Reading                    | Lectures complémentaires               |
| article-text             | References                         | Références                             |
| change-request           | Document Information               | Informations du document               |
| change-request           | Summary                            | Résumé                                 |
| change-request           | Description                        | Description                            |
| change-request           | Justification                      | Justification                          |
| change-request           | Impact                             | Impact                                 |
| change-request           | Alternatives                       | Alternatives                           |
| change-request           | Approval                           | Approbation                            |
| changelog-file           | Changes                            | Modifications                          |
| changelog-file           | Version                            | Version                                |
| changelog-file           | Added                              | Ajouté                                 |
| changelog-file           | Improved                           | Amélioré                               |
| changelog-file           | Fixed                              | Corrigé                                |
| changelog-file           | Removed                            | Supprimé                               |
| contributing-file        | Purpose                            | Objet                                  |
| contributing-file        | Ways To Contribute                 | Comment contribuer                     |
| contributing-file        | Reporting Issues                   | Signalement de problèmes               |
| contributing-file        | Development Setup                  | Environnement de développement         |
| contributing-file        | Pull Requests                      | Pull Requests                          |
| contributing-file        | AI-Assisted Contributions          | Contributions assistées par IA         |
| contributing-file        | License                            | Licence                                |
| contributing-file        | Code Of Conduct                    | Code de conduite                       |
| contributing-file        | Getting Help                       | Obtenir de l'aide                      |
| daily-plan               | Priorities                         | Priorités                              |
| daily-plan               | Schedule                           | Échéancier                             |
| daily-plan               | Tasks                              | Tâches                                 |
| daily-plan               | Notes                              | Remarques                              |
| daily-plan               | Carry Over                         | Report                                 |
| daily-plan               | Document Information               | Informations du document               |
| daily-plan               | Version History                    | Historique des versions                |
| daily-plan               | Contents                           | Sommaire                               |
| decision-record          | Status                             | Statut                                 |
| decision-record          | Context and Problem Statement      | Contexte et problème                   |
| decision-record          | Decision Drivers                   | Facteurs de décision                   |
| decision-record          | Considered Options                 | Options envisagées                     |
| decision-record          | Decision Outcome                   | Résultat de la décision                |
| decision-record          | Consequences                       | Conséquences                           |
| decision-record          | Positive Consequences              | Conséquences positives                 |
| decision-record          | Negative Consequences              | Conséquences négatives                 |
| decision-record          | Pros and Cons of the Options       | Avantages et inconvénients des options |
| decision-record          | Links                              | Liens                                  |
| decision-record          | Supersedes                         | Remplace                               |
| engineering-standard     | Purpose                            | Objet                                  |
| engineering-standard     | Scope                              | Portée                                 |
| engineering-standard     | How To Use This Standard           | Utilisation de cette norme             |
| engineering-standard     | Order Of Operations                | Ordre d'application                    |
| engineering-standard     | Precedence                         | Priorité                               |
| engineering-standard     | Non-Negotiable Rules               | Règles non négociables                 |
| engineering-standard     | Agent Intake Protocol              | Protocole d'accueil de l'agent         |
| engineering-standard     | Detection First                    | Détection d'abord                      |
| engineering-standard     | Existing Project                   | Projet existant                        |
| engineering-standard     | New Project                        | Nouveau projet                         |
| engineering-standard     | Documentation                      | Documentation                          |
| engineering-standard     | Language Version                   | Version du langage                     |
| engineering-standard     | Core Technologies                  | Technologies principales               |
| engineering-standard     | Project Structure                  | Structure du projet                    |
| engineering-standard     | Naming Conventions                 | Conventions de nommage                 |
| engineering-standard     | Code Conventions                   | Conventions de code                    |
| engineering-standard     | Formatting and Linting             | Formatage et lint                      |
| engineering-standard     | Testing                            | Tests                                  |
| engineering-standard     | Build                              | Build                                  |
| engineering-standard     | Dependencies                       | Dépendances                            |
| engineering-standard     | Security                           | Sécurité                               |
| engineering-standard     | Observability                      | Observabilité                          |
| engineering-standard     | Logging                            | Journalisation                         |
| engineering-standard     | Comments                           | Commentaires                           |
| engineering-standard     | Error Handling                     | Gestion des erreurs                    |
| engineering-standard     | Verification                       | Vérification                           |
| engineering-standard     | Definition of Done                 | Definition of Done                     |
| engineering-standard     | Correctness                        | Exactitude                             |
| engineering-standard     | Structure                          | Structure                              |
| engineering-standard     | Quality                            | Qualité                                |
| engineering-standard     | Hygiene                            | Hygiène                                |
| engineering-standard     | General Principles                 | Principes généraux                     |
| engineering-standard     | Sources                            | Sources                                |
| format-specification     | Document Information               | Informations du document               |
| format-specification     | Version History                    | Historique des versions                |
| format-specification     | Quick Overview                     | Aperçu rapide                          |
| format-specification     | Design Principles                  | Principes de conception                |
| format-specification     | Structure                          | Structure                              |
| format-specification     | Implementation Notes               | Notes d'implémentation                 |
| management-plan          | Purpose                            | Objet                                  |
| management-plan          | Methodology                        | Méthodologie                           |
| management-plan          | Methodology and Approach           | Méthodologie et approche               |
| management-plan          | Roles and Responsibilities         | Rôles et responsabilités               |
| management-plan          | Thresholds and Tolerances          | Seuils et tolérances                   |
| management-plan          | Cadence                            | Cadence                                |
| management-plan          | Process                            | Processus                              |
| management-plan          | Cadence and Process                | Cadence et processus                   |
| management-plan          | Tools                              | Outils                                 |
| management-plan          | Reporting                          | Rapports                               |
| management-plan          | Related Plans                      | Plans associés                         |
| management-plan          | Related Registers                  | Registres associés                     |
| management-plan          | Related Plans and Registers        | Plans et registres associés            |
| management-plan          | Change Control                     | Contrôle des changements               |
| management-plan          | Master Plan                        | Plan directeur                         |
| meeting-minutes          | Meeting Details                    | Détails de la réunion                  |
| meeting-minutes          | Attendees                          | Participants                           |
| meeting-minutes          | Absentees                          | Absents                                |
| meeting-minutes          | Agenda                             | Ordre du jour                          |
| meeting-minutes          | Discussion                         | Discussion                             |
| meeting-minutes          | Decisions                          | Décisions                              |
| meeting-minutes          | Action Items                       | Actions à mener                        |
| meeting-minutes          | Open Questions                     | Questions ouvertes                     |
| meeting-minutes          | Next Meeting                       | Prochaine réunion                      |
| meeting-minutes          | Facilitator                        | Animateur                              |
| meeting-minutes          | Minute Taker                       | Rédacteur du compte rendu              |
| meeting-minutes          | Due Date                           | Date d'échéance                        |
| meeting-minutes          | Owner                              | Responsable                            |
| message-document         | Background                         | Contexte                               |
| message-document         | Details                            | Détails                                |
| message-document         | Action Required                    | Action requise                         |
| message-document         | Next Steps                         | Prochaines étapes                      |
| message-document         | Contact                            | Contact                                |
| message-document         | Document Information               | Informations du document               |
| message-document         | Version History                    | Historique des versions                |
| message-document         | Contents                           | Sommaire                               |
| project-charter          | Purpose and Justification          | Objet et justification                 |
| project-charter          | Measurable Objectives              | Objectifs mesurables                   |
| project-charter          | Success Criteria                   | Critères de réussite                   |
| project-charter          | High-Level Requirements            | Exigences générales                    |
| project-charter          | Scope Boundaries                   | Limites du périmètre                   |
| project-charter          | In Scope                           | Dans le périmètre                      |
| project-charter          | Out of Scope                       | Hors périmètre                         |
| project-charter          | Deliverables and Milestones        | Livrables et jalons                    |
| project-charter          | Deliverables                       | Livrables                              |
| project-charter          | Milestones                         | Jalons                                 |
| project-charter          | High-Level Budget                  | Budget prévisionnel                    |
| project-charter          | Key Stakeholders                   | Parties prenantes clés                 |
| project-charter          | Project Manager Role and Authority | Rôle et autorité du chef de projet     |
| project-charter          | Assumptions and Constraints        | Hypothèses et contraintes              |
| project-charter          | High-Level Risks                   | Risques majeurs                        |
| project-charter          | Exit Criteria                      | Critères de sortie                     |
| project-charter          | Approval                           | Approbation                            |
| project-document         | Document Purpose                   | Objet du document                      |
| project-document         | Document Navigation                | Navigation du document                 |
| project-document         | Glossary                           | Glossaire                              |
| project-document         | Abbreviations                      | Abréviations                           |
| project-document         | Vision                             | Vision                                 |
| project-document         | Goals                              | Objectifs                              |
| project-document         | Non-Goals                          | Non-objectifs                          |
| project-document         | Quality Requirements               | Exigences de qualité                   |
| project-document         | System Architecture                | Architecture du système                |
| project-document         | Component Diagram                  | Diagramme de composants                |
| project-document         | Functional Requirements            | Exigences fonctionnelles               |
| project-document         | Non-Functional Requirements        | Exigences non fonctionnelles           |
| project-document         | Use Cases                          | Cas d'utilisation                      |
| project-document         | Design Decisions                   | Décisions de conception                |
| project-document         | Implementation Phases              | Phases d'implémentation                |
| project-document         | Testing Strategy                   | Stratégie de test                      |
| project-document         | Naming Conventions                 | Conventions de nommage                 |
| project-document         | Version Control                    | Gestion de versions                    |
| project-document         | Documentation                      | Documentation                          |
| proposal-document        | Status                             | Statut                                 |
| proposal-document        | Summary                            | Résumé                                 |
| proposal-document        | Background                         | Contexte                               |
| proposal-document        | Background and Context             | Contexte et arrière-plan               |
| proposal-document        | Proposal                           | Proposition                            |
| proposal-document        | Alternatives Considered            | Alternatives envisagées                |
| proposal-document        | Risks and Mitigations              | Risques et mesures d'atténuation       |
| proposal-document        | Open Questions                     | Questions ouvertes                     |
| proposal-document        | Decision                           | Décision                               |
| proposal-document        | Reviewers                          | Réviseurs                              |
| procedure-manual         | Purpose                            | Objet                                  |
| procedure-manual         | Audiences                          | Publics                                |
| procedure-manual         | Operating Modes                    | Modes de fonctionnement                |
| procedure-manual         | Decision Points                    | Points de décision                     |
| procedure-manual         | Roles and Locations                | Rôles et emplacements                  |
| procedure-manual         | Procedures                         | Procédures                             |
| procedure-manual         | Validation                         | Validation                             |
| procedure-manual         | Examples                           | Exemples                               |
| procedure-manual         | Template Library                   | Bibliothèque de modèles                |
| procedure-manual         | Appendix                           | Annexe                                 |
| readme-application       | Contents                           | Sommaire                               |
| readme-application       | Overview                           | Aperçu                                 |
| readme-application       | Download                           | Téléchargement                         |
| readme-application       | Installation                       | Installation                           |
| readme-application       | Project Status                     | État du projet                         |
| readme-application       | Technical Stack                    | Pile technique                         |
| readme-application       | Features                           | Fonctionnalités                        |
| readme-application       | Quick Start                        | Démarrage rapide                       |
| readme-application       | Usage                              | Utilisation                            |
| readme-application       | Configuration                      | Configuration                          |
| readme-application       | Repository Structure               | Structure du dépôt                     |
| readme-application       | Documentation                      | Documentation                          |
| readme-application       | Changelog                          | Journal des modifications              |
| readme-application       | License                            | Licence                                |
| readme-application       | Credits                            | Crédits                                |
| readme-cli               | Overview                           | Aperçu                                 |
| readme-cli               | Install                            | Installation                           |
| readme-cli               | Commands                           | Commandes                              |
| readme-cli               | Options                            | Options                                |
| readme-cli               | Examples                           | Exemples                               |
| readme-cli               | Configuration                      | Configuration                          |
| readme-cli               | License                            | Licence                                |
| readme-collection        | Overview                           | Aperçu                                 |
| readme-collection        | About This Repository              | À propos de ce dépôt                   |
| readme-collection        | Contents                           | Sommaire                               |
| readme-collection        | Usage                              | Utilisation                            |
| readme-collection        | Notices                            | Avis                                   |
| readme-collection        | License                            | Licence                                |
| readme-collection        | Credits                            | Crédits                                |
| readme-docs              | Overview                           | Aperçu                                 |
| readme-docs              | Documentation                      | Documentation                          |
| readme-docs              | Project Guidelines                 | Directives du projet                   |
| readme-docs              | Repository Layout                  | Structure du dépôt                     |
| readme-docs              | License                            | Licence                                |
| readme-general           | Contents                           | Sommaire                               |
| readme-general           | Overview                           | Aperçu                                 |
| readme-general           | Installation                       | Installation                           |
| readme-general           | Usage                              | Utilisation                            |
| readme-general           | Project Layout                     | Structure du projet                    |
| readme-general           | Documentation                      | Documentation                          |
| readme-general           | License                            | Licence                                |
| readme-general           | Credits                            | Crédits                                |
| readme-library           | Install                            | Installation                           |
| readme-library           | Usage                              | Utilisation                            |
| readme-library           | API Reference                      | Référence de l'API                     |
| readme-library           | Configuration                      | Configuration                          |
| readme-library           | Contributing                       | Contribution                           |
| readme-library           | License                            | Licence                                |
| readme-skill             | Contents                           | Sommaire                               |
| readme-skill             | Overview                           | Aperçu                                 |
| readme-skill             | What The Skill Does                | Fonctions de la compétence             |
| readme-skill             | Installation                       | Installation                           |
| readme-skill             | Agent Environments                 | Environnements d'agents                |
| readme-skill             | Usage                              | Utilisation                            |
| readme-skill             | Example Prompts                    | Exemples de prompts                    |
| readme-skill             | What's Inside                      | Contenu                                |
| readme-skill             | Verification                       | Vérification                           |
| readme-skill             | License                            | Licence                                |
| readme-skill             | Credits                            | Crédits                                |
| register-log             | Purpose                            | Objet                                  |
| register-log             | Scoring Definitions                | Définitions de l'échelle de cotation   |
| register-log             | Notes                              | Remarques                              |
| register-log             | Register                           | Registre                               |
| register-log             | Probability                        | Probabilité                            |
| register-log             | Impact                             | Impact                                 |
| register-log             | Score                              | Score                                  |
| register-log             | Response Strategy                  | Stratégie de réponse                   |
| register-log             | Owner                              | Responsable                            |
| register-log             | Status                             | Statut                                 |
| register-log             | Review Date                        | Date de revue                          |
| register-log             | Raised Date                        | Date de signalement                    |
| register-log             | Due Date                           | Date d'échéance                        |
| register-log             | Resolution                         | Résolution                             |
| register-log             | Priority                           | Priorité                               |
| register-log             | Description                        | Description                            |
| register-log             | Category                           | Catégorie                              |
| register-log             | Assumption                         | Hypothèse                              |
| register-log             | Constraint                         | Contrainte                             |
| register-log             | Validated By                       | Validé par                             |
| register-log             | Submitted By                       | Soumis par                             |
| register-log             | Decision                           | Décision                               |
| register-log             | Authority                          | Instance décisionnaire                 |
| register-log             | Recommendation                     | Recommandation                         |
| rules-document           | Purpose                            | Objet                                  |
| rules-document           | Sources Of Truth                   | Sources de référence                   |
| rules-document           | Scope                              | Portée                                 |
| rules-document           | General Rules                      | Règles générales                       |
| rules-document           | Exceptions                         | Exceptions                             |
| rules-document           | Correct                            | Correct                                |
| rules-document           | Incorrect                          | Incorrect                              |
| rules-document           | Example Content                    | Contenu d'exemple                      |
| rules-document           | File Maintenance                   | Maintenance des fichiers               |
| rules-document           | Verification                       | Vérification                           |
| status-report            | Reporting Period                   | Période de rapport                     |
| status-report            | Overall Status                     | État général                           |
| status-report            | Status by Area                     | État par domaine                       |
| status-report            | Schedule                           | Échéancier                             |
| status-report            | Budget                             | Budget                                 |
| status-report            | Scope                              | Portée                                 |
| status-report            | Risk                               | Risque                                 |
| status-report            | Summary                            | Résumé                                 |
| status-report            | Accomplishments                    | Réalisations                           |
| status-report            | Milestones                         | Jalons                                 |
| status-report            | Metrics                            | Indicateurs                            |
| status-report            | Top Risks and Issues               | Risques et problèmes majeurs           |
| status-report            | Planned Next Period                | Prévisions pour la période suivante    |
| status-report            | Decisions Needed                   | Décisions requises                     |
| summary-document         | Purpose                            | Objet                                  |
| summary-document         | Abstract                           | Abrégé                                 |
| summary-document         | Summary                            | Résumé                                 |
| summary-document         | Detailed Abstract                  | Abrégé détaillé                        |
| summary-document         | Omitted Material                   | Contenu omis                           |
| supplement-document      | Purpose                            | Objet                                  |
| supplement-document      | Continuation Scope                 | Portée de la continuation              |
| supplement-document      | Extended Content                   | Contenu étendu                         |
| supplement-document      | Continued Entries                  | Entrées poursuivies                    |
| supplement-document      | Updated Conclusions                | Conclusions mises à jour               |
| technical-document       | Purpose                            | Objet                                  |
| technical-document       | Overview                           | Aperçu                                 |
| technical-document       | Prerequisites                      | Prérequis                              |
| technical-document       | Configuration                      | Configuration                          |
| technical-document       | Usage                              | Utilisation                            |
| technical-document       | Examples                           | Exemples                               |
| technical-document       | Troubleshooting                    | Dépannage                              |
| technical-document       | Limitations                        | Limites                                |
| technical-document       | References                         | Références                             |
| work-breakdown-structure | Structure                          | Structure                              |
| work-breakdown-structure | Work Packages                      | Lots de travaux                        |
| work-breakdown-structure | WBS Dictionary                     | Dictionnaire SDP                       |
| work-breakdown-structure | Acceptance Criteria                | Critères d'acceptation                 |
| work-breakdown-structure | Owner                              | Responsable                            |
| work-breakdown-structure | Estimate                           | Estimation                             |
| work-breakdown-structure | Dependencies                       | Dépendances                            |
| work-breakdown-structure | RACI Matrix                        | Matrice RACI                           |
| work-breakdown-structure | Baseline                           | Ligne de base                          |

### Éléments propres aux types

Certains types de document fixent aussi des titres, des schémas de titres et des clés
de champs français.

| Type de document         | Élément                                  | Forme française                                        |
|--------------------------|------------------------------------------|--------------------------------------------------------|
| changelog-file           | titre H1                                 | `# Modifications`                                      |
| management-plan          | schéma du titre H1                       | `# Plan de gestion de <domaine>`                       |
| project-charter          | nom du type et schéma du titre H1        | `charte de projet`, `# Charte de projet <nom>`         |
| project-document         | titres de document typiques              | `conception de la solution`, `spécification du projet` |
| project-document         | groupe d'exigences H3                    | `Jalon I : ...`                                        |
| project-document         | ligne de mécanismes du cas d'utilisation | `**Mécanismes utilisés :**`                            |
| project-document         | clés de la table de métadonnées          | `Nom du projet`, `Version`                             |
| register-log             | titre H1 du registre des risques         | `# Registre des risques`                               |
| work-breakdown-structure | nom du type et abréviation               | `structure de découpage du projet` (SDP)               |

## Particularités typographiques

Les documents formels français numérotent souvent les chapitres et les sous-chapitres,
par exemple `# 1 Mentions générales` et `## 1.1 Objet`.

Ils peuvent aussi employer des pseudo-titres en gras comme `**Note**`,
`**Important**` ou `**Description :**` à la place de titres de sections.

Une table de métadonnées à en-tête vide peut remplacer le commentaire de version dans
la convention française du document de projet.

```markdown
|               |                          |
|---------------|--------------------------|
| Nom du projet | Data Integration Service |
| Version       | 1.0.7                    |
```

Preservez ces traits lors de l'édition selon `conventions/markdown-dialects.md`.

## Tableaux

Les tables doivent rester lisibles dans la vue texte avant qu'un lecteur Markdown
ne les traite.

L'alignement des colonnes et le remplissage régulier des cellules sont le but
principal du formatage.

### Délimiteurs

Séparez les colonnes par la barre verticale (`|`).

Mettez une espace après la barre qui ouvre une cellule et une espace avant la barre
qui la ferme.

N'ajoutez pas d'autres espaces autour des barres au-delà de celle qui est requise.

Commencez chaque ligne - en-tête, ligne de séparation et ligne de données - par une
seule barre verticale.

Une double barre en tête de ligne (`||`) est interprétée comme une première cellule vide.

L'outil de formatage la transforme alors en colonne vide supplémentaire,
ce qui endommage la structure de la table sans se limiter à la décaler.

Écrivez une première cellule volontairement vide sous la forme `| |` et seulement
quand la table en a réellement besoin.

Une cellule vide n'est permise que dans une colonne que la ligne de séparation déclare -
sa cellule de séparation doit contenir au moins un tiret.

Une colonne vide dans chaque ligne, en-tête compris, n'est jamais permise - retirez-la.

### Ligne de séparation

Placez la ligne de séparation immédiatement après l'en-tête.

La ligne de séparation ne contient que des tirets et des barres verticales.

Chaque cellule de la ligne de séparation contient au moins un tiret - une cellule
d'espaces ne déclare pas la colonne.

Les tirets rejoignent les barres verticales sans espace.

La largeur d'un séparateur de colonne égale la largeur de la colonne plus deux tirets.

Les deux tirets supplémentaires représentent l'espace avant la valeur de la cellule et
l'espace après.

La largeur minimale d'une colonne est de trois caractères.

### Remplissage des cellules

Remplissez chaque cellule à gauche avec des espaces jusqu'à la largeur de la colonne.

Remplissez les cellules vides avec des espaces jusqu'à la largeur de la colonne.

Ne remplissez pas les cellules au-delà de la largeur de la colonne.

Ne tronquez jamais le contenu d'une cellule.

Utilisez l'alignement à gauche dans toutes les cellules.

### Largeur des colonnes

La largeur d'une colonne est le plus grand nombre de caractères parmi toutes les
cellules de cette colonne, en-tête compris.

Mesurez la largeur comme la longueur du **texte source** de la cellule,
non du texte affiché.

C'est la règle la plus importante du formatage des tables.

Comptez chaque caractère présent dans la source Markdown, y compris tous les caractères
de formatage.

Ne retirez, n'interprétez et ne regroupez aucun caractère avant de mesurer.

Le lecteur Markdown masque les backticks et les astérisques,
ces caractères sont pourtant présents dans la source et doivent être comptés.

Les éléments suivants font partie du contenu de la cellule et entrent dans la mesure
de la largeur.

- Les backticks du code en ligne, par exemple la cellule `` `nom.valeur` `` a 12 caractères, pas 10.
- Les doubles backticks autour de valeurs comme des codes et des nombres,
  par exemple la cellule `` `` 00 `` `` a 6 caractères, pas 2.
- Les astérisques de l'italique, par exemple la cellule `*italique*` a 10 caractères, pas 8.
- Les doubles astérisques du gras, par exemple la cellule `**gras**` a 8 caractères, pas 4.
- Les underscores du formatage, par exemple la cellule `_texte_` a 7 caractères, pas 5.
- Les espaces, la ponctuation et tous les autres caractères visibles dans la source.

Les lettres accentuées et le ç comptent chacun pour un caractère,
par exemple le mot `Fréquence` a 9 caractères.

Écrivez les lettres accentuées sous forme composée, comme un seul caractère Unicode,
pour que la mesure de la largeur corresponde au nombre de caractères visibles.

L'erreur de formatage la plus fréquente consiste à mesurer la largeur du texte affiché
au lieu de celle du texte source.

La cellule `` ` api/configuration ` `` a 21 caractères dans la source,
le lecteur n'en affiche pourtant que 19.

L'emploi de 19 au lieu de 21 produit une colonne trop étroite et des barres verticales
décalées dans la vue texte.

### Compactage

Compactez la table après le calcul des largeurs de colonnes.

Retirez le remplissage qui dépasse la cellule la plus large de chaque colonne.

Recalculez après le compactage la ligne de séparation et le remplissage de toutes
les cellules.

Une table compactée a les plus petites largeurs de colonnes qui suffisent à l'affichage
correct de toutes les cellules.

La version compactée est la version correcte.

### Cellules multilignes

Évitez les cellules multilignes.

Si une cellule doit être coupée,
appliquez les mêmes règles de formatage dans toutes les lignes de la table.

### Contenu d'exemple

La table suivante est compactée et alignée.

Les largeurs de colonnes sont de 10, 8 et 13 caractères.

```markdown
| Colonne    | Valeur   | Description   |
|------------|----------|---------------|
| `kunde_id` | ``0001`` | Code client   |
| `nom`      | ``ABC``  | Nom court     |
```

## Noms de fichiers

Écrivez les noms des nouveaux fichiers de documentation en minuscules et séparez les mots
par des underscores, par exemple `specification_technique.md`.

N'utilisez pas de lettres accentuées ni d'espaces dans les noms des nouveaux fichiers.

Conservez les noms convenus dans leur forme d'origine, par exemple `README.md`,
`CHANGELOG.md` ou `SPECIFICATION.md`.

Préférez les mots complets aux abréviations que la demande n'emploie pas,
par exemple `rapport_de_fusion.md` plutôt que `rdf_rapport.md`.

Le nom du fichier doit correspondre au sujet du document.

## Exemple

### Correct

```markdown
# Plan des vues de données

## Objet

Ce document décrit les vues de données prévues dans la couche `gold`.

Chaque phrase est séparée par une ligne vide.

## Règles d'édition

- Écrivez des phrases courtes.
- Utilisez une phrase par paragraphe.
- Gardez les noms de sections courts.
```

### Incorrect

```markdown
# Plan des vues de données

## Objet
Ce document décrit les vues de données prévues dans la couche gold. Chaque phrase se trouve dans le même paragraphe ; le texte devient difficile à comparer en diff.

## Règles d'édition (obligatoires):
- Écrivez des phrases courtes.
- Utilisez une phrase par paragraphe.
- Gardez les noms de sections courts.
```

## Maintenance des fichiers

Conservez le style des fins de ligne et l'encodage du document que vous éditez.

Créez les nouveaux fichiers en encodage UTF-8.

Ne changez pas les conventions d'un document existant pour la numérotation des sections,
la numérotation des listes et les sections optionnelles, sauf si la commande de
modification les couvre.

Lors de l'édition, limitez les changements à la portée de la commande.

## Question de mise à jour

Lorsque des changements entrants sont prêts à être récupérés pour le dépôt de la
compétence, la question de mise à jour est
`Une mise à jour de la compétence est disponible (<n> nouveaux commits). Mettre à jour maintenant ou ignorer pour cette session ?`.

Les options de réponse sont `Mettre à jour maintenant` et `Ignorer pour cette session`.

## Phrases d'activation

Les demandes adressées à cette compétence peuvent être formulées en français.

Les phrases suivantes activent la compétence de la même façon que leurs équivalents
anglais dans `languages/en.md`.

Traitez une demande qui correspond à une phrase de la table comme son équivalent anglais.

| Phrase                                            | Équivalent anglais                       |
|---------------------------------------------------|------------------------------------------|
| crée un document                                  | create a document                        |
| rédige un document                                | create a document                        |
| spécification                                     | draft a specification                    |
| conception de solution                            | project document                         |
| documentation technique                           | technical documentation                  |
| documentation de projet                           | project documentation                    |
| article                                           | write an article                         |
| note                                              | quick note                               |
| document yaml                                     | yaml document                            |
| rédige une configuration yaml                     | write a yaml config                      |
| modifie ce fichier yaml                           | edit this yaml file                      |
| corrige ce tableau                                | fix this table                           |
| formate ce tableau                                | format this table                        |
| mets à jour ce document                           | update this document                     |
| traduis ce document                               | translate this document                  |
| traduis en allemand                               | translate to German                      |
| traduis en anglais                                | translate to English                     |
| traduis en polonais                               | translate to Polish                      |
| traduction de document                            | translate this document                  |
| nouveau document dans ce projet                   | new document in this project             |
| document de fonctionnalité                        | add a feature document                   |
| plan d'implémentation                             | write an implementation plan             |
| rédige un adr                                     | write an ADR                             |
| proposition de conception                         | design proposal                          |
| charte de projet                                  | project charter                          |
| registre des risques                              | risk register                            |
| registre des parties prenantes                    | stakeholder register                     |
| rapport d'avancement                              | status report                            |
| compte rendu de réunion                           | meeting minutes                          |
| plan de gestion                                   | management plan                          |
| structure de découpage du projet                  | work breakdown structure                 |
| plan du jour                                      | daily plan                               |
| message                                           | write a message                          |
| annonce                                           | write a message                          |
| demande de modification                           | change request                           |
| détecte la mise en page                           | detect document layout                   |
| analyse la structure du document                  | analyze document structure               |
| audit du document                                 | audit this document                      |
| vérifie le formatage du document                  | check document formatting                |
| planifie les corrections des constats             | plan fixes for findings                  |
| audit de traduction                               | audit this translation                   |
| vérifie la traduction                             | check the translation                    |
| contrôle la traduction                            | verify the translation                   |
| corrige la traduction                             | fix this translation                     |
| améliore la traduction                            | fix this translation                     |
| applique les corrections de revue à la traduction | apply review findings to the translation |
| traduction adaptée                                | adapted translation                      |
| document d'instructions d'agent                   | agent instruction document               |
| document de préparation                           | preparation document                     |
| guide de contribution                             | contributing guide                       |
| guide du contributeur                             | contributing guide                       |
| décris                                            | describe                                 |
| décris brièvement                                 | describe shortly                         |
| rédige une description                            | make a description                       |
| résume                                            | summarize                                |
| rédige un résumé                                  | write a summary                          |
| donne un aperçu                                   | give an overview                         |
| description courte                                | short description                        |
| description détaillée                             | detailed description                     |
| décris en détail                                  | describe in detail                       |
| description complète                              | full description                         |
| résume ce document dans un fichier                | summarize this document to a file        |
| abrégé du document                                | write an abstract of this document       |
| rédige un abrégé de ce document                   | write a brief of this document           |
| abrège ce document                                | abridge this document                    |
| rédige un supplément                              | write a supplement                       |
| étends ce rapport                                 | extend this report                       |
| travaille sur panther                             | work on panther                          |
| travaille sur cette compétence                    | work on this skill                       |
| répare cette compétence                           | fix this skill                           |
| ajuste la compétence                              | adjust the skill                         |
| mets à jour les documents de la compétence        | update the skill documents               |
| lance panther                                     | run panther                              |
| utilise panther                                   | use panther                              |
| utilise la compétence                             | use skill                                |
| utilise cette compétence                          | use this skill                           |
| active la compétence                              | activate the skill                       |
| travaille avec la compétence                      | work with skill                          |
| liste toutes les opérations                       | list all operations                      |
| montre toutes les capacités                       | show all capabilities                    |
| corrige ce document                               | correct this document                    |
| corriger ce document                              | correct this document                    |
| relis ce document                                 | proofread this document                  |
| humanise ce document                              | humanize this document                   |
| comme si une personne l'avait écrit               | make it read like a person wrote it      |
| réécris la voix du document                       | rewrite the voice                        |
| corrige la grammaire                              | correct the grammar                      |
| corrige les fautes                                | fix the typos                            |
| corrige les erreurs du document                   | fix the errors in this document          |
