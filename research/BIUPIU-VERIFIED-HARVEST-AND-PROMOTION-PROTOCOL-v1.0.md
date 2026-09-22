# Biupiu Verified Harvest and Promotion Protocol v1.0

**Date:** 2026-09-22  
**Status:** REGISTERED / IMPLEMENTATION SPECIFICATION  
**Authority:** Biupiu repository governance  

## Objective
Prioritise resources with reproducible evidence and prevent unverified, broken, incompatible or legally unsuitable material from entering authoritative Biupiu systems.

## Mandatory evidence classes
- **VERIFIED-WORKING:** independently executed in the declared environment, with reproducible test evidence, expected output and recorded commit/version.
- **REPOSITORY-VERIFIED-UNTESTED:** cross-linked to an authoritative repository record but not executed in the current environment.
- **CANDIDATE:** discovered resource awaiting repository mapping, licence review and tests.
- **QUARANTINED:** failed, broken, incompatible, insecure, unlicensed for intended use, or otherwise blocked.
- **SUPERSEDED:** replaced by a newer verified version; retained for lineage.

No resource may be marked VERIFIED-WORKING solely because documentation, popularity, a successful import, or an AI assertion exists.

## Harvest pipeline
`DISCOVER -> IDENTIFY VERSION/COMMIT -> REPOSITORY CROSS-LINK -> LICENCE/SECURITY REVIEW -> DEPENDENCY CHECK -> STATIC CHECK -> UNIT TEST -> INTEGRATION TEST -> REGRESSION TEST -> EVIDENCE BUNDLE -> HUMAN PROMOTION -> INDEX/LEARNING UPDATE`

## Promotion rules
1. Prefer an existing Biupiu module when it meets the required contract and has stronger evidence.
2. Compare versions before updating. Update only when the current repository version is outdated, vulnerable, incompatible, or demonstrably inferior under the declared acceptance tests.
3. Never overwrite a working implementation without preserving its previous version, commit, test evidence and rollback path.
4. External code is adapted through interfaces where possible; no unreviewed third-party code is copied into authoritative core systems.
5. Licence, security, privacy, provenance and dependency constraints are promotion gates.
6. Failed resources are quarantined with failure signatures, reproduction steps, affected modules and a remediation owner.
7. A test result is scoped to its environment, version, inputs and date; it is not a universal guarantee of reliability.

## Required evidence bundle
- Resource ID and canonical URL/repository
- Exact version, tag or commit SHA
- Local Biupiu module(s) considered and comparison result
- Runtime, OS, language and dependency versions
- Licence and intended-use classification
- Test commands, fixtures and expected results
- Actual output, logs and failure traces
- Security and dependency findings
- Decision: promote / retain / quarantine / supersede
- Reviewer and timestamp

## Learning-system event schema
Every maintenance action produces a structured event containing:
- `event_id`, `event_type`, `timestamp`
- `resource_id`, `module_id`, `old_version`, `new_version`
- `change_summary`, `bug_signature`, `root_cause` (if established)
- `tests_run`, `tests_passed`, `tests_failed`, `environment`
- `evidence_refs`, `licence_status`, `security_status`
- `promotion_state`, `rollback_ref`, `human_approval`

Learning records preserve lineage. They support retrieval, regression-test generation and conflict detection; they do not imply autonomous training or scientific validation.

## Blockchain anchoring boundary
Only approved hashes/identifiers and non-confidential release metadata may be anchored. Raw source code, secrets, private datasets, unpublished IP and sensitive logs remain off-chain. Anchoring is optional and occurs only after repository verification and human release approval.

## Hard implementation requirements
- Fail closed on missing evidence, unknown licence, unresolved dependency conflict, failed tests or absent rollback reference.
- Separate discovery from promotion.
- Separate test status from trust status.
- Make quarantine reversible and auditable.
- Treat indexes and digests as derived views of authoritative records.
- Require post-change regression checks across linked systems before marking a gate complete.

## Initial integration targets
This protocol cross-links with:
- Federation harvest and adapter records
- Gate-learning architecture and matrix
- Native arcade/runtime verification
- Smart-farming and hardware/OEM harvest registers
- OS/DMS subsystem master index
- Algorithm and blockchain registry layers

**Gate state:** protocol registered; repository-wide runtime execution and external resource verification remain pending until executed in a suitable environment.
