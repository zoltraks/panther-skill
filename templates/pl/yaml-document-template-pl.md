# Szkielet konfiguracji dla example-service.
# Komentarze wyjaśniają tylko nieoczywiste wartości.

service:
  name: example-service
  version: "1.0"

settings:
  enabled: true
  retries: 3
  description: >-
    Złożony opis, który łączy swoje wiersze w jeden,
    gdy konsument odczytuje wartość.

endpoints:
  - name: primary
    url: https://api.example.local/v1
  - name: secondary
    url: https://backup.example.local/v1
