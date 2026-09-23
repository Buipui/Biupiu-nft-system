# Biupiu Federated Missing-Module Harvest — 2026-09-23

## Scope
Internal cross-check of Digital Twin / adaptive federation / UE 5.8.3 / native-learning implementation, followed by an external federation harvest for executable gaps.

## Internal cross-check

| Area | Existing evidence | Missing executable layer | Action |
|---|---|---|---|
| Federation gates | F01-F22 | F23-F25 registration | Added F23-F25 |
| Digital Twin policy | architecture baseline | deterministic resource/path selector | Added adaptive_federation.py |
| Passive learning | learning.py passive observations | runtime telemetry -> governed learning bridge | Added RuntimeTelemetryObservation |
| OEM compatibility | architecture/performance matrix | executable provider/runtime registry | Added oem_registry.py |
| ONNX/NNE | architecture references | explicit provider adapter inventory | Added canonical registry |
| Testing | existing federation/learning/quantum tests | adaptive/OEM regression coverage | Added two test modules |
| UE 5.8.3 | external migration matrix | local EngineAssociation/runtime verification | remains OPEN; requires local PC |
| Hardware | capability architecture | physical GPU/NPU/device measurements | remains OPEN |
| QPU | quantum learning/routing | QPU validation | remains OPEN |
| Blockchain | anchor manifest | authorized transaction + independent confirmation | remains PREPARED |

## External deep harvest findings

1. ONNX Runtime uses Execution Providers as the hardware-acceleration boundary and documents CPU, GPU, mobile/edge and vendor-specific providers. This supports the capability-first adapter model.
2. ONNX Runtime plugin EP libraries provide a dynamic registration boundary, allowing providers to be loaded independently rather than becoming hard dependencies of the core runtime.
3. Qualcomm QNN EP explicitly supports Snapdragon Android and Windows targets and exposes CPU/GPU/HTP(NPU) backend choices; strict validation can disable CPU fallback.
4. Intel OpenVINO EP covers CPU/GPU/NPU classes; this was missing from the executable compatibility registry.
5. AMD's ONNX Runtime ROCm EP is removed from ORT 1.23 onward; MIGraphX is the migration target. The registry therefore records AMD through MIGraphX.
6. Unreal Engine 5.8 updates NNE's ONNX Runtime to 1.24.3, DirectML to 1.15.4, IREE to 3.11.0 and adds CoreML .mlpackage import; the NNE/ORT boundary must be versioned independently from the Biupiu learning layer.
7. UE 5.8 also adds an experimental MCP plugin and additional OpenXR/mobile changes. These remain editor/device verification gates, not claims of local execution.

## Semantic/coding audit

- Application boundaries are provider-neutral.
- Hardware/vendor names are isolated in the OEM registry.
- Adaptive decisions are fail-closed on missing capability, provenance, safety or validated execution path.
- PASSIVE state does not activate a module.
- Runtime telemetry requires bounded latency/resource values and a correlation ID.
- Learning records retain provenance hashes and do not grant promotion authority.
- External facts are represented as registered evidence, not proof of physical hardware validation.
- No production credentials, wallet secrets or private invention details were added.

## Functional test coverage added

- Passive compatibility manifest remains PASSIVE.
- Missing capability is DEGRADED.
- Validated GPU selection responds to resource pressure.
- Unverified provenance cannot activate a module.
- Runtime telemetry is bounded and correlated.
- OEM registry contains Qualcomm/QNN, Intel/OpenVINO, NVIDIA/CUDA, AMD/MIGraphX, Epic/NNE and Khronos/OpenXR entries.
- Registry is deterministic and all entries have explicit fallback paths.

## Verification boundary

Repository code and test definitions were updated through GitHub. The linked repository currently reports no commit status checks for the new commits, so this pass cannot truthfully mark the Python suite as executed by CI. Local execution is therefore OPEN.

Local-only gates still open:
- UE 5.8.3 project/EngineAssociation and filesystem provenance
- Unreal Editor compile/PIE/visual regression
- physical Qualcomm/Intel/NVIDIA/AMD accelerator tests
- Android/device and OpenXR runtime tests
- ECU/HIL tests
- QPU execution validation
- authorized blockchain submission and independent confirmation

## Status

**REGISTERED / INTEGRATED:** F23-F25, adaptive resource controller, OEM runtime registry, runtime telemetry learning bridge, regression tests, external compatibility harvest.

**PENDING VERIFICATION:** local runtime/CI execution and physical hardware/device measurements.