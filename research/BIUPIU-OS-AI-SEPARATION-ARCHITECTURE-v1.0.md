# Biupiu OS / Biupiu AI Separation Architecture v1.0

Date: 2026-09-19

## Purpose

This document establishes the canonical separation between **Biupiu OS** and **Biupiu AI** while preserving one integrated Biupiu system.

The initial Biupiu R&D OS implementation is the **core OS baseline**. Future OS releases must extend or replace implementation components without redefining the core system contract.

## Canonical layers

### 1. Biupiu OS — Core System

Path: `software/rnd-os-web/`, `software/rnd-os-mobile/`, and the shared OS contracts documented under `software/` and `research/`.

The OS owns:

- application lifecycle and navigation
- workspace/project state
- research-object and evidence records
- Digital Laboratory records
- Digital Asset & Provenance controls
- release/mint gates
- audit/event interfaces
- local/offline workspace contracts
- package/module loading boundaries
- Digital Twin and simulation integration contracts
- platform adapters for Windows, Android and future desktop/mobile targets

The OS is the stable integration layer. AI is not required for the core OS to represent, validate or preserve durable records.

### 2. Biupiu AI — Intelligence Layer

Path: `software/rnd-os-ai/`.

Biupiu AI owns:

- provider-neutral model interfaces
- context assembly and repository retrieval
- agent routing/orchestration
- research assistance
- experiment-generation adapters
- AI-specific audit/provenance hooks
- external-resource registry and licence-aware integration
- future AI planning, tool use and verification services

AI may request OS operations through defined interfaces. AI does not bypass OS validation or write authoritative state directly.

### 3. Integrated system

The relationship is:

`Biupiu AI -> OS interfaces -> validation/audit -> authoritative state`

and:

`Biupiu OS -> AI service interface -> optional intelligence -> structured response`

This permits the OS to run without AI, while AI can operate as a first-class subsystem when enabled.

## Core invariants

1. The original Biupiu R&D OS v1.0 implementation remains the baseline reference.
2. Future OS work must preserve its core research/provenance model unless a versioned architecture change explicitly supersedes it.
3. AI remains modular and replaceable.
4. AI-generated suggestions are not authoritative until accepted through OS validation boundaries.
5. Third-party resources remain external references until licence, security and compatibility gates pass.
6. Web3/NFT, Digital Twin, simulation, robotics and platform packages remain consumers/adapters around the core OS rather than redefining it.
7. Windows and Android remain supported targets; future Mac/Linux/Java and other adapters may integrate through platform-neutral contracts.
8. Package separation must not create incompatible forks of the system model.

## Dependency direction

Preferred:

`Platform -> OS -> packages/services -> AI adapters`

AI integration:

`Platform -> OS -> AI service -> external provider/resources`

Avoid:

`AI -> direct database/state mutation`

`package -> private OS internals`

## Versioning rule

- **OS v1.x**: compatible extensions to the original core contract.
- **OS v2.x**: explicit architecture migration requiring compatibility documentation.
- **AI v1.x**: independent intelligence-layer evolution.
- AI versions must not silently change OS semantics.

## Repository rule

The repository remains the authoritative engineering archive. Specifications, source, tests, resource manifests and gate records must identify whether an item belongs to Core OS, AI, a package/adapter, or an external reference.

## Current status

**SEPARATION-01: EXECUTED — Biupiu OS core and Biupiu AI are formally separated at the architecture boundary while remaining integrated through versioned interfaces.**

Live production deployment remains subject to the existing testing, security, persistence and platform-build gates.


## Simulator authority extension — OS-SIM

The simulator kernel is a Core OS capability, not an AI capability.

Canonical direction:

`AI proposal -> OS simulation interface -> validation/audit -> simulation state -> Digital Twin/provenance`

Engine direction:

`Core OS simulation state -> Bevy/Unreal/Godot/other adapters`

AI may propose scenarios, parameters, experiments or analysis, but the authoritative simulation lifecycle and durable state remain under OS contracts.

The simulator gate therefore extends the existing separation invariant without changing OS/AI ownership.


## P0 C/C++/Rust Core Integration — 20 September 2026

The multi-language kernel architecture is now a first-class extension of the OS contract. C is the durable ABI/HAL boundary; Rust is preferred for new memory/concurrency/security-sensitive core services; C++ is the primary native layer for simulation, geometry, graphics and high-performance scientific subsystems. This allocation is consistent with the Rust Embedded guidance that C ABI boundaries are the stable interoperability mechanism for Rust/C/C++ systems. NASA F´ also demonstrates componentized C++ embedded architecture with defined interfaces and unit/integration testing. 

Canonical contract: Hardware -> C ABI/HAL -> Rust/C++ services -> OS validation -> DMS -> Intelligence -> applications/subsystems.

Rules:
- No language may bypass OS authority.
- No C++ ABI/STL object crosses a durable system boundary.
- Cross-language interfaces require explicit ownership, lifetime, error, alignment, serialization, version and concurrency contracts.
- Third-party source remains external until licence, security, build, smoke and regression gates pass.
- Resource documentation can enrich Intelligence but cannot itself promote executable code.
- Failed builds, failed translations and rejected dependencies remain learning evidence.

Canonical architecture record: `research/BIUPIU-MULTILANGUAGE-KERNEL-ARCHITECTURE-v1.0.md`.
Canonical resource registry: `research/BIUPIU-C-CPP-RUST-RESOURCE-MANIFEST-v1.0.json`.

Status: ARCHITECTURE INTEGRATED / HOST RUNTIME VALIDATION PENDING.
