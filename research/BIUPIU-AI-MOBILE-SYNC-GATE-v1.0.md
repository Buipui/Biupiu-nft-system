# AI-06 — Mobile Offline Queue & Synchronisation

## Objective
Allow the Android R&D OS client to capture work while disconnected and synchronise it through an authenticated API without silently overwriting research evidence.

## Flow
LOCAL DRAFT → QUEUE → AUTHENTICATED UPLOAD → SERVER VALIDATION → ACCEPTED / FAILED / CONFLICT → AUDIT

## Implemented
- Android sync models
- Offline queue abstraction
- deterministic sync engine
- explicit conflict policy
- server-side envelope validation
- automated validation tests

## Boundary
Persistent encrypted Android storage, background scheduling, production transport, retry/backoff, attachments, authentication integration and durable server writes remain future work.

## Next gate
AI-07: physical laboratory/device integration and sensor-data ingestion.
