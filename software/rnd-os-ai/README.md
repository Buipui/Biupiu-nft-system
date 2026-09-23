# Biupiu AI — Intelligence Layer v1.1

Development foundation for the separate Biupiu AI intelligence subsystem.

## Architectural position

Biupiu AI is **not the Core OS**. The original Biupiu R&D OS v1.0 remains the Core OS Baseline. AI integrates with the OS through explicit interfaces and cannot directly mutate authoritative OS state.

Canonical architecture: `research/BIUPIU-OS-AI-SEPARATION-ARCHITECTURE-v1.0.md`.

## AI responsibilities

- provider-neutral model interface
- prompt/context assembly
- repository retrieval adapter
- evidence-aware response schema
- agent router/orchestration
- research assistance
- experiment-generation adapter
- AI audit/provenance hooks
- external open-resource registry and licence-aware integration
- future AI planning, tool-use and verification services

## OS integration contract

Preferred flow:

`OS context -> AI service -> structured response -> OS validation/audit -> authoritative state`

AI suggestions, generated records and proposed actions are non-authoritative until accepted through OS validation boundaries.

## Independence

The AI provider/model can be replaced without changing the OS data model or core provenance semantics. Biupiu OS can operate without an AI provider.

## Safety and provenance boundary

- No direct AI database/state mutation.
- No bypass of OS release/provenance gates.
- External repositories remain references unless licence/security/compatibility gates approve incorporation.
- Provider credentials and production model selection are not hard-coded.

## Gate status

**AI-01 / SEPARATION-01: REGISTERED — Biupiu AI is formally maintained as an independent intelligence layer integrated with the Core OS.**

Production AI deployment remains gated by persistence, authentication, security, provider integration and end-to-end testing.


## Global Language Translation — HARD-CODED CORE FEATURE

**Gate AI-26 / GLOBAL-LANGUAGE-01: REGISTERED** — multilingual translation is now a first-class Biupiu AI capability and is connected to the global multilingual research protocol.

Implementation: `src/global_language_translation.py`  
Regression tests: `tests/test_global_language_translation.py`  
Research protocol: `research/BIUPIU-GLOBAL-MULTILINGUAL-RESEARCH-INTELLIGENCE-PROTOCOL-v1.0.md`

### Contract
- Preserves original-language source text.
- Normalises BCP-47-style language tags to registered base languages.
- Includes African, European, Asian, Middle Eastern and other major language families in the initial registry.
- Supports provider injection rather than hard-coding credentials or a commercial vendor.
- Records translation provider and provenance.
- Marks supplied machine translations `translated-unverified` until validation.
- Leaves translation `pending` when no backend is configured rather than fabricating output.
- Rejects unknown language codes.
- Translation never bypasses OS validation, evidence, licence or provenance gates.

### Hard-code boundary
The language registry, validation rules and translation provenance contract are hard-coded into the Biupiu AI layer. Actual translation engines remain replaceable plugins/backends so the core architecture does not become vendor-locked.


## Simulator/Open-Source Integration Gates

- **SIM-OSS-01:** adapter layer implemented.
- **SIM-OSS-02:** controlled validation pipeline registered.
- **SIM-OSS-03:** non-executing backend validation harness implemented; production approval remains gated.

The simulator adapter boundary only probes local availability and constructs safe commands. It does not install or automatically execute external backends.


## Federated adaptive runtime — 2026-09-23

- **F23:** REGISTERED — Digital Twin performance federation, passive-state policy, adaptive acceleration/deceleration and runtime telemetry.
- **F24:** REGISTERED — OEM/shared-development-resource compatibility registry with provider-neutral adapters.
- **F25:** REGISTERED — cross-matrix capability/dependency/resource/backpressure/fail-closed contract.
- Runtime telemetry now feeds governed learning records without autonomous promotion.
- External compatibility harvest integrated for ONNX Runtime EPs, Qualcomm QNN, Intel OpenVINO, NVIDIA CUDA, AMD MIGraphX, Epic NNE and OpenXR.
- Local/physical verification remains separately gated.
