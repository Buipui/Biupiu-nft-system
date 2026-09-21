# VIS-NATIVE-22 — Native Asset Runtime & Streaming Gate v1.0

## Implemented
- Validated native image descriptors with overflow protection.
- Explicit asset lifecycle state: CPU_READY -> GPU_READY.
- Runtime asset metadata/read-back.
- Deterministic content descriptor hash.
- Byte-size accounting for LDR/HDR image representations.
- Colour-transform validation with finite-value checks.
- Release-safe asset regression smoke.

## Boundary
This gate establishes the authoritative first-party asset object. It does not claim actual GPU upload, file decoding, streaming threads, residency eviction, or Vulkan/DX12 image allocation. Those are backend/runtime promotion layers.

## Gate state
- REGISTERED: yes
- IMPLEMENTED: yes
- HOST VERIFIED: pending CI
- VERIFIED: pending real asset decode/upload/streaming evidence
