# Native Coding Matrix — Scientific Compute Extension — 2026-09-22
## Hard rules
1. Scientific libraries are providers behind a stable Biupiu contract.
2. Capability detection is explicit; library presence is never inferred from documentation.
3. Numerical code declares domains, units, tolerances and failure behaviour.
4. Eigen/GSL interoperability must not leak third-party types across durable ABI boundaries.
5. GSL remains an optional licensing boundary because GPL obligations must be evaluated against the final distribution model.
6. Deterministic native fallback remains available when external providers are absent.
7. Provider changes require semantic, numerical, regression and provenance evidence.
8. Android NDK and device verification remain separate from source-level implementation.
## Required path
REQUIREMENT -> INTERNAL GAP CHECK -> EXTERNAL HARVEST -> LICENCE/PROVENANCE -> ADAPTER -> SEMANTIC TEST -> BUILD -> NUMERICAL REGRESSION -> RUNTIME -> PROMOTION.
## Cross-system contract
MATH <-> GEOMETRY <-> PHYSICS <-> SIMULATORS <-> DIGITAL-TWIN <-> AI/ML <-> OS/DMS <-> MINI-OS <-> ANDROID.
Status: GOVERNANCE EXTENSION IMPLEMENTED / RUNTIME VERIFICATION OPEN.
