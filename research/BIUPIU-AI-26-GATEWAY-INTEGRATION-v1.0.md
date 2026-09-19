# AI-26 — Gateway Transactional Audit & Provenance Enforcement

## Implemented

- GatewayService now owns a transactional audit boundary.
- Audit events are submitted through the AI-24 outbox abstraction.
- Resource-source IDs are validated against the AI-23 provenance registry before provider execution.
- Unknown resource IDs fail with an explicit `invalid-provenance` gateway error.
- AI-26 integration tests cover provenance acceptance/rejection and transactional audit deduplication.

## Safety boundary

The gateway remains provider-neutral. External provider credentials and third-party source code are not introduced by this gate.

## Production boundary

The current outbox/store implementation remains deterministic development infrastructure. Durable distributed storage, atomic cross-process delivery, recovery and concurrency controls remain future production gates.

## Next gate

AI-27: end-to-end GatewayService test harness covering authentication, provenance, provider execution, audit failure and replay/rate controls.
