# Biupiu Render Provenance Test Harness Gate 07 v1.0

## Gate
RENDER-07 — automated provenance and asset-lineage test harness.

## Objective
Define deterministic checks that verify every derivative render/showcase asset remains traceable to an authoritative Biupiu source asset, revision, engine configuration and output checksum.

## Required lineage
SOURCE_ASSET → SOURCE_REVISION → SCENE_ID → ENGINE_ADAPTER → ENGINE_VERSION → CONFIG_ID → OUTPUT_ID → OUTPUT_CHECKSUM

## Automated checks
- Required-field validation.
- Stable source asset and revision identifiers.
- Geometry checksum presence.
- Material/texture provenance presence.
- Engine and adapter version presence.
- Configuration identifier presence.
- Output identifier uniqueness.
- Output checksum presence.
- Timestamp presence.
- Reviewer/status field presence.
- Detection of orphaned showcase outputs.
- Detection of outputs referencing unknown source revisions.
- Detection of duplicate output IDs.
- Detection of missing conversion/failure notes.

## Machine-readable status model
- PASS — evidence is complete and internally consistent.
- FAIL — a required lineage or provenance condition is violated.
- PENDING — the test requires workstation-generated evidence not yet available.
- BLOCKED — required source data or environment is unavailable.

## Test fixtures
Fixture A: complete source-to-output lineage — expected PASS.
Fixture B: missing source revision — expected FAIL.
Fixture C: missing output checksum — expected FAIL.
Fixture D: duplicate output ID — expected FAIL.
Fixture E: unknown source asset — expected FAIL.
Fixture F: workstation render not yet executed — expected PENDING, not PASS.

## Integrity rules
1. Never infer missing provenance.
2. Never generate fake checksums or render measurements.
3. Never treat a visual similarity result as proof of engineering equivalence.
4. Preserve the original source asset and revision.
5. Keep proprietary binaries, licence keys and credentials outside the repository.
6. Record adapter conversion warnings rather than silently normalizing them away.

## Current gate result
RENDER-07 specification and test model: PASS.
Automated execution against real workstation render outputs: PENDING.

## Next gate
RENDER-08 — repository-side provenance schema implementation and fixture validation.