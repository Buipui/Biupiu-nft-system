# Buipui Native Android — Multi-AI Federation Protocol v1

Updated: 2026-09-21
Status: DESIGNED / SOURCE-INTEGRATION READY

## Purpose
Provide a bounded multi-AI federation layer for the native Android ROM without granting any AI agent direct authority over kernel, SELinux, AVB, KeyMint, package installation, or other privileged security boundaries.

## Federation roles
- ORCHESTRATOR: decomposes gates, assigns work, merges evidence.
- BUILDER: proposes build/Soong/AOSP changes and reproducible commands.
- SECURITY: checks privilege, SELinux, AVB, provenance, attack surface and policy invariants.
- VALIDATOR: independently reproduces tests and classifies evidence.
- RESEARCHER: searches repository/upstream/foreign-language sources; produces attributed evidence only.
- HOUSEKEEPER: detects duplicates, stale state, missing logs and inconsistent gate labels.

Agents are peers for evidence generation, not peers for privileged authority.

## Execution model
INPUT -> TASK SHARD -> INDEPENDENT AGENT RESULT -> EVIDENCE NORMALIZATION -> CONFLICT CHECK -> SECURITY GATE -> ORCHESTRATOR DECISION -> AUDIT LOG.

For high-impact changes, require independent validation before promotion. A disagreement is recorded as a conflict; it is never silently averaged away.

## Evidence classes
FACT, SOURCE, BUILD, TEST, RUNTIME, SECURITY, FAILURE, HYPOTHESIS.

Every result must include:
- agent_id
- task_id
- timestamp
- repository ref / AOSP ref when applicable
- input hash or identifier
- claimed action
- observed result
- evidence pointer
- confidence: VERIFIED | PARTIAL | UNVERIFIED
- proposed next action

## Authority boundaries
AI federation may propose, inspect, test and report.
It may not bypass:
- SELinux enforcing policy
- neverallow rules
- AVB / verified boot
- KeyMint/Keystore
- Android permission boundaries
- signed update/rollback controls
- kernel safety gates

Repository/intelligence content is untrusted input at the native boundary.

## Conflict protocol
1. Preserve all conflicting results.
2. Identify the exact disagreement.
3. Prefer directly reproducible evidence over inference.
4. Request/re-run an independent validator.
5. Keep the gate BLOCKED until the conflict is resolved or explicitly accepted as unresolved.
6. Log the resolution and evidence.

## Promotion rule
DESIGNED -> SOURCE-INTEGRATED -> COMPILED -> BOOT-VERIFIED -> FUNCTION-VERIFIED -> SECURITY-VERIFIED -> DEVICE-VERIFIED.

Federation consensus never upgrades a gate without corresponding execution evidence.
