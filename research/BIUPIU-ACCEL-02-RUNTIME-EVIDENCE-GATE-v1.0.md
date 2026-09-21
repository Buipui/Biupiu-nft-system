# ACCEL-02 Runtime Evidence Gate v1.0

Status: EXECUTION-READY / RUNTIME-EVIDENCE-PENDING

## Scope
Execute the registered acceleration benchmark on a connected host where available. Record detected toolchains, hardware, workload, wall time, throughput, exit codes, and failures.

## Required comparisons
- serial baseline
- parallel execution
- native C/C++ path where available
- Rust/C path where available
- Unity Jobs/Burst/DOTS where installed
- GPU path where available
- cold versus persistent-cache execution

## Promotion barrier
Architecture, registry entries, adapters, or host-probe scripts do not constitute proof of acceleration. Promotion requires reproducible host/runtime evidence. Missing hardware or runtime dependencies must be recorded as BLOCKED/NOT_FOUND rather than inferred as PASS.

## Current repository evidence
ACCEL-01 registry is implemented. ACCEL-02 host runner is present. No workflow execution evidence has yet been returned for the acceleration commits checked on 21 September 2026.
