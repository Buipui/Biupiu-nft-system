# Biupiu Animation Research Index — Gate 8
**Version:** 1.0  
**Date:** 2026-09-19  
**Status:** IMPLEMENTED — EXPORT ARTIFACT INGESTION CONTRACT

## Added
- `research/pipeline-tests/ingest_export_contract.py`
- `research/pipeline-tests/expected_export_artifact.example.json`

## Purpose
Gate 8 creates the handoff boundary for real Blender, Unreal, OpenUSD, or other DCC-generated artifacts. An exporter/adapter can emit the defined JSON contract, after which the repository comparator checks hierarchy, types, frame range, and authored animation sample coordinates.

OpenUSD's official documentation describes USD as a system for hierarchically organized static and time-sampled scene data and identifies TimeSamples as a broadly interoperable mechanism for animated values. citeturn0search1turn0search0

## Provenance
External artifacts must identify their producing application/version and generation timestamp. The example is deliberately a template and is not presented as runtime evidence.

## Runtime boundary
No external DCC export is claimed as passed. Gate 8 establishes ingestion and comparison infrastructure only.

## Next gate
Gate 9: add CI schema/fixture checks without treating the example artifact as a real external export, then add a controlled runtime-artifact intake path.
