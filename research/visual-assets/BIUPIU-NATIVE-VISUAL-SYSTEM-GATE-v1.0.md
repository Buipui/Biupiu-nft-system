# Biupiu Native Visual System Gate v1.0
**Priority:** P0
**Status:** SOURCE-LEVEL CONTRACT IMPLEMENTED / RUNTIME OPEN

## Current state
The repository already had a unified renderer router, visual asset manifest/provenance, UE5 visual bridge, animation scene contract, visualization package and GPU host-safety gate. This gate unifies those pieces behind a Biupiu-native rendering/animation/video API.

## Maturity assessment
- AI governance/interface layer: substantially architected and source-level implemented; runtime/provider connectivity remains incomplete.
- World/engine abstraction: implemented at architecture/registry level.
- Visual asset/provenance layer: implemented.
- Renderer routing: implemented.
- Animation contract: implemented at repository/static comparison level.
- Native visual API: implemented now as source-level C ABI + schema.
- Native renderer implementation: OPEN.
- Native animation runtime: OPEN.
- Native video/codec runtime: OPEN.
- Host GPU runtime verification: OPEN.
- Unity/UE5 adapter runtime verification: OPEN.

## P0 runtime sequence
VIS-NATIVE-02 Capability probe
VIS-NATIVE-03 Native render smoke
VIS-NATIVE-04 Animation deterministic sample
VIS-NATIVE-05 Frame capture
VIS-NATIVE-06 Video encode smoke
VIS-NATIVE-07 Unity adapter
VIS-NATIVE-08 UE5 adapter
VIS-NATIVE-09 Cross-provider equivalence
VIS-NATIVE-10 Full visual regression

## Design rule
Unity and UE5 are providers. Biupiu owns canonical scene/job/provenance contracts. The native layer must remain capable of operating with a fallback provider.
