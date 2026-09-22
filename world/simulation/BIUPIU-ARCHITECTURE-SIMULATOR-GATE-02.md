# Biupiu Architecture Simulator — Gate 02

Status: IMPLEMENTED — repository prototype verification
Date: 2026-09-22

## Gate objective
Connect the architecture simulator to the existing World asset-pipeline contract and add deterministic validation for rights, GIS site state, country filtering and architectural massing.

## Verified against repository
- Existing World Asset Pipeline metadata requirements.
- Existing simulation engine and historical-evidence schema.
- Architecture simulator prototype.
- Architecture federation manifest.

## Smoke-test specification
A valid GREEN asset may enter the production candidate pool.
BLUE/YELLOW/ORANGE/GREY assets remain review/reference candidates.
RED assets are blocked.
A site without CRS is rejected.
Positive footprint, levels and bay dimensions produce deterministic massing.
Country filtering removes assets without matching country tags when country-specific tags exist.
Validation reports missing site or blocked assets.

## Integration contract
Architecture simulator output must preserve:
biupiu_id
version
department
asset_type
evidence_state
provenance
licence_status
source_refs
Digital Twin reference
LOD tier

## Next runtime gate
UE/Blender runtime execution with a real GIS/LiDAR dataset remains OPEN. This cannot be marked verified from repository inspection alone.
