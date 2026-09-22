# Biupiu Eigen + GSL Federation — Pass 2 — 2026-09-22

## Scope
Second-pass federation: upstream status reconciliation, foreign-language reference harvest, optimization candidate harvest, guided fault finding, and native coding-matrix hardening.

## External reconciliation
Eigen official documentation identifies the 5.0 development line and documents dense/sparse linear algebra, decompositions, geometry, and SIMD/vectorization. The official site currently lists 5.0.0 as stable while development documentation exposes 5.0.1-dev. citeturn0search0turn0search2turn0search12
GSL official documentation identifies GSL 2.8 and documents optimized functions, numeric types, portability and thread-safety. citeturn0search5turn0search9

## Foreign-language harvest
The official GNU GSL page exposes Japanese and Portuguese reference-manual translations. These are reference evidence only; no translated code or third-party material was copied. citeturn0search11

## Optimization candidates
- ARM NEON/SIMD paths
- sparse linear algebra
- geometry modules
- alignment-sensitive paths
- GSL optimized functions
- GSL numeric-type paths
- GSL thread-safety review

These remain benchmark-gated candidates, not claims of Android acceleration. Eigen documents architecture-specific vectorization, while GSL documents optimized-function and thread-safety facilities. citeturn0search2turn0search5

## Fault finding
- Corrected the previous version record: Eigen stable = 5.0.0; 5.0.1 is represented as development/reference state.
- Prevented external SIMD documentation from being treated as measured device performance.
- Preserved provider capability detection and deterministic fallback.
- Preserved GSL licence gate.
- Preserved foreign-language sources as evidence rather than executable authority.

## Verification
PASS 2 SOURCE/REFERENCE AUDIT: CLOSED
FOREIGN-LANGUAGE REFERENCE HARVEST: PASS
OPTIMIZATION CANDIDATE HARVEST: PASS
CI EXECUTION: OPEN
ANDROID NDK/GRADLE: OPEN
DEVICE SIMD/PERFORMANCE: OPEN
GSL RUNTIME: OPEN
STATUS: PASS 2 SOURCE GATE CLOSED / RUNTIME GATES OPEN
