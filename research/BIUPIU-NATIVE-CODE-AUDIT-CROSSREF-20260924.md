# Biupiu Native Code Audit + Cross-Reference — 2026-09-24

Status: SOURCE AUDIT COMPLETED / EXECUTION EVIDENCE PENDING

Audited native paths:
- apps/windows/ForeignLanguageHarvestRegistry.cs
- apps/windows/ForeignLanguageHarvestRegistryTests.cs
- apps/windows/MainWindow.xaml.cs
- software/rnd-os-ai/src/biupiu_ai/compute_federation.py
- software/rnd-os-ai/src/biupiu_ai/quantum_federation.py
- software/rnd-os-ai/src/biupiu_ai/federation_protocol.py
- software/rnd-os-ai/tests/test_quantum_federation.py
- software/rnd-os-ai/tests/test_compute_federation.py

Cross-reference:
- Baseline A
- Native Quantum vs Federation blind audit + optimisation
- PC foreign-language harvest integration
- Coding/authority boundaries
- Android/AOSP external-language evidence
- machine-readable provenance and fail-closed promotion

## Findings

### Windows
The foreign-language registry preserves six language lanes and eight fault checks. External evidence cannot promote executable code because executable promotion is disabled for every registered lane.

The WPF startup path executes registry tests, loads the language registry, reports harvest state and resolves department entitlements. This is source-level integration only until an actual Windows build and UI run produce evidence.

### Federation compute
compute_federation.py uses capability-first topology discovery, preferred-class ordering, capacity-aware planning and fail-closed minimum capability requirements. The prior preferred-class ordering fault is explicitly guarded and remains a useful regression case.

### Quantum
quantum_federation.py is framework-neutral and fail-closed. It distinguishes simulator/classical-emulation/hardware modes, records passive learning observations, and routes candidates to simulator validation or classical baseline. It does not establish QPU execution or quantum advantage.

### Federation authority
federation_protocol.py defines 25 canonical gates. Readiness requires explicit VERIFIED status and all required evidence. Quantum/ML, runtime, multicore, native-platform and cross-matrix gates are governed boundaries rather than automatic permissions.

### Test coverage
Existing unit tests cover quantum promotion fail-closed behaviour, hardware security review, stable capability names, heterogeneous compute planning and required-accelerator failure.

The source audit does not prove Windows runtime, Android runtime, physical SIMD/GPU/NPU performance, UE5 runtime, QPU execution or cross-device behaviour.

## Fresh external cross-reference
The September 2026 AOSP/Android search confirms:
- android-latest-release currently references android17-release.
- Android 17 QPR2 beta 5 lists x86-64 and ARM v8-A emulator support.
- Android 17 QPR1 GSI provides ARM64 and x86_64 AOSP images.
- Android 17 security notes were updated September 3, 2026.
- AOSP documentation recently updated Stable AIDL module-level version headers and GKI release information.
- AndroidX Security State 1.1.0 provides component-level security-state visibility.

These remain external evidence/reference inputs. They do not alter the native authority chain or promote external executable code.

## Fault checks
1. SOURCE_IMPL_AS_RUNTIME_EVIDENCE
2. FOREIGN_DOC_AS_IMPLEMENTATION_AUTHORITY
3. TRANSLATED_CLAIM_WITHOUT_ORIGINAL_SOURCE
4. ARCHITECTURE_LINEAGE_COLLAPSE
5. SIMULATOR_AS_QPU_EVIDENCE
6. CAPABILITY_REGISTRATION_AS_PERFORMANCE_EVIDENCE
7. WPF_SOURCE_AS_WINDOWS_RUNTIME_EVIDENCE
8. OPTIMISATION_AS_AUTOMATIC_PROMOTION

## Status matrix
| Area | Source audit | Runtime evidence | Promotion |
|---|---|---|---|
| PC foreign-language registry | PASS | OPEN | BLOCKED |
| Federation scheduler | PASS | OPEN | governed |
| Quantum federation | PASS | QPU OPEN | BLOCKED |
| Quantum unit tests | REGISTERED | execution pending | NONE |
| Windows WPF | PASS | Windows build/UI OPEN | NONE |
| Android/AOSP cross-reference | PASS | device/build OPEN | NONE |
| SIMD/GPU/NPU | capability contracts | physical performance OPEN | NONE |
| UE5 | boundary present | runtime OPEN | NONE |

Conclusion: native source contracts are internally cross-consistent with the established authority, provenance and fail-closed model. The benchmark must therefore be a matched blind execution test, not a source-derived winner calculation.
