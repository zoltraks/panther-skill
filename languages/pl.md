---
code: pl
name: Polish
native-name: polski
---

# Styl i formatowanie dokumentów Markdown

## Przeznaczenie

Ten dokument definiuje styl tekstu oraz zasady formatowania dokumentów Markdown pisanych w języku polskim.

Obowiązuje w całej dokumentacji projektu, w tym w wytycznych, standardach, szablonach, notatkach i materiałach referencyjnych.

Jest przeznaczony dla narzędzi generujących treść oraz agentów AI, ale ma pozostać czytelny dla człowieka.

Zasady opisane poniżej stosują się również do samego tego dokumentu.

## Spis treści

| Sekcja                             | Wiersz | Zakres                                      |
|------------------------------------|--------|---------------------------------------------|
| Struktura dokumentu                | 45     | Tytuł, cel i układ dokumentu                |
| Nagłówki                           | 63     | Wielkość liter i kwalifikatory              |
| Numeracja sekcji                   | 95     | Zasady numerowania sekcji                   |
| Zasady spisu treści                | 107    | Kiedy dodawać spis treści                   |
| Akapity i zdania                   | 121    | Budowa zdań i akapitów                      |
| Zawijanie wierszy                  | 135    | Wiersze logiczne i twarde łamania           |
| Listy                              | 149    | Punktory, numeracja i odstępy               |
| Puste wiersze i odstępy            | 171    | Zasady odstępów                             |
| Bloki kodu                         | 185    | Ogrodzenia, znaczniki i kod liniowy         |
| Formatowanie w treści              | 199    | Cudzysłowy, pogrubienia i kursywa           |
| Średniki                           | 215    | Zakaz średników w tekście                   |
| Znaki specjalne                    | 241    | Znaki ramek i emoji                         |
| Słownictwo polskie                 | 249    | Preferowane terminy i kalki                 |
| Nazwy sekcji według typu dokumentu | 275    | Polskie nazwy sekcji i elementy typów       |
| Cechy dialektów                    | 523    | Numeracja rozdziałów i pseudo-nagłówki      |
| Tabele                             | 540    | Wyrównanie według źródła                    |
| Nazwy plików                       | 654    | Nazywanie nowych plików dokumentacji        |
| Przykład                           | 664    | Przykład poprawny i niepoprawny             |
| Utrzymanie plików                  | 698    | Kodowanie i złamania wierszy                |
| Pytanie o aktualizację             | 708    | Polskie brzmienie pytania o aktualizację    |
| Frazy aktywujące                   | 714    | Polskie frazy i ich angielskie odpowiedniki |

## Struktura dokumentu

Stosuj ten sam układ w każdym dokumencie.

- Tytuł H1 (`#`) na początku pliku, jeden na dokument, zwięzły i opisowy.
- Sekcja przeznaczenia lub celu, jeden akapit mówiący, co dokument obejmuje.
- Sekcje główne w poziomie H2 (`##`), podsekcje w poziomie H3 (`###`).

Sekcje **Informacje o dokumencie** oraz **Historia wersji** są opcjonalne.

Nie dodawaj tych sekcji do istniejącego dokumentu.

Nie dodawaj ich także w nowym dokumencie, o ile żądanie utworzenia dokumentu wyraźnie tego nie wymaga.

Jeśli dokument już je zawiera, aktualizuj je przy każdej zmianie treści.

Nie używaj nagłówków H4 i głębszych.

## Nagłówki

Nazwy sekcji i podsekcji pisz zwykłą wielką literą na początku, pozostałe wyrazy małą literą.

Nie stosuj angielskiego Stylu Tytułowego, w którym każdy wyraz zaczyna się wielką literą.

Nazwy własne, skróty i nazwy technologii zachowują swoją pisownię, na przykład "Formatowanie XML", "Integracja z Microsoft Fabric", "Warstwa gold w Lakehouse".

Utrzymuj krótkie nazwy sekcji.

Nie umieszczaj kwalifikatorów w nawiasach w nazwie sekcji.

Kwalifikatory w rodzaju "obowiązkowe" lub "nie powtarzać" umieszczaj w treści sekcji.

Nie kończ nagłówka znakiem interpunkcyjnym.

### Poprawnie

```markdown
## Zakres danych źródłowych

### Formatowanie XML
```

### Niepoprawnie

```markdown
## Zakres Danych Źródłowych

### Formatowanie XML (obowiązkowe):
```

## Numeracja sekcji

Domyślnie nie numeruj sekcji.

Brak numeracji upraszcza reorganizację dokumentu, ponieważ przeniesienie sekcji nie wymaga przenumerowania pozostałych.

Jeśli redagowany dokument już zawiera numerację sekcji, zachowaj ją i utrzymaj prawidłową kolejność numerów.

Po dodaniu, usunięciu lub przeniesieniu sekcji przenumeruj sekcje tak, aby numery były ciągłe i zgodne z kolejnością w dokumencie.

Numeracja podsekcji odzwierciedla numer sekcji nadrzędnej, na przykład `3.1.` w sekcji `3.`.

## Zasady spisu treści

Domyślnie nie dodawaj spisu treści.

Spis treści dodawaj tylko na żądanie i tylko wtedy, gdy sekcje dokumentu są numerowane.

Plik referencyjny dłuższy niż 300 wierszy może zawierać spis treści nawet bez numerowania sekcji.

Umieszczaj go na początku dokumentu, bezpośrednio po opcjonalnej sekcji informacji o dokumencie i opcjonalnej sekcji historii wersji.

Jeśli tych sekcji nie ma, spis treści jest pierwszą sekcją po tytule H1.

Po zmianie struktury dokumentu zaktualizuj spis treści.

## Akapity i zdania

Pisz krótkie zdania.

Dla opisów technicznych stosuj jedno zdanie na akapit.

Taki układ pozostaje czytelny w edytorach tekstu, w terminalu i w wyniku porównania wersji.

Oddzielaj każde zdanie pustym wierszem.

Zdanie może zawierać kilka powiązanych części, jeśli wyrażają jedną myśl.

Nie upychaj niepowiązanych myśli w jednym długim akapicie.

## Zawijanie wierszy

Nie zawijaj tekstu na sztywno na ustalonej szerokości kolumny.

Każde zdanie zajmuje jeden wiersz logiczny.

Zdanie może być długie, gdy myśl jest długa, edytor lub przeglądarka zawinie tekst przy wyświetlaniu.

Wstawiaj twarde złamanie wiersza tylko wtedy, gdy wymaga tego sama treść źródłowa, na przykład w bloku kodu lub w diagramie.

Wyjątek: gdy własne reguły repozytorium narzucają twardy limit, na przykład `STYLE.md` wymagający wierszy nie dłuższych niż 100 znaków, wykryj tę konwencję przed formatowaniem i zastosuj `tools/wrap-prose.py --width N`.

Narzędzie tylko dzieli wiersze - nigdy ich nie łączy i nie rusza tabel, bloków kodu ani wciętych bloków kodu.

## Listy

Stosuj myślnik (`-`) dla punktów wypunktowania.

Domyślnie nie numeruj pozycji list.

Numerację stosuj dla kroków wykonywanych po kolei, gdy redagowany dokument już ją stosuje w danej liście albo gdy żądanie zmiany wyraźnie tego wymaga.

Jeśli lista jest numerowana, utrzymaj ciągłość numerów po dodaniu lub usunięciu pozycji.

Wstawiaj jeden pusty wiersz przed listą i jeden po liście.

Nie wstawiaj pustych wierszy między krótkimi pozycjami listy.

Wstawiaj pusty wiersz między pozycjami, gdy pozycje są długie lub zawierają kilka zdań.

Wstawiaj jeden pusty wiersz między pozycją nadrzędną a jej listą podrzędną.

Listę podrzędną wcinaj do poziomu pozycji nadrzędnej.

Listy zadań zapisuj w postaci `- [ ]` dla pozycji otwartej i `- [x]` dla pozycji wykonanej.

## Puste wiersze i odstępy

Stosuj jeden pusty wiersz między akapitami.

Stosuj jeden pusty wiersz przed listą i po liście.

Stosuj jeden pusty wiersz przed blokiem kodu i po bloku kodu.

Stosuj jeden pusty wiersz przed tabelą i po tabeli.

Nie zostawiaj kilku pustych wierszy jeden po drugim.

Nie zostawiaj znaków odstępu na końcu wiersza.

## Bloki kodu

Każdy blok kodu ogradzaj trzema znakami odwróconego apostrofu.

Podawaj znacznik języka tylko wtedy, gdy blok zawiera kod w języku programowania, znaczników lub danych.

Bloki ze zwykłym tekstem, drzewami katalogów, diagramami, wynikami konsoli lub tabelami pozostawiaj bez znacznika.

Nie zostawiaj pustego wiersza jako pierwszego ani jako ostatniego wiersza wewnątrz bloku.

Utrzymuj bloki kodu zwięzłe i związane z opisywanym zagadnieniem.

Nazwy plików, katalogów, polecenia, nazwy kolumn i wartości zapisuj w kodzie liniowym, na przykład `docs/wytyczne`, `SELECT`, `Fact_Sales`.

## Formatowanie w treści

Do zwykłego tekstu używaj podstawowych znaków, bez ozdobnych odpowiedników.

Stosuj proste cudzysłowy ASCII (`"`) zamiast cudzysłowów typograficznych.

Stosuj prosty apostrof ASCII (`'`) zamiast apostrofu typograficznego.

Jeśli redagowany dokument konsekwentnie stosuje inną konwencję, zachowaj konwencję tego dokumentu.

Definicje terminów zapisuj z użyciem pogrubienia w postaci **Termin**: definicja.

Kursywę stosuj oszczędnie.

Nie nadużywaj wyróżnień.

## Średniki

Nie używaj znaku średnika w tekście ciągłym.

Dwa blisko powiązane zdania składowe łącz przecinkiem.

Gdy zdania składowe wyrażają osobne myśli, rozdziel je na osobne zdania.

Zasada nie dotyczy bloków kodu, kodu liniowego ani ścieżek plików.

### Poprawnie

```markdown
Dane surowe trafiają do warstwy `bronze`, warstwa `silver` zawiera dane oczyszczone.

Nazwa nosi znaczenie, komentarz nosi uzasadnienie.
```

### Niepoprawnie

```markdown
Dane surowe trafiają do warstwy `bronze`; warstwa `silver` zawiera dane oczyszczone.

Nazwa nosi znaczenie; komentarz nosi uzasadnienie.
```

## Znaki specjalne

Znaki rysowania ramek są dozwolone w blokach kodu, w diagramach i w schematach.

Nie zamieniaj znaków rysowania ramek na `+`, `-` ani na inne przybliżenia ASCII.

Nie używaj emoji, o ile nie zostało to wyraźnie zamówione.

## Słownictwo polskie

Pisz poprawną polszczyzną i unikaj przypadkowych kalek z języka angielskiego.

Nie odmieniaj angielskich wyrazów polskimi końcówkami, gdy istnieje naturalny polski odpowiednik.

| Zamiast           | Używaj                |
|-------------------|-----------------------|
| ownerzy biznesowi | właściciele biznesowi |
| dane skrapane     | dane skrapowane       |
| deployować        | wdrażać               |
| requestować       | zgłaszać              |
| update'ować       | aktualizować          |
| fixować           | poprawiać             |
| kastomizacja      | dostosowanie          |
| performance       | wydajność             |
| stakeholderzy     | interesariusze        |
| status report     | raport o statusie     |
| meeting minutes   | protokół zebrania     |

Ustalone nazwy własne, nazwy produktów i nazwy elementów architektury zachowuj w formie oryginalnej, na przykład Microsoft Fabric, Lakehouse, Warehouse, Power BI, workspace.

Nazwy techniczne pochodzące z systemu źródłowego zapisuj dokładnie tak, jak występują w systemie.

W nagłówkach przykładów stosuj polskie nazwy sekcji, na przykład "Przykład zawartości", "Poprawnie" oraz "Niepoprawnie".

## Nazwy sekcji według typu dokumentu

Nazwy polskich sekcji deklaruje wyłącznie ta sekcja.

Pliki w `types/` wymieniają tylko nazwy angielskie.

Dobieraj polską nazwę sekcji według typu dokumentu z poniższej tabeli.

| Typ dokumentu            | Sekcja angielska                   | Sekcja polska                          |
|--------------------------|------------------------------------|----------------------------------------|
| agent-instruction        | Purpose                            | Przeznaczenie                          |
| agent-instruction        | Audiences                          | Odbiorcy                               |
| agent-instruction        | Use Cases                          | Przypadki użycia                       |
| agent-instruction        | Decision Points                    | Punkty decyzyjne                       |
| agent-instruction        | Procedures                         | Procedury                              |
| agent-instruction        | Validation                         | Weryfikacja                            |
| agent-instruction        | Example Content                    | Przykład zawartości                    |
| agent-instruction        | Best Practices                     | Dobre praktyki                         |
| agent-instruction        | References                         | Referencje                             |
| article-text             | Introduction                       | Wprowadzenie                           |
| article-text             | Summary                            | Podsumowanie                           |
| article-text             | Further Reading                    | Dalsza lektura                         |
| article-text             | References                         | Referencje                             |
| changelog-file           | Changes                            | Zmiany                                 |
| changelog-file           | Version                            | Wersja                                 |
| changelog-file           | Added                              | Dodane                                 |
| changelog-file           | Improved                           | Ulepszone                              |
| changelog-file           | Fixed                              | Naprawione                             |
| changelog-file           | Removed                            | Usunięte                               |
| decision-record          | Status                             | Stan                                   |
| decision-record          | Context                            | Kontekst                               |
| decision-record          | Decision Drivers                   | Czynniki decyzyjne                     |
| decision-record          | Considered Options                 | Rozważane opcje                        |
| decision-record          | Decision Outcome                   | Wynik decyzji                          |
| decision-record          | Consequences                       | Konsekwencje                           |
| decision-record          | Positive Consequences              | Konsekwencje pozytywne                 |
| decision-record          | Negative Consequences              | Konsekwencje negatywne                 |
| decision-record          | Pros and Cons of Options           | Zalety i wady opcji                    |
| decision-record          | Links                              | Linki                                  |
| decision-record          | Supersedes                         | Zastępuje                              |
| management-plan          | Methodology                        | Metodyka                               |
| management-plan          | Roles and Responsibilities         | Role i odpowiedzialności               |
| management-plan          | Thresholds and Tolerances          | Progi i tolerancje                     |
| management-plan          | Cadence                            | Częstotliwość przeglądów               |
| management-plan          | Process                            | Proces                                 |
| management-plan          | Tools                              | Narzędzia                              |
| management-plan          | Reporting                          | Raportowanie                           |
| management-plan          | Related Plans                      | Plany powiązane                        |
| management-plan          | Related Registers                  | Powiązane rejestry                     |
| management-plan          | Change Control                     | Kontrola zmian                         |
| management-plan          | Master Plan                        | Plan główny                            |
| meeting-minutes          | Meeting Details                    | Dane zebrania                          |
| meeting-minutes          | Attendees                          | Obecni                                 |
| meeting-minutes          | Absentees                          | Nieobecni                              |
| meeting-minutes          | Agenda                             | Porządek obrad                         |
| meeting-minutes          | Discussion                         | Dyskusja                               |
| meeting-minutes          | Decisions                          | Decyzje                                |
| meeting-minutes          | Action Items                       | Elementy działania                     |
| meeting-minutes          | Open Questions                     | Otwarte pytania                        |
| meeting-minutes          | Next Meeting                       | Następne zebranie                      |
| meeting-minutes          | Facilitator                        | Prowadzący                             |
| meeting-minutes          | Minute Taker                       | Protokolant                            |
| meeting-minutes          | Due Date                           | Termin                                 |
| meeting-minutes          | Owner                              | Właściciel                             |
| project-charter          | Purpose and Justification          | Uzasadnienie                           |
| project-charter          | Measurable Objectives              | Mierzalne cele                         |
| project-charter          | Success Criteria                   | Kryteria sukcesu                       |
| project-charter          | High-Level Requirements            | Wymagania ogólne                       |
| project-charter          | Scope Boundaries                   | Granice zakresu                        |
| project-charter          | In Scope                           | W zakresie                             |
| project-charter          | Out of Scope                       | Poza zakresem                          |
| project-charter          | Deliverables                       | Rezultaty                              |
| project-charter          | Milestones                         | Kamienie milowe                        |
| project-charter          | High-Level Budget                  | Budżet                                 |
| project-charter          | Key Stakeholders                   | Kluczowi interesariusze                |
| project-charter          | Project Manager Role and Authority | Rola i uprawnienia kierownika projektu |
| project-charter          | Assumptions and Constraints        | Założenia i ograniczenia               |
| project-charter          | High-Level Risks                   | Ryzyka ogólne                          |
| project-charter          | Exit Criteria                      | Kryteria zakończenia                   |
| project-charter          | Approval                           | Zatwierdzenie                          |
| project-document         | Document Purpose                   | Cel dokumentu                          |
| project-document         | Document Navigation                | Nawigacja dokumentu                    |
| project-document         | Glossary                           | Słownik pojęć                          |
| project-document         | Abbreviations                      | Skróty                                 |
| project-document         | Vision                             | Wizja                                  |
| project-document         | Goals                              | Cele                                   |
| project-document         | Non-Goals                          | Cele wykluczone                        |
| project-document         | Quality Requirements               | Wymagania jakościowe                   |
| project-document         | System Architecture                | Architektura systemu                   |
| project-document         | Component Diagram                  | Diagram komponentów                    |
| project-document         | Functional Reqs                    | Wymagania funkcjonalne                 |
| project-document         | Non-Functional Reqs                | Wymagania niefunkcjonalne              |
| project-document         | Use Cases                          | Przypadki użycia                       |
| project-document         | Design Decisions                   | Decyzje architektoniczne               |
| project-document         | Implementation Phases              | Fazy realizacji                        |
| project-document         | Testing Strategy                   | Strategia testowania                   |
| project-document         | Naming Conventions                 | Konwencje nazewnicze                   |
| project-document         | Version Control                    | Kontrola wersji                        |
| project-document         | Documentation                      | Dokumentacja                           |
| proposal-document        | Status                             | Stan                                   |
| proposal-document        | Summary                            | Podsumowanie                           |
| proposal-document        | Background                         | Tło                                    |
| proposal-document        | Proposal                           | Propozycja                             |
| proposal-document        | Alternatives Considered            | Rozważane alternatywy                  |
| proposal-document        | Risks and Mitigations              | Ryzyka i środki zaradcze               |
| proposal-document        | Open Questions                     | Otwarte pytania                        |
| proposal-document        | Decision                           | Decyzja                                |
| proposal-document        | Reviewers                          | Recenzenci                             |
| readme-application       | Contents                           | Spis treści                            |
| readme-application       | Overview                           | Przegląd                               |
| readme-application       | Download                           | Pobieranie                             |
| readme-application       | Installation                       | Instalacja                             |
| readme-application       | Project Status                     | Status projektu                        |
| readme-application       | Technical Stack                    | Stos technologiczny                    |
| readme-application       | Features                           | Funkcje                                |
| readme-application       | Quick Start                        | Szybki start                           |
| readme-application       | Usage                              | Użycie                                 |
| readme-application       | Configuration                      | Konfiguracja                           |
| readme-application       | Repository Structure               | Struktura repozytorium                 |
| readme-application       | Documentation                      | Dokumentacja                           |
| readme-application       | Changelog                          | Dziennik zmian                         |
| readme-application       | License                            | Licencja                               |
| readme-application       | Credits                            | Autorzy                                |
| readme-cli               | Overview                           | Przegląd                               |
| readme-cli               | Install                            | Instalacja                             |
| readme-cli               | Commands                           | Polecenia                              |
| readme-cli               | Options                            | Opcje                                  |
| readme-cli               | Examples                           | Przykłady                              |
| readme-cli               | Configuration                      | Konfiguracja                           |
| readme-cli               | License                            | Licencja                               |
| readme-collection        | Overview                           | Przegląd                               |
| readme-collection        | About This Repository              | O tym repozytorium                     |
| readme-collection        | Contents                           | Spis treści                            |
| readme-collection        | Usage                              | Użycie                                 |
| readme-collection        | Notices                            | Uwagi                                  |
| readme-collection        | License                            | Licencja                               |
| readme-collection        | Credits                            | Autorzy                                |
| readme-docs              | Overview                           | Przegląd                               |
| readme-docs              | Documentation                      | Dokumentacja                           |
| readme-docs              | Project Guidelines                 | Zasady projektu                        |
| readme-docs              | Repository Layout                  | Struktura repozytorium                 |
| readme-docs              | License                            | Licencja                               |
| readme-general           | Contents                           | Spis treści                            |
| readme-general           | Overview                           | Przegląd                               |
| readme-general           | Installation                       | Instalacja                             |
| readme-general           | Usage                              | Użycie                                 |
| readme-general           | Project Layout                     | Struktura projektu                     |
| readme-general           | Documentation                      | Dokumentacja                           |
| readme-general           | License                            | Licencja                               |
| readme-general           | Credits                            | Autorzy                                |
| readme-library           | Install                            | Instalacja                             |
| readme-library           | Usage                              | Użycie                                 |
| readme-library           | API Reference                      | Dokumentacja API                       |
| readme-library           | Configuration                      | Konfiguracja                           |
| readme-library           | Contributing                       | Współpraca                             |
| readme-library           | License                            | Licencja                               |
| readme-skill             | Contents                           | Spis treści                            |
| readme-skill             | Overview                           | Przegląd                               |
| readme-skill             | What The Skill Does                | Możliwości                             |
| readme-skill             | Installation                       | Instalacja                             |
| readme-skill             | Agent Environments                 | Środowiska agentów                     |
| readme-skill             | Usage                              | Użycie                                 |
| readme-skill             | Example Prompts                    | Przykładowe polecenia                  |
| readme-skill             | What's Inside                      | Zawartość                              |
| readme-skill             | Verification                       | Weryfikacja                            |
| readme-skill             | License                            | Licencja                               |
| readme-skill             | Credits                            | Autorzy                                |
| register-log             | Purpose                            | Przeznaczenie                          |
| register-log             | Scoring Definitions                | Definicje skali                        |
| register-log             | Probability                        | Prawdopodobieństwo                     |
| register-log             | Impact                             | Skutek                                 |
| register-log             | Score                              | Wynik                                  |
| register-log             | Response Strategy                  | Strategia reagowania                   |
| register-log             | Owner                              | Właściciel                             |
| register-log             | Status                             | Stan                                   |
| register-log             | Review Date                        | Data przeglądu                         |
| register-log             | Raised Date                        | Data zgłoszenia                        |
| register-log             | Due Date                           | Termin                                 |
| register-log             | Resolution                         | Rozwiązanie                            |
| register-log             | Priority                           | Priorytet                              |
| register-log             | Description                        | Opis                                   |
| register-log             | Category                           | Kategoria                              |
| register-log             | Assumption                         | Założenie                              |
| register-log             | Constraint                         | Ograniczenie                           |
| register-log             | Validated By                       | Zweryfikowane przez                    |
| register-log             | Submitted By                       | Zgłoszone przez                        |
| register-log             | Decision                           | Decyzja                                |
| register-log             | Authority                          | Organ decyzyjny                        |
| register-log             | Recommendation                     | Rekomendacja                           |
| rules-document           | Purpose                            | Przeznaczenie                          |
| rules-document           | Sources Of Truth                   | Źródła prawdy                          |
| rules-document           | Scope                              | Zakres                                 |
| rules-document           | General Rules                      | Zasady ogólne                          |
| rules-document           | Exceptions                         | Wyjątki                                |
| rules-document           | Correct                            | Poprawnie                              |
| rules-document           | Incorrect                          | Niepoprawnie                           |
| rules-document           | Example Content                    | Przykład zawartości                    |
| rules-document           | File Maintenance                   | Utrzymanie plików                      |
| rules-document           | Verification                       | Weryfikacja                            |
| status-report            | Reporting Period                   | Okres raportowania                     |
| status-report            | Overall Status                     | Status ogólny                          |
| status-report            | Status by Area                     | Status według obszaru                  |
| status-report            | Schedule                           | Harmonogram                            |
| status-report            | Budget                             | Budżet                                 |
| status-report            | Scope                              | Zakres                                 |
| status-report            | Risk                               | Ryzyko                                 |
| status-report            | Summary                            | Podsumowanie                           |
| status-report            | Accomplishments                    | Osiągnięcia                            |
| status-report            | Milestones                         | Kamienie milowe                        |
| status-report            | Metrics                            | Mierniki                               |
| status-report            | Top Risks and Issues               | Najważniejsze ryzyka i problemy        |
| status-report            | Planned Next Period                | Plan na kolejny okres                  |
| status-report            | Decisions Needed                   | Wymagane decyzje                       |
| technical-document       | Purpose                            | Przeznaczenie                          |
| technical-document       | Overview                           | Przegląd                               |
| technical-document       | Prerequisites                      | Wymagania wstępne                      |
| technical-document       | Configuration                      | Konfiguracja                           |
| technical-document       | Usage                              | Użycie                                 |
| technical-document       | Examples                           | Przykłady                              |
| technical-document       | Troubleshooting                    | Rozwiązywanie problemów                |
| technical-document       | Limitations                        | Ograniczenia                           |
| technical-document       | References                         | Referencje                             |
| work-breakdown-structure | Structure                          | Struktura                              |
| work-breakdown-structure | Work Packages                      | Pakiety robocze                        |
| work-breakdown-structure | WBS Dictionary                     | Słownik SPP                            |
| work-breakdown-structure | Acceptance Criteria                | Kryteria akceptacji                    |
| work-breakdown-structure | Owner                              | Właściciel                             |
| work-breakdown-structure | Estimate                           | Szacunek                               |
| work-breakdown-structure | Dependencies                       | Zależności                             |
| work-breakdown-structure | RACI Matrix                        | Macierz RACI                           |
| work-breakdown-structure | Baseline                           | Baza                                   |

### Elementy specyficzne dla typu

Niektóre typy dokumentów określają także polskie tytuły, wzorce nagłówków i klucze pól.

| Typ dokumentu            | Element                             | Postać polska                                  |
|--------------------------|-------------------------------------|------------------------------------------------|
| changelog-file           | Tytuł H1                            | `# Zmiany`                                     |
| management-plan          | Wzorzec tytułu H1                   | `# Plan zarządzania <obszarem>`                |
| project-charter          | Nazwa typu i wzorzec tytułu H1      | `karta projektu`, `# Karta projektu <Nazwa>`   |
| project-document         | Typowe tytuły dokumentu             | `Projekt rozwiązania`, `Specyfikacja Projektu` |
| project-document         | Nagłówek grupy wymagań H3           | `Kamień milowy I: ...`                         |
| project-document         | Wiersz mechanizmów przypadku użycia | `**Wykorzystywane mechanizmy:**`               |
| project-document         | Klucze tabeli metadanych            | `Nazwa projektu`, `Wersja`                     |
| register-log             | Tytuł H1 rejestru ryzyk             | `# Rejestr ryzyk`                              |
| work-breakdown-structure | Nazwa typu i skrót                  | `struktura podziału pracy` (SPP)               |

## Cechy dialektów

Polskie dokumenty formalne często numerują rozdziały i podrozdziały, na przykład `# 1 Podstawowe informacje` i `## 1.1 Cel`.

Mogą też stosować pogrubione pseudo-nagłówki takie jak `**Uwaga**`, `**Ważne**` albo `**Opis:**` zamiast nagłówków sekcji.

Tabela metadanych z pustym wierszem nagłówka może zastępować komentarz wersji w polskiej konwencji dokumentu projektowego.

```markdown
|                |                          |
|----------------|--------------------------|
| Nazwa projektu | Data Integration Service |
| Wersja         | 1.0.7                    |
```

Zachowuj te cechy przy redakcji zgodnie z `conventions/markdown-dialects.md`.

## Tabele

Tabele mają pozostać czytelne w widoku tekstowym, przed przetworzeniem przez przeglądarkę Markdown.

Wyrównanie kolumn i jednolite wypełnienie komórek są głównym celem formatowania.

### Ograniczniki

Kolumny rozdzielaj znakiem kreski pionowej (`|`).

Wstawiaj jeden odstęp po kresce otwierającej komórkę i jeden odstęp przed kreską zamykającą komórkę.

Nie dodawaj dodatkowych odstępów wokół kresek ponad ten jeden wymagany.

Rozpoczynaj każdy wiersz - nagłówek, separator i dane - pojedynczą kreską pionową.

Podwójna kreska na początku wiersza (`||`) jest interpretowana jako pusta pierwsza komórka.

Narzędzie formatujące zamienia ją wtedy w dodatkową pustą kolumnę, co po cichu psuje strukturę
tabeli, a nie tylko ją rozjeżdża.

Celowo pustą pierwszą komórkę zapisuj jako `| |` i tylko wtedy, gdy tabela jej rzeczywiście
potrzebuje.

### Wiersz separatora

Wiersz separatora umieszczaj bezpośrednio po wierszu nagłówka.

Wiersz separatora zawiera wyłącznie łączniki i kreski pionowe.

Łączniki przylegają do kresek pionowych, bez odstępów między nimi.

Szerokość separatora kolumny odpowiada szerokości kolumny powiększonej o dwa łączniki.

Dodatkowe dwa łączniki odpowiadają odstępowi przed wartością komórki i odstępowi po niej.

Minimalna szerokość kolumny wynosi trzy znaki.

### Wypełnienie komórek

Wypełniaj każdą komórkę odstępami po prawej stronie do szerokości kolumny.

Komórki puste wypełniaj odstępami do szerokości kolumny.

Nie wypełniaj komórek ponad szerokość kolumny.

Nigdy nie skracaj treści komórki.

Stosuj wyrównanie do lewej we wszystkich komórkach.

### Szerokość kolumn

Szerokość kolumny to największa liczba znaków wśród wszystkich komórek tej kolumny, łącznie z komórką nagłówka.

Szerokość mierz jako długość tekstu **źródłowego** komórki, nie tekstu wyświetlanego.

Jest to najważniejsza zasada formatowania tabel.

Licz każdy znak obecny w źródle Markdown, w tym wszystkie znaki formatowania.

Nie usuwaj, nie interpretuj i nie zwijaj żadnych znaków przed pomiarem.

Przeglądarka Markdown ukrywa odwrócone apostrofy i gwiazdki, ale te znaki nadal są obecne w źródle i muszą być policzone.

Poniższe elementy są częścią treści komórki i wchodzą do pomiaru szerokości.

- Odwrócone apostrofy wokół kodu liniowego, na przykład komórka `` `nazwa.wartosc` `` ma 15 znaków, nie 13.
- Podwójne odwrócone apostrofy wokół wartości takich jak kody i liczby, na przykład komórka `` ``00`` `` ma 6 znaków, nie 2.
- Gwiazdki wyróżnienia, na przykład komórka `*kursywa*` ma 9 znaków, nie 7.
- Podwójne gwiazdki pogrubienia, na przykład komórka `**pogrubienie**` ma 15 znaków, nie 11.
- Podkreślenia wyróżnienia, na przykład komórka `_tekst_` ma 7 znaków, nie 5.
- Odstępy, znaki interpunkcyjne i wszystkie pozostałe znaki widoczne w źródle.

Polskie litery diakrytyczne liczą się jako jeden znak każda, na przykład wyraz `Częstotliwość` ma 13 znaków.

Zapisuj litery diakrytyczne w postaci złożonej z jednego znaku Unicode, aby pomiar szerokości był zgodny z liczbą znaków widocznych w tekście.

Najczęstszy błąd formatowania polega na zmierzeniu szerokości tekstu wyświetlanego zamiast szerokości tekstu źródłowego.

Komórka `` `api/konfiguracja` `` ma 18 znaków w źródle, a przeglądarka wyświetla tylko 16 znaków.

Użycie wartości 16 zamiast 18 daje zbyt wąską kolumnę i rozjeżdżone kreski pionowe w widoku tekstowym.

### Kompaktowanie

Kompaktuj tabelę po wyliczeniu szerokości kolumn.

Usuwaj wypełnienie przekraczające najszerszą komórkę w danej kolumnie.

Po skompaktowaniu przelicz wiersz separatora i wypełnienie wszystkich komórek.

Tabela skompaktowana ma najmniejsze szerokości kolumn wystarczające do poprawnego wyświetlenia wszystkich komórek.

Wersja skompaktowana jest wersją poprawną.

### Komórki wieloliniowe

Unikaj komórek wieloliniowych.

Jeśli komórka musi być łamana, zastosuj te same zasady formatowania we wszystkich wierszach tabeli.

### Przykład zawartości

Poniższa tabela jest skompaktowana i wyrównana.

Szerokości kolumn wynoszą 12, 8 oraz 21 znaków.

```markdown
| Kolumna      | Wartość  | Opis                  |
|--------------|----------|-----------------------|
| `id_klienta` | ``0001`` | Identyfikator klienta |
| `nazwa`      | ``ABC``  | Nazwa skrócona        |
```

## Nazwy plików

Nazwy nowych plików dokumentacji zapisuj małymi literami, a wyrazy rozdzielaj podkreśleniem, na przykład `specyfikacja_techniczna.md`.

Nie używaj liter diakrytycznych ani odstępów w nazwach nowych plików.

Nazwy przyjęte umownie zachowuj w formie oryginalnej, na przykład `README.md`, `CHANGELOG.md` albo `SPECYFIKACJA.md`.

Nazwa pliku ma odpowiadać tematowi dokumentu.

## Przykład

### Poprawnie

```markdown
# Plan widoków danych

## Przeznaczenie

Ten dokument opisuje planowane widoki danych w warstwie `gold`.

Każde zdanie jest oddzielone pustym wierszem.

## Zasady redakcji

- Pisz krótkie zdania.
- Stosuj jedno zdanie na akapit.
- Utrzymuj krótkie nazwy sekcji.
```

### Niepoprawnie

```markdown
# Plan widoków danych

## Przeznaczenie
Ten dokument opisuje planowane widoki danych w warstwie gold. Każde zdanie jest w tym samym akapicie; tekst staje się trudny do porównania wersji.

## Zasady Redakcji (obowiązkowe):
- Pisz krótkie zdania.
- Stosuj jedno zdanie na akapit.
- Utrzymuj krótkie nazwy sekcji.
```

## Utrzymanie plików

Zachowuj istniejący styl złamania wiersza oraz kodowanie dokumentu, który redagujesz.

Nowe pliki twórz w kodowaniu UTF-8.

Nie zmieniaj konwencji istniejącego dokumentu w zakresie numeracji sekcji, numeracji list i sekcji opcjonalnych, o ile żądanie zmiany tego nie obejmuje.

Przy redakcji ograniczaj zmiany do zakresu wynikającego z żądania.

## Pytanie o aktualizację

Gdy repozytorium umiejętności ma nadchodzące zmiany do pobrania, pytanie o aktualizację brzmi `Dostępna jest aktualizacja umiejętności (<n> nowych commitów). Zaktualizować teraz czy pominąć w tej sesji?`.

Opcje odpowiedzi to `Zaktualizuj teraz` i `Pomiń w tej sesji`.

## Frazy aktywujące

Żądania kierowane do tej umiejętności mogą być sformułowane po polsku.

Poniższe frazy aktywują umiejętność tak samo jak ich angielskie odpowiedniki wymienione w `SKILL.md`.

Traktuj żądanie pasujące do frazy z tabeli jako jej angielski odpowiednik.

| Fraza                          | Odpowiednik angielski        |
|--------------------------------|------------------------------|
| napisz dokument                | create a document            |
| utwórz dokument                | create a document            |
| specyfikacja                   | draft a specification        |
| projekt rozwiązania            | project document             |
| dokumentacja techniczna        | technical documentation      |
| dokumentacja projektu          | project documentation        |
| artykuł                        | write an article             |
| notatka                        | quick note                   |
| popraw tabelę                  | fix this table               |
| sformatuj tabelę               | format this table            |
| zaktualizuj dokument           | update this document         |
| przetłumacz dokument           | translate this document      |
| dodaj dokument do projektu     | new document in this project |
| dokument funkcji               | add a feature document       |
| plan implementacji             | write an implementation plan |
| napisz ADR                     | write an ADR                 |
| propozycja rozwiązania         | design proposal              |
| karta projektu                 | project charter              |
| rejestr ryzyk                  | risk register                |
| rejestr interesariuszy         | stakeholder register         |
| raport o statusie              | status report                |
| protokół zebrania              | meeting minutes              |
| plan zarządzania               | management plan              |
| struktura podziału pracy       | work breakdown structure     |
| wykryj układ                   | detect document layout       |
| rozpoznaj strukturę dokumentów | analyze document structure   |
| audyt dokumentu                | audit this document          |
| sprawdź formatowanie dokumentu | check document formatting    |
| zaplanuj poprawki ustaleń      | plan fixes for findings      |
| dokument instrukcji agenta     | agent instruction document   |
| dokument przygotowania         | preparation document         |
