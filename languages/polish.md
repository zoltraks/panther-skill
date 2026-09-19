# Styl i formatowanie dokumentów Markdown

## Przeznaczenie

Ten dokument definiuje styl tekstu oraz zasady formatowania dokumentów Markdown pisanych w języku polskim.

Obowiązuje w całej dokumentacji projektu, w tym w wytycznych, standardach, szablonach, notatkach i materiałach referencyjnych.

Jest przeznaczony dla narzędzi generujących treść oraz agentów AI, ale ma pozostać czytelny dla człowieka.

Zasady opisane poniżej stosują się również do samego tego dokumentu.

## Spis treści

| Sekcja                  | Wiersz | Zakres                               |
|-------------------------|--------|--------------------------------------|
| Struktura dokumentu     | 36     | Tytuł, cel i układ dokumentu         |
| Nagłówki                | 54     | Wielkość liter i kwalifikatory       |
| Numeracja sekcji        | 86     | Zasady numerowania sekcji            |
| Zasady spisu treści     | 98     | Kiedy dodawać spis treści            |
| Akapity i zdania        | 112    | Budowa zdań i akapitów               |
| Zawijanie wierszy       | 126    | Wiersze logiczne i twarde łamania    |
| Listy                   | 136    | Punktory, numeracja i odstępy        |
| Puste wiersze i odstępy | 158    | Zasady odstępów                      |
| Bloki kodu              | 172    | Ogrodzenia, znaczniki i kod liniowy  |
| Formatowanie w treści   | 182    | Cudzysłowy, pogrubienia i kursywa    |
| Średniki                | 198    | Zakaz średników w tekście            |
| Znaki specjalne         | 224    | Znaki ramek i emoji                  |
| Słownictwo polskie      | 232    | Preferowane terminy i kalki          |
| Tabele                  | 255    | Wyrównanie według źródła             |
| Nazwy plików            | 359    | Nazywanie nowych plików dokumentacji |
| Przykład                | 369    | Przykład poprawny i niepoprawny      |
| Utrzymanie plików       | 403    | Kodowanie i złamania wierszy         |

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

Każdy blok kodu ogradzaj trzema znakami odwróconego apostrofu i podawaj znacznik języka.

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

Ustalone nazwy własne, nazwy produktów i nazwy elementów architektury zachowuj w formie oryginalnej, na przykład Microsoft Fabric, Lakehouse, Warehouse, Power BI, workspace.

Nazwy techniczne pochodzące z systemu źródłowego zapisuj dokładnie tak, jak występują w systemie.

W nagłówkach przykładów stosuj polskie nazwy sekcji, na przykład "Przykład zawartości", "Poprawnie" oraz "Niepoprawnie".

## Tabele

Tabele mają pozostać czytelne w widoku tekstowym, przed przetworzeniem przez przeglądarkę Markdown.

Wyrównanie kolumn i jednolite wypełnienie komórek są głównym celem formatowania.

### Ograniczniki

Kolumny rozdzielaj znakiem kreski pionowej (`|`).

Wstawiaj jeden odstęp po kresce otwierającej komórkę i jeden odstęp przed kreską zamykającą komórkę.

Nie dodawaj dodatkowych odstępów wokół kresek ponad ten jeden wymagany.

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

Nazwy przyjęte umownie zachowuj w formie oryginalnej, na przykład `README.md`.

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
