# Biupiu Federation Changelog — Jolt / Bullet / QuTiP / OpenFermion / OpenGL

Date: 2026-09-22

## Added
- External federation harvest records for Jolt Physics, Bullet Physics, QuTiP, OpenFermion and Khronos OpenGL/OpenGL ES.
- Internal-first provider contracts for classical physics, quantum simulation and graphics.
- Native dependency-free smoke contracts so repository tests do not silently acquire third-party runtime dependencies.
- Cross-links to Maths/Physics/Quantum, Digital Twin, Native Coding Matrix, semantic audit, native ML learning and blockchain-anchor boundary.

## Integration policy
- External source code is not copied into the repository merely because it is available upstream.
- Jolt is already a registered physics candidate; this gate extends its provider contract and adds Bullet as a validation lane.
- QuTiP and OpenFermion are quantum-provider contracts; classical and quantum numerical results remain separate evidence classes.
- OpenGL/OpenGL ES are graphics API contracts, not physics solvers.
- Runtime promotion remains fail-closed until dependency, build, integration, security, regression and real-runtime evidence exists.

## Verification
- Repository source contracts: PASS
- Licence/source provenance review: PASS for the recorded upstream candidates
- Native semantic contract: ADDED
- Dependency-free smoke tests: ADDED
- CI/runtime/device verification: OPEN in the GitHub connector environment
- Production promotion: OPEN
