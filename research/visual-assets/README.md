# Biupiu Visual Asset Manifest

This directory defines the provenance-controlled manifest used by the Lumion, Unreal Engine 5, Blender and V-Ray visualization pipeline.

## Files
- `biupiu-visual-asset-manifest.schema.json` — JSON Schema.
- `example-visual-asset.json` — non-production example.

## Design basis
The manifest uses explicit provenance/licence fields and PBR fields aligned conceptually with glTF 2.0's asset metadata and metallic-roughness material model. Khronos glTF defines asset metadata such as generator/copyright and standardized PBR material parameters including base color, metallic and roughness. citeturn0search1turn0search3

## Rule
An asset with `licence.status` other than `verified` cannot be promoted into the approved production asset registry. Engineering/material performance data must remain separate from visual PBR appearance data.
