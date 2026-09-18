# BIUPIU OPEN-ASSET + PBR COMPATIBILITY REGISTRY v1.0

**Gate:** LUM-02 — executed
**Date:** 18 September 2026
**Purpose:** controlled discovery registry for legitimate open assets and PBR material resources feeding Lumion, Unreal Engine 5, Blender, V-Ray and the Biupiu Digital Twin.

## Approved discovery classes

| Resource | GitHub / source | Licence status | Biupiu use |
|---|---|---|---|
| Poly Haven | https://polyhaven.com/ | CC0 | HDRIs, PBR textures, models, environments |
| AmbientCG | https://ambientcg.com/ | CC0 source library; verify current asset terms at ingestion | PBR materials/textures |
| texturedesign/materials-dataset | https://github.com/texturedesign/materials-dataset | Repository licence/source terms require review | PBR/SVBRDF dataset generation and research |
| dcc-mcp/dcc-asset-polyhaven | https://github.com/dcc-mcp/dcc-asset-polyhaven | Review repository licence/dependencies before deployment | Poly Haven discovery/download automation reference |
| Papyszoo/CC0-Public-Domain-Textures | https://github.com/Papyszoo/CC0-Public-Domain-Textures | Repository states CC0; verify upstream provenance at ingestion | PBR catalog/reference |

## Compatibility policy
- Lumion: presentation/real-time visualization endpoint.
- Unreal Engine 5: interactive Digital Twin/world endpoint.
- Blender: asset conditioning, UV/material inspection and conversion.
- V-Ray: high-fidelity rendering endpoint.
- CAD/CAE: authoritative engineering geometry/model source.
- R&D OS Materials Genome: authoritative research/material provenance source.

## Ingestion gate
Every asset entering a Biupiu project must receive: source URL, repository URL where applicable, creator, licence, asset ID, download date, file format, resolution, PBR map inventory, transformation history and project usage.

Do not commit third-party bulk asset libraries to the Biupiu repository unless there is a specific need and the licence permits redistribution. Prefer manifests and source references for large external libraries.

## PBR minimum record
`Base Color/Albedo`, `Normal`, `Roughness`, `Metallic` where applicable, `Height/Displacement` where available, `AO` where available, colour-space metadata, UV scale and real-world scale.

## Biupiu material research boundary
Visual PBR appearance is not a substitute for measured material properties. Material Genome records must distinguish visualisation parameters from mechanical, thermal, chemical, optical or durability data.

## Current GitHub findings
- `texturedesign/materials-dataset` is useful as a research/dataset-generation reference; its README describes AmbientCG and Poly Haven as supported CC0 sources.
- `Papyszoo/CC0-Public-Domain-Textures` provides a large PBR catalog with provenance metadata and states CC0 licensing.
- `dcc-mcp/dcc-asset-polyhaven` provides an automation reference for discovering/downloading Poly Haven assets and returning provenance information.
- Search results for Lumion-specific GitHub repositories remain sparse; therefore Biupiu will not treat arbitrary Lumion asset repositories as approved merely because they contain downloadable files.

## LUM-02 acceptance
**Executed.** The Biupiu repository now has a controlled open-asset/PBR compatibility registry. External assets are discovery inputs, not automatically imported assets. Licence and provenance checks precede project use.

## Next gate
`LUM-03` — create the machine-readable asset/material manifest schema and connect it to the R&D OS Materials Genome, Digital Twin and media-job provenance systems.