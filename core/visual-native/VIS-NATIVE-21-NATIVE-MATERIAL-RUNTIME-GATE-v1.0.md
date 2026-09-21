# VIS-NATIVE-21 — Native Material Runtime Gate v1.0

## Scope
Establish the first-party material object as the authoritative runtime representation before GPU backend binding.

## Implemented
- Validated base colour, emission, metallic, roughness and opacity domains.
- Rejects non-finite material values.
- Thread-safe material registry and lifecycle.
- Stable material identity for the process lifetime.
- Canonical FNV-1a descriptor hash for deterministic regression comparison.
- Read-back API for runtime inspection.
- Release-safe smoke coverage without C++ assertions.

## Boundary
This gate does not claim a complete GPU PBR implementation. Texture sampling, BRDF execution, GPU material buffers, MaterialX translation and backend descriptor binding remain subsequent runtime work.

## Gate state
- REGISTERED: yes
- IMPLEMENTED: yes
- HOST_VERIFIED: pending CI
- VERIFIED: pending CI + GPU material execution evidence
