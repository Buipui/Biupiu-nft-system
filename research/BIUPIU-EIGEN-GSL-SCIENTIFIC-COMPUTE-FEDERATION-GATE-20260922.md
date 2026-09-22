# Biupiu Eigen + GNU Scientific Library Federation Gate — 2026-09-22
## Scope
External harvest, internal-gap reconciliation, native adapter integration and cross-system routing for Eigen and GNU Scientific Library (GSL). “Elgen” is interpreted as Eigen; no unverified project named Elgen is promoted.
## External harvest
- Eigen is a C++ template library for linear algebra; current tagged release observed: 5.0.1. citeturn1search0turn1search5turn1search6
- GSL is the GNU C numerical library with broad numerical facilities including special functions and linear algebra. Official GNU material also exposes Japanese and Portuguese manual translations. citeturn0search5turn1search24
- Elmer FEM was checked as a possible naming ambiguity. It is a separate multiphysics FEM suite and is not silently merged into this provider boundary. citeturn0search0turn0search1
## Internal-first reconciliation
Existing Biupiu native compute, geometry, simulator, Digital Twin, federation and ML contracts remain canonical. The scientific layer is an adapter/provider boundary, not a second mathematical authority.
## Native integration
Added the scientific C++ adapter, smoke fixture, and Android native build hook. Compile-time capability detection selects Eigen first, GSL second, and the deterministic native implementation as fallback.
## System routing
Provider capability is routed to computational geometry, maths, physics/simulation adapters, registered simulators, Digital Twin numerical services, Biupiu Intelligence/ML feature extraction, Biupiu OS, Biupiu Mini OS and Android native build.
## Licensing boundary
Eigen 5.0.1 is MPL-2.0. GSL is GPL-licensed. GSL therefore remains an optional provider boundary unless the final distribution/licensing model explicitly permits its obligations. No GSL source is copied into Biupiu.
## Guided fault finding
- Ambiguous “Elgen” identity resolved to Eigen; Elmer remains separate.
- Provider authority leakage blocked by capability contract.
- Missing-provider build failure avoided by deterministic native fallback.
- Invalid vector inputs fail closed.
- Runtime provider availability remains evidence-gated.
## Semantic/code checks
Explicit types; deterministic fallback; bounded dependency boundary; provenance/licence gate; no copied proprietary binaries/source; testable adapter contract; runtime evidence separated from source presence.
## Verification
SOURCE IMPLEMENTATION: PASS
SMOKE FIXTURE: DEFINED
CI EXECUTION: OPEN until observed
ANDROID NDK/GRADLE: OPEN
DEVICE/HARDWARE: OPEN
LIVE EXTERNAL PROVIDER ENUMERATION: OPEN
Status: IMPLEMENTATION COMPLETE / RUNTIME VERIFICATION OPEN.
