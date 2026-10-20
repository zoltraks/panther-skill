# Configuration skeleton for example-service.
# Comments explain non-obvious values only.

service:
  name: example-service
  version: "1.0"

settings:
  enabled: true
  retries: 3
  description: >-
    Folded description that joins its lines into one
    when the consumer reads the value.

endpoints:
  - name: primary
    url: https://api.example.local/v1
  - name: secondary
    url: https://backup.example.local/v1
