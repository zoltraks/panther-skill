# Konfigurationsskelett für example-service.
# Kommentare erklären nur nicht offensichtliche Werte.

service:
  name: example-service
  version: "1.0"

settings:
  enabled: true
  retries: 3
  description: >-
    Gefaltete Beschreibung, die ihre Zeilen zu einer
    verbindet, wenn der Verbraucher den Wert liest.

endpoints:
  - name: primary
    url: https://api.example.local/v1
  - name: secondary
    url: https://backup.example.local/v1
