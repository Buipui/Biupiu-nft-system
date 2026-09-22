# BIUPIU NATIVE CODE AUDIT / HARVEST / HOUSEKEEPING LOG v1.0

Date: 2026-09-22
Repository: Buipui/Biupiu-nft-system
Base state audited: main, commit family current at audit time
Governance standard added: research/BIUPIU-NATIVE-CODING-PHILOSOPHY-AND-ENGINEERING-MATRIX-v1.0.md

## Audit result

### Confirmed native architecture present
- Core R&D OS: software/rnd-os/
- Intelligence/AI: software/rnd-os-ai/
- Mobile: software/rnd-os-mobile/
- Web: software/rnd-os-web/
- Native simulation/interop: core/multilang/, packages/, simulators/
- Learning: software/rnd-os-ai/src/biupiu_ai/learning.py
- Continual adaptation: software/rnd-os-ai/src/biupiu_ai/ml/continual_adaptation.py
- Promotion boundary: software/rnd-os-ai/src/biupiu_ai/promotion_router.py
- Simulator adapters: software/rnd-os-ai/src/simulator_adapters.py
- Federation/learning CI already exists in .github/workflows/

### Existing design rules confirmed
1. AI is separated from authoritative OS state.
2. AI cannot bypass OS validation/audit.
3. External engines are adapter/reference inputs rather than automatically installed or executed.
4. Learning records preserve lineage and failure evidence.
5. Promotion is fail-closed and requires provenance/licence/security/compatibility/test/human gates.
6. Simulator outputs are not automatically treated as physical truth.
7. C is the durable ABI/HAL boundary; Rust is preferred for new memory/concurrency/security-sensitive core services; C++ is used for simulation/geometry/graphics/scientific high-performance paths.
8. Android/device/runtime verification is separate from source/CI verification.

## Housekeeping / coding philosophy changes

ADDED:
- hard native coding philosophy and engineering matrix;
- universal engineering rules;
- language-specific rules;
- evidence and authority hierarchy;
- ML/AI lifecycle requirements;
- simulator and federation contracts;
- third-party harvest rules;
- verification ladder;
- release/change-control rules.

NOT AUTOMATICALLY DELETED:
- research records;
- historical failures;
- superseded algorithms;
- unverified assets;
- external references;
- speculative research.

These remain subject to classification/quarantine because lineage and research value must not be destroyed by housekeeping.

## External research cross-reference

NASA:
- NPR 7150.2D / software engineering requirements;
- NASA-STD-8739.8B software assurance and software safety;
- NASA software handbook and coding-standard/static-analysis guidance.
Adopted principles: requirements/design/code traceability, coding-standard verification, static analysis, unit testing, formal test records, software version descriptions, assurance throughout lifecycle. citeturn0search0turn0search4turn0search7

MIT:
- MIT OpenCourseWare software-engineering lifecycle guidance;
- MIT research on randomness-aware testing of ML systems;
- MIT open-access computer-science publishing.
Adopted principles: lifecycle engineering, testing of nondeterministic ML, mathematical/tolerance-aware verification, reusable open research patterns. citeturn2search4turn2search5turn1search1

DARPA:
- Assured Autonomy;
- ANSR;
- PROVERS;
- CLARA / AI assurance.
Adopted principles: continual assurance, runtime monitoring/recovery, evidence-based assurance, hybrid ML + reasoning, formal/proof-oriented verification. citeturn2search2turn2search7turn2search3turn2search8

ResearchGate / academic literature:
- software engineering practices for ML;
- software testing for ML;
- current LLM-based software testing research.
Adopted principles: mature engineering around ML, testing beyond conventional deterministic oracles, robustness/adversarial considerations, reproducibility and evidence maturity. citeturn1search13turn1search16turn1search17

Emerald Insight:
- software-engineering skills and longitudinal software-engineering data research;
- current AI/software-engineering research catalogue.
Adopted principle: engineering practice includes analysis, design, coding, testing, collaboration and longitudinal evidence. citeturn2search9turn2search0

Open books / public code:
- MIT Press open-access CS texts;
- Machine Learning Engineering Open Book;
- public MLOps repositories and testing examples.
Adopted patterns: versioned assets, automated testing, data/model monitoring, reproducible ML lifecycle and production-oriented engineering. citeturn1search1turn1search6turn1search2

## Harvest policy

The external search pass is treated as a knowledge/module-discovery layer, not a licence bypass.

External candidates are mapped into:
REFERENCE -> PATTERN -> ADAPTER -> ASSET -> DEPENDENCY -> PROHIBITED

No external source is copied into authoritative native code solely because it appears useful. Licence, provenance, security, compatibility, build, smoke and regression evidence are mandatory before executable promotion.

## Native ML integration rule

The existing learning layer remains the canonical learning record mechanism. Continual adaptation remains bounded and reference-anchored. Promotion remains fail-closed.

Canonical loop:
SIMULATOR/OS EVENT
-> DIGITAL TWIN
-> FEDERATION EVENT
-> LEARNING RECORD
-> FAILURE/DRIFT CLASSIFICATION
-> BOUNDED ADAPTATION
-> TEST/REGRESSION
-> PROMOTION PROPOSAL
-> OS VALIDATION
-> HUMAN RELEASE AUTHORITY

## Smoke-test status

SOURCE/STRUCTURE:
VERIFIED by repository inspection.

LEARNING CORE:
Previously recorded as CI-verified in repository documentation.

CROSS-PLATFORM:
NOT VERIFIED by this repository-only audit.

ANDROID DEVICE/RUNTIME:
NOT VERIFIED by repository inspection alone.

HARDWARE/GPU/PHYSICAL:
NOT VERIFIED.

THIRD-PARTY SIMULATOR EXECUTION:
NOT VERIFIED unless a runtime probe/build result exists.

The audit does not convert source presence into runtime verification.

## Current gate

CODING PHILOSOPHY: IMPLEMENTED
ENGINEERING MATRIX: REGISTERED
NATIVE ARCHITECTURE AUDIT: COMPLETED
EXTERNAL RESEARCH CROSS-REFERENCE: COMPLETED FOR THE NAMED SOURCE CLASSES
HARVEST GOVERNANCE: IMPLEMENTED
LEARNING/PROMOTION BOUNDARY: CONFIRMED
FULL REPOSITORY CLEAN BUILD: OPEN
CROSS-PLATFORM BUILD: OPEN
ANDROID DEVICE SMOKE TEST: OPEN
HARDWARE/PHYSICAL CORRELATION: OPEN

Status: PARTIALLY VERIFIED — governance and repository architecture updated; runtime-dependent gates remain open.
