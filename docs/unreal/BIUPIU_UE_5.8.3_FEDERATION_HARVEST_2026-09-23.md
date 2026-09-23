# BIUPIU UE 5.8.3 FEDERATION HARVEST & MIGRATION MATRIX

Date: 2026-09-23
Status: External harvest completed; repository integration record created
Scope: Unreal Engine 5.8/5.8.3, Biupiu World/Desktop, Landing Layer provenance, Launcher-vs-source/installed-build association, implementation gates

## External authoritative harvest

| Module / system | UE 5.8/5.8.3 finding | Biupiu relevance | Repository action | Gate |
|---|---|---|---|---|
| Engine association / Launcher | Launcher foreign projects use the official version number in .uproject EngineAssociation; source/custom builds can use a GUID/local registration. | Critical because 5.8.3 is now loading through Epic Games Launcher rather than the previous fork/source-style layout. | Preserve old engine as baseline; record current association before migration. | OPEN – local verification |
| Installed Build / provenance | Epic distinguishes Launcher-installed engines from custom Installed Builds and their registration models. | Explains different project resolution behavior without implying data loss. | Add provenance check to migration gate. | OPEN |
| StateTree | UE 5.8 adds starting-state/compiler/property-binding improvements; 5.8.3 fixes a StateTree stack allocation issue affecting 5+ nested entries. | Simulation/state orchestration and VSS cleanup. | Compile/runtime regression test. | PENDING |
| Mass Framework | UE 5.8 expands Mass with core Mass Signals, lock-free scheduling, sparse/virtual fragments and improved processor execution. | Federated world/simulation entities and scalable workloads. | Compatibility review. | PENDING |
| Rendering / Nanite | UE 5.8 adds Nanite performance/streaming/tessellation improvements; 5.8.3 fixes dynamic-resolution/split-screen Nanite LOD selection. | AAA Biupiu World visual layer. | Visual regression. | PENDING |
| World Building / PCG | 5.8 expands worldbuilding/PCG; 5.8.3 fixes HLOD GPU virtual-address exhaustion, FastGeo processing and PCG metadata drift. | Procedural regenerative landscapes and large environments. | HLOD/FastGeo/PCG smoke tests. | PENDING |
| Chaos / Dataflow | 5.8 adds runtime Dataflow evaluation, tooling, skeletal authoring and caching; 5.8.3 fixes a Dataflow async-load data race. | Composite/material/physics simulation. | Async-load/runtime graph test. | PENDING |
| OpenXR / XR | 5.8 changes stereo-layer ordering and adds XR/mobile improvements; 5.8.3 fixes OpenXR swapchain creation fallback. | Future AR/VR Biupiu World endpoints. | Preserve layer priorities; XR startup test. | PENDING |
| Mobile / iOS | 5.8 adds experimental iOS SM6; 5.8.3 changes iOS/tvOS/iPadOS framework signing and bundled .NET/IPPs. | Cross-platform/mobile pipeline. | Packaging migration test. | PENDING |
| Windows ARM64 | 5.8 adds experimental ARM64/ARM64EC game-target packaging; editor is not supported on ARM64. | Future heterogeneous-device federation. | Record as target capability only. | INFORMATIONAL |
| MCP | 5.8 adds an assistant toolset for animation features and fixes ECA Bridge boolean parsing. | AI-assisted editor/VSS integration. | Add MCP compatibility inventory. | PENDING |
| NNE / AI-ML | 5.8 updates ONNX Runtime/DirectML/IREE and CoreML support; NNERuntimeORTDml drops the NPU execution interface. | Biupiu Intelligence / GPU-NPU federation. | Review NNE/ONNX/DirectML/NPU assumptions before cleanup. | OPEN |
| Composure | 5.8 moves Composure to Beta with Sequencer/passes/keying changes; 5.8.3 fixes cooked-game legacy references via ComposureShared. | Cinematic landing layer/render pipeline. | Search Composure/ComposureShared references. | PENDING |
| Blueprint / Editor UI | 5.8.3 fixes Blueprint action-database tooltip crash, Blueprint transform loss after error recovery, editor UI issues and a rare VS opening crash. | Landing Layer Blueprint recovery and VSS workflow. | Blueprint compile/transform checks. | PENDING |
| Sequencer | 5.8.3 fixes multiple Sequencer crashes and binding/time-warp issues. | Cinematic landing/intro sequences. | Regression test Biupiu Sequencer assets. | PENDING |
| Landscape | 5.8.3 fixes landscape initialization, shader warnings/crashes and foliage snapping. | Landing terrain/regenerative environments. | Landscape/foliage smoke test. | PENDING |
| Movie Render Pipeline | 5.8.3 fixes naming-token resolution and accumulation DOF/aberration alpha issues. | Showreels/cinematic landing renders. | MRQ smoke render. | PENDING |

## Repository-derived Biupiu implementation inventory

| Existing Biupiu item | Evidence status | Required 5.8.3 treatment |
|---|---|---|
| Biupiu World visual/landing concepts | FOUND in Library; concept evidence only | Design target, not executable proof. |
| Biupiu Mini OS UI/Home landing concept | FOUND in Library; concept evidence only | Map into actual UE assets after filesystem verification. |
| Federation Layer | RECORDED in IP/architecture register | Preserve architecture; verify executable implementation separately. |
| DT_Bootstrap map contract | Previously recorded | Verify exact map/dependencies locally. |
| UE5 Asset Studio scaffold | Previously recorded | Verify source/assets/plugins locally. |
| Landing Layer file reported in Recycle Bin | HISTORICALLY REPORTED; may have been restored | Trace restored path, timestamps and asset type before modification. |
| Desktop runtime/build verification | OPEN | Run against 5.8.3 after provenance check. |
| Old UE release | PRESERVE as reference baseline | No cleanup/overwrite/migration deletion until differential audit closes. |

## Landing Layer forensic path

1. Locate restored file/folder and exact original path.
2. Determine whether it is .uasset, .umap, Blueprint Widget, Level, plugin content, C++ or generated data.
3. Compare timestamps and hashes with the old UE release/current project.
4. Read the current .uproject EngineAssociation.
5. Compare project plugins/modules/startup maps.
6. Inspect Unreal logs, Launcher/update records and repository history for the relevant time window.
7. Only then classify the removal as user action, migration/update tooling, generated-data cleanup, repository operation, or another process. Do not assume malicious activity without evidence.

## VSS/Copilot migration contract

OLD BASELINE -> INVENTORY -> ENGINE ASSOCIATION -> API/PLUGIN DELTA -> MINIMAL CODE CHANGES -> COMPILE -> AUTOMATED TEST -> EDITOR/PIE SMOKE TEST -> VISUAL REGRESSION -> HASH/DIFF -> VERIFIED

Generated folders such as Intermediate, Saved and DerivedDataCache are not authoritative source implementation. Preserve source assets, Config, Plugins, Content and C++ as the evidence layer.

## Source/IP controls

Epic material is third-party reference material, not Biupiu-owned IP. Preserve source URL, retrieval date, version/license status and exact Biupiu contribution. Keep third-party code/licensing separate from Biupiu-authored implementation.

## Gate status

- UE 5.8.3 external specification harvest: COMPLETE
- UE 5.8.3 hotfix harvest: COMPLETE
- Repository/library semantic harvest: COMPLETE for available Library evidence
- Engine provenance migration matrix: REGISTERED
- Landing Layer provenance: OPEN
- Old-vs-new filesystem differential: OPEN (requires local PC access)
- .uproject EngineAssociation verification: OPEN (requires local project file)
- VSS cleanup/refactor: HOLD until provenance + compile tests
- Runtime/PIE verification: OPEN
- Final 5.8.3 implementation verification: OPEN

## Authoritative external sources

- https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-8-release-notes
- https://dev.epicgames.com/documentation/unreal-engine/installed-build-reference-guide-for-unreal-engine
- https://dev.epicgames.com/documentation/unreal-engine/managing-game-code-in-unreal-engine
- https://forums.unrealengine.com/t/5-8-3-hotfix-released/2833315
