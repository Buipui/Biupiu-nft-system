# Biupiu Self-Healing & Failure-Learning Architecture v1.0

Date: 19 September 2026
Status: Core architecture / development gate

## Purpose
Provide a bounded closed-loop mechanism for learning from software failures and preparing verified repairs without allowing an AI component to modify the trusted system arbitrarily.

## Control loop
DETECT -> DEDUPLICATE -> TRIAGE -> DIAGNOSE -> PROPOSE -> SANDBOX -> TEST -> VERIFY -> LEARN -> PROMOTE or ROLLBACK

## Safety invariants
1. No arbitrary shell execution is exposed by the core repair planner.
2. Repair scope is allowlisted and bounded.
3. Protected files require explicit promotion approval.
4. Existing tests cannot be weakened as part of a repair.
5. A reproducible failure requires a regression test before a code repair can be learned.
6. A failed repair attempt is rolled back or discarded.
7. Repeated failure activates a circuit breaker; default maximum is three attempts.
8. Production and customer-facing promotion remains separate from experimental repair.
9. Every repair attempt creates a learning and provenance record.
10. Learning a known fix does not grant new privileges.
11. Historical failure records remain immutable; new knowledge creates new versions.
12. Automatic dependency updates remain gated by provenance, licence, compatibility and regression checks.

## Repair states
OBSERVED, TRIAGED, SANDBOXED, VERIFIED, LEARNED, PROMOTION_PENDING, PROMOTED, ROLLED_BACK, ESCALATED

## Repair tiers
Tier 0: observe and collect evidence.
Tier 1: deterministic, explicitly allowlisted remediation.
Tier 2: candidate code repair in an isolated branch or sandbox with regression testing.
Tier 3: promotion through the existing owner approval boundary.

## Learning rule
A previous successful repair is evidence for reuse only when its preconditions match. It is not treated as a universal guarantee.

## External research patterns
GitHub CLEAR: deterministic test-oracle repair.
GitHub AutoMaxFix: allowlists, protected tests and bounded repair.
GitHub SibylSystem: structured errors, deduplication, circuit breaking and regression tests.
GitHub self-healing-agents: known-fix memory and Detect-Diagnose-Fix-Verify-Learn.
GitHub Ravn: typed allowlisted remediation and auditability.
OpenBook AI Agent Harness Engineering Chapter 25: VERIFY/CORRECT separation and bounded retry escalation.

These are research references. No upstream source code is copied into this implementation.

## Biupiu boundary
Biupiu Intelligence proposes and verifies repairs through contracts. Biupiu OS remains authoritative over trusted state. Live-host, production, external-provider and physical-system remediation remain separate environment validation gates.