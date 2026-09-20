# ENGINE-06 — Reality Scan Resource Gate

**Status:** IMPLEMENTED at source/repository level.

## Gate
Resource discovery -> licence verification -> compatibility classification -> isolated gateway -> contract smoke test -> promotion state.

## Connected
- Reality Scan resource manifest
- Native Biupiu Engine provider architecture
- ResourceGateway
- deterministic promotion state
- existing provider-bus architecture

## Initial candidates
OpenXR SDK, Jolt Physics, Project Chrono, MuJoCo and OpenEXR are recorded with explicit licences and source URLs. glTF is recorded as mixed/file-level licensing and is therefore not treated as a blanket single-license dependency.

## Result
The repository-level smoke gate can prove the gateway contract and promotion mechanics. It cannot prove native compilation, GPU execution, XR hardware, UE5/Unity/Lumion runtime operation, or third-party numerical equivalence.

**Promotion:** REGISTERED -> INTEGRATED -> CONNECTED -> VERIFIED; failures -> BLOCKED.
