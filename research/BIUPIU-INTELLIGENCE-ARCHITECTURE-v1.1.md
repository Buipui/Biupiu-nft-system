# Biupiu R&D OS — Intelligence Architecture v1.1

**Date:** 18 September 2026
**Status:** Development architecture

## Purpose
The Intelligence Layer is the AI orchestration layer of the Biupiu R&D OS. It assists research, evidence control, hypothesis generation, simulation planning, experiment logging and repository maintenance without treating unverified claims as facts.

## Architecture
PROJECT → RESEARCH OBJECT → SOURCE → CLAIM → HYPOTHESIS → MODEL → SIMULATION → EXPERIMENT → DATASET → RESULT → REPLICATION → TECHNOLOGY READINESS → IP → PROTOTYPE → PRODUCT

### Intelligence services
- Research Retrieval: repository/RAG search and source discovery.
- Evidence Engine: provenance, confidence, contradiction and evidence-state tracking.
- Hypothesis Engine: converts claims into falsifiable hypotheses.
- Experiment Planner: proposes controlled experiments with variables, controls and expected observations.
- Simulation Router: selects computational tools/domains; simulation results remain distinct from physical validation.
- Results Analyst: statistical analysis, uncertainty and reproducibility checks.
- Knowledge Graph: maintains source→claim→hypothesis→experiment→result relationships.
- Failure/Lessons Service: records negative and inconclusive outcomes.
- Repository Agent: proposes structured repository updates and never silently rewrites evidence.
- Mobile AI Gateway: authenticated API boundary for Android clients.

## AI operating rule
The AI must distinguish:
1. sourced fact,
2. model output,
3. hypothesis,
4. simulation result,
5. physical measurement,
6. interpretation.

No speculative source is promoted to established fact without independent evidence.

## Initial implementation
Use an external LLM/API as the reasoning engine, with Biupiu-owned retrieval, schemas, experiment records and audit logs around it. Model-specific code is isolated behind an AI provider interface so the model can later be replaced or supplemented by a local model.

## Security boundaries
The mobile application does not access PostgreSQL directly. Secrets remain server-side. AI actions that modify durable research records should pass through validated API operations and audit logging.

## Build gates
- Gate AI-01: provider abstraction + structured request/response schema.
- Gate AI-02: repository retrieval/RAG.
- Gate AI-03: hypothesis/experiment generation.
- Gate AI-04: evidence-aware result analysis.
- Gate AI-05: authenticated mobile AI gateway.
- Gate AI-06: offline mobile queue and sync.
- Gate AI-07: physical-lab/device integration.

**Current gate:** AI-21 transactional audit integration; AI-22 durable-store readiness remains pending.

## Learning Layer extension — 2026-09-19
The Intelligence Layer now has a dedicated learning/provenance foundation:
- `research/BIUPIU-INTELLIGENCE-LEARNING-LAYER-v1.0.md`
- `research/BIUPIU-INTELLIGENCE-LEARNING-SCHEMA-v1.0.json`
- `software/rnd-os-ai/src/biupiu_ai/learning.py`
- `software/rnd-os-ai/tests/test_learning.py`

The learning layer records versioned lineage across research, experiments, models, datasets, repository changes and World systems. It preserves old/new knowledge rather than treating duplication or supersession as automatic deletion.

### Blockchain checkpoint boundary
Approved learning checkpoints can be anchored through `contracts/BiupiuLearningRegistry.sol`. Raw datasets, prompts, private model outputs, credentials and confidential IP remain off-chain. Blockchain anchoring is a commitment/integrity function, not model training or proof of scientific truth.

### Core AI maintenance function
The Intelligence Layer now treats bug fixes, code updates, technology updates, dependency/security audits, index synchronization, provenance checks and regression evidence as first-class learning events. Human approval remains required for durable promotion, deletion, public release, IP transitions and blockchain anchoring.


## Federation Harvest Learning Integration — 22 September 2026

The learning layer now consumes federation harvest events as structured comparison evidence. External resources are treated as candidate knowledge objects until independently verified.

Routing:
`FEDERATION DISCOVERY -> RESOURCE RECORD -> INTERNAL MATCH -> TEST EVIDENCE -> FAILURE/RESULT -> LEARNING EVENT -> RETRIEVAL INDEX -> PREVENTATIVE TEST -> HUMAN PROMOTION`

The learning layer must preserve both the internal baseline and the external candidate lineage. It may improve retrieval, comparison, diagnostics and test generation; it may not silently replace authoritative code, erase failures or self-authorise promotion.

Linked checkpoint: `research/BIUPIU-LEARNING-CHECKPOINT-FED-HARVEST-20260922.md`.


## Multilingual Federation Learning Extension — 22 September 2026

The Intelligence Layer now receives a governed multilingual engineering event stream:
FOREIGN-LANGUAGE DISCOVERY -> ORIGINAL SOURCE RETENTION -> LOCALE/TERMINOLOGY NORMALISATION -> INTERNAL MATCH -> TEST VECTOR -> RESULT/FAILURE -> LEARNING EVENT -> INDEX/DIGEST -> PROMOTION REVIEW.

Native language capability is anchored at:
- apps/shared/runtime/BIUPIU-LANGUAGE-CONTRACT-v1.json
- apps/shared/runtime/LanguageSelector.kt
- software/rnd-os-ai/src/biupiu_ai/global_language_translation.py

Learning must preserve:
- original language;
- canonical locale tag;
- script/region;
- source terminology;
- provenance;
- licence state;
- test evidence;
- translation verification state;
- fallback behaviour;
- failure class;
- source commit.

The learning layer may generate preventative multilingual tests and retrieval improvements. It may not promote translated code, change evidence state, or overwrite authoritative language contracts without the normal validation and human release gates.

Blockchain boundary remains unchanged: only approved hashes/manifests/IDs may be anchored; private knowledge, raw translation data, credentials and confidential IP remain off-chain.
