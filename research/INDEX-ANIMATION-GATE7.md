# Biupiu Animation Research Index — Gate 7
**Version:** 1.0  
**Date:** 2026-09-19  
**Status:** IMPLEMENTED — CI CONTRACT VALIDATION ADDED

## Added
- `.github/workflows/animation-gate7-contract.yml`

## Validation
Gate 7 connects the canonical Gate 6 scene contract to repository CI. The workflow validates the checked-in canonical USDA fixture and the machine-readable JSON contract on pushes, pull requests, and manual dispatch.

The contract deliberately validates structure and authored animation samples rather than claiming a Blender, Unreal, or renderer export. OpenUSD documents TimeSamples as a primary mechanism for animated values and notes their broad interoperability across DCC tools and renderers. citeturn0search1turn0search0

## Runtime boundary
No external DCC runtime pass is claimed by this gate. Export-artifact comparison remains dependent on real Blender/Unreal/OpenUSD-generated artifacts.

## Next gate
Gate 8: add an artifact-ingestion contract for external USD/JSON exports, with explicit provenance and pass/fail reporting.
