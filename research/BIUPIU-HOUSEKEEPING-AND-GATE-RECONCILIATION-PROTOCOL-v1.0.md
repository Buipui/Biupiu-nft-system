# Biupiu Housekeeping & Gate Reconciliation Protocol v1.0

**Date:** 19 September 2026  
**Status:** EXECUTED — protocol registered; runtime closure not assumed

## Purpose
Maintain a single, evidence-preserving view of historical execution requests, repository implementations, validation results and unfinished work across Biupiu research, software, simulation, rendering, mobile and production streams.

## Exterminate / housekeeping rules
1. Discover historical `EXECUTE`, `NEXT GATE`, `FIREFLY`, `EXTERMINATE` and `UPDATE INDEX` requests.
2. Reconcile each request against repository evidence, not conversation wording alone.
3. Never equate implementation with validation or completion.
4. Preserve intentional unfinished research and deferred work; do not delete it.
5. Fix only verified accidental defects; record proposed or unverified fixes separately.
6. Record workflow runs, job logs, test output, artifact hashes and host/device evidence before closing runtime gates.
7. Treat missing CI results as `IMPLEMENTED-BUT-UNVERIFIED` or `BLOCKED`, never as PASS.
8. Separate source/research architecture from local runtime, device, physical and production validation.
9. Keep public/declassified and lawful research boundaries; no restricted or weapon-development work.
10. Update the master index and open-gate register after every reconciliation pass.

## Canonical gate states
- `CLOSED/VERIFIED`: implementation, integration and required validation evidence are recorded.
- `IMPLEMENTED-BUT-UNVERIFIED`: repository implementation exists, but required runtime or external evidence is missing.
- `READY/NOT EXECUTED`: test definition and inputs exist, but execution has not occurred.
- `DEFERRED BY DESIGN`: intentionally postponed with rationale and re-entry condition.
- `BLOCKED`: execution prevented by missing host, permission, dependency, data, licence or safety condition.
- `SUPERSEDED/OBSOLETE`: replaced by a newer controlled record; retain historical traceability.

## Required reconciliation sequence
`DISCOVER → IDENTIFY → MAP → CLASSIFY → VERIFY EVIDENCE → PRESERVE OPEN WORK → UPDATE REGISTER → UPDATE INDEX → COMMIT → RECHECK`

## Minimum record fields
Gate ID, source thread/request, repository path, implementation state, validation evidence, dependencies, owner/action, next action, evidence status, last checked date and commit/reference.

## Current known non-closure conditions
Runtime CI, UE5/local rendering, Android/device execution, physical experiments, production identity/database/security deployment and live third-party application execution must remain open or blocked until direct evidence is recorded.
