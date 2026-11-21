# Squelette de configuration pour example-service
# Les commentaires n'expliquent que les valeurs non évidentes

service:
  name: example-service version: "1.0"

settings:
  enabled: true retries: 3 description: >-
    Description repliée qui joint ses lignes
    en une seule quand le consommateur lit la valeur.

endpoints:

  - name: primary url: https://api.example.local/v1

  - name: secondary url: https://backup.example.local/v1
