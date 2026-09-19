# Biupiu RED-08 — Multi-Provider Asset Equivalence Matrix

**Gate:** RED-08
**Status:** repository contract implemented; live provider execution gated.

## Objective
Compare the same authoritative source asset across every registered render provider without allowing provider-specific derivatives to redefine engineering truth.

## Provider matrix
BLENDER, MAXON Cinema 4D, Redshift, Unreal Engine 5, Twinmotion, Lumion, KeyShot, Octane, V-Ray, Adobe, Firefly and Runway are registered. A provider may render or transform an asset, but the asset registry remains authoritative.

## Comparison domains
Geometry, transform, material, metadata and provenance are compared. RED-06 conversion/loss reports are the source for known material translation limitations; RED-07 supplies round-trip drift semantics.

## Classification
PASS means no contract-level variance. DRIFT means an asset property differs and requires review. BLOCKED means source identity, model lineage or provenance differs. Cosmetic image differences are not automatically treated as engineering drift.

## Acceptance boundary
Contract tests can prove classification logic. Live equivalence requires connected application hosts, real import/export, deterministic settings, measured outputs, hashes and provenance records. No live provider result is claimed by this repository gate.