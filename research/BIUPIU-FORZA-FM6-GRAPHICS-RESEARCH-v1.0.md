# Biupiu Forza Motorsport 6 Graphics Research v1.0

**Gate:** FM6-01
**Date:** 19 September 2026
**Status:** EXECUTED — reference/integration specification

## Purpose
Study publicly available GitHub tooling and documentation around the ForzaTech/Forza Motorsport 6 graphics pipeline to improve Biupiu's original automotive and world-rendering systems.

## Rights boundary
Forza Motorsport 6 assets, extracted proprietary models/textures, encrypted game resources, proprietary shaders, sounds and binaries are **not production dependencies**. This gate captures technical concepts only. Any third-party code or asset must pass its own licence/provenance review before reuse.

## GitHub research targets
- D3FEKT/ForzaTechStudio — FM6/FM7 model/material/scene inspection and conversion research.
- Doliman100/ForzaTech-extraction-tools — FM6-oriented format/import research.
- Doliman100/ForzaTech-crypto-tool — encryption/format research only; no proprietary keys or extracted content are imported.

## Biupiu translation matrix
| FM6/ForzaTech concept | Biupiu implementation target |
|---|---|
| LOD/model structure | Vehicle LOD policy and scalable digital-twin geometry |
| Vertex normals/tangents/UVs | Canonical geometry validation and material handoff |
| Material/shader parameter organization | Provider-neutral automotive material schema |
| Car-paint presentation | Original Biupiu paint/clearcoat material presets |
| Scene/lighting presentation | Automotive studio, road and cinematic lighting presets |
| Vehicle assembly hierarchy | Stable Biupiu vehicle/component asset graph |
| Texture/resource optimization | PBR asset optimisation and render-budget rules |
| Automotive camera/photo presentation | Original Biupiu camera presets and showreel framing |
| Open-world road/environment composition | Modern Japan/automotive world scene system |

## Integration targets
- Unreal Engine 5
- Blender
- Redshift
- V-Ray
- Octane
- Lumion
- KeyShot
- provider-neutral Biupiu render pipeline

## Required validation
1. Validate original Biupiu vehicle geometry through the universal asset manifest.
2. Generate equivalent original materials rather than converting Forza materials directly.
3. Test LOD transitions in Unreal.
4. Compare PBR material appearance across render providers.
5. Record conversion loss, renderer/version, provenance and output hashes.
6. Keep Forza references isolated from production asset directories.

## Result
FM6-01 establishes a rights-clean **Forza graphics research adapter/reference layer**. It improves the automotive rendering specification without importing proprietary Forza production assets.
