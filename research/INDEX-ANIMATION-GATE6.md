# Biupiu Animation Research Index — Gate 6
**Version:** 1.0  
**Date:** 2026-09-19  
**Status:** IMPLEMENTED — CANONICAL CONTRACT + COMPARISON TOOL ADDED

## Added
- `research/pipeline-tests/expected_scene_contract.json`
- `research/pipeline-tests/compare_usda_contract.py`

## Purpose
Gate 6 establishes a machine-readable canonical scene contract so later Blender, Unreal, and renderer exports can be compared against a stable repository reference rather than judged manually.

The contract records the root prim, frame rate/range, expected prim hierarchy, and required animation sample points.

OpenUSD documentation describes USD as supporting hierarchically organized static and time-sampled scene data and interchange between DCC applications. citeturn0search0turn0search3

## Boundary
The comparison tool is a repository-level static comparison. It does not claim that Blender, Unreal, or another DCC has produced a round-trip export.

## Next gate
Gate 7: connect the canonical contract to CI and add export-artifact comparison hooks.
