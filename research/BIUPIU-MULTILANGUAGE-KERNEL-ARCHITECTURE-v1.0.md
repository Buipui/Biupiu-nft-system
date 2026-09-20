# Biupiu Multi-Language Kernel Architecture v1.0

Priority: P0 / Core Architecture
Date: 20 September 2026
Status: ARCHITECTURE INTEGRATED — SOURCE IMPORT/BUILD HOST VALIDATION PENDING

## Objective
Establish C, C++ and Rust as the controlled low-level language stack for Biupiu OS, Biupiu AI infrastructure and domain subsystems.

- C: stable low-level ABI, boot/runtime primitives, hardware-facing compatibility, portable FFI and legacy integration.
- C++: high-performance systems, simulation, graphics, numerical/geometry engines, robotics and existing scientific/engineering libraries.
- Rust: memory-safety-oriented kernel services, concurrency-sensitive infrastructure, embedded services and new security-sensitive components.

External code is never considered safe, correct, compatible or commercially reusable merely because it is indexed.

## Canonical dependency direction
Hardware/Platform -> C ABI / HAL -> Rust or C++ subsystem -> OS contracts -> AI services -> applications

AI never bypasses authoritative OS interfaces.

## Kernel/service allocation
| Layer | Primary | Secondary | Rule |
|---|---|---|---|
| Boot/ABI/HAL | C | Rust | Keep boundary small and stable |
| Memory/concurrency/security | Rust | C | Prefer Rust for new safety-sensitive code |
| Platform/runtime interfaces | C | C++/Rust | Wrap before rewrite |
| Simulation/geometry/graphics | C++ | Rust/C | Benchmark-driven |
| Scientific/numerical kernels | C++/C | Rust | Benchmark before promotion |
| Embedded MCU services | Rust/C | C++ | Target-specific |
| AI native acceleration | C++ | Rust/C | Isolate vendor SDKs |
| FFI boundary | C ABI | Rust/C++ | Versioned and tested |

## Multi-language protocol
Every cross-language component requires: stable C-compatible interface where needed; explicit ownership/lifetime rules; explicit error model; versioned ABI/API; concurrency contract; memory alignment and serialization rules; deterministic test vectors; licence/dependency metadata; security classification; source provenance.

Preferred data exchange is versioned structured records rather than language-specific object layouts.

## Boundary rules
Rust/C: use extern C compatible interfaces and opaque handles where practical. Rust owns internal safety invariants.
C/C++: use a C ABI facade for durable boundaries; do not expose C++ ABI or STL types across the OS boundary.
Rust/C++: prefer a C ABI boundary unless a specific binding technology is validated.

## Proposed kernel and subsystem layout
kernel/boot — C + target assembly where required
kernel/hal — C/Rust
kernel/memory — Rust-first
kernel/scheduler — Rust-first
kernel/ipc — Rust/C ABI
kernel/security — Rust-first
kernel/storage — Rust/C
kernel/device — Rust/C
subsystems/compute — C/C++
subsystems/geometry — C++
subsystems/robotics — C++/Rust
subsystems/digital-twin — C++
subsystems/photonics — C/C++
ai/native — C++/Rust adapters
ai/ffi — C ABI
ai/verification — Rust/C++

## Intelligence learning model
Language resources become structured learning/provenance records rather than blind training data.

Record: language, standard/edition, compiler/toolchain, target, API/ABI, dependency graph, SPDX/licence, source URL and immutable reference, tests, benchmarks, security findings, limitations, architecture pattern, failure modes, performance, portability, confidence and evidence class.

Promotion classes:
REFERENCE_ONLY -> ANALYZED -> LICENCE_CLEARED -> BUILD_VERIFIED -> SMOKE_TESTED -> REGRESSION_VERIFIED -> PROMOTED_ADAPTER -> PROMOTED_CORE

Documentation alone can never promote third-party code to PROMOTED_CORE.

## NASA / DARPA
NASA open-source software is a high-value reference pool. Relevant examples include Core Flight System components, F-prime flight software, Vision Workbench and EADINLite. NASA F-prime documents C/C++ tooling and optional Rust components.

DARPA TRACTOR is directly relevant to the learning architecture because it researches automated C-to-Rust translation using static/dynamic analysis and machine-learning/LLM techniques. Biupiu treats this as a translation-with-verification research pattern, not as proof of automatic correctness.

## Declassified government evidence
Declassified CIA/FOIA material is historical systems-engineering evidence only. Relevant themes include security kernels/reference monitors, computer-system planning, software engineering and programming systems. Historical documents are not treated as current best practice without modern validation.

## Foreign-language research
Preserve original-language metadata and translated summaries. Candidate channels: HAL, CiNii Research, KoreaScience, Chinese-language academic repositories where legally accessible, and CyberLeninka.
Translation is an interpretation layer. Original titles, abstracts and source identifiers must be preserved.

## Open books and GitHub
Open educational resources are learning references, not unrestricted code sources. Rust official books and the Embedded Rust Bookshelf provide low-level learning material. GitHub provides source provenance, release metadata, issues, CI and commit references.

## Exterminate / conflict rules
1. Do not copy third-party code into Biupiu core solely because it is public.
2. Do not train on or redistribute restricted material without rights review.
3. Do not mix incompatible ABIs silently.
4. AI-generated code must pass compilation, tests and security gates.
5. Literature findings are not implementation evidence.
6. Historical/declassified material cannot become a modern security claim without validation.
7. Preserve failed translations, failed builds and rejected dependencies as learning evidence.
8. Keep commercial DTIC material separate from personal R&D resources.

## Verification ladder
DISCOVER -> CLASSIFY -> LICENCE -> STATIC ANALYSIS -> BUILD -> UNIT TEST -> ABI TEST -> FUZZ/SAFETY TEST -> BENCHMARK -> CROSS-SYSTEM REGRESSION -> PROVENANCE -> PROMOTION

## Current gate
Architecture: IMPLEMENTED IN REPOSITORY
Resource manifest: IMPLEMENTED
OS/AI/subsystem mapping: IMPLEMENTED
External source-code import: NOT PERFORMED
Local C/C++/Rust toolchain build: NOT VERIFIED on user's development host
Kernel runtime: NOT CLAIMED
Physical/embedded validation: NOT CLAIMED

This gate establishes the architecture and intelligence schema without falsely claiming that a kernel has already been compiled or deployed.
