# BIUPIU BENCHMARK PROGRAM HARVEST GATE — 2026-09-22

Status: SOURCE-INTEGRATED / RUNTIME VERIFICATION PENDING

## Purpose
Harvest usable engineering patterns from benchmark programs identified in the benchmark study, then route them through the Biupiu native coding matrix. This is pattern/adapter integration, not vendor-source copying.

## Benchmark-to-native matrix

| Benchmark | Usable pattern | Biupiu native destination | Harvest class |
|---|---|---|---|
| Palantir Ontology | operational ontology; objects/links/actions; governed model integration | DMS, Digital Twin, federation, intelligence graph | PATTERN/ADAPTER |
| Siemens Xcelerator | industrial lifecycle, digital thread, interoperability | DMS, Digital Twin, instrumentation/automation | PATTERN/ADAPTER |
| Dassault 3DEXPERIENCE | virtual-twin lifecycle and engineering collaboration | Digital Twin, simulation, CAD/engineering contracts | PATTERN/ADAPTER |
| NVIDIA Omniverse/OpenUSD | interoperable 3D scene layer, physical AI, simulation | World, Digital Twin, universal simulator, robotics | ADAPTER/PATTERN |
| PTC ThingWorx | IIoT asset/device modelling and operational context | DMS, telemetry/context, machine capability | PATTERN/ADAPTER |
| Bentley iTwin | infrastructure twin and engineering/IoT integration | Digital Twin, GIS/land, telemetry | PATTERN/ADAPTER |
| Unreal Engine 5 | real-time 3D visualization/simulation host | world/adapters, rendering, showcase | EXTERNAL ADAPTER |
| Unity 6 | cross-platform real-time 3D presentation/simulation | world/adapters, presentation/simulation | EXTERNAL ADAPTER |

## Native routing rules
1. Benchmark software never becomes Biupiu authority.
2. Proprietary source, binaries, assets, credentials and restricted material are excluded.
3. Open standards may be implemented independently where licensing permits.
4. C ABI is the durable native boundary.
5. Rust remains preferred for new safety/concurrency/security-sensitive services.
6. C++ remains the high-performance simulation/geometry/graphics layer.
7. Every harvested pattern receives provenance, evidence state, licence status and target module.
8. External runtime adapters remain replaceable and cannot silently change authoritative OS/DMS state.
9. Simulation results remain model evidence until validation/correlation gates pass.
10. Failed adapter/build/runtime tests become learning evidence and regression inputs.

## Existing reusable modules confirmed
- core/multilang/ — native C/C++ boundary.
- software/rnd-os-ai/ — intelligence, learning, promotion.
- packages/biupiu-unreal-engine/ — Unreal adapter.
- world/adapters/unity6/ — Unity adapter scaffold.
- research/BIUPIU-UNIVERSAL-SIMULATOR-FEDERATION-GATE-36.md — common simulator federation.
- research/BIUPIU-INSTRUMENTATION-AUTOMATION-ROBOTICS-AI-GATE-v1.0.md — machine/industrial protocol routing.
- enterprise/BIUPIU-ENTERPRISE-DIGITAL-TWIN-SYSTEM-v1.0.md — enterprise twin integration.

## External evidence
Palantir documents its Ontology as an operational layer connecting datasets/models to real-world counterparts. NVIDIA documents Omniverse as libraries/microservices for industrial digital twins and robotics simulation using OpenUSD. These are benchmark facts only; Biupiu does not adopt vendor architecture as authority.

## Verification
STATIC_SOURCE_AUDIT: PASS for new adapter contract
CONTRACT_SMOKE: SOURCE ADDED
PACKAGE_BUILD: PENDING
CROSS_SYSTEM_RUNTIME: PENDING
UE5/Unity HOST RUNTIME: PENDING
HARDWARE/PHYSICAL: PENDING

No runtime verification is claimed by this gate.


## Native audit update — 2026-09-22

Audit found one governance weakness in the first implementation: the native benchmark record required provenance/evidence but did not enforce licence state and source-version metadata at the ABI contract. This has now been corrected.

New mandatory native fields:
- `licence_state`
- `source_version`

The smoke path now supplies both fields. A harvested module therefore cannot pass native validation merely by having a capability name and provenance reference.

This aligns the implementation with the coding matrix's third-party rule: licence verification + provenance + compatibility/build/testing evidence are prerequisites for promotion. Benchmark references remain non-authoritative until validated.

External benchmark evidence remains descriptive: Palantir's Ontology documents objects/properties/links plus actions and governance as an operational layer; NVIDIA documents OpenUSD as an open, extensible scene framework and Omniverse as an application/library layer around it. citeturn0search2turn0search0turn0search1

Updated verification state:
- STATIC_SOURCE_AUDIT: PASS (contract hardened)
- CONTRACT_SMOKE: SOURCE UPDATED; execution pending
- LICENCE/PROVENANCE GATE: ENFORCED AT CONTRACT LEVEL
- PACKAGE_BUILD: OPEN
- CROSS_SYSTEM_RUNTIME: OPEN
- UE5/Unity HOST RUNTIME: OPEN
- HARDWARE/PHYSICAL: OPEN
- FINAL VERIFIED: OPEN
