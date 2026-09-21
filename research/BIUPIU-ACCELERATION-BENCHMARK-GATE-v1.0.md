# Biupiu Acceleration Benchmark Gate v1.0

Date: 21 September 2026

## Gate
ACCEL-02 — live acceleration benchmark + smoke/regression gate.

## Objective
Provide a reproducible host-side gate that measures only capabilities actually present on the connected development machine. No GPU, Unity Jobs/Burst/DOTS, cache, or hardware acceleration is promoted from architecture-only evidence.

## Required evidence
1. Host inventory: PowerShell, .NET, Git, VS Code, Unity.
2. Unity project identity: ProjectVersion.txt, Packages/manifest.json and packages-lock.json when present.
3. Cold versus warm execution where a benchmark workload exists.
4. Serial baseline versus parallel path where both are implemented.
5. Unity Jobs/Burst/DOTS only when the installed project resolves those packages and the runtime test completes.
6. GPU/vendor path only when the host exposes the relevant runtime and the benchmark records device/driver information.
7. Exit codes, elapsed time, throughput, errors and regression result.

## Promotion states
- REGISTERED — documented candidate.
- IMPLEMENTED — executable adapter/gate exists.
- RUNTIME-VERIFIED — reproducible measurement captured.
- REGRESSION-PASS — post-change smoke/regression passes.
- BLOCKED — required host/runtime dependency unavailable.

## Current result
**IMPLEMENTED / RUNTIME-VERIFICATION PENDING**

The repository contains a Unity host gate, but this connector session does not expose a connected Unity desktop runtime. Therefore no live performance number is fabricated.

## Smoke-test rule
A benchmark result cannot be promoted if the host gate fails, Unity compilation fails, required packages do not resolve, or the workload exits non-zero.

## Evidence boundary
Architecture, package references and scripts prove implementation of the gate—not activation of acceleration on a physical machine.
