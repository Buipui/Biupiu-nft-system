# Biupiu Engine Interoperability Protocol v1.0

**Gate:** XENG-01  
**Status:** INTEGRATED at source/contract level; connected-host execution required

## Canonical topology
BIUPIU OS / DMS -> Universal Asset + Digital Twin Manifest -> canonical interchange -> Blender/CAD, Unreal Engine 5, Unity, Lumion, Twinmotion, XR/Web -> provenance -> Digital Twin.

OpenUSD is the preferred scene-composition boundary where supported; glTF/GLB is the preferred portable runtime delivery boundary. Provider-native files remain local to their owning applications.

Lumion remains a presentation/environment layer. Unity and Unreal remain interactive/XR/simulation providers. Blender remains an open authoring/reference route. No provider derivative may overwrite the canonical source.

## Cross-engine health protocol
Every registered provider receives: version, capabilities, licence state, dependency state, connection state, test results, warnings, failures and last verified timestamp.

Status vocabulary: REGISTERED -> INTEGRATED -> CONNECTED -> VERIFIED. BLOCKED and DEPRECATED are terminal review states until revalidated.

## Exterminate sequence
DISCOVER -> LICENSE -> DEPENDENCY -> SCHEMA -> CONTRACT -> SECURITY -> STATIC/UNIT -> CROSS-ENGINE -> REGRESSION -> PROVENANCE -> PROMOTE.

Reject copied proprietary binaries, cracks/keygens/unlocks, unclear-license assets, direct engine-to-engine mutation, and visual output being used as engineering evidence.

## Connected-host gates
XENG-02 installed-engine discovery; XENG-03 controlled Blender/CAD -> UE5 -> Unity -> Lumion round trip; XENG-04 geometry/material/transform/provenance drift; XENG-05 OpenXR smoke test; XENG-06 persistent cross-engine world state and XR site twin.

Repository contracts establish architecture only. Connected applications and devices must produce measured host evidence before runtime status becomes VERIFIED.
