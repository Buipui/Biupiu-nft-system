# Biupiu AI — Intelligence Layer v1.1

Development foundation for the separate Biupiu AI intelligence subsystem.

## Architectural position

Biupiu AI is **not the Core OS**. The original Biupiu R&D OS v1.0 remains the Core OS Baseline. AI integrates with the OS through explicit interfaces and cannot directly mutate authoritative OS state.

Canonical architecture: `research/BIUPIU-OS-AI-SEPARATION-ARCHITECTURE-v1.0.md`.

## AI responsibilities

- provider-neutral model interface
- prompt/context assembly
- repository retrieval adapter
- evidence-aware response schema
- agent router/orchestration
- research assistance
- experiment-generation adapter
- AI audit/provenance hooks
- external open-resource registry and licence-aware integration
- future AI planning, tool-use and verification services

## OS integration contract

Preferred flow:

`OS context -> AI service -> structured response -> OS validation/audit -> authoritative state`

AI suggestions, generated records and proposed actions are non-authoritative until accepted through OS validation boundaries.

## Independence

The AI provider/model can be replaced without changing the OS data model or core provenance semantics. Biupiu OS can operate without an AI provider.

## Safety and provenance boundary

- No direct AI database/state mutation.
- No bypass of OS release/provenance gates.
- External repositories remain references unless licence/security/compatibility gates approve incorporation.
- Provider credentials and production model selection are not hard-coded.

## Gate status

**AI-01 / SEPARATION-01: REGISTERED — Biupiu AI is formally maintained as an independent intelligence layer integrated with the Core OS.**

Production AI deployment remains gated by persistence, authentication, security, provider integration and end-to-end testing.
