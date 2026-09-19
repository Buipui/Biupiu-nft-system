# Biupiu Intelligence Architecture — Global Resource Audit
**Date:** 19 September 2026  
**Purpose:** identify reusable architecture patterns and permissively reusable/open educational resources for Biupiu Intelligence. No third-party code is copied into Biupiu by this audit.

## Resource findings

### NASA
- **NASA Open Source Software catalog** — official catalog of NASA projects approved for open-source release. Useful for discovering reusable engineering patterns; each project still requires individual licence/provenance review. https://code.nasa.gov/
- **NASA-IMPACT AKD-CARE** — staged engineering methodology for scientific AI agents: scope/decompose, information elicitation, reasoning policies/guardrails, tool orchestration and benchmarking. Its structure supports Biupiu's gate-based AI engineering model.
- **NASA-IMPACT Accelerated Discovery Framework** — human-centric scientific discovery, attribution, conflicting-evidence identification, reproducibility and planner/orchestrator patterns.
- **OnAIR** — NASA open-source onboard-AI research platform/cognitive-architecture pipeline; useful as a reference for lifecycle-oriented AI systems.

### MIT
- **MIT 6.034 Artificial Intelligence** — knowledge representation, search, inference and learning.
- **MIT 6.036 Introduction to Machine Learning** — representation, overfitting/generalization, supervised and reinforcement learning.
- **MIT 6.7960 Deep Learning** — neural architectures including graph networks and transformers, automatic differentiation and generalization.
- **MIT Knowledge-Based Applications Systems** — knowledge representation/acquisition and expert-system engineering.
These are educational references; implementation reuse must follow the licence attached to each individual artifact.

### Wits
- **Wits RAIL** — reinforcement learning, computer vision and deep-network research.
- **Wits PRIME Lab** — machine learning, signal processing, computer vision, NLP and medical ML, including resource-constrained settings.
- **Wits MIND Institute** — interdisciplinary AI, machine/human/animal intelligence and AI governance.
- Public Wits-linked GitHub research includes reinforcement-learning, safe-RL, skill composition and world-value-function work. Individual repositories require their own licence review before code reuse.

### Open GitHub architecture patterns
- **KnowledgeForge** — hybrid vector + graph + keyword retrieval, confidence-labelled graph extraction, provenance and impact analysis.
- **LLM-Knowledge-Graph** — local-first evidence-bearing project knowledge and bidirectional architecture-to-code understanding.
- **Provenance** — citation-grounded RAG + typed knowledge graph + claim-level verification/refusal.
- **Prior** — auditable literature contribution graph with supports/builds_on/refines/contradicts relations.
- **ATLAS** — typed entities/relationships, anomalies, question-oriented queries and CI documentation QA.
- **AgentVerse / khive / imi** — evolving knowledge graphs, governed memory, provenance ingestion and agent-facing interfaces.

### Open books / educational foundations
- MIT OpenCourseWare provides openly shared AI/ML educational materials and code exercises.
- The Harvard CS249r Machine Learning Systems book/courseware is publicly indexed on GitHub and covers machine-learning systems, agentic AI and physical AI.
- Educational resources are retained as learning references, not automatically imported as code.

## Architecture changes selected for Biupiu

1. **Hybrid retrieval contract** — combine lexical, vector and graph retrieval instead of relying on one retrieval mechanism.
2. **Typed evidence graph** — claims and relations carry explicit provenance and evidence/confidence states.
3. **Contradiction graph** — support, refine, build-on and contradict relations become first-class.
4. **Claim-level grounding gate** — unsupported claims should fail closed or be explicitly marked unsupported.
5. **Impact analysis** — architecture/code changes should identify dependent objects before promotion.
6. **Evaluation registry** — benchmark cases become versioned research objects, not ad-hoc tests.
7. **Human approval boundary** — AI can propose learning/promotion actions; durable promotion, deletion, release and blockchain anchoring remain approval-controlled.
8. **Scientific lifecycle orchestration** — Planner → Retrieval → Evidence → Tool/Simulation → Evaluation → Learning Record → Next Candidate.
9. **Memory preservation** — old/new artifacts remain traceable and are not removed solely because a newer artifact exists.
10. **Resource/licence registry** — external resources must record source, licence/status, intended use and whether code was actually imported.

## Important boundary
This audit identifies architecture patterns and public resources. It does not establish that any third-party code is compatible with Biupiu's licensing, IP or commercial requirements. Any future import must pass provenance/licence/security review first.
