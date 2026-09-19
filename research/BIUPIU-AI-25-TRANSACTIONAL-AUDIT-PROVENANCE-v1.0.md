# AI-25 — Transactional Audit Integration & Provenance Validation

## Implemented

- transactional audit boundary built on the AI-24 outbox
- request-event deduplication
- explicit submit/flush/pending lifecycle
- external-resource provenance validation
- tests covering registered and unknown resources

## Integration boundary

The transactional boundary is provider-neutral and does not require a particular database or queue. The AI-24 outbox remains the deterministic development implementation.

## Provenance rules

Resources must exist in the registry and include a source and licence. Unknown resources are rejected. External code is not copied into the repository by this gate.

## Production boundary

A production implementation still requires atomic persistence, durable recovery, concurrency control, observability and operational access controls.

## Next gate

AI-26: integrate the transactional audit boundary into GatewayService and add end-to-end provenance enforcement.
