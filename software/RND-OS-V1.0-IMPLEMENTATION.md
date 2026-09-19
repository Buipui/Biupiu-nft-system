# Biupiu R&D OS v1.0 — Core Baseline

Date: 2026-09-19

## Baseline designation

The original Biupiu R&D OS v1.0 implementation is now designated the **Core OS Baseline** for subsequent development.

This designation does not delete, replace or invalidate existing modules. It establishes the reference architecture from which future OS updates are built.

## Core baseline functions

- Research-object registry with explicit evidence classes.
- Digital laboratory experiment logging.
- Audit-event records.
- Digital Asset & Provenance console.
- Deterministic SHA-256 mint payload generation.
- NFT release gate model: READY_FOR_REVIEW -> TESTNET -> VERIFIED -> RELEASE.
- Local JSON workspace export.
- Offline-first PWA structure for Windows and Android browsers.
- Android navigation exposing Research, Digital Lab, Assets/NFT and Control Centre.

## Separated intelligence layer

Biupiu AI is maintained separately under `software/rnd-os-ai/`.

The AI layer can consume OS context and request operations through OS-defined interfaces, but it does not become the authoritative system of record and does not bypass validation/audit controls.

## Future extension rule

Future OS updates must build on the core contracts above. New capabilities such as Digital Twin, simulation, robotics, package managers, platform adapters, additional desktop/mobile targets and Web3 integrations must attach through explicit interfaces.

## Production boundary

The baseline remains a functional prototype, not a production release. Production persistence, authentication/RBAC, encrypted storage, repository integration, AI service deployment, simulation runners, signing infrastructure, security testing and packaged platform builds remain gated.

**CORE-OS-BASELINE-01: REGISTERED**

## SELF-HEAL-01 — Core OS Failure-Recovery Contract

The Core OS owns the authoritative safety boundary for self-healing operations. Biupiu AI may propose candidate repairs, but OS-controlled validation must precede durable state changes.

Required flow: DETECT -> TRIAGE -> SANDBOX -> TEST -> VERIFY -> LEARN -> PROMOTE or ROLLBACK.

Hard safety rules: bounded repair scope; protected core files; regression-test enforcement; rollback on failed verification; circuit breaker after repeated failure; provenance record for every attempt; no privilege escalation through learned fixes; explicit promotion for production/customer-facing changes.

Implementation: software/rnd-os-ai/src/biupiu_ai/self_healing.py. The AI controller remains modular, while the OS contract is authoritative.

SELF-HEAL-01: CORE OS CONTRACT REGISTERED.