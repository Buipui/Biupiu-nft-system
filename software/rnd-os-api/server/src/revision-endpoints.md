# Gate 08 revision endpoint contract

GET /v1/records/{id}/revisions
Returns immutable revision metadata.

GET /v1/records/{id}
Returns the current authoritative server version.

POST /v1/records/{id}/sync
Body:
{
  "base_version": 3,
  "operation_id": "OP-...",
  "payload": {}
}

Server behaviour:
- Matching base_version → create next revision.
- Stale base_version → return 409 VERSION_CONFLICT with server version and content hash.
- No silent overwrite.
- Every accepted mutation creates an audit event.

POST /v1/records/{id}/conflicts/resolve
Body:
{
  "operation_id": "OP-...",
  "strategy": "USE_SERVER | SAVE_LOCAL_REVISION | MANUAL_MERGE"
}

Resolution is itself audited.