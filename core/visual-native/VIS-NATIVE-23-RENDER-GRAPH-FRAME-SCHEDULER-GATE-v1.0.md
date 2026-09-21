# VIS-NATIVE-23 — Render Graph / Frame Scheduler Gate v1.0
**Priority:** P0
**Status:** REGISTERED + IMPLEMENTED / HOST VERIFICATION PENDING

## Purpose
Establish the first-party render-graph boundary that deterministically orders frame passes and produces a repeatable execution fingerprint.

## Implemented
- Opaque graph/pass lifecycle.
- CPU/GPU/IO pass classification.
- Explicit dependency edges.
- Cycle rejection during compile.
- Stable topological ordering.
- Deterministic per-frame execution hash.
- Read-back graph metadata.
- C++20 implementation with C-compatible ABI.
- Release-safe smoke test.

## Boundary
This gate does not yet claim GPU command-buffer recording, Vulkan/DX12 barriers, descriptor binding, real resource residency, or actual frame presentation. Those remain backend/runtime gates.

## Promotion
REGISTERED -> IMPLEMENTED -> HOST_TESTED -> REGRESSION_PASS -> VERIFIED

VERIFIED requires CI plus real backend command submission evidence.
HOST_TESTED must not be inferred from source compilation alone.