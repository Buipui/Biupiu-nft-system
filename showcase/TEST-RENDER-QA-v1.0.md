# Biupiu Test Render QA v1.0
Gate 07 validates actual Blender execution.
- Four registered frames must exist and open correctly.
- Scene fingerprint must match executed metadata.
- Asset IDs, provenance and licence records must exist.
- Evidence state and claim class must be preserved.
- Placeholder geometry must not be presented as verified product.
- Camera, geometry, materials and lighting require visual inspection.
- Unsupported engineering claims must be absent.
Failed frames remain RENDER_FAILED and are not released.
Default release state: HOLD_UNTIL_QA.