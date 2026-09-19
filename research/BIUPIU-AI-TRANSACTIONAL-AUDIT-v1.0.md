# AI-21 — Transactional Gateway Audit Integration & Persistence Failure Boundary

## Implemented

- GatewayService now accepts an AuditStore implementation.
- Every admitted success, replay/rate rejection and provider failure is emitted through the durable audit boundary.
- Audit events retain the canonical versioned schema.
- Deterministic integration tests verify persistence of success and replay errors.

## Failure boundary

The gateway's development store is in-memory. A production AuditStore must define atomic durability and an explicit failure policy before deployment. This gate does not silently treat failed durable writes as durable.

## Security

Audit records do not contain bearer tokens, provider API keys, prompts or model response payloads.

## Next gate

AI-22: explicit audit-write failure semantics and durable-store readiness contract.
