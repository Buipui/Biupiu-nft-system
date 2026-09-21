# VIS-NATIVE-18 — CI Evidence Artifact Gate v1.0

## Purpose

Generate host-specific, machine-readable evidence for the seven optional visual providers and retain a human-readable promotion report as a CI artifact.

## Evidence schema

`provider-evidence.json` contains the gate identifier and one record per provider with:

- provider and runtime version marker
- discovery/link/runtime-probe flags
- deterministic and repeat-pass flags
- promotion state
- first and repeated output hashes
- result: `PASS`, `FAIL`, or `SKIPPED`

## Promotion rules

- `PASS`: runtime fixture executes twice and canonical output is byte- and hash-identical.
- `FAIL`: provider is linked but runtime execution or deterministic repeat validation fails.
- `SKIPPED`: optional SDK is unavailable; the native core may still build and test.
- `HOST_READY` and `REGRESSION_PASS` require runtime evidence; compile-time discovery alone is insufficient.
- `VERIFIED` remains reserved for reviewed CI artifacts from the applicable host matrix.

## CI outputs

The workflow builds on Ubuntu and Windows, runs CTest and provider validation, generates evidence, and uploads a host-specific artifact containing:

- `provider-evidence-<host>.json`
- `provider-promotion-report-<host>.md`

## Current status

Source and CI artifact generation are registered. Host execution and promotion remain pending until the workflow produces and is reviewed for the relevant commit.
