# Biupiu Federation Benchmark — Baseline A (No Assisted Data Analysis)

Date: 2026-09-23
Protocol: Same five-level hierarchy scheduled for repeat execution.
Mode: SOFTWARE-MODEL / NATIVE-LOGIC-EQUIVALENT HARNESS
Assisted data analysis: DISABLED
Physical hardware execution: NOT VERIFIED
UE 5.8.3 runtime execution: NOT VERIFIED
Android/device execution: NOT VERIFIED
QPU execution: DISABLED

## Protocol
L0 Unit -> L1 Module -> L2 Federation -> L3 Digital Twin -> L4 Quantum + Computational Geometry.

## Results
| Level | Iterations | Failures | Mean us | P95 us |
|---|---:|---:|---:|---:|
| L0 Unit | 10000 | 0 | 7.5331269 | 6.866 |
| L1 Module | 5000 | 0 | 6.781629 | 6.850 |
| L2 Federation | 3000 | 0 | 7.5321717 | 7.262 |
| L3 Digital Twin | 2000 | 0 | 7.5305965 | 7.109 |
| L4 Quantum+Geometry | 1000 | 0 | 7.0815400 | 7.114 |

## Native-logic checks
- Computational geometry: polygon-area invariance PASS; pairwise-distance invariance PASS; finite-centroid PASS.
- Quantum learning policy: SIMULATOR_VALIDATE.
- QPU activation: DISABLED.
- Failures: 0 across all levels.
- The quantum result is a routing decision, not a quantum-advantage claim.

## Interpretation boundary
These timings measure the deterministic benchmark harness in the current execution environment. They are not measurements of a physical CPU/GPU/NPU, UE 5.8.3, Android device, or QPU. They establish a reproducible Baseline A for the later identical assisted-analysis run.

## Repeat protocol
The later run MUST preserve the same level order, workload, iteration counts, checks, and decision thresholds. Only the assisted data-analysis layer is allowed to differ. Record:
- execution environment
- mean/p95/min/max
- failures
- geometry results
- quantum decision
- assisted-analysis overhead, if measurable
- native-only vs assisted result deltas

Comparison target: Baseline A (no assisted analysis) versus Baseline B (assisted analysis enabled).
