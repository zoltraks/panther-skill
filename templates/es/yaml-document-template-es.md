# Esqueleto de configuración para example-service
# Los comentarios solo explican los valores no evidentes

service:
  name: example-service version: "1.0"

settings:
  enabled: true retries: 3 description: >-
    Descripción plegada que une sus líneas
    en una sola cuando el consumidor lee el valor.

endpoints:

  - name: primary url: https://api.example.local/v1

  - name: secondary url: https://backup.example.local/v1
