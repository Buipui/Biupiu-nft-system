# BIUPIU AI External Resource & Module Cross-Link Register v1.0

**Date:** 20 September 2026
**Status:** IMPLEMENTED — research/resource registry; runtime/provider connectivity remains separately gated.

## Purpose

Cross-link external AI, machine-learning, agent, evaluation, open-model, research and developer resources into the Biupiu Intelligence Layer without treating discovery as automatic integration.

Pipeline:

`DISCOVER -> SOURCE/LICENCE CHECK -> CAPABILITY MAP -> SECURITY REVIEW -> COMPATIBILITY TEST -> SANDBOX -> EVALUATE -> HUMAN APPROVAL -> PROMOTE`

## 1. OpenAI / Codex

### OpenAI Codex
- Repository: https://github.com/openai/codex
- License: Apache-2.0.
- Use class: **OPEN-SOURCE CODE CANDIDATE**.
- Candidate capabilities: coding-agent architecture, repository operations, developer tooling, Rust implementation patterns, test/build workflows.
- Biupiu routes: COMPUTE/CODEX, AI, SYSTEM-BUILDER, REPOSITORY, DMS, SOFTWARE-ENGINEERING.
- Current action: reference and compatibility candidate; do not copy wholesale into Biupiu OS.

### OpenAI Agents SDK — Python
- Repository: https://github.com/openai/openai-agents-python
- License: MIT.
- Candidate capabilities: agents, tools, handoffs, guardrails, tracing/evaluation patterns.
- Biupiu routes: AI, ORCHESTRATION, DMS, RESEARCH, EVALUATION, HUMAN-IN-LOOP.

### OpenAI Agents SDK — JavaScript/TypeScript
- Repository: https://github.com/openai/openai-agents-js
- License: MIT.
- Candidate capabilities: provider-agnostic agent workflows, sandbox/realtime agents, tools/MCP, guardrails, sessions and tracing.
- Biupiu routes: AI, CROSS-PLATFORM, WEB, MOBILE, DMS, MCP.

### OpenAI open-weight models
- gpt-oss-20b / gpt-oss-120b and gpt-oss-safeguard are recorded as open-weight resources under Apache 2.0.
- Candidate capabilities: local/private model experimentation, reasoning, safety-policy experimentation and offline/edge architecture research.
- Biupiu routes: LOCAL-AI, EDGE-AI, SAFETY, EVALUATION, DMS.

### OpenAI file/vector-store concepts
- Candidate architecture: document ingestion, persistent file references, metadata, vector-store attachment and retrieval.
- Biupiu routes: RESEARCH REGISTRY, EVIDENCE GRAPH, PROVENANCE, RAG, DMS.
- Rule: external hosted services are integration targets, not copied proprietary internals.

## 2. Google Gemini

### Gemini API examples
- Repository: https://github.com/google-gemini/api-examples
- License: Apache-2.0.
- Candidate capabilities: API integration patterns and executable examples across languages.
- Biupiu routes: MULTI-MODEL GATEWAY, AI, CODEX, TESTING.
- Use: adapter/reference implementation only; credentials remain external.

### Gemini / Google model-provider lane
- Treat Gemini as an external model provider.
- Cross-model evaluation must compare outputs using the same task, evidence set, tools, temperature/configuration where applicable, and validation criteria.
- No provider is authoritative by default.

## 3. Meta / Llama

### Meta Llama
- Repository: https://github.com/meta-llama/llama3
- Current repository metadata reports an 'Other' licence/no SPDX assertion; model/community licence terms must therefore be checked before redistribution or commercial embedding.
- Use class: **REFERENCE / LICENCE-GATED**, not automatic code-import.
- Biupiu routes: LOCAL-AI, EDGE-AI, MULTI-MODEL, MODEL-EVALUATION.

### Llama Stack / ecosystem
- Route for model-serving, agent/runtime and deployment architecture research.
- Promotion requires component-level licence and dependency review.

## 4. Model Context Protocol

### Official MCP repositories
- https://github.com/modelcontextprotocol/modelcontextprotocol
- https://github.com/modelcontextprotocol/servers
- https://github.com/modelcontextprotocol/python-sdk
- https://github.com/modelcontextprotocol/typescript-sdk
- Python SDK is MIT-licensed.
- Candidate capabilities: standardised model/tool/context interfaces and connector architecture.
- Biupiu routes: DMS, INTELLIGENCE GATEWAY, TOOLS, REPOSITORY, DIGITAL-TWIN, EXTERNAL-SOURCE ADAPTERS.
- Security gate: every server/connector is untrusted until permissions, provenance, secrets, network scope and output validation pass.

## 5. Stanford

### Stanford CRFM HELM
- Repository: https://github.com/stanford-crfm/helm
- License: Apache-2.0.
- Capability: reproducible holistic evaluation across models, scenarios and metrics.
- Important current state: HELM entered maintenance mode on 1 June 2026.
- Biupiu routes: MODEL-EVALUATION, BENCHMARKING, SAFETY, MULTIMODAL, PROVIDER-COMPARISON.

### Stanford NLP / Stanza
- Repository: https://github.com/stanfordnlp/stanza
- Capability: multilingual NLP, tokenisation, sentence segmentation, NER and parsing.
- Biupiu routes: MULTILINGUAL, RESEARCH, KNOWLEDGE GRAPH, DOCUMENT PROCESSING.
- Licence must be checked at the component/version level before vendoring.

### Stanford DSPy
- Repository: https://github.com/stanfordnlp/dspy
- Capability: programmatic optimisation of language-model pipelines.
- Biupiu routes: PROMPT/PROGRAM OPTIMISATION, EVALUATION, AGENT PIPELINES.
- Licence: MIT per current public repository metadata.

## 6. MIT

### MIT CSAIL
- Official research hub: https://www.csail.mit.edu/
- GitHub organisation: https://github.com/csail
- Use class: **RESEARCH DISCOVERY + CODE CANDIDATES**.
- Search lanes: machine learning, robotics, computer vision, systems, HCI, optimisation, formal methods, computational science and AI safety.
- Rule: identify exact project, version and licence before code reuse.

## 7. Harvard

### Harvard AI / ML research lane
- Primary source hub: https://www.harvard.edu/
- Route through Harvard-affiliated labs, publications, datasets and public repositories.
- Use class: **ACADEMIC EVIDENCE / RESEARCH DISCOVERY**.
- Search lanes: machine learning, computational science, biomedical AI, NLP, vision, optimisation, responsible AI and scientific ML.
- No Harvard affiliation or permission is inferred merely from public availability.

## 8. DARPA

### AI Forge
- Official programme: https://www.darpa.mil/research/programs/ai-forge
- Focus: AI interpretability, AI control, adversarial robustness, reliability and secure deployment research.
- Biupiu routes: SAFETY, CONTROL, ADVERSARIAL TESTING, ROBUSTNESS, HIGH-STAKES VALIDATION.
- Use class: **RESEARCH / PROGRAMME / TECHNICAL-EVIDENCE SOURCE**. DARPA programme material is not treated as automatically reusable software.

## 9. Cross-model Intelligence Gateway

Canonical provider abstraction:

`TASK -> EVIDENCE SET -> MODEL ADAPTER(S) -> TOOL PLAN -> RESPONSE -> FACT/CITATION EXTRACTION -> CROSS-MODEL CHECK -> VALIDATION -> LEARNING RECORD`

Provider lanes:
- OPENAI/CODEX
- GOOGLE/GEMINI
- META/LLAMA
- OTHER APPROVED PROVIDERS
- LOCAL/OPEN-WEIGHT MODELS
- SPECIALIST DOMAIN MODELS

The gateway must preserve provider/model/version metadata and must never silently merge contradictory outputs.

## 10. Open-source promotion gate

A component can move from REFERENCE to CANDIDATE only when:
1. Exact repository and commit/version recorded.
2. Licence identified.
3. Dependency licence tree reviewed.
4. Security/adversarial review completed.
5. Interface/schema compatibility checked.
6. Tests exist.
7. Sandbox result recorded.
8. Performance/regression baseline recorded.
9. Provenance and attribution requirements recorded.
10. Human approval obtained for durable promotion.

## 11. Proprietary/shared-development rule

Public access is not permission to copy proprietary code.

For closed/proprietary systems from OpenAI, Google, Meta, Harvard, Stanford, MIT, DARPA or other organisations:
- record public APIs/specifications and documented behaviour;
- build clean-room adapters where permitted;
- use official SDKs/examples where their licence permits;
- never extract, bypass, scrape, reconstruct or redistribute non-public implementation;
- retain provider attribution and contractual restrictions;
- isolate provider-specific code behind Biupiu interfaces.

## 12. Biupiu integration map

`EXTERNAL AI -> PROVIDER ADAPTER -> INTELLIGENCE GATEWAY -> EVIDENCE/RAG -> MATH/COMPUTE -> DOMAIN SIMULATOR -> DIGITAL TWIN -> VALIDATION -> DMS/PROVENANCE -> LEARNING`

Affected departments:
AI, COMPUTE, MATH, GEOMETRY, DIGITAL-TWIN, ROBOTICS, ADV-MFG, PHOTONICS, BIO, BIOMED, AGRI, MATERIALS, AERO, MARINE, WATER, ENERGY, LAND-GIS and IP.

## 13. Status

**REGISTERED / IMPLEMENTED:** external-resource cross-link layer.

**NOT YET CLAIMED:** automatic live connectivity to every provider, automatic code import, autonomous self-modification, production deployment or physical actuation.

**Next gate:** AI-29 — build the provider-neutral Intelligence Gateway adapter schema and a licence/security/evaluation manifest for each candidate module.
