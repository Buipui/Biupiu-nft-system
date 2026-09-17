# Biupiu R&D OS — CI Verification

## Purpose

Record the repository-side verification boundary for the R&D OS continuous-integration gate.

## Current state

- Root GitHub Actions workflow: `.github/workflows/rnd-os-ci.yml`
- Node target: 20
- R&D OS working directory: `software/rnd-os`
- Test command: `npm test`
- npm lockfile: present
- PostgreSQL runtime: not claimed live or integrated in CI
- Production security: not claimed verified

## Verification rule

A CI gate may only be marked **PASSED** when GitHub reports an actual workflow run for the relevant commit and the test job completes successfully.

Absence of a workflow run is **NOT VERIFIED**, not PASS.

## Next gate

After a recognised workflow run exists:

1. Inspect workflow result.
2. Inspect individual job result.
3. If failed, inspect logs and patch the smallest necessary defect.
4. Re-run CI.
5. Only then close the software-test gate.
6. Proceed to PostgreSQL integration verification separately.

## Status

**CI verification: TRIGGERED VIA PULL REQUEST**

No production, security-certification, regulatory-LIMS, or PostgreSQL-live claim is made by this document.
