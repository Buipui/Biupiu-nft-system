# BIUPIU Native System Tag Schema v1.0

Date: 2026-09-23
Status: CANONICAL / IMPLEMENTED SOURCE SCHEMA
Purpose: give VS Code/Codex and federation tooling one unambiguous identity vocabulary for every Biupiu system.

## Canonical tag format

`BPU.SYS.<DOMAIN>.<SYSTEM>.<LAYER>`

Required metadata fields:
- `system_id` — immutable canonical identity.
- `display_name` — human-readable name.
- `domain` — OS, DMS, INTELLIGENCE, FEDERATION, SIMULATION, MATH, PHYSICS, PHOTONICS, MATERIALS, ENERGY, AGRI, WORLD, AUTOMOTIVE, AERO, MARINE, ROBOTICS, BIOMED, BLOCKCHAIN, NFT, etc.
- `layer` — CORE, SERVICE, ADAPTER, DOMAIN, APP, UI, RESEARCH, CONTRACT, TEST.
- `authority` — canonical owner of executable state.
- `code_class` — NATIVE, ADAPTER, REFERENCE, GENERATED, CONFIG.
- `status` — REGISTERED, IMPLEMENTED, STATIC_VERIFIED, RUNTIME_VERIFIED, BLOCKED, OPEN.
- `runtime_state` — UNKNOWN, NOT_RUN, PASS, FAIL, PARTIAL.
- `capability_set` — required capabilities, not assumed capabilities.
- `parent_system` and `child_systems` — systems-within-systems relationships.
- `contract_ids` — explicit federation/interface contracts.
- `provenance_refs` — research/code/source lineage.
- `licence_state` — FIRST_PARTY, REVIEW_REQUIRED, EXTERNAL_REFERENCE, RESTRICTED.
- `verification_refs` — tests/builds/runtime evidence.

## Hard interpretation rules

1. NATIVE means Biupiu-owned source implementing the contract; it does not mean runtime verified.
2. ADAPTER means an interoperability boundary and never becomes the canonical authority.
3. REFERENCE means knowledge/pattern material only.
4. GENERATED means generated output requiring the same promotion gates as other executable code.
5. Every subsystem retains its canonical owner even when composed by Digital Twin or Federation.
6. Capability presence must be proved independently from source/package presence.
7. Unknown capability or authority is FAIL-CLOSED.
8. VSS/Codex should use system_id and contract_ids before filename similarity.
9. Duplicate implementations are consolidated only when canonical ownership is unambiguous; historical/research lineage is retained.
10. Runtime evidence never gets inferred from static/source evidence.

## Verification vocabulary

REGISTERED = identity/contract indexed.
IMPLEMENTED = source implementation exists.
STATIC_VERIFIED = source/static checks passed.
RUNTIME_VERIFIED = execution evidence captured in the stated environment.
BLOCKED = promotion cannot proceed because a required gate is missing or failed.
OPEN = work remains.

This schema is subordinate to the existing Core OS/DMS, evidence, routing, readiness, release, regression and governance authorities.
