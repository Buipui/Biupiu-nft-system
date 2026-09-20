# Biupiu Learning Algorithm Update — 2026-09-20

**Status:** VERIFIED — dedicated CI learning-core gate passed.

## Objective
Strengthen the original Biupiu development objective: continuously research new technologies, distinguish usable from non-usable inputs, preserve cross-platform architecture, learn from breakage, and prevent clean-state maintenance from destroying useful lineage.

## Deep/foreign research integration rule
Foreign-language and external research is treated as discovery/evidence input, not automatic implementation authority. Each candidate follows:
RESEARCH → TRANSLATE/INTERPRET → SOURCE/PROVENANCE → COMPATIBILITY → LICENCE/SECURITY → STATIC TEST → CONTRACT TEST → CROSS-PLATFORM REGRESSION → SIMULATION/RUNTIME → HUMAN PROMOTION.

Machine translation is not scientific validation.

## Learning algorithm
The deterministic learning substrate now adds:
- stable failure fingerprints;
- failure-class taxonomy;
- repeated-failure/stalled-loop detection;
- fix and cross-regression learning levels L0–L4;
- incremental EWMA error-drift detection;
- bounded candidate scoring using information gain, uncertainty reduction, model disagreement, feasibility and regression safety;
- explicit promotion checks for provenance, licence and human approval.

## Safety boundary
Learning records are evidence and decision-support. They do not silently rewrite authoritative OS code, safety policy, release controls or production state. External code remains reference/dependency candidate until licence, security, compatibility and regression checks pass.

## Architecture propagation
The learning layer remains upstream of:
- Biupiu Intelligence evidence/retrieval and research routing;
- Biupiu Core OS authority, validation and compatibility gates;
- Biupiu AI/ML routing and model evaluation;
- DMS / Digital Twin / simulator failure records;
- repository housekeeping, index synchronization and regression evidence.

## Verification state
The learning source and test files are registered on `main`:
- `software/rnd-os-ai/src/biupiu_ai/learning.py`
- `software/rnd-os-ai/tests/test_learning.py`
- `.github/workflows/learning-core-tests.yml`

The dedicated learning CI run `35537554602` completed successfully. CI-level learning verification is **VERIFIED**. Broader cross-platform/runtime and production integration remain separate gates.


## Verification result
Dedicated GitHub Actions run `35537554602` completed with conclusion `success` for commit `562937df342980fc490c7bc048d998bf5c6becb3`. The learning test suite passed. This establishes the learning-core implementation as **VERIFIED at CI test level**; broader cross-platform/runtime and production integration remain separate gates.