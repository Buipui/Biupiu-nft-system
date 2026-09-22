# BIUPIU NATIVE CODING PHILOSOPHY & ENGINEERING MATRIX v1.0

Date: 2026-09-22
Status: HARD-CODED GOVERNANCE STANDARD
Scope: All native Biupiu software, AI/ML, simulators, Digital Twin, federation, OS/DMS, Android, web, native C/C++/Rust, Python, TypeScript/JavaScript, Solidity, data schemas, build systems and CI/CD.

## 1. Core philosophy

Biupiu code is engineered, not merely generated.

Every executable change MUST be:
1. traceable to a requirement, defect, research record, experiment or approved maintenance task;
2. deterministic where determinism is technically possible;
3. explicit about assumptions, uncertainty and evidence state;
4. modular, testable and replaceable at defined interfaces;
5. secure by construction and fail-closed at authority boundaries;
6. reproducible from versioned source, dependencies and build instructions;
7. observable through structured logs and machine-readable evidence;
8. regression-tested before promotion;
9. licence/provenance checked before third-party code or models enter an executable path;
10. reversible unless an explicit human-controlled release gate authorizes an irreversible action.

No generated code, harvested code, model output, research text, asset or dependency becomes authoritative merely because it exists.

## 2. Authority hierarchy

AUTHORITATIVE:
- validated source code;
- versioned requirements/contracts;
- passing tests and build evidence;
- signed/versioned release manifests;
- verified measurements and approved datasets.

NON-AUTHORITATIVE UNTIL VALIDATED:
- AI-generated code;
- external repositories;
- papers and research notes;
- simulator outputs;
- model predictions;
- scraped/harvested code;
- third-party assets;
- hypotheses and speculative material.

Learning MAY propose. Intelligence MAY classify and route. Core OS/DMS validation decides. Human/release authority promotes.

## 3. Evidence state

Every material software/research input MUST carry one of:
ESTABLISHED | SUPPORTED | PRELIMINARY | HYPOTHESIS | SPECULATIVE | CONTRADICTED | INCONCLUSIVE

Executable promotion requires the evidence state and provenance to be explicit.

## 4. Universal engineering rules

| Domain | Hard rule | Required evidence |
|---|---|---|
| Requirements | Every significant feature has a requirement/record | requirement ID |
| Architecture | Interfaces and ownership are explicit | architecture record |
| Code | Small, cohesive modules; single responsibility | review/static checks |
| Types | Prefer explicit types and validated schemas | type/build result |
| Errors | No silent exception swallowing; fail closed at trust boundaries | negative tests |
| Security | Secrets never committed; least privilege; input validation | security checks |
| Dependencies | Pin/record versions; licence/security review | dependency manifest |
| Testing | Unit + integration + regression appropriate to risk | test report |
| Static analysis | Lint/type/static analysis where supported | CI artifact |
| Reproducibility | Build/test from clean checkout | CI result |
| Observability | Structured event IDs and provenance | log/evidence record |
| Release | Version + changelog + source commit + hashes | release manifest |
| Rollback | Known-good baseline retained | rollback record |
| Documentation | Code and contracts remain synchronized | documentation check |

## 5. Language matrix

### Python
- Type hints for public APIs.
- Standard-library deterministic core where practical.
- pytest for tests.
- Explicit validation at boundaries.
- No hidden global state.
- Numerical code declares units, tolerances and domains.
- ML code records model/data/version lineage.

### TypeScript / JavaScript
- Strict TypeScript for new typed modules.
- No implicit any in authoritative modules.
- Runtime validation at external boundaries.
- npm lockfile and reproducible installs.
- Unit/integration tests for contracts and adapters.

### C
- Reserved for stable ABI/HAL and low-level interoperability.
- Explicit ownership/lifetime/error conventions.
- No undefined behaviour accepted at validated boundaries.
- C ABI is the durable cross-language boundary.

### C++
- Used for high-performance simulation, geometry, graphics and scientific subsystems.
- RAII/resource ownership.
- No C++ STL/ABI objects across durable ABI boundaries.
- Explicit serialization and versioned interfaces.

### Rust
- Preferred for new memory/concurrency/security-sensitive native services where practical.
- Explicit Result/error handling.
- Safe code by default; unsafe blocks require documented justification and tests.
- C ABI for durable interoperability.

### Kotlin/Android
- Lifecycle-safe components.
- Explicit coroutine/thread ownership.
- UI separated from domain/data layers.
- Build reproducibility and unit tests required before Android release claims.
- Device/runtime verification remains distinct from source/CI verification.

### Solidity
- Minimal privileged surface.
- Explicit access control.
- Tests for invariants and failure paths.
- Dependency/licence/version review.
- Never treat local compilation as deployment verification.

## 6. Architecture boundaries

Canonical flow:

Research/Input
-> Evidence Classification
-> Biupiu Intelligence
-> AI/ML proposal
-> Core OS/DMS validation
-> Digital Twin
-> Federation envelope
-> Simulator/adapter
-> Test/verification
-> Learning log
-> Regression gate
-> Human/release approval
-> Versioned promotion

AI MUST NOT:
- rewrite authoritative OS code autonomously;
- bypass validation;
- promote third-party code;
- silently alter historical records;
- convert uncertainty into fact.

## 7. Federation rules

Federation is a coordination layer, not an authority bypass.

Every federated message SHOULD carry:
event_id, source, target, schema_version, source_commit, timestamp, evidence_state, provenance_refs, model_version, confidence/uncertainty where relevant, validation_state, correlation_id.

Unknown schema/version -> reject or quarantine.
Invalid provenance -> reject/quarantine.
Untrusted executable dependency -> block promotion.
Conflicting authoritative state -> preserve both records and open a reconciliation gate.

## 8. Learning rules

Learning is append-only evidence first.

The learning system MUST preserve:
- input;
- prior state/version;
- observed outcome;
- expected outcome;
- error/residual;
- uncertainty;
- failure class;
- changed components;
- regression result;
- model/algorithm version;
- provenance hash;
- next action;
- promotion decision.

Adaptation is bounded and reference-anchored.
Drift triggers monitoring/review/rollback according to risk.
Repeated failure becomes a reusable pattern only after a verified fix and passing regression evidence.
A model may propose a preventative test; the test must pass before it becomes a release gate.

## 9. ML/AI engineering matrix

Every model/algorithm MUST track:
data version | feature/schema version | model version | code commit | hyperparameters/config | training/evaluation method | metrics | uncertainty/limitations | licence/provenance | deployment target | rollback baseline.

Required lifecycle:
INGEST -> VALIDATE DATA -> TRAIN/ADAPT -> TEST -> EVALUATE -> DRIFT CHECK -> PACKAGE -> SECURITY/LICENCE CHECK -> RELEASE GATE -> MONITOR -> LEARN.

For non-deterministic systems, tests MUST use statistical/tolerance-based or property-based assertions where exact equality is inappropriate.

## 10. Simulator rules

Simulation output is a model result, not physical truth.

Each simulator records:
model version, assumptions, units, parameters, input provenance, numerical tolerances, solver/backend, source commit and verification state.

Safety/engineering simulators MUST distinguish:
SCREENING | MODEL VALIDATION | CORRELATED | PHYSICAL VALIDATION | CERTIFIED

No screening result may be presented as certification.

## 11. Third-party harvest rules

External research/code may be harvested into Intelligence as:
REFERENCE | PATTERN | ADAPTER | ASSET | DEPENDENCY | PROHIBITED

Promotion to executable code requires:
licence verification + provenance + security review + compatibility/build + deterministic/regression tests + human approval.

Do not copy restricted, classified, credentialed, proprietary or unauthorized material.

## 12. Clean-code and housekeeping rules

Exterminate:
- dead code;
- duplicate implementations;
- unreachable branches;
- obsolete APIs;
- stale build artifacts;
- secret material;
- untracked generated binaries;
- contradictory documentation;
- unversioned dependencies;
- silent error paths;
- test bypasses.

But deletion is never automatic when lineage/IP/research value is uncertain. Quarantine and classify first.

## 13. Verification ladder

L0 syntax/import/schema validation
L1 unit tests
L2 integration/contract tests
L3 static analysis/type/lint/security checks
L4 clean-build verification
L5 smoke test
L6 regression suite
L7 cross-platform/runtime verification
L8 hardware/device/physical correlation
L9 release verification

A higher gate cannot be claimed from a lower gate.

## 14. Required CI gate

Every authoritative build SHOULD execute, as applicable:
- source checkout;
- dependency installation from lock/version manifests;
- syntax/type/static checks;
- unit tests;
- integration tests;
- security/secret checks;
- licence/provenance checks;
- build/package;
- smoke test;
- regression suite;
- evidence/log publication.

## 15. Change-control rule

A change is not complete until:
IMPLEMENTED -> BUILT -> TESTED -> REGRESSION-PASSED -> LOGGED -> VERIFIED -> PROMOTED

If any stage is missing, status remains OPEN or PARTIALLY VERIFIED.

## 16. Current Biupiu implementation mapping

Core OS: software/rnd-os/
AI: software/rnd-os-ai/
Mobile: software/rnd-os-mobile/
Web: software/rnd-os-web/
Native simulation: core/multilang/, packages/, simulators/
Digital Twin/federation: research/ + software/rnd-os-ai/
Learning: software/rnd-os-ai/src/biupiu_ai/learning.py
Continual adaptation: software/rnd-os-ai/src/biupiu_ai/ml/continual_adaptation.py
Promotion: software/rnd-os-ai/src/biupiu_ai/promotion_router.py
Simulator adapters: software/rnd-os-ai/src/simulator_adapters.py

## 17. External engineering cross-reference adopted

The matrix incorporates compatible principles from NASA software engineering requirements/assurance: requirements traceability, coding-standard verification, static analysis, unit testing, version descriptions, bidirectional traceability, formal testing and independent verification concepts.

It also incorporates research themes found in MIT software engineering/ML testing work, DARPA assured-autonomy and neuro-symbolic assurance work, ResearchGate literature on software engineering for ML and ML testing, Emerald software-engineering research, open-access computer-science texts, and public GitHub MLOps/testing patterns.

These sources inform Biupiu engineering; they do not become Biupiu authority.

## 18. Hard rule

NO CODE IS TRUSTED BECAUSE IT IS GENERATED.
NO MODULE IS TRUSTED BECAUSE IT IS POPULAR.
NO MODEL IS TRUSTED BECAUSE IT IS ACCURATE ON ONE DATASET.
NO RESEARCH IS TRUSTED BECAUSE IT IS PUBLISHED.
NO BUILD IS VERIFIED BECAUSE SOURCE EXISTS.

Trust is earned by:
TRACEABILITY + PROVENANCE + TESTING + SECURITY + REPRODUCIBILITY + REGRESSION + OBSERVABILITY + APPROPRIATE HUMAN RELEASE CONTROL.

Status: HARD-CODED GOVERNANCE STANDARD v1.0
