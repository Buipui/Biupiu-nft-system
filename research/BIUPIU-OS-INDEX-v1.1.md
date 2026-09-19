# Biupiu OS Index v1.1

Updated: 19 September 2026

## Core
- Windows, macOS, Linux, Android, Web
- Node/TypeScript, Java/JVM, Python, Rust
- shared contracts and modular package routing

## Enterprise
- DMS control plane
- DMS DTM digital-twin registry
- identity, entitlement, site and audit boundaries

## Digital Twin
- DigitalTwinRef and TwinEvent contracts
- microturbine schema
- bio-composite twin
- BM-11 calibration/active learning
- evidence states T0-T9
- provenance/model-version controls

## Research
- NASA/MIT/open-source registry
- ResearchGate/Emerald discovery
- declassified-document provenance
- patent/prior-art gate
- GitHub provenance/licence gate
- public-release-first discovery protocol

## Extermination protocol
DISCOVER -> PUBLIC-RELEASE-FIRST -> STATIC CHECK -> CONTRACT CHECK -> PLATFORM CHECK -> SECURITY/PROVENANCE CHECK -> TEST -> INDEX -> COMMIT -> RELEASE GATE

## DOS and Firmware
- DOS compatibility layer and runtime matrix
- BIOS/UEFI/Device Tree firmware boundaries
- normalized BootInfo contract
- G01 boot foundation and C header committed
- VM/hosted validation required before physical firmware testing

## Full OS Build
- G00-G29 full build gate matrix
- G01 boot foundation implementation contract executed
- G02 architecture HAL + memory contract added
- Primary first executable target: x86_64 hosted/VM-safe boot harness
- Secondary architecture targets: ARM64, RISC-V64, legacy x86 adapter
- Production completion requires build, boot, runtime, regression, security and provenance evidence

## Simulator Core
- OS-SIM-01/02/03 source-level simulator kernel registered under `packages/biupiu-bevy-adapter/`.
- Bevy is an execution adapter; Core OS remains authoritative.
- Digital Twin, physics, graphics, AI and domain systems route through versioned interfaces.
- OS-SIM-04/05/06/07 remain implementation gates.
- Rust CI workflow added; PASS is withheld until an actual workflow run succeeds.

Architecture is implemented in source/contracts. Native packaging, authenticated DMS transport, physical telemetry, boot execution and production security remain runtime gates.

## G02 Architecture HAL + Memory
- `research/BIUPIU-G02-ARCH-HAL-MEMORY-CONTRACT-v1.0.md`
- `research/BIUPIU-G02-ARCH-HAL-MEMORY.h`
- CPU architecture metadata, page sizing, memory region types, mapping flags and allocation/mapping interfaces defined.
- Alignment, zero-page and overflow checks included in contract helpers.
- **Status: CONTRACT IMPLEMENTED; runtime/VM validation OPEN.**


## OS-UNIX-HARVEST-01 — 19 September 2026
- Unix/Unix-like and microkernel research harvest integrated.
- Reference families: Unix/xv6, NetBSD, OpenBSD, seL4, MINIX, QNX, Redox.
- Open textbook conceptual layer added for OS fundamentals.
- Unix/POSIX concepts are compatibility/reference layers, not the definition of the Core OS.
- Microkernel/service-isolation/capability concepts routed to Core OS architecture.
- AI remains a bounded service layer and cannot bypass Core OS authority.
- Implementation queue OS-G03 through OS-G13 added.
- Checkpoint: `research/checkpoints/OS-UNIX-HARVEST-01.md`.
- Runtime, VM/host and physical firmware validation remain OPEN until execution evidence exists.
