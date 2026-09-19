# Biupiu USD Interchange Matrix — Gate 5

**Date:** 2026-09-19  
**Status:** TEST PLAN IMPLEMENTED — RUNTIME EXECUTION PENDING

## Objective
Define a controlled interchange test between the repository's USD scene and the target 3D stack.

| Path | Test | Expected evidence |
|---|---|---|
| USDA → USD/OpenUSD | Parse/open stage | Stage opens; expected prims and time samples remain |
| USDA → Blender | Import/open USD | Camera/object hierarchy and animation preserved |
| USDA → Unreal | USD Stage / Interchange import | Scene loads and transform animation is represented |
| Blender → USDA | Export/re-save test asset | Required hierarchy and animation survive round-trip |
| Unreal → USD | Export/round-trip where supported | Compare prim inventory and transforms |
| OTIO manifest | Editorial handoff | Timeline/clip metadata remains intact |

## Acceptance checks
- Root prim: `/BiupiuScene`
- Environment and VehiclePlaceholder remain addressable.
- AnimatedCamera remains present.
- Vehicle translation has frame/time samples at 1 and 48.
- Camera translation has frame/time samples at 1 and 48.
- 24 fps / 48-frame test duration remains consistent.
- No proprietary or production media is embedded in the test fixture.

## Integration notes
OpenUSD is designed for interchange of animated 3D scenes and provides schemas/composition for geometry, shading, lighting and animation. citeturn0search10

Unreal Engine 5.8 documents USD Stage support and USD through Interchange; Epic describes USD asset import through Interchange as production-ready while level import remains experimental in 5.8. citeturn0search0turn0search11

## Execution boundary
This file defines the next runtime test contract. It does **not** claim Blender, Unreal, or an OpenUSD runtime has been executed in this environment.
