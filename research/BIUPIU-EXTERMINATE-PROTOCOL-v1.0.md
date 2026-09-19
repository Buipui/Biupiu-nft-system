# EXTERMINATE PROTOCOL — Repository Hygiene Gate v1.0

Date: 19 September 2026
Scope: SELF-HEAL-01 integration

## Objective
Remove or quarantine avoidable repository hazards without deleting authoritative research, source, provenance or historical records.

## Rules
1. Inspect before deletion; never mass-delete by filename pattern alone.
2. Preserve authoritative source, tests, indexes, provenance and research history.
3. Reject generated caches, credentials, temporary artifacts and accidental build output when discovered.
4. Remove dead imports/code only when static inspection establishes that the removal is behavior-preserving.
5. Do not rewrite learning history to make a failed repair appear successful.
6. Do not weaken tests to make a repair pass.
7. Keep experimental/self-healing code isolated until validation evidence exists.
8. Update the master index whenever a cleanup changes architecture or lifecycle status.
9. Use rollback/branch isolation for destructive cleanup.

## SELF-HEAL-01 audit result
- No generated cache, .pyc, node_modules, build, dist, coverage or log artifacts were found in the repository tree inspected for this gate.
- No duplicate SELF-HEAL-01 implementation was identified.
- The self-healing controller's imports are purposeful; no safe dead-code deletion was identified.
- The learning/provenance module remains authoritative and was not modified by cleanup.
- Static syntax inspection of the self-healing core passed.
- Remote GitHub Actions reported no workflow runs for the integration commit, so CI execution remains unverified.

## Outcome
EXTERMINATE-01: CLEANUP COMPLETE WITHOUT DESTRUCTIVE DELETION.
SELF-HEAL-01 remains isolated on the feature branch pending CI/mainline validation.