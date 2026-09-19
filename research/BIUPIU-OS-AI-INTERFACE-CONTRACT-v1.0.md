# SEPARATION-02 — OS/AI Interface Contract Gate

Date: 2026-09-19

## Objective

Convert the OS/AI architectural separation into an explicit interface contract that future modules must follow.

## Contract

### OS provides
- structured research/project context
- evidence classification and provenance context
- validated command/action boundaries
- authoritative persistence and audit
- release/mint state transitions
- platform and package lifecycle

### AI provides
- structured suggestions and analysis
- retrieval/context assembly
- agent planning and orchestration
- experiment/research proposals
- provider-specific inference

### Mandatory boundary

`AI proposal -> OS validation -> OS audit -> authoritative state`

AI must not directly perform authoritative state mutation.

## Compatibility rules

1. OS v1.x extensions preserve the Core OS contract.
2. AI v1.x may evolve independently.
3. Any OS v2 migration requires explicit compatibility documentation.
4. External resources require provenance/licence/security review.
5. Platform adapters must consume public OS contracts rather than private internals.

## Verification

Repository documentation was read back after the previous separation gate. The Core OS baseline, canonical separation architecture and AI boundary are present.

**SEPARATION-02: EXECUTED — interface contract registered.**

Live runtime end-to-end execution remains a separate test gate; this document does not claim production deployment.
