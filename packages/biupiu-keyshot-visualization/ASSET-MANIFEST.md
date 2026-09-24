# Biupiu Visual Asset Manifest

Stage 12 connects visual assets to the material/environment provenance layer.

## Gate
Every renderable asset records identity, source/provenance, geometry validation, material references, environment profile and validation state.

## Controls
- Geometry must be validated before rendering.
- Restricted materials cannot enter a render manifest.
- Material provenance remains authoritative in the Stage 11 registry.
- Source hashes can be recorded for reproducibility.
- The manifest is renderer-neutral and can feed KeyShot, Unreal Engine 5, Twinmotion or future render backends.

No proprietary renderer assets are bundled.
