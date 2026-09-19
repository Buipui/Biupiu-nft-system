# BIUPIU UNIFIED RENDERER ROUTER v1.0

**Gate:** LUM-05 — executed

## Purpose
Route approved visualisation jobs to the appropriate renderer/application while preserving one asset/provenance manifest.

## Routing matrix
| Requirement | Primary route | Secondary route |
|---|---|---|
| Fast architectural/environment presentation | Lumion | Unreal Engine 5 |
| Interactive Digital Twin | Unreal Engine 5 | Blender |
| High-fidelity product/material render | V-Ray | Blender |
| Asset conditioning/PBR inspection | Blender | CAD |
| CAD/BIM live design review | Lumion LiveSync | Native CAD/BIM viewport |
| Cinematic real-time sequence | Unreal Engine 5 | Lumion |
| Engineering geometry authority | CAD/CAE | Blender for visual conditioning only |

## Lumion interoperability
Lumion documents support for DAE, SKP, FBX, DWG, DXF, glTF, 3DS, OBJ and MAX, with LiveSync integrations for SketchUp, Revit, ArchiCAD, Vectorworks, AutoCAD, Rhino, BricsCAD, FormIt and Allplan. citeturn0search0turn0search1
Lumion 2026 documentation also identifies real-time PBR material/settings synchronization through LiveSync for SketchUp and Revit. citeturn0search4

## Routing contract
1. Validate visual asset manifest.
2. Resolve authoritative source model/version.
3. Select renderer using project requirements.
4. Condition geometry/materials only in approved authoring tools.
5. Record renderer/application/version.
6. Render or export.
7. Record output hash and provenance.
8. Never overwrite the authoritative engineering model with presentation output.

## Cross-links
- Lumion → `research/BIUPIU-VISUALIZATION-PIPELINE-LUMION-v1.0.md`
- PBR → `research/BIUPIU-OPEN-ASSET-PBR-COMPATIBILITY-REGISTRY-v1.0.md`
- Asset schema → `research/visual-assets/biupiu-visual-asset-manifest.schema.json`
- Job provenance → `research/visual-assets/VISUALIZATION-JOB-PROVENANCE-v1.0.md`
- Unreal Engine 5 / V-Ray / Blender tracks remain complementary endpoints.

## Safety/quality boundary
Renderer selection affects presentation output, not engineering validity. Physics, CFD, FEA, measured material properties and certification remain outside the renderer layer.

## LUM-05 acceptance
**Executed.** A unified routing contract now connects the Lumion track to the existing visualisation architecture without making Lumion, Unreal, V-Ray or Blender the single source of engineering truth.