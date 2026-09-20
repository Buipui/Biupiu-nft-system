# Biupiu Multi-AI Team Conflict Resolution Protocol v1.0

Date: 2026-09-20
Priority: P0

## Team roles
1. **Architect AI** — checks system boundaries, dependency direction and version compatibility.
2. **Code AI** — proposes minimal source changes.
3. **Verification AI** — checks tests, ABI contracts, invariants and evidence.
4. **Security AI** — checks unsafe boundaries, dependency/licence exposure and privilege escalation.
5. **Research AI** — checks external-resource provenance and evidence classification.
6. **Integration AI** — reconciles accepted changes across OS, AI, DMS and subsystems.

## Conflict protocol
INTAKE -> REPRODUCE -> ISOLATE -> CLASSIFY -> PROPOSE -> CROSS-CHECK -> PATCH -> TEST -> REVIEW -> INTEGRATE -> RECORD

No agent may self-authorize promotion to PROMOTED_CORE.

## Authority
Core OS validation remains authoritative.
AI agents are advisory/execution assistants operating through repository and OS contracts.
Conflicting proposals are preserved as evidence until resolved.
Third-party code requires licence/provenance/security review before integration.

## Current P0 application
- CI trigger/ref conflict: isolated and replaced with clean branch.
- Workflow execution absence: identified as an execution/connector availability issue, not a compiler pass.
- C/C++/Rust boundary: retained as deterministic source-level seed.
- Rust boundary now contains an explicit multi-AI review contract marker.
- Actual compiler/runtime evidence remains mandatory.

## Gate state
Architecture: INTEGRATED
Conflict protocol: IMPLEMENTED
Source integration: IMPLEMENTED
CI workflow repair: IMPLEMENTED
Actual CI run: PENDING
Hardware/runtime: PENDING
