# Biupiu R&D OS — Intelligence Architecture v1.2
**Date:** 19 September 2026  
**Status:** Core architecture extension

## 1. Architecture

`USER/RESEARCHER → INTELLIGENCE ORCHESTRATOR → RETRIEVAL → EVIDENCE GRAPH → TOOLS/SIMULATION → EVALUATION → LEARNING MEMORY → GOVERNED PROMOTION`

### Retrieval
Use three complementary routes:
- lexical retrieval for exact identifiers and terminology;
- semantic/vector retrieval for concept similarity;
- graph retrieval for relationships, dependencies and provenance.

Retrieval results must retain source references.

### Evidence graph
Core relation types:
- `SUPPORTS`
- `CONTRADICTS`
- `REFINES`
- `BUILDS_ON`
- `DERIVED_FROM`
- `TESTS`
- `PRODUCES`
- `DEPENDS_ON`

Every material assertion should be traceable to source/evidence records.

### Evidence state
The system distinguishes:
`ESTABLISHED | SUPPORTED | PRELIMINARY | HYPOTHESIS | SPECULATIVE | CONTRADICTED | INCONCLUSIVE | UNSUPPORTED`

An unsupported AI statement cannot silently become established knowledge.

## 2. Scientific/engineering orchestration

1. Define question and acceptance criteria.
2. Retrieve relevant evidence.
3. Identify conflicting or missing evidence.
4. Form hypothesis/model.
5. Select simulation, computation or experiment.
6. Execute only when required inputs/provenance are present.
7. Evaluate against expected evidence and benchmarks.
8. Record failure/success/uncertainty.
9. Generate candidate next actions.
10. Require human approval for durable promotion.

This adapts the stage-gated, human-in-the-loop patterns identified in NASA scientific-AI resources while keeping Biupiu's own interfaces and schemas.

## 3. Evaluation

Each model/provider/system version should have reproducible evaluation cases covering:
- source recall;
- claim grounding;
- evidence-state accuracy;
- contradiction detection;
- unsupported-claim refusal;
- tool selection;
- regression behaviour;
- reproducibility;
- latency/resource cost where measurable.

A successful text-generation response is not by itself an intelligence-quality pass.

## 4. Change impact

Before promoting a core change, identify:
- direct dependencies;
- downstream consumers;
- schema/API compatibility;
- security implications;
- licence/provenance implications;
- private-vs-public boundary;
- affected tests and gates.

## 5. Learning memory

Learning records remain append-only at the event level. Supersession creates a new relationship rather than erasing the old event.

## 6. Blockchain

Blockchain remains a selective integrity anchor:
- approved model/checkpoint commitments;
- dataset manifest hashes;
- lineage roots;
- metrics/policy hashes.

Raw knowledge, confidential IP, credentials, prompts and private datasets remain off-chain.

## 7. Human control

AI may retrieve, compare, analyse and propose. Human-controlled gates remain required for:
- production promotion;
- deletion;
- public/customer release;
- IP transitions;
- external code import;
- blockchain anchoring;
- safety-critical execution.

## 8. Resource integration rule

External resources are **reference inputs** until individually reviewed for licence, provenance, security and compatibility. The Intelligence Layer must never represent a referenced project as Biupiu-owned code.
