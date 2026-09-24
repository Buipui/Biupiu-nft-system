# Biupiu DigiCat + DigiFile Cross-System Architecture v1.0

Date: 2026-09-24
Status: REGISTERED / SOURCE CROSS-LINKED / RUNTIME OPEN

## Naming

**DigiCat** is the canonical short name introduced for the Digital Capability & Knowledge Catalogue function.

**DigiFile** is the canonical short name introduced for the Digital Evidence & Filing function already represented by the DMS and `software/digital-filing-cabinet/`.

These names are architecture aliases/roles; they do not replace the canonical subsystem ownership.

## Core relationship

```
External Research / Internal Research
            ↓
        DigiCat
   classify + catalogue
            ↓
     Native Intelligence
   reason / compare / propose
            ↓
      Federation Core
 contract + capability routing
            ↓
   Core OS / DMS validation
            ↓
       DigiFile
 evidence + provenance + hashes
            ↓
      Digital Twin / Simulators
            ↓
 Quantum AI / domain systems
            ↓
 regression + learning
            ↺
         DigiCat
```

## Core vs Federation vs Quantum AI

| Layer | Role | Authority |
|---|---|---|
| Core OS / DMS | canonical state, security, validation, release/promotion | authoritative |
| Native Intelligence | retrieval, reasoning, classification, proposal, learning | proposal/intelligence |
| DigiCat | catalogue, capability taxonomy, cross-reference and routing metadata | index/catalogue |
| DigiFile | evidence, provenance, filing, hashes, manifests and audit lineage | evidence/file record |
| Federation | contract negotiation, adapter routing, reconciliation, observation and failure-learning transport | federation/service |
| Digital Twin | validated model/state/context and simulation mirror | model/context |
| Quantum AI | quantum/quantum-ML research, simulation and candidate optimisation | domain/provider; simulator-first |
| Quantum providers | Qiskit/PennyLane/etc. | adapter/provider only until promotion |

No layer silently inherits another layer's authority.

## Cross-reference contract

Every DigiCat record should resolve, where applicable, to:
- canonical system ID
- subsystem/domain
- capability
- version
- interface/contract
- dependency
- platform/hardware family
- Digital Twin relationship
- Federation route
- Quantum relevance
- DigiFile evidence record
- provenance
- licence/IP state
- validation state
- regression state
- rollback/revocation reference
- hash

Every DigiFile evidence record should preserve:
- source
- parent task
- timestamp
- source version/commit
- classification
- evidence state
- test/build/runtime state
- validation result
- contradiction/failure record
- affected systems
- promotion/revocation state
- immutable/hash reference where available.

## Quantum cross-reference

Quantum AI is connected through the same catalogue/evidence layer, but the evidence boundary is explicit:

THEORY → NUMERICAL MODEL → CLASSICAL BASELINE → QUANTUM SIMULATION → EXPERIMENT → INDEPENDENT REPLICATION → QPU EXECUTION → PRODUCTION CAPABILITY

DigiCat records the capability and evidence relationships.
DigiFile records the supporting evidence.
Federation routes the workload/provider.
Core OS/DMS controls promotion.

A quantum simulation, literature claim or provider registration does not become a verified QPU capability automatically.

## Digital Twin cross-reference

Digital Twin records consume approved release manifests and retain:
- scenario/configuration
- model version
- telemetry/correlation ID
- provenance
- validation/VVUQ state
- regression lineage
- owner/context.

DigiCat indexes these relationships; DigiFile stores the evidence chain.

## Learning cross-reference

Learning flow:

`DigiCat DISCOVER → CLASSIFY → CROSS-LINK → Federation ROUTE → Core VALIDATE → DigiFile RECORD → Twin/SIMULATE → REGRESSION → LEARN → DigiCat UPDATE`

Failed observations remain evidence. They are not deleted because they contain diagnostic learning value.

## External knowledge rule

External material is classified:
ESTABLISHED → SUPPORTED RESEARCH → PLAUSIBLE MODEL → UNRESOLVED → INCONSISTENT → SPECULATIVE/INSPIRATIONAL

External executable implementations remain REFERENCE/PATTERN/ADAPTER until provenance, licence, security, compatibility, build, smoke, regression and human-promotion gates pass.

Translation is not validation.

## Status

DigiCat: REGISTERED / SOURCE MAPPED / RUNTIME OPEN
DigiFile: REGISTERED / EXISTING DMS-FILING LAYER MAPPED / RUNTIME OPEN
Core cross-reference: UPDATED
Federation cross-reference: UPDATED
Digital Twin cross-reference: UPDATED
Quantum AI cross-reference: UPDATED
Learning cross-reference: UPDATED
Build/CI: PENDING FRESH EXECUTION
Device/HIL/QPU: OPEN
Promotion: EVIDENCE-GATED
