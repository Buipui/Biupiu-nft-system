# BIUPIU NATIVE CODING PHILOSOPHY & ENGINEERING MATRIX v1.1

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
\n## 19. Digital Orchestra governance extension — 22 September 2026\n\nThe Digital Orchestra is registered as a separate but interlinked coordination subsystem. It does not replace the Native Coding Philosophy & Engineering Matrix; it operationalises its gates for workflow routing, provenance, filing, verification and resumable execution.\n\nOrchestra-specific hard rules:\n- smallest useful workflow first;\n- scope and authority locked before execution;\n- capability discovery precedes routing;\n- orchestration logic remains separate from domain/business logic;\n- external-language harvest retains original source metadata and does not grant authority;\n- workflow state and evidence are durable and resumable;\n- parallel execution is permitted only where dependency analysis allows it;\n- execution history, correlation IDs and provenance are retained;\n- real-surface verification is required before promotion;\n- failed or conflicting material is quarantined rather than silently discarded.\n\nCanonical records:\n- software/digital-orchestra/\n- research/BIUPIU-DIGITAL-ORCHESTRA-ARCHITECTURE-v1.0.md\n- research/BIUPIU-DIGITAL-FILING-SYSTEM-v1.0.md\n- research/BIUPIU-FOREIGN-CODING-PHILOSOPHY-HARVEST-v1.0.md\n- research/BIUPIU-ORCHESTRATION-MATRIX-LINK-v1.0.md\n\nStatus: ORCHESTRATION SOURCE INTEGRATED / HOST RUNTIME AND CI VERIFICATION PENDING.\n
## Digital Filing + Hierarchy Preservation Extension — 22 September 2026
Digital Filing Cabinet is a separate native subsystem. It owns catalogue/filing metadata only. Digital Orchestra owns coordination; Intelligence owns discovery/proposals; OS/DMS and each domain system retain their own execution authority.
Digital Twin may compose subsystems into other subsystem contexts, but must preserve canonical owner, canonical parent and subsystem path. Federation links and diagnoses systems without merging their identities or authorities.
Federated fault/healing must diagnose across boundaries while returning execution to the canonical owning system.
Status: SOURCE INTEGRATED / RUNTIME VERIFICATION PENDING.


## 20. Federation semantic-code gate — 22 September 2026

A Federation semantic coding pass cross-referenced the native engineering matrix against the active federation/AI code paths:
- `software/rnd-os-ai/src/biupiu_ai/federation_protocol.py`
- `software/rnd-os-ai/src/biupiu_ai/federation_registry.py`
- `software/rnd-os-ai/src/biupiu_ai/learning.py`
- `software/rnd-os-ai/src/biupiu_ai/promotion_router.py`
- `software/rnd-os-ai/src/simulator_adapters.py`
- corresponding federation, learning, promotion and simulator tests.

Semantic findings and fixes:
1. Federation gate evaluation was made explicitly typed at the mapping/sequence boundary and documented as deterministic fail-closed behaviour.
2. Federation readiness now has an explicit sequence/mapping contract rather than relying on untyped inputs.
3. Registry activation semantics were clarified with explicit boolean defaults and documentation; blocked systems remain unconditionally ineligible.
4. Native ML learning-promotion semantics were clarified and formatted as an explicit bounded gate requiring reusable-pattern evidence, verified provenance, licence checking and human approval.
5. Existing promotion routing remains proposal-only; Digital Twin eligibility does not transfer execution authority.
6. Simulator adapters remain probe-only until explicitly invoked and reject unsafe argument forms; missing backends remain non-executable.
7. The stale federation test expectation discovered during the prior pass was replaced with an authoritative registry-derived assertion.
8. A cross-system federation AI smoke test now connects registry -> promotion -> learning -> federation readiness -> simulator safety.

Matrix cross-reference:
- Python public APIs: explicit type annotations added at federation boundaries.
- Errors: fail-closed behaviour retained and made clearer.
- Testing: semantic regression coverage added.
- Observability/evidence: federation and learning remain evidence-gated.
- Learning: promotion remains append-only/evidence-first and human-controlled.
- Architecture: federation coordinates but does not bypass canonical authority.
- Verification ladder: source cleanup does not elevate CI/runtime/HIL status.

Status: SEMANTIC CODE CLEANUP IMPLEMENTED / SOURCE CROSS-LINKED / RUNTIME VERIFICATION PENDING.


## 21. Modern multilingual/native engineering extension — 22 September 2026

Foreign-language federation harvest was reconciled against the native matrix. Compatible principles from Unicode CLDR/UTS #35, FLORES/NLLB evaluation practice, i18next fallback design and multilingual Kotlin/Android implementations were adopted as engineering patterns, not as Biupiu authority.

### New hard rules
- Locale identity MUST preserve language plus applicable script and region subtags.
- BCP-47-compatible tags are the canonical exchange form for user-selected locales.
- Locale selection, translation content, formatting data and language evidence are separate concerns.
- Fallback MUST be deterministic, ordered and observable.
- Translation MUST NOT alter evidence state or provenance.
- Language support claims MUST declare the actual support level: display, input, selection, minimal i18n, full i18n, UI or advanced.
- Multilingual tests MUST include script, region, RTL/complex-script and fallback cases where applicable.
- Foreign-language source discovery MUST retain original terminology and source metadata.
- External multilingual code remains reference/candidate material until licence, dependency, security, build, integration and regression gates pass.

### Native mapping
- Shared language contract: apps/shared/runtime/BIUPIU-LANGUAGE-CONTRACT-v1.json
- Native selector: apps/shared/runtime/LanguageSelector.kt
- Selector tests: apps/shared/runtime/LanguageSelectorTest.kt
- Android UI integration: apps/android/app/src/main/java/com/biupiu/rndos/BiupiuShell.kt
- Windows locale registry: apps/windows/BiupiuLanguageRegistry.cs
- Windows UI integration: apps/windows/MainWindow.xaml + MainWindow.xaml.cs
- Intelligence translation: software/rnd-os-ai/src/biupiu_ai/global_language_translation.py
- Intelligence tests: software/rnd-os-ai/tests/test_global_language_translation.py
- Smart Farming cross-link: smart-farming/README.md
- Harvest record: research/BIUPIU-FOREIGN-LANGUAGE-CODING-PHILOSOPHY-HARVEST-20260922.md

### Verification interpretation
Source-level semantic verification: PASS.
Native unit-test coverage added: IMPLEMENTED.
CI execution: OPEN until observed.
Android/Windows runtime UI verification: OPEN.
Full multilingual translation quality: OPEN and requires controlled evaluation data plus human/linguistic validation.

### Engineering principle
**DIGITAL-FIRST, NATIVE-FIRST, EVIDENCE-FIRST, LANGUAGE-NEUTRAL AUTHORITY.**
External languages expand discovery; they do not change ownership, authority or evidence state.


## 22. Federation guided fault-finding and bug-fix matrix — 22 September 2026

The Federation-led diagnostic pass extends the matrix with a deterministic fault-fix boundary. Internal repository modules are searched and reconciled before external harvest. External material is reference-only unless all existing provenance, licence, security, build, regression, runtime and human-promotion gates pass.

### Diagnostic contract
OBSERVE -> CLASSIFY -> OWNERSHIP -> GUIDED EVIDENCE -> ISOLATE -> REPAIR PROPOSAL -> INDEPENDENT VALIDATION -> REGRESSION -> LEARNING RECORD -> CONTROLLED REUSE.

### Fault-fix matrix
| Fault class | Diagnostic focus | Repair boundary | Verification |
|---|---|---|---|
| TRANSPORT | delivery, TTL, backpressure | routing/queue policy | replay delivery path + regression |
| DEPENDENCY | version/lock state | compatible pinned version or quarantine | clean build + dependency regression |
| CONTRACT | schema/version/content-type | boundary contract only | compatibility regression |
| VALIDATION | captured failing inputs | smallest validated logic fix | unit + regression |
| AUTHORITY | canonical owner/conflict | reconcile through owner | authority regression |
| MODEL | assumptions/units/version | explicit model/config correction | numerical regression |
| DATA | provenance/schema/range/unit | quarantine or boundary repair | data-contract regression |
| RUNTIME | trace/environment | reversible runtime fix | smoke + regression |
| SECURITY | integrity/quarantine | security review only | security regression + human release |

Unknown fault classes fail closed. Security faults remain quarantined. No diagnostic result itself grants execution authority.

### External multilingual engineering patterns
NASA IV&V contributes objective-evidence, traceability and off-nominal verification principles; Japanese FMEA/IEC 60812 material contributes structured failure-mode/effect analysis; Unicode CLDR/BCP 47 contributes canonical locale validation and deterministic language matching/fallback. Public diagnostic/self-healing repositories are pattern references only.

### Native ML integration
Failure fingerprints, verified-fix state, regression state, platform/version context and evidence references are learning inputs. A repeated failure becomes reusable only after the existing learning-level, provenance, licence and human-promotion requirements pass. Preventative tests remain proposed until independently passing.

Status: IMPLEMENTED / SOURCE-CROSS-LINKED / CI-RUNTIME VERIFICATION PENDING.


## 23. Blockchain-anchor, Digital Twin and semantic-code extension — 22 September 2026

Deep federation harvest identified a missing explicit machine-checkable boundary between deterministic learning/trust checkpoints and external blockchain anchoring. The native boundary is now represented by intelligence/BIUPIU-BLOCKCHAIN-ANCHOR-BOUNDARY.py.

Hard rules:
- Blockchain is an integrity/provenance anchor, not the Digital Twin state authority and not the AI learning engine.
- Checkpoint payloads remain off-chain by default; the anchor carries a deterministic checkpoint root plus reference metadata.
- CANDIDATE, SUBMITTED, and INCLUDED are not equivalent to verified finality.
- VERIFIED requires both a transaction reference and inclusion proof.
- No private keys, wallets, credentials or signing secrets enter repository records.
- Anchor failure/quarantine never invalidates the underlying append-only learning evidence; it creates a new diagnostic event.
- Real chain execution is a separate runtime gate and must not be inferred from deterministic local hashing.

### Deep external harvest incorporated as reference patterns
- Sigstore/Rekor: append-only transparency logging, inclusion verification and cryptographic auditability. citeturn0search3turn0search4
- SLSA: verifiable build provenance linking artifacts to production process. citeturn0search16
- Blockchain/Digital Twin literature: provenance, lifecycle traceability, cross-validation and fault diagnosis are recurring integration concerns; blockchain should not replace the twin or evidence model. citeturn1search7turn0search0turn1search1
- AI lifecycle provenance research: Merkle-style provenance structures can connect datasets, features, models, metrics and human approvals while keeping policy evaluation off-chain. citeturn1search9
- Multilingual harvest included Japanese-language assurance/provenance material and Korean-language 2026 digital-twin/blockchain security research; these were retained as reference patterns only. citeturn1search5turn1search1

### Native semantic-code gate
intelligence/BIUPIU-NATIVE-SEMANTIC-CODE-AUDIT.py checks that key native AI, learning/federation, OS federation-contract, blockchain-anchor and guided-fault modules expose the semantic controls they claim. This is a source-level semantic audit, not runtime certification.

### Internal optimisation harvest
Existing native optimisation assets are cross-linked rather than duplicated: ML engine capability routing, continual adaptation, math optimisation, simulator adapters, failure learning, federation registry, AI-74 trust/checkpoint logic, rendering/resource optimisation and the research optimization registries. External optimisation engines remain adapter/reference candidates until licence, provenance, security, build, smoke and regression gates pass.

Status: SOURCE IMPLEMENTED / SEMANTIC AUDIT IMPLEMENTED / EXTERNAL HARVEST REGISTERED / LIVE BLOCKCHAIN EXECUTION AND FULL RUNTIME VERIFICATION OPEN.

## 23. Usable adapter federation + Native ML optimisation — 22 September 2026

Internal-first adapter discovery was completed before external federation harvest.

Native adapter registry:
- `software/rnd-os-ai/src/biupiu_ai/adapter_registry.py`
- `software/rnd-os-ai/tests/test_adapter_registry.py`
- `software/rnd-os-ai/src/biupiu_ai/federation_registry.py`

Current adapter families normalised into one contract include MQTT 5, Eclipse Ditto, OPC UA PubSub, ROS 2/DDS, OpenUSD, FMI/FMU, Flower, NVIDIA FLARE, OpenTelemetry, A2A, OpenSharing and AUTOSAR CAPI.

Hard rule: adapter presence is never equivalent to executable verification. Promotion requires provenance, licence, security, build, regression, runtime and human evidence.

Native ML upgrade:
- `LearningEvidence` captures verified-fix, regression-safety, provenance-quality, uncertainty-reduction, recurrence and drift.
- `score_governed_learning_candidate()` provides deterministic bounded candidate prioritisation.
- `learning_reuse_ready()` keeps reusable learning behind the existing Core OS/human promotion boundary.
- Drift is treated as a penalty/review signal rather than an authority bypass.

Semantic check requirements:
adapter identity -> capability/family routing -> evidence gates -> learning scoring -> drift handling -> human promotion -> regression.

Status: IMPLEMENTED / SOURCE CROSS-LINKED / TESTS ADDED / RUNTIME VERIFICATION PENDING.


## 24. Multilanguage coding and semantic equivalence extension — 22 September 2026

The native matrix now has a dedicated language-neutral extension: `research/BIUPIU-MULTILANGUAGE-NATIVE-CODING-MATRIX-v1.0.md`.

Hard rule: language syntax may differ; contract semantics, authority boundaries, evidence states, provenance, failure classes and verification meaning MUST remain equivalent.

Canonical sequence:
SEMANTIC CONTRACT -> LANGUAGE ADAPTER -> LANGUAGE-NATIVE TEST -> CROSS-LANGUAGE FIXTURE -> FEDERATION REGRESSION.

Durable cross-language boundaries use versioned schemas, stable IDs, explicit states, hashes, timestamps, BCP-47 locale identity, units, provenance references and correlation/trace identifiers. Language-specific object layouts do not cross durable boundaries.

The matrix now explicitly covers Python, TypeScript, JavaScript, C, C++, Rust, Kotlin, C#, Solidity, JSON/YAML/schema and CI/shell automation. External language guidance remains reference/pattern material until Biupiu-side validation.

## 25. AI coding hard-implementation gate — 22 September 2026

Every AI coding request MUST be evaluated against `intelligence/BIUPIU-AI-CODING-HARD-GATE-v1.0.json` and `intelligence/BIUPIU-AI-CODING-HARD-GATE.py` before generated/assisted code is treated as implementation.

REQUIREMENT -> OWNER -> LANGUAGE -> CONTRACT -> PROVENANCE -> SECURITY -> DEPENDENCIES -> SEMANTIC_AUDIT -> LANGUAGE_TEST -> CROSS_LANGUAGE_TEST -> REGRESSION -> ROLLBACK -> PROMOTION.

Missing requirement, owner, contract, provenance or test evidence keeps the change non-authoritative. Security or semantic failure blocks the path. Unknown languages are quarantined until a language rule exists. Runtime verification is never inferred from source inspection.

This is an AI control boundary, not a prompt suggestion: it is machine-readable, executable and CI-testable.

## 26. Native-code cleanup and federation implementation rule — 22 September 2026

Native cleanup is now governed as a semantic migration rather than a cosmetic rewrite:
DETECT -> CLASSIFY -> CROSS-REFERENCE OLD WORK -> PRESERVE LINEAGE -> SMALLEST REPAIR -> LANGUAGE TEST -> CROSS-LANGUAGE TEST -> REGRESSION -> LEARNING RECORD -> PROMOTION.

Duplicate code is consolidated only when canonical ownership is unambiguous. Historical/research lineage is retained or quarantined. External code is never merged merely to make a native subsystem look modern.

Federation harvest must compare existing internal capability before adding an external module. If the internal implementation already satisfies the contract, the external resource remains a reference/benchmark. If a gap exists, add the smallest adapter/contract needed and retain the external version, licence and provenance metadata.

## 27. ML learning-algorithm governance extension — 22 September 2026

Native ML learning now treats coding quality and semantic verification as evidence inputs rather than separate documentation.

For reusable coding/repair patterns, learning evidence MUST include:
- coding-matrix version;
- language/runtime version;
- source commit and changed-component identity;
- semantic-audit result;
- language-native test result;
- cross-language contract result where applicable;
- regression result;
- provenance/licence/security state;
- rollback baseline;
- residual error/uncertainty;
- promotion decision.

A learning pattern is reusable only when the verified-fix, regression, provenance, licence and human/OS promotion gates pass. Learning can propose a coding improvement or preventative test; it cannot promote the implementation itself.

## 28. Observability and semantic naming extension — 22 September 2026

Cross-system diagnostics MUST use stable semantic names for events, states, errors, operations and resources. OpenTelemetry's semantic-convention model is adopted as a reference pattern because common naming improves correlation and consumption across codebases and platforms; Biupiu retains its own native contract authority. citeturn0search0turn0search4

Minimum diagnostic identity:
event_id | operation | component | state | error_type | trace/correlation_id | source_version | provenance_ref | evidence_state.

Language implementations may map these fields idiomatically, but the federation meaning must remain stable.

## 29. External coding-philosophy federation harvest — 22 September 2026

The latest external harvest was reconciled with older Biupiu work instead of replacing it. NASA coding-standard guidance supports explicit structure, error handling, module sizing, library use, types, naming and automated adherence verification; this is now mapped into the universal engineering matrix. citeturn0search12turn0search16

OpenTelemetry cross-language semantic conventions support common operation/data naming and language-specific implementations under a shared specification. citeturn0search0turn0search7

These are external engineering references, not Biupiu authorities. Conflicting practices are preserved as provenance-linked candidates and resolved through the native contract, tests and regression evidence.

## 30. Repository-wide hard implementation status — 22 September 2026

Governance layer: IMPLEMENTED.
Multilanguage coding matrix: IMPLEMENTED.
AI coding hard gate: IMPLEMENTED SOURCE + MACHINE-CHECKABLE MANIFEST.
Semantic audit: IMPLEMENTED SOURCE-LEVEL.
ML learning cross-link: IMPLEMENTED IN GOVERNANCE + LEARNING BOUNDARY.
Federation/external harvest: CROSS-LINKED.
Native runtime/device/hardware/blockchain execution: remains separate and OPEN until directly evidenced.


## 21. External-fix gap and repeated-harvest semantic gate — 22 September 2026
AI-assisted repair MUST distinguish INTERNAL_PRESENT, MISSING_INTERNAL and PARTIAL_INTERNAL. An externally found fix that is absent internally becomes a governed candidate, not an automatic patch. Required sequence: SOURCE -> INTERNAL MATCH -> SEMANTIC MATCH -> PROVENANCE -> LICENCE -> SECURITY -> NATIVE IMPLEMENTATION -> TEST -> REGRESSION -> ROLLBACK -> PROMOTION.
Repeated harvests MUST retain pass identity and compare common/unique evidence. Result-set divergence is a diagnostic signal, not proof of a root cause. Foreign-language evidence retains original terminology and provenance.
\n\n## 23. Graphics / Godot / Vulkan federation extension — 22 September 2026\n\nThe native matrix now explicitly governs graphics API and engine federation.\n\nHard rules:\n- Renderer selection MUST be capability-driven, never name-driven.\n- Engine/API presence MUST NOT be treated as live GPU/device support.\n- Vulkan loader, API version, feature set, device limits and extensions are separate evidence fields.\n- Validation layers are development diagnostics, not production rendering dependencies.\n- Godot remains an external engine/provider boundary; engine source is not silently promoted into the native OS.\n- Renderer fallbacks MUST preserve a known-good path and be observable.\n- GPU resources, synchronization and lifetime ownership MUST remain inside the renderer/provider boundary.\n- Shader/toolchain versions and backend capabilities MUST be versioned before promotion.\n- Android Vulkan support is verified only from device/runtime evidence, not from source dependencies.\n\nVerification mapping: source/contract checks may establish adapter correctness; clean Android builds, live Vulkan enumeration, Godot runtime, frame timing and GPU regression remain higher verification gates.\n

## 22. Simulator federation extension — 22 September 2026

For harvested simulation libraries:
- keep solver/model ownership explicit;
- use provider-neutral adapters rather than copying whole external repositories;
- separate model results from physical truth;
- record units, solver/backend, version, provenance and numerical tolerance;
- expose capability discovery separately from executable availability;
- fail closed when a backend is absent or incompatible;
- Android endpoints may exchange jobs/state and visualize controlled results, but may not claim desktop/server solver execution without a compatible native build;
- cross-domain links must preserve canonical ownership in Vehicle, Architecture/Building, Agriculture, World, Environment and Digital Twin systems.

Required sequence:
INTERNAL GAP HARVEST -> EXTERNAL HARVEST -> LICENCE/PROVENANCE -> NATIVE CONTRACT -> SEMANTIC CHECK -> UNIT/INTEGRATION -> SMOKE -> REGRESSION -> RUNTIME -> PROMOTION.

Status: GOVERNANCE EXTENSION INTEGRATED / RUNTIME VERIFICATION OPEN.

## 22. Secure-native verification extension — 22 September 2026

New hard principles:
1. Authority validation is an executable contract; documentation alone is insufficient.
2. Security/licence/provenance gates default to fail-closed.
3. Risk penalties must reduce, never increase, candidate-selection priority.
4. Core-OS validation is an explicit federation gate.
5. Memory safety is a first-class native verification gate.
6. Privileged native code receives stronger sanitizer, CFI, fuzzing and boundary verification according to risk.
7. Every discovered defect becomes a permanent regression test.
8. Third-party components are verified as part of the system.
9. Clean-build evidence is distinct from source presence.
10. Canonical architecture, changelog, matrix, implementation and tests must agree.

External engineering references incorporated: NIST SSDF; NIST developer verification guidance; Android Open Source Project native security, memory safety, CFI and Rust guidance; CISA/FBI secure-by-design memory-safety guidance.

References:
- https://csrc.nist.gov/projects/ssdf
- https://www.nist.gov/itl/executive-order-14028-improving-nations-cybersecurity/software-supply-chain-security-guidance-3
- https://source.android.com/docs/security/overview/implement
- https://source.android.com/docs/security/test/memory-safety
- https://source.android.com/docs/security/test/cfi
- https://source.android.com/docs/setup/build/rust/building-rust-modules/overview
- https://www.cisa.gov/sites/default/files/2025-02/secure-by-design-alert-eliminating-buffer-overflow-vulnerabilities-508c.pdf

Applied corrections:
- learning.py licence promotion gate defaults fail-closed;
- learning.py drift penalty no longer increases model-disagreement score;
- federation_protocol.py F01 explicitly requires Core OS validation;
- authority hierarchy has executable enforcement and regression tests;
- identified semantic defects have dedicated regression tests.

Status: v1.1 governance extension implemented at source; host/CI/runtime evidence remains required.


## 2026-09-22 — AI / Multimedia / UI Federation Hardening
For Android external AI/multimedia/UI federation:
1. Runtime family identity and concrete executable provider identity MUST remain separate.
2. Vendor/platform SDKs such as Qualcomm IMSDK/QAIRT and Huawei HiAI MUST remain adapter/device/licence boundaries until external evidence is complete.
3. TensorFlow Lite compatibility MUST NOT create a competing forward runtime when LiteRT is the current Google runtime path.
4. API-level features MUST be guarded by runtime capability checks; source availability is not device availability.
5. Compose-first UI dependencies MUST remain separated from domain/native authority; UI migration does not promote the underlying OS/DMS contract.
6. Navigation state MUST be typed and serializable when persistence is required.
7. ONNX/LiteRT/provider dependency presence MUST be recorded separately from runtime, accelerator and model-performance verification.
8. External SDKs, vendor binaries and restricted source MUST NOT be copied into the repository without explicit provenance/licence approval.
