# Biupiu V-Ray Integration

V-Ray is registered as a proprietary professional rendering option in the Biupiu Media/Render OS. This directory contains only verified open-source/reference material from Chaos Group repositories plus Biupiu integration documentation.

## Usable upstream components
- `vendor/chaos/vray_gltf/` — Python glTF 2.0 parsing/rendering reference using the V-Ray App SDK.
- `vendor/chaos/vraymtl_glsl/vraymtl.glsl` — MIT-licensed V-Ray 6 VRayMtl GLSL reference suitable for material/viewport research.
- V-Ray App SDK — connector target for future provider integration; the SDK itself is proprietary/runtime-dependent.

## Biupiu use cases
- Microturbine and blade visualization
- Hemp/bio-composite and resin material studies
- Marine, automotive, helicopter and eVTOL concept visualization
- Digital-twin presentation assets
- Textile/hemp surface studies
- glTF/GLB asset interchange
- Render-pass and compositing workflows

## Evidence boundary
V-Ray output is classified as `VISUALIZATION_ONLY` unless a separate validated engineering simulation establishes evidence. Render appearance must not be treated as proof of structural, aerodynamic, thermal, propulsion or materials performance.

## Licensing boundary
Do not copy proprietary V-Ray binaries, installers, license files or commercial assets into this repository. Upstream files copied here retain their original notices/licenses.
