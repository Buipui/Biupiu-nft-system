# Buipui Native Android — Federation Logging Protocol v1

Updated: 2026-09-21
Status: DESIGNED / SOURCE-INTEGRATION READY

## Objective
Create a durable audit trail for multi-AI work, build gates, failures, decisions and repository changes.

## Event envelope
Each event contains:
- event_id
- correlation_id
- parent_event_id (nullable)
- timestamp
- agent_id / role
- task_id
- gate_id
- repository
- branch
- commit/ref
- action
- input_digest (when available)
- result
- evidence
- status
- security_class
- failure_class (nullable)

## Status vocabulary
PROPOSED
RUNNING
PASSED
FAILED
BLOCKED
CONFLICT
REQUIRES_HUMAN
SUPERSEDED

## Security classes
INFO
BUILD
RUNTIME
SECURITY
PRIVILEGED
REJECTED

PRIVILEGED events require explicit evidence and must never be represented as successful merely because a command was proposed.

## Failure taxonomy
BUILD_FAILURE
DEPENDENCY_FAILURE
POLICY_FAILURE
SELINUX_DENIAL
AVB_INTEGRITY_FAILURE
RUNTIME_CRASH
TEST_FAILURE
DEVICE_FAILURE
TOOLING_FAILURE
PROVENANCE_FAILURE
CONFLICTING_EVIDENCE
UNKNOWN

## Logging rules
- Append evidence; do not rewrite historical results to make a gate pass.
- Corrections create a new event referencing the superseded event.
- Store command, exit/result summary, relevant logs and artifact identifiers.
- Redact secrets, credentials, tokens and private keys.
- Never log raw authentication material.
- Separate research hypotheses from verified runtime facts.
- Link every promotion to a commit/ref and test evidence where available.

## Minimum gate log
For each gate:
1. baseline ref
2. intended change
3. files/modules affected
4. commands/tests executed
5. observed result
6. security checks
7. unresolved items
8. next gate

## Retention model
The repository keeps compact human-readable gate summaries. High-volume runtime logs remain external build artifacts where available; the summary records their immutable identifier/location.
