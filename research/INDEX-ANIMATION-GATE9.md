# Biupiu Animation Research Index — Gate 9
**Version:** 1.0  
**Date:** 2026-09-19  
**Status:** IMPLEMENTED — CI SCHEMA + STATIC FIXTURE GUARDRAILS

## Added
- `.github/workflows/animation-gate9-artifact.yml`

## Gate objective
Gate 9 makes the export-artifact contract CI-aware without fabricating runtime evidence. CI validates the canonical JSON contracts, the repository USDA fixture, and explicit markers showing that the example export remains a template.

This is aligned with OpenUSD's documented model of hierarchically organized, time-sampled scene data and its API support for querying authored time samples. citeturn0search0turn0search1turn0search4

## Evidence boundary
The example export is **not** used as a passing external runtime artifact. A real Blender/Unreal/OpenUSD export must be supplied separately and must include provenance.

## Next gate
Gate 10: define a controlled artifact intake/report format for real runtime exports and connect the report to the animation research index.
