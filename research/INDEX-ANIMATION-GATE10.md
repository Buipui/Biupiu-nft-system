# Biupiu Animation Research Index — Gate 10
**Version:** 1.0  
**Date:** 2026-09-19  
**Status:** IMPLEMENTED — CONTROLLED RUNTIME-ARTIFACT REPORT CONTRACT

## Added
- `research/pipeline-tests/GATE10-RUNTIME-ARTIFACT-REPORT.md`
- `research/pipeline-tests/runtime_artifact_report.example.json`

## Gate objective
Define the evidence format required before a Blender, Unreal, OpenUSD, or other DCC runtime export can be recorded as PASS.

## Evidence rule
A repository fixture or example file cannot satisfy runtime evidence. A real artifact must identify the producing application/version/time and carry an explicit comparator result.

## Integration relevance
Unreal Engine's current USD documentation describes USD Stage loading, animation access through Sequencer, and USD write/export workflows, providing a concrete downstream runtime target for this intake contract. citeturn0search0turn0search3

## Next gate
Gate 11: add an automated report generator that consumes comparator output and emits the controlled Gate 10 report without allowing a template to become PASS evidence.
