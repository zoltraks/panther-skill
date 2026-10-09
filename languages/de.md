---
code: de
name: German
native-name: Deutsch
---

# Stil und Formatierung von Markdown-Dokumenten

## Zweck

Dieses Dokument definiert den Textstil und die Formatierungsregeln für Markdown-Dokumente in deutscher Sprache.

Es gilt für die gesamte Projektdokumentation, einschließlich Richtlinien, Standards, Vorlagen, Notizen und Referenzmaterial.

Es richtet sich an Inhalte erzeugende Werkzeuge und KI-Agenten, bleibt aber für Menschen lesbar.

Die unten beschriebenen Regeln gelten auch für dieses Dokument selbst.

## Inhaltsverzeichnis

| Abschnitt                        | Zeile | Umfang                                          |
|----------------------------------|-------|-------------------------------------------------|
| Dokumentstruktur                 | 45    | Titel, Zweck und Aufbau des Dokuments           |
| Überschriften                    | 63    | Groß- und Kleinschreibung sowie Qualifikatoren  |
| Abschnittsnummerierung           | 95    | Regeln zur Nummerierung von Abschnitten         |
| Regeln zum Inhaltsverzeichnis    | 107   | Wann ein Inhaltsverzeichnis eingefügt wird      |
| Absätze und Sätze                | 121   | Aufbau von Sätzen und Absätzen                  |
| Zeilenumbruch                    | 135   | Logische Zeilen und harte Zeilenumbrüche        |
| Listen                           | 159   | Aufzählungszeichen, Nummerierung und Abstände   |
| Leerzeilen und Abstände          | 181   | Regeln für Abstände                             |
| Codeblöcke                       | 195   | Zäune, Sprachkennzeichnungen und Inline-Code    |
| Inline-Formatierung              | 209   | Anführungszeichen, Fettung und Kursivierung     |
| Semikolons                       | 225   | Verbot des Semikolons im Fließtext              |
| Sonderzeichen                    | 251   | Rahmenzeichen und Emoji                         |
| Deutscher Wortschatz             | 259   | Bevorzugte Begriffe und Übersetzungskalküle     |
| Abschnittsnamen nach Dokumenttyp | 289   | Deutsche Abschnittsnamen und Elemente der Typen |
| Dialektmerkmale                  | 602   | Kapitelnummerierung und Pseudo-Überschriften    |
| Tabellen                         | 619   | Ausrichtung nach dem Quelltext                  |
| Dateinamen                       | 740   | Benennung neuer Dokumentationsdateien           |
| Beispiel                         | 750   | Richtiges und falsches Beispiel                 |
| Dateipflege                      | 784   | Kodierung und Zeilenenden                       |
| Aktualisierungsfrage             | 794   | Deutsche Formulierung der Aktualisierungsfrage  |
| Aktivierungsphrasen              | 800   | Deutsche Phrasen und englische Entsprechungen   |

## Dokumentstruktur

Verwende denselben Aufbau in jedem Dokument.

- Eine H1-Überschrift (`#`) am Anfang der Datei, eine pro Dokument, knapp und beschreibend.
- Ein Abschnitt zum Zweck oder Ziel, ein Absatz, der sagt, was das Dokument abdeckt.
- Hauptabschnitte auf Ebene H2 (`##`), Unterabschnitte auf Ebene H3 (`###`).

Die Abschnitte **Dokumentinformationen** und **Versionsverlauf** sind optional.

Füge diese Abschnitte nicht zu einem bestehenden Dokument hinzu.

Füge sie auch dann nicht in ein neues Dokument ein, wenn der Erstellungsauftrag dies nicht ausdrücklich verlangt.

Wenn das Dokument sie bereits enthält, aktualisiere sie bei jeder inhaltlichen Änderung.

Verwende keine Überschriften der Ebene H4 und tiefer.

## Überschriften

Schreibe Abschnitts- und Unterabschnittsnamen mit einem Großbuchstaben am Anfang und folge für die übrigen Wörter der normalen deutschen Groß- und Kleinschreibung.

Wende keinen englischen Title Case an, bei dem jedes Wort großgeschrieben wird.

Eigennamen, Abkürzungen und Technologienamen behalten ihre Schreibweise, zum Beispiel "XML-Formatierung", "Integration mit Microsoft Fabric", "Gold-Layer im Lakehouse".

Halte Abschnittsnamen kurz.

Setze keine Qualifikatoren in Klammern in den Abschnittsnamen.

Qualifikatoren wie "verpflichtend" oder "nicht wiederholen" gehören in den Text des Abschnitts.

Beende eine Überschrift nicht mit einem Satzzeichen.

### Richtig

```markdown
## Umfang der Quelldaten

### XML-Formatierung
```

### Falsch

```markdown
## Umfang Der Quelldaten

### XML-Formatierung (verpflichtend):
```

## Abschnittsnummerierung

Nummeriere Abschnitte standardmäßig nicht.

Das Fehlen der Nummerierung vereinfacht die Umorganisation eines Dokuments, weil das Verschieben eines Abschnitts keine Neunummerierung der übrigen erfordert.

Wenn das bearbeitete Dokument bereits eine Abschnittsnummerierung enthält, behalte sie bei und halte die richtige Reihenfolge der Nummern ein.

Nummeriere die Abschnitte nach dem Hinzufügen, Entfernen oder Verschieben so um, dass die Nummern lückenlos bleiben und der Reihenfolge im Dokument folgen.

Die Nummerierung eines Unterabschnitts spiegelt die Nummer des übergeordneten Abschnitts, zum Beispiel `3.1.` unter Abschnitt `3.`.

## Regeln zum Inhaltsverzeichnis

Füge standardmäßig kein Inhaltsverzeichnis hinzu.

Füge ein Inhaltsverzeichnis nur auf Anfrage ein und nur dann, wenn die Abschnitte des Dokuments nummeriert sind.

Eine Referenzdatei mit mehr als 300 Zeilen darf ein Inhaltsverzeichnis auch ohne Abschnittsnummerierung enthalten.

Platziere es am Anfang des Dokuments, unmittelbar nach dem optionalen Abschnitt Dokumentinformationen und dem optionalen Abschnitt Versionsverlauf.

Wenn diese Abschnitte fehlen, ist das Inhaltsverzeichnis der erste Abschnitt nach der H1-Überschrift.

Aktualisiere das Inhaltsverzeichnis nach jeder Änderung der Dokumentstruktur.

## Absätze und Sätze

Schreibe kurze Sätze.

Verwende für technische Beschreibungen einen Satz pro Absatz.

Dieser Aufbau bleibt in Texteditoren, im Terminal und im Versionsvergleich lesbar.

Trenne jeden Satz durch eine Leerzeile.

Ein Satz darf mehrere verbundene Teile enthalten, wenn sie einen Gedanken ausdrücken.

Packe keine unverbundenen Gedanken in einen langen Absatz.

## Zeilenumbruch

Breche den Text nicht hart an einer festen Spaltenbreite um.

Jeder Satz belegt eine logische Zeile.

Ein Satz darf lang sein, wenn der Gedanke lang ist, Editor oder Browser brechen den Text bei der Anzeige um.

Setze einen harten Zeilenumbruch nur dann, wenn der Quelltext selbst ihn erfordert, zum Beispiel in einem Codeblock oder in einem Diagramm.

Für ein bestehendes Dokument gewinnt dessen eigene Umbruchkonvention gegenüber dieser Vorgabe.

Erkenne, ob das Dokument Text an einer festen Breite umbricht oder logische Zeilen nutzt, behalte diese Konvention bei und ändere sie nur, wenn der Auftrag sie abdeckt.

Regeln des Repositorys wie ein `STYLE.md` mit Zeilen von höchstens 100 Zeichen legen die Konvention für neue Dateien fest und entscheiden in uneindeutigen Fällen.

Verwende `scripts/reflow-prose.py --wrap --width N`, um eine feste Breite anzuwenden, und `scripts/reflow-prose.py --unwrap`, um umgebrochene Zeilen zu logischen Zeilen zu verbinden.

Der Wrap-Modus teilt Zeilen nur, der Unwrap-Modus fügt sie nur zusammen, beide lassen Tabellen, Codeblöcke und eingezogene Codeblöcke unverändert.

Das Layout eines erzeugten Dokuments folgt `conventions/prose-layout.md` - diese Grundlage beschreibt die Konvention `separated`, und die Aufnahmeparameter `line-wrapping`, `sentence-spacing` und `wrap-width` können bei der Erstellung `flowing`, `bounded` oder `justified` wählen.

Die Erkennung des Layouts eines bestehenden Dokuments folgt `conventions/prose-layout.md` und nimmt niemals eine Vorgabe an.

## Listen

Verwende den Bindestrich (`-`) für Aufzählungspunkte.

Nummeriere Listeneinträge standardmäßig nicht.

Verwende eine Nummerierung für nacheinander ausgeführte Schritte, wenn das bearbeitete Dokument sie in der betreffenden Liste bereits verwendet oder wenn der Änderungsauftrag sie ausdrücklich verlangt.

Wenn die Liste nummeriert ist, halte die Nummern nach dem Hinzufügen oder Entfernen von Einträgen lückenlos.

Setze eine Leerzeile vor die Liste und eine Leerzeile hinter die Liste.

Setze keine Leerzeilen zwischen kurze Listeneinträge.

Setze eine Leerzeile zwischen Einträge, wenn die Einträge lang sind oder mehrere Sätze enthalten.

Setze eine Leerzeile zwischen einen übergeordneten Eintrag und seine untergeordnete Liste.

Rücke die untergeordnete Liste auf die Ebene des übergeordneten Eintrags ein.

Schreibe Aufgabenlisten als `- [ ]` für einen offenen Eintrag und `- [x]` für einen erledigten Eintrag.

## Leerzeilen und Abstände

Setze eine Leerzeile zwischen Absätze.

Setze eine Leerzeile vor eine Liste und eine hinter eine Liste.

Setze eine Leerzeile vor einen Codeblock und eine hinter einen Codeblock.

Setze eine Leerzeile vor eine Tabelle und eine hinter eine Tabelle.

Lasse nicht mehrere Leerzeilen hintereinander stehen.

Lasse keine Leerzeichen am Ende einer Zeile stehen.

## Codeblöcke

Fasse jeden Codeblock mit drei Backticks ein.

Gib die Sprachkennzeichnung nur dann an, wenn der Block Code in einer Programmier-, Auszeichnungs- oder Datensprache enthält.

Blöcke mit reinem Text, Prompts, Konsolen- oder stdout-Ausgaben, Verzeichnisbäumen, Diagrammen oder Tabellen bleiben ohne Kennzeichnung - `text` und `txt` sind ebenfalls Kennzeichnungen, und ein Dokument mit konsistenter `text`-Konvention behält sie.

Lasse keine Leerzeile als erste oder als letzte Zeile innerhalb des Blocks stehen.

Halte Codeblöcke knapp und auf das beschriebene Thema bezogen.

Schreibe Dateinamen, Verzeichnisnamen, Befehle, Spaltennamen und Werte als Inline-Code, zum Beispiel `docs/richtlinien`, `SELECT`, `Fact_Sales`.

## Inline-Formatierung

Verwende für normalen Text die Grundzeichen ohne typografische Varianten.

Verwende gerade ASCII-Anführungszeichen (`"`) anstelle typografischer Varianten wie deutscher Anführungszeichen oder Guillemets.

Verwende das gerade ASCII-Apostroph (`'`) anstelle des typografischen Apostrophs.

Wenn das bearbeitete Dokument konsequent einer anderen Konvention folgt, behalte die Konvention dieses Dokuments bei.

Schreibe Begriffsdefinitionen mit Fettung in der Form **Begriff**: Definition.

Setze Kursivierung sparsam ein.

Überstrapaziere keine Auszeichnungen.

## Semikolons

Verwende das Semikolon nicht im Fließtext.

Verbinde zwei eng verwandte Teilsätze mit einem Komma.

Wenn die Teilsätze eigene Gedanken ausdrücken, teile sie in eigene Sätze.

Die Regel gilt nicht für Codeblöcke, Inline-Code und Dateipfade.

### Richtig

```markdown
Rohdaten gelangen in den `bronze`-Layer, der `silver`-Layer enthält bereinigte Daten.

Der Name trägt die Bedeutung, der Kommentar trägt die Begründung.
```

### Falsch

```markdown
Rohdaten gelangen in den `bronze`-Layer; der `silver`-Layer enthält bereinigte Daten.

Der Name trägt die Bedeutung; der Kommentar trägt die Begründung.
```

## Sonderzeichen

Rahmenzeichen sind in Codeblöcken, Diagrammen und Schemata erlaubt.

Ersetze Rahmenzeichen nicht durch `+`, `-` oder andere ASCII-Näherungen.

Verwende keine Emoji, sofern es nicht ausdrücklich angefordert wurde.

## Deutscher Wortschatz

Schreibe korrektes Deutsch und vermeide zufällige Übersetzungskalküle aus dem Englischen.

Flektiere englische Wörter nicht mit deutschen Endungen, wenn ein natürliches deutsches Äquivalent existiert.

| Statt            | Verwende          |
|------------------|-------------------|
| deployen         | bereitstellen     |
| updaten          | aktualisieren     |
| fixen            | beheben           |
| customizen       | anpassen          |
| downgeloadet     | heruntergeladen   |
| challengen       | hinterfragen      |
| reviewen         | prüfen            |
| mergen           | zusammenführen    |
| syncen           | synchronisieren   |
| saven            | speichern         |
| performant       | leistungsfähig    |
| die Performance  | die Leistung      |
| der Statusreport | der Statusbericht |

Etablierte Eigennamen, Produktnamen und Architekturbegriffe behalten ihre Originalform, zum Beispiel Microsoft Fabric, Lakehouse, Warehouse, Power BI, Workspace.

Als Lehnwörter etablierte Fachbegriffe bleiben ebenfalls unverändert, zum Beispiel Commit, Pull Request, Merge, Branch, Repository, Deployment, Pipeline, Cache, Backend, Frontend, Framework und Endpoint.

Technische Namen aus dem Quellsystem schreibe exakt so, wie sie im System vorkommen.

Verwende in den Überschriften von Beispielen die deutschen Abschnittsnamen, zum Beispiel "Beispielinhalt", "Richtig" und "Falsch".

## Abschnittsnamen nach Dokumenttyp

Deutsche Abschnittsnamen werden ausschließlich in diesem Abschnitt deklariert.

Dateien in `types/` nennen nur die englischen Namen.

Wähle den deutschen Abschnittsnamen passend zum Dokumenttyp aus der folgenden Tabelle.

| Dokumenttyp              | Englischer Abschnitt               | Deutscher Abschnitt                     |
|--------------------------|------------------------------------|-----------------------------------------|
| agent-instruction        | Purpose                            | Zweck                                   |
| agent-instruction        | Audiences                          | Zielgruppen                             |
| agent-instruction        | Use Cases                          | Anwendungsfälle                         |
| agent-instruction        | Decision Points                    | Entscheidungspunkte                     |
| agent-instruction        | Procedures                         | Verfahren                               |
| agent-instruction        | Validation                         | Validierung                             |
| agent-instruction        | Example Content                    | Beispielinhalt                          |
| agent-instruction        | Best Practices                     | Bewährte Verfahren                      |
| agent-instruction        | References                         | Referenzen                              |
| article-text             | Introduction                       | Einleitung                              |
| article-text             | Summary                            | Zusammenfassung                         |
| article-text             | Further Reading                    | Weiterführende Literatur                |
| article-text             | References                         | Referenzen                              |
| change-request           | Document Information               | Dokumentinformationen                   |
| change-request           | Summary                            | Zusammenfassung                         |
| change-request           | Description                        | Beschreibung                            |
| change-request           | Justification                      | Begründung                              |
| change-request           | Impact                             | Auswirkung                              |
| change-request           | Alternatives                       | Alternativen                            |
| change-request           | Approval                           | Genehmigung                             |
| changelog-file           | Changes                            | Änderungen                              |
| changelog-file           | Version                            | Version                                 |
| changelog-file           | Added                              | Hinzugefügt                             |
| changelog-file           | Improved                           | Verbessert                              |
| changelog-file           | Fixed                              | Behoben                                 |
| changelog-file           | Removed                            | Entfernt                                |
| contributing-file        | Purpose                            | Zweck                                   |
| contributing-file        | Ways To Contribute                 | Möglichkeiten zur Mitarbeit             |
| contributing-file        | Reporting Issues                   | Probleme melden                         |
| contributing-file        | Development Setup                  | Entwicklungsumgebung einrichten         |
| contributing-file        | Pull Requests                      | Pull Requests                           |
| contributing-file        | AI-Assisted Contributions          | KI-gestützte Beiträge                   |
| contributing-file        | License                            | Lizenz                                  |
| contributing-file        | Code Of Conduct                    | Verhaltenskodex                         |
| contributing-file        | Getting Help                       | Hilfe erhalten                          |
| daily-plan               | Priorities                         | Prioritäten                             |
| daily-plan               | Schedule                           | Zeitplan                                |
| daily-plan               | Tasks                              | Aufgaben                                |
| daily-plan               | Notes                              | Notizen                                 |
| daily-plan               | Carry Over                         | Übertragen                              |
| daily-plan               | Document Information               | Dokumentinformationen                   |
| daily-plan               | Version History                    | Versionsverlauf                         |
| daily-plan               | Contents                           | Inhaltsverzeichnis                      |
| decision-record          | Status                             | Status                                  |
| decision-record          | Context                            | Kontext                                 |
| decision-record          | Decision Drivers                   | Entscheidungsfaktoren                   |
| decision-record          | Considered Options                 | Betrachtete Optionen                    |
| decision-record          | Decision Outcome                   | Entscheidungsergebnis                   |
| decision-record          | Consequences                       | Konsequenzen                            |
| decision-record          | Positive Consequences              | Positive Konsequenzen                   |
| decision-record          | Negative Consequences              | Negative Konsequenzen                   |
| decision-record          | Pros and Cons of Options           | Vor- und Nachteile der Optionen         |
| decision-record          | Links                              | Verweise                                |
| decision-record          | Supersedes                         | Ersetzt                                 |
| engineering-standard     | Purpose                            | Zweck                                   |
| engineering-standard     | Scope                              | Geltungsbereich                         |
| engineering-standard     | How To Use This Standard           | Verwendung dieser Norm                  |
| engineering-standard     | Order Of Operations                | Reihenfolge der Anwendung               |
| engineering-standard     | Precedence                         | Rangfolge                               |
| engineering-standard     | Non-Negotiable Rules               | Nicht verhandelbare Regeln              |
| engineering-standard     | Agent Intake Protocol              | Aufnahmeprotokoll des Agenten           |
| engineering-standard     | Detection First                    | Erkennung zuerst                        |
| engineering-standard     | Existing Project                   | Bestehendes Projekt                     |
| engineering-standard     | New Project                        | Neues Projekt                           |
| engineering-standard     | Documentation                      | Dokumentation                           |
| engineering-standard     | Language Version                   | Sprachversion                           |
| engineering-standard     | Core Technologies                  | Kerntechnologien                        |
| engineering-standard     | Project Structure                  | Projektstruktur                         |
| engineering-standard     | Naming Conventions                 | Namenskonventionen                      |
| engineering-standard     | Code Conventions                   | Codekonventionen                        |
| engineering-standard     | Formatting and Linting             | Formatierung und Linting                |
| engineering-standard     | Testing                            | Tests                                   |
| engineering-standard     | Build                              | Build                                   |
| engineering-standard     | Dependencies                       | Abhängigkeiten                          |
| engineering-standard     | Security                           | Sicherheit                              |
| engineering-standard     | Observability                      | Observability                           |
| engineering-standard     | Logging                            | Protokollierung                         |
| engineering-standard     | Comments                           | Kommentare                              |
| engineering-standard     | Error Handling                     | Fehlerbehandlung                        |
| engineering-standard     | Verification                       | Verifikation                            |
| engineering-standard     | Definition of Done                 | Definition of Done                      |
| engineering-standard     | Correctness                        | Korrektheit                             |
| engineering-standard     | Structure                          | Struktur                                |
| engineering-standard     | Quality                            | Qualität                                |
| engineering-standard     | Hygiene                            | Hygiene                                 |
| engineering-standard     | General Principles                 | Allgemeine Grundsätze                   |
| engineering-standard     | Sources                            | Quellen                                 |
| management-plan          | Methodology                        | Methodik                                |
| management-plan          | Roles and Responsibilities         | Rollen und Verantwortlichkeiten         |
| management-plan          | Thresholds and Tolerances          | Schwellenwerte und Toleranzen           |
| management-plan          | Cadence                            | Prüfungsrhythmus                        |
| management-plan          | Process                            | Prozess                                 |
| management-plan          | Tools                              | Werkzeuge                               |
| management-plan          | Reporting                          | Berichterstattung                       |
| management-plan          | Related Plans                      | Verwandte Pläne                         |
| management-plan          | Related Registers                  | Verwandte Register                      |
| management-plan          | Change Control                     | Änderungskontrolle                      |
| management-plan          | Master Plan                        | Masterplan                              |
| meeting-minutes          | Meeting Details                    | Sitzungsdaten                           |
| meeting-minutes          | Attendees                          | Teilnehmer                              |
| meeting-minutes          | Absentees                          | Abwesende                               |
| meeting-minutes          | Agenda                             | Tagesordnung                            |
| meeting-minutes          | Discussion                         | Diskussion                              |
| meeting-minutes          | Decisions                          | Beschlüsse                              |
| meeting-minutes          | Action Items                       | Aufgaben                                |
| meeting-minutes          | Open Questions                     | Offene Fragen                           |
| meeting-minutes          | Next Meeting                       | Nächste Sitzung                         |
| meeting-minutes          | Facilitator                        | Moderator                               |
| meeting-minutes          | Minute Taker                       | Protokollführer                         |
| meeting-minutes          | Due Date                           | Fälligkeitsdatum                        |
| meeting-minutes          | Owner                              | Verantwortlicher                        |
| message-document         | Background                         | Hintergrund                             |
| message-document         | Details                            | Details                                 |
| message-document         | Action Required                    | Erforderliche Aktion                    |
| message-document         | Next Steps                         | Nächste Schritte                        |
| message-document         | Contact                            | Kontakt                                 |
| message-document         | Document Information               | Dokumentinformationen                   |
| message-document         | Version History                    | Versionsverlauf                         |
| message-document         | Contents                           | Inhaltsverzeichnis                      |
| project-charter          | Purpose and Justification          | Zweck und Begründung                    |
| project-charter          | Measurable Objectives              | Messbare Ziele                          |
| project-charter          | Success Criteria                   | Erfolgskriterien                        |
| project-charter          | High-Level Requirements            | Rahmenanforderungen                     |
| project-charter          | Scope Boundaries                   | Grenzen des Projektumfangs              |
| project-charter          | In Scope                           | Im Projektumfang                        |
| project-charter          | Out of Scope                       | Außerhalb des Projektumfangs            |
| project-charter          | Deliverables                       | Ergebnisse                              |
| project-charter          | Milestones                         | Meilensteine                            |
| project-charter          | High-Level Budget                  | Budgetrahmen                            |
| project-charter          | Key Stakeholders                   | Wichtige Stakeholder                    |
| project-charter          | Project Manager Role and Authority | Rolle und Befugnisse des Projektleiters |
| project-charter          | Assumptions and Constraints        | Annahmen und Rahmenbedingungen          |
| project-charter          | High-Level Risks                   | Übergreifende Risiken                   |
| project-charter          | Exit Criteria                      | Abschlusskriterien                      |
| project-charter          | Approval                           | Genehmigung                             |
| project-document         | Document Purpose                   | Zweck des Dokuments                     |
| project-document         | Document Navigation                | Dokumentnavigation                      |
| project-document         | Glossary                           | Glossar                                 |
| project-document         | Abbreviations                      | Abkürzungen                             |
| project-document         | Vision                             | Vision                                  |
| project-document         | Goals                              | Ziele                                   |
| project-document         | Non-Goals                          | Nicht-Ziele                             |
| project-document         | Quality Requirements               | Qualitätsanforderungen                  |
| project-document         | System Architecture                | Systemarchitektur                       |
| project-document         | Component Diagram                  | Komponentendiagramm                     |
| project-document         | Functional Reqs                    | Funktionale Anforderungen               |
| project-document         | Non-Functional Reqs                | Nichtfunktionale Anforderungen          |
| project-document         | Use Cases                          | Anwendungsfälle                         |
| project-document         | Design Decisions                   | Entwurfsentscheidungen                  |
| project-document         | Implementation Phases              | Umsetzungsphasen                        |
| project-document         | Testing Strategy                   | Teststrategie                           |
| project-document         | Naming Conventions                 | Namenskonventionen                      |
| project-document         | Version Control                    | Versionskontrolle                       |
| project-document         | Documentation                      | Dokumentation                           |
| proposal-document        | Status                             | Status                                  |
| proposal-document        | Summary                            | Zusammenfassung                         |
| proposal-document        | Background                         | Hintergrund                             |
| proposal-document        | Proposal                           | Vorschlag                               |
| proposal-document        | Alternatives Considered            | Betrachtete Alternativen                |
| proposal-document        | Risks and Mitigations              | Risiken und Gegenmaßnahmen              |
| proposal-document        | Open Questions                     | Offene Fragen                           |
| proposal-document        | Decision                           | Entscheidung                            |
| proposal-document        | Reviewers                          | Prüfer                                  |
| readme-application       | Contents                           | Inhaltsverzeichnis                      |
| readme-application       | Overview                           | Überblick                               |
| readme-application       | Download                           | Download                                |
| readme-application       | Installation                       | Installation                            |
| readme-application       | Project Status                     | Projektstatus                           |
| readme-application       | Technical Stack                    | Technologiestack                        |
| readme-application       | Features                           | Funktionen                              |
| readme-application       | Quick Start                        | Schnellstart                            |
| readme-application       | Usage                              | Verwendung                              |
| readme-application       | Configuration                      | Konfiguration                           |
| readme-application       | Repository Structure               | Repository-Struktur                     |
| readme-application       | Documentation                      | Dokumentation                           |
| readme-application       | Changelog                          | Änderungsprotokoll                      |
| readme-application       | License                            | Lizenz                                  |
| readme-application       | Credits                            | Mitwirkende                             |
| readme-cli               | Overview                           | Überblick                               |
| readme-cli               | Install                            | Installation                            |
| readme-cli               | Commands                           | Befehle                                 |
| readme-cli               | Options                            | Optionen                                |
| readme-cli               | Examples                           | Beispiele                               |
| readme-cli               | Configuration                      | Konfiguration                           |
| readme-cli               | License                            | Lizenz                                  |
| readme-collection        | Overview                           | Überblick                               |
| readme-collection        | About This Repository              | Über dieses Repository                  |
| readme-collection        | Contents                           | Inhaltsverzeichnis                      |
| readme-collection        | Usage                              | Verwendung                              |
| readme-collection        | Notices                            | Hinweise                                |
| readme-collection        | License                            | Lizenz                                  |
| readme-collection        | Credits                            | Mitwirkende                             |
| readme-docs              | Overview                           | Überblick                               |
| readme-docs              | Documentation                      | Dokumentation                           |
| readme-docs              | Project Guidelines                 | Projektrichtlinien                      |
| readme-docs              | Repository Layout                  | Repository-Struktur                     |
| readme-docs              | License                            | Lizenz                                  |
| readme-general           | Contents                           | Inhaltsverzeichnis                      |
| readme-general           | Overview                           | Überblick                               |
| readme-general           | Installation                       | Installation                            |
| readme-general           | Usage                              | Verwendung                              |
| readme-general           | Project Layout                     | Projektstruktur                         |
| readme-general           | Documentation                      | Dokumentation                           |
| readme-general           | License                            | Lizenz                                  |
| readme-general           | Credits                            | Mitwirkende                             |
| readme-library           | Install                            | Installation                            |
| readme-library           | Usage                              | Verwendung                              |
| readme-library           | API Reference                      | API-Referenz                            |
| readme-library           | Configuration                      | Konfiguration                           |
| readme-library           | Contributing                       | Mitarbeit                               |
| readme-library           | License                            | Lizenz                                  |
| readme-skill             | Contents                           | Inhaltsverzeichnis                      |
| readme-skill             | Overview                           | Überblick                               |
| readme-skill             | What The Skill Does                | Funktionen des Skills                   |
| readme-skill             | Installation                       | Installation                            |
| readme-skill             | Agent Environments                 | Agenten-Umgebungen                      |
| readme-skill             | Usage                              | Verwendung                              |
| readme-skill             | Example Prompts                    | Beispiel-Prompts                        |
| readme-skill             | What's Inside                      | Inhalt                                  |
| readme-skill             | Verification                       | Überprüfung                             |
| readme-skill             | License                            | Lizenz                                  |
| readme-skill             | Credits                            | Mitwirkende                             |
| register-log             | Purpose                            | Zweck                                   |
| register-log             | Scoring Definitions                | Definitionen der Bewertungsskala        |
| register-log             | Probability                        | Eintrittswahrscheinlichkeit             |
| register-log             | Impact                             | Auswirkung                              |
| register-log             | Score                              | Bewertung                               |
| register-log             | Response Strategy                  | Umgangsstrategie                        |
| register-log             | Owner                              | Verantwortlicher                        |
| register-log             | Status                             | Status                                  |
| register-log             | Review Date                        | Überprüfungsdatum                       |
| register-log             | Raised Date                        | Erfassungsdatum                         |
| register-log             | Due Date                           | Fälligkeitsdatum                        |
| register-log             | Resolution                         | Lösung                                  |
| register-log             | Priority                           | Priorität                               |
| register-log             | Description                        | Beschreibung                            |
| register-log             | Category                           | Kategorie                               |
| register-log             | Assumption                         | Annahme                                 |
| register-log             | Constraint                         | Einschränkung                           |
| register-log             | Validated By                       | Validiert durch                         |
| register-log             | Submitted By                       | Gemeldet durch                          |
| register-log             | Decision                           | Entscheidung                            |
| register-log             | Authority                          | Entscheidungsinstanz                    |
| register-log             | Recommendation                     | Empfehlung                              |
| rules-document           | Purpose                            | Zweck                                   |
| rules-document           | Sources Of Truth                   | Maßgebliche Quellen                     |
| rules-document           | Scope                              | Geltungsbereich                         |
| rules-document           | General Rules                      | Allgemeine Regeln                       |
| rules-document           | Exceptions                         | Ausnahmen                               |
| rules-document           | Correct                            | Richtig                                 |
| rules-document           | Incorrect                          | Falsch                                  |
| rules-document           | Example Content                    | Beispielinhalt                          |
| rules-document           | File Maintenance                   | Dateipflege                             |
| rules-document           | Verification                       | Überprüfung                             |
| status-report            | Reporting Period                   | Berichtszeitraum                        |
| status-report            | Overall Status                     | Gesamtstatus                            |
| status-report            | Status by Area                     | Status nach Bereich                     |
| status-report            | Schedule                           | Zeitplan                                |
| status-report            | Budget                             | Budget                                  |
| status-report            | Scope                              | Umfang                                  |
| status-report            | Risk                               | Risiko                                  |
| status-report            | Summary                            | Zusammenfassung                         |
| status-report            | Accomplishments                    | Erreichte Ergebnisse                    |
| status-report            | Milestones                         | Meilensteine                            |
| status-report            | Metrics                            | Kennzahlen                              |
| status-report            | Top Risks and Issues               | Wichtigste Risiken und Probleme         |
| status-report            | Planned Next Period                | Plan für den nächsten Zeitraum          |
| status-report            | Decisions Needed                   | Benötigte Entscheidungen                |
| technical-document       | Purpose                            | Zweck                                   |
| technical-document       | Overview                           | Überblick                               |
| technical-document       | Prerequisites                      | Voraussetzungen                         |
| technical-document       | Configuration                      | Konfiguration                           |
| technical-document       | Usage                              | Verwendung                              |
| technical-document       | Examples                           | Beispiele                               |
| technical-document       | Troubleshooting                    | Fehlerbehebung                          |
| technical-document       | Limitations                        | Einschränkungen                         |
| technical-document       | References                         | Referenzen                              |
| work-breakdown-structure | Structure                          | Struktur                                |
| work-breakdown-structure | Work Packages                      | Arbeitspakete                           |
| work-breakdown-structure | WBS Dictionary                     | PSP-Verzeichnis                         |
| work-breakdown-structure | Acceptance Criteria                | Abnahmekriterien                        |
| work-breakdown-structure | Owner                              | Verantwortlicher                        |
| work-breakdown-structure | Estimate                           | Schätzung                               |
| work-breakdown-structure | Dependencies                       | Abhängigkeiten                          |
| work-breakdown-structure | RACI Matrix                        | RACI-Matrix                             |
| work-breakdown-structure | Baseline                           | Basislinie                              |

### Typspezifische Elemente

Einige Dokumenttypen legen auch deutsche Titel, Überschriftenmuster und Feldschlüssel fest.

| Dokumenttyp              | Element                              | Deutsche Form                               |
|--------------------------|--------------------------------------|---------------------------------------------|
| changelog-file           | H1-Titel                             | `# Änderungen`                              |
| management-plan          | H1-Titelmuster                       | `# Managementplan für <Bereich>`            |
| project-charter          | Typname und H1-Titelmuster           | `Projektauftrag`, `# Projektauftrag <Name>` |
| project-document         | Typische Dokumenttitel               | `Lösungsentwurf`, `Projektspezifikation`    |
| project-document         | H3-Anforderungsgruppe                | `Meilenstein I: ...`                        |
| project-document         | Mechanismenzeile des Anwendungsfalls | `**Verwendete Mechanismen:**`               |
| project-document         | Schlüssel der Metadatentabelle       | `Projektname`, `Version`                    |
| register-log             | H1-Titel des Risikoregisters         | `# Risikoregister`                          |
| work-breakdown-structure | Typname und Abkürzung                | `Projektstrukturplan` (PSP)                 |

## Dialektmerkmale

Deutsche formale Dokumente nummerieren häufig Kapitel und Unterkapitel, zum Beispiel `# 1 Grundlegende Angaben` und `## 1.1 Ziel`.

Sie können auch fettgedruckte Pseudo-Überschriften wie `**Hinweis**`, `**Wichtig**` oder `**Beschreibung:**` anstelle von Abschnittsüberschriften verwenden.

Eine Metadatentabelle mit leerer Kopfzeile kann den Versionskommentar in der deutschen Projektdokument-Konvention ersetzen.

```markdown
|             |                        |
|-------------|------------------------|
| Projektname | Data Integration Service |
| Version     | 1.0.7                  |
```

Bewahre diese Merkmale bei der Bearbeitung gemäß `conventions/markdown-dialects.md`.

## Tabellen

Tabellen müssen in der Textansicht lesbar bleiben, bevor ein Markdown-Viewer sie verarbeitet.

Die Ausrichtung der Spalten und die gleichmäßige Auffüllung der Zellen sind das Hauptziel der Formatierung.

### Trennzeichen

Trenne Spalten mit dem senkrechten Strich (`|`).

Setze ein Leerzeichen nach dem eine Zelle öffnenden Strich und ein Leerzeichen vor dem eine Zelle schließenden Strich.

Füge keine weiteren Leerzeichen um die Striche über das eine erforderliche hinaus ein.

Beginne jede Zeile - Kopfzeile, Trennzeile und Datenzeile - mit einem einzelnen senkrechten Strich.

Ein doppelter Strich am Zeilenanfang (`||`) wird als leere erste Zelle interpretiert.

Das Formatierungswerkzeug wandelt ihn dann in eine zusätzliche leere Spalte um, was die Struktur der Tabelle unbemerkt beschädigt und nicht nur verschiebt.

Schreibe eine absichtlich leere erste Zelle als `| |` und nur dann, wenn die Tabelle sie wirklich benötigt.

Eine leere Zelle ist nur in einer Spalte erlaubt, die die Trennzeile deklariert - ihre
Trennzelle muss mindestens einen Bindestrich enthalten.

Eine Spalte, die in jeder Zeile einschließlich der Kopfzeile leer ist, ist nie erlaubt -
entferne sie.

### Trennzeile

Setze die Trennzeile unmittelbar hinter die Kopfzeile.

Die Trennzeile enthält ausschließlich Bindestriche und senkrechte Striche.

Jede Zelle der Trennzeile enthält mindestens einen Bindestrich - eine Zelle aus Leerzeichen
deklariert die Spalte nicht.

Die Bindestriche schließen ohne Leerzeichen an die senkrechten Striche an.

Die Breite eines Spaltentrenners entspricht der Spaltenbreite plus zwei Bindestriche.

Die zwei zusätzlichen Bindestriche stehen für das Leerzeichen vor dem Zellenwert und das Leerzeichen danach.

Die minimale Spaltenbreite beträgt drei Zeichen.

### Zellenauffüllung

Fülle jede Zelle rechtsbündig mit Leerzeichen auf die Spaltenbreite auf.

Fülle leere Zellen mit Leerzeichen auf die Spaltenbreite auf.

Fülle Zellen nicht über die Spaltenbreite hinaus auf.

Kürze niemals den Inhalt einer Zelle.

Verwende linksbündige Ausrichtung in allen Zellen.

### Spaltenbreite

Die Spaltenbreite ist die größte Zeichenanzahl aller Zellen dieser Spalte, einschließlich der Kopfzelle.

Miss die Breite als Länge des **Quelltexts** der Zelle, nicht des angezeigten Textes.

Dies ist die wichtigste Regel der Tabellenformatierung.

Zähle jedes im Markdown-Quelltext vorhandene Zeichen, einschließlich aller Formatierungszeichen.

Entferne, interpretiere oder fasse keines der Zeichen vor dem Messen zusammen.

Der Markdown-Viewer verbirgt Backticks und Sternchen, diese Zeichen sind jedoch im Quelltext vorhanden und müssen mitgezählt werden.

Die folgenden Elemente sind Teil des Zelleninhalts und fließen in die Breitenmessung ein.

- Backticks um Inline-Code, zum Beispiel hat die Zelle `` `name.wert` `` 10 Zeichen, nicht 8.
- Doppelte Backticks um Werte wie Codes und Zahlen, zum Beispiel hat die Zelle `` ``00`` `` 6 Zeichen, nicht 2.
- Sternchen der Kursivierung, zum Beispiel hat die Zelle `*kursiv*` 9 Zeichen, nicht 7.
- Doppelte Sternchen der Fettung, zum Beispiel hat die Zelle `**fett**` 9 Zeichen, nicht 5.
- Unterstriche der Auszeichnung, zum Beispiel hat die Zelle `_text_` 7 Zeichen, nicht 5.
- Leerzeichen, Satzzeichen und alle übrigen im Quelltext sichtbaren Zeichen.

Deutsche Umlaute und ß zählen jeweils als ein Zeichen, zum Beispiel hat das Wort `Häufigkeit` 10 Zeichen.

Schreibe Umlaute in der komponierten Form als ein einzelnes Unicode-Zeichen, damit die Breitenmessung mit der Anzahl der sichtbaren Zeichen übereinstimmt.

Der häufigste Formatierungsfehler besteht darin, die Breite des angezeigten Textes anstelle der Breite des Quelltextes zu messen.

Die Zelle `` `api/konfiguration` `` hat 19 Zeichen im Quelltext, der Viewer zeigt jedoch nur 17 Zeichen.

Die Verwendung von 17 statt 19 ergibt eine zu schmale Spalte und verschobene senkrechte Striche in der Textansicht.

### Kompaktieren

Kompaktiere die Tabelle nach der Berechnung der Spaltenbreiten.

Entferne die Auffüllung, die über die breiteste Zelle der jeweiligen Spalte hinausgeht.

Berechne nach dem Kompaktieren die Trennzeile und die Auffüllung aller Zellen neu.

Eine kompaktierte Tabelle hat die kleinsten Spaltenbreiten, die zur korrekten Anzeige aller Zellen ausreichen.

Die kompaktierte Version ist die korrekte Version.

### Mehrzeilige Zellen

Vermeide mehrzeilige Zellen.

Wenn eine Zelle umgebrochen werden muss, wende dieselben Formatierungsregeln in allen Zeilen der Tabelle an.

### Beispielinhalt

Die folgende Tabelle ist kompaktiert und ausgerichtet.

Die Spaltenbreiten betragen 10, 8 und 13 Zeichen.

```markdown
| Spalte     | Wert     | Beschreibung  |
|------------|----------|---------------|
| `kunde_id` | ``0001`` | Kundenkennung |
| `name`     | ``ABC``  | Kurzname      |
```

## Dateinamen

Schreibe die Namen neuer Dokumentationsdateien klein und trenne die Wörter mit Unterstrichen, zum Beispiel `technische_spezifikation.md`.

Verwende keine Umlaute und keine Leerzeichen in den Namen neuer Dateien.

Behalte vereinbarte Namen in ihrer Originalform, zum Beispiel `README.md`, `CHANGELOG.md` oder `SPEZIFIKATION.md`.

Der Dateiname soll dem Thema des Dokuments entsprechen.

## Beispiel

### Richtig

```markdown
# Plan für Datensichten

## Zweck

Dieses Dokument beschreibt die geplanten Datensichten im `gold`-Layer.

Jeder Satz ist durch eine Leerzeile getrennt.

## Bearbeitungsregeln

- Schreibe kurze Sätze.
- Verwende einen Satz pro Absatz.
- Halte Abschnittsnamen kurz.
```

### Falsch

```markdown
# Plan für Datensichten

## Zweck
Dieses Dokument beschreibt die geplanten Datensichten im Layer gold. Jeder Satz steht im selben Absatz; der Text wird schwer im Versionsvergleich zu lesen.

## Bearbeitungs-Regeln (verpflichtend):
- Schreibe kurze Sätze.
- Verwende einen Satz pro Absatz.
- Halte Abschnittsnamen kurz.
```

## Dateipflege

Bewahre den vorhandenen Stil der Zeilenenden und die Kodierung des bearbeiteten Dokuments.

Erstelle neue Dateien in UTF-8-Kodierung.

Ändere die Konventionen eines bestehenden Dokuments bei Abschnittsnummerierung, Listennummerierung und optionalen Abschnitten nicht, sofern der Änderungsauftrag dies nicht umfasst.

Begrenze Bearbeitungen auf den Umfang des Auftrags.

## Aktualisierungsfrage

Wenn für das Skill-Repository eingehende Änderungen zum Abruf bereitstehen, lautet die Aktualisierungsfrage `Ein Update des Skills ist verfügbar (<n> neue Commits). Jetzt aktualisieren oder in dieser Sitzung überspringen?`.

Die Antwortoptionen sind `Jetzt aktualisieren` und `In dieser Sitzung überspringen`.

## Aktivierungsphrasen

An diese Fähigkeit gerichtete Anfragen können auf Deutsch formuliert sein.

Die folgenden Phrasen aktivieren die Fähigkeit genauso wie ihre englischen Entsprechungen in `SKILL.md`.

Behandle eine Anfrage, die einer Phrase aus der Tabelle entspricht, wie ihre englische Entsprechung.

| Phrase                                | Englische Entsprechung                   |
|---------------------------------------|------------------------------------------|
| erstelle ein dokument                 | create a document                        |
| schreibe ein dokument                 | create a document                        |
| spezifikation                         | draft a specification                    |
| lösungsentwurf                        | project document                         |
| technische dokumentation              | technical documentation                  |
| projektdokumentation                  | project documentation                    |
| artikel                               | write an article                         |
| notiz                                 | quick note                               |
| tabelle korrigieren                   | fix this table                           |
| tabelle formatieren                   | format this table                        |
| dokument aktualisieren                | update this document                     |
| dokument übersetzen                   | translate this document                  |
| übersetze ins deutsche                | translate to German                      |
| übersetze ins englische               | translate to English                     |
| übersetze ins polnische               | translate to Polish                      |
| dokumentenübersetzung                 | translate this document                  |
| neues dokument im projekt             | new document in this project             |
| funktionsdokument                     | add a feature document                   |
| implementierungsplan                  | write an implementation plan             |
| schreibe einen adr                    | write an ADR                             |
| entwurfsvorschlag                     | design proposal                          |
| projektauftrag                        | project charter                          |
| risikoregister                        | risk register                            |
| stakeholder-register                  | stakeholder register                     |
| statusbericht                         | status report                            |
| besprechungsprotokoll                 | meeting minutes                          |
| managementplan                        | management plan                          |
| projektstrukturplan                   | work breakdown structure                 |
| tagesplan                             | daily plan                               |
| nachricht                             | write a message                          |
| mitteilung                            | write a message                          |
| änderungsantrag                       | change request                           |
| layout erkennen                       | detect document layout                   |
| dokumentstruktur analysieren          | analyze document structure               |
| dokument-audit                        | audit this document                      |
| formatierung prüfen                   | check document formatting                |
| korrekturen für feststellungen planen | plan fixes for findings                  |
| übersetzungs-audit                    | audit this translation                   |
| prüfe die übersetzung                 | check the translation                    |
| überprüfe die übersetzung             | verify the translation                   |
| korrigiere die übersetzung            | fix this translation                     |
| verbessere die übersetzung            | fix this translation                     |
| wende die übersetzungskorrekturen an  | apply review findings to the translation |
| adaptiv übersetzen                    | adapted translation                      |
| agenten-anweisungsdokument            | agent instruction document               |
| vorbereitungsdokument                 | preparation document                     |
| contributing-leitfaden                | contributing guide                       |
| mitarbeitsleitfaden                   | contributing guide                       |
| beschreibe                            | describe                                 |
| beschreibe kurz                       | describe shortly                         |
| erstelle eine beschreibung            | make a description                       |
| fasse zusammen                        | summarize                                |
| schreibe eine zusammenfassung         | write a summary                          |
| gib einen überblick                   | give an overview                         |
| kurzbeschreibung                      | short description                        |
| ausführliche beschreibung             | detailed description                     |
| beschreibe detailliert                | describe in detail                       |
| vollständige beschreibung             | full description                         |
| dokument-zusammenfassung erstellen    | summarize this document to a file        |
| kurzfassung des dokuments             | write an abstract of this document       |
| schreibe eine kurzfassung             | write a brief of this document           |
| kürze dieses dokument                 | abridge this document                    |
| schreibe eine ergänzung               | write a supplement                       |
| ergänzung zum bericht                 | extend this report                       |
| arbeite an panther                    | work on panther                          |
| arbeite an dieser fähigkeit           | work on this skill                       |
| repariere diese fähigkeit             | fix this skill                           |
| passe diese fähigkeit an              | adjust the skill                         |
| aktualisiere die fähigkeitsdokumente  | update the skill documents               |
| starte panther                        | run panther                              |
| verwende panther                      | use panther                              |
| verwende die fähigkeit                | use skill                                |
| verwende diese fähigkeit              | use this skill                           |
| aktiviere die fähigkeit               | activate the skill                       |
