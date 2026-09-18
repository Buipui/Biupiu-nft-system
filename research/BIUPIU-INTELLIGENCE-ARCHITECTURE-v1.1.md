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

**Current gate:** AI-01 architecture/foundation.
