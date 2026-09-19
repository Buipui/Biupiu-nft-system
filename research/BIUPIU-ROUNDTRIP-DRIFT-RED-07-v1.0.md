# Biupiu RED-07 — Automated Round-Trip Drift Testing

**Gate:** RED-07  
**Status:** repository contract implemented; live renderer execution gated.

## Objective
Detect asset drift across SOURCE ASSET → PROVIDER → INTERCHANGE → PROVIDER → SOURCE ASSET.

## Drift domains
Geometry, transforms, materials, textures, camera, metadata and provenance are separately reportable. Provider-specific cosmetic render differences are not automatically treated as authoritative asset drift.

## Canonical comparison
Each snapshot carries stable signatures for geometry, transforms, materials, metadata and provenance. The contract compares returned signatures with the authoritative source snapshot. Signature generation from real files/renderers is an execution concern and is not faked by the repository contract.

## Severity policy
- PASS: no signature differences.
- DRIFT: asset differences require review.
- BLOCKED: source identity or provenance changes invalidate the round trip.
- RED-06 unsupported material translations must be represented as material drift/loss, not silently accepted.

## Acceptance criteria
1. Source asset identity and model version remain traceable.
2. Geometry and transform drift is detected.
3. Material and metadata drift is detected.
4. Provenance drift blocks acceptance.
5. Derivatives never replace the authoritative source.
6. Live acceptance requires connected provider hosts and measured outputs with hashes/provenance.

## Execution boundary
Repository tests establish the contract only. Actual Blender/UE5/Redshift/V-Ray/Octane/Lumion/KeyShot round trips remain gated until connected application environments produce measured outputs.
