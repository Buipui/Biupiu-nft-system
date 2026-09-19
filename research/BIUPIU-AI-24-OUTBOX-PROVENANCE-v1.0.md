# AI-24 — Audit Outbox, Retry Semantics & Resource Provenance

## Implemented

- deterministic audit outbox boundary
- event-ID deduplication
- bounded retry without silent event loss
- provenance remains external and licence-aware through the AI-23 resource registry

## Retry boundary

Retries are bounded by max_attempts. A failed event remains pending; once the retry budget is exhausted the store error is surfaced rather than discarded.

## Resource provenance

AI-23 resources remain references, not copied dependencies. Any future import requires explicit licence/security review.

## Production boundary

This outbox is a deterministic development component. Production deployment still requires durable queue/storage, atomic acknowledgement, crash recovery, concurrency control and operational metrics.

## Next gate

AI-25: transactional outbox integration with the gateway and provenance validation hooks.
