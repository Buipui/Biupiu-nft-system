# BIUPIU LEARNING CHECKPOINT — FEDERATION EXTERNAL HARVEST 2026-09-22

- event_id: FED-HARVEST-20260922-01
- event_type: external_resource_harvest_crosslink
- parent_gate: FEDERATION-EXTERNAL-HARVEST
- prior_state: existing federation contracts F17-F22 + native harvest validator + internal simulation/learning/provenance layers
- change: added current external candidates and explicit internal cross-links without promoting external code
- expected: improve resource discovery while preserving native authority and fail-closed promotion
- observed: candidate/reference set recorded; no runtime promotion performed
- evidence: external repository documentation/search results + internal repository cross-link records
- tests_run: source/registry inspection only
- tests_passed: source-level record consistency
- tests_failed: none asserted; runtime tests not executed
- environment: repository inspection environment
- promotion_state: CANDIDATE / PATTERN-REFERENCE
- regression_scope: federation contracts, harvest gate, DMS/OS boundaries, learning/provenance, World boundary, blockchain boundary
- rollback_ref: git history prior to this checkpoint
- human_approval: REQUIRED before executable promotion
- next_gate: version/commit capture -> licence/IP -> static -> unit -> integration -> regression -> runtime -> human promotion

## Learning principle
This is retrieval/diagnostic learning evidence, not autonomous model training. It improves future search, comparison and preventative-test generation while preserving authoritative state and old/new lineage.
## Follow-up correction
Audit found that the documented harvest pipeline was broader than the native validator's enforced evidence fields and the index did not expose all recent module-testing protocols together. The validator and CI workflow were hardened and the canonical testing registry was added. This is retained as a learning event and regression target.
- correction_class: governance/enforcement mismatch
- affected_modules: federation harvest gate, test harness, CI verification, harvest index/digest
- new evidence: version/dependency/normalisation/integration/rollback gates
- state: SOURCE-CORRECTED / CI-VERIFICATION-OPEN


## Multilingual coding harvest extension — 2026-09-22

Learning event: FED-HARVEST-20260922-MLANG-01

Observed:
- locale identity was previously lossy in the Python normaliser;
- foreign-language engineering sources independently reinforced script/region preservation, deterministic fallback and controlled multilingual evaluation;
- OS language selection belongs at the shared OS contract boundary, not inside individual domain systems.

Corrective learning:
- preserve BCP-47-compatible tags;
- test exact locale -> language family -> default fallback;
- distinguish language selection from translation quality;
- record original-language evidence and provenance;
- classify support level before making language-support claims.

Native changes:
- shared language contract;
- Android selector;
- Windows selector/registry;
- Python translation normalisation/fallback;
- regression tests;
- coding-matrix changelog.

Promotion state:
SOURCE IMPLEMENTED / TESTS ADDED / CI RESULT PENDING / RUNTIME OPEN.

The learning system may reuse these patterns for future multilingual diagnostics and test generation but cannot self-authorise promotion.
