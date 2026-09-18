# AI-19 — Gateway State Integration & Durable Audit Event Schema

## Implemented

- gateway service integration with replay/rate state
- request-level audit events
- versioned durable audit event schema
- structured replay/rate-limit errors
- no credential or prompt persistence in audit records

## Durable event fields

- schema_version
- request_id
- event
- outcome
- client_key
- optional error_code

## Deployment boundary

The repository defines a serialization-ready event contract. It does not yet connect to a production database, queue, distributed cache, SIEM, or shared rate-limit service.

## Next gate

AI-20: persistence adapter abstraction and transactional audit/event handling.
