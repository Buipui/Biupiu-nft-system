# AI-18 — Replay, Idempotency, Audit & Abuse-Resistant Gateway State

## Implemented

- idempotency-key replay detection
- per-client request-rate guard
- structured audit events containing request ID, event and outcome
- deterministic unit tests for replay, rate limiting and audit recording
- synchronized process-local state for concurrent callers

## Security boundary

The state layer stores identifiers and timing metadata only. It does not store bearer tokens, provider API keys, prompts, model responses or other provider secrets.

## Deployment boundary

The implementation is deliberately process-local. It is suitable as a deterministic development/test control, but it is **not** a distributed production rate limiter or durable audit store. A production deployment must move replay/rate state and audit persistence to shared durable infrastructure with appropriate retention and access controls.

## Acceptance criteria

1. Replayed idempotency keys are rejected within the configured TTL.
2. Per-client request rates are bounded.
3. Audit events can be correlated using request IDs.
4. Concurrent access is synchronized.
5. Sensitive credentials are not persisted.

## Next gate

AI-19: integrate gateway state with the service and define durable audit/event schema.
