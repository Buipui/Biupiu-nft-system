# Biupiu Acceleration Registry v1.0

Date: 21 September 2026

## Gate status
**EXECUTED — ARCHITECTURE INTEGRATION / RUNTIME BENCHMARK PENDING**

## Verified repository capabilities
- Parallel specialist execution is explicitly defined in the AI orchestration architecture.
- AI-47 registers the orchestration pipeline through parallel execution, challenge, contradiction resolution, maths/physics validation, simulation/digital-twin checks, regression, provenance and promotion.
- The multi-language architecture assigns C++ to native high-performance simulation/geometry work, Rust/C to safety-sensitive/embedded paths, and a C ABI as the durable interoperability boundary.
- Unity 6 integration identifies DOTS/Entities/Physics and Jobs/Burst as performance/parallelism candidates.
- Unity batch-mode host automation exists for headless build execution.
- Render/simulation jobs have queue/persistence contracts.

## Acceleration candidates
1. Parallel task orchestration — **REGISTERED / ARCHITECTURALLY IMPLEMENTED**
2. C++ native numerical/simulation kernels — **REGISTERED / ARCHITECTURALLY IMPLEMENTED**
3. Rust/C safety-sensitive kernels — **REGISTERED / ARCHITECTURALLY IMPLEMENTED**
4. Unity Jobs/Burst/DOTS — **REGISTERED / ADAPTER CANDIDATE; LIVE RUNTIME VERIFICATION PENDING**
5. GPU/vendor-native acceleration — **NOT YET VERIFIED**
6. Hardware-specific acceleration — **NOT YET VERIFIED**
7. Persistent cache/compiled-kernel cache — **NOT VERIFIED**
8. Live before/after benchmark — **PENDING CONNECTED RUNTIME**

## Execution rule
Do not claim hardware/GPU acceleration merely because an adapter or research reference exists. Promotion requires a reproducible runtime test with environment, version, workload, wall time, throughput and failure state recorded.

## Next benchmark matrix
- baseline serial execution
- parallel execution
- C++ kernel path
- Unity Jobs/Burst/DOTS path where installed
- GPU path where available
- cache-enabled versus cold execution
- regression/smoke test after each promotion

## Evidence boundary
Repository architecture is not proof of live runtime activation. Live execution remains separately verified when a connected build/runtime host is available.
