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

## Extermination protocol
DISCOVER -> STATIC CHECK -> CONTRACT CHECK -> PLATFORM CHECK -> SECURITY/PROVENANCE CHECK -> TEST -> INDEX -> COMMIT -> RELEASE GATE

Architecture is implemented in source/contracts. Native packaging, authenticated DMS transport, physical telemetry and production security remain runtime gates.


## Simulator Core

- OS-SIM-01/02/03 source-level simulator kernel registered under `packages/biupiu-bevy-adapter/`.
- Bevy is an execution adapter; Core OS remains authoritative.
- Digital Twin, physics, graphics, AI and domain systems route through versioned interfaces.
- OS-SIM-04/05/06/07 remain implementation gates.
- Rust CI workflow added; PASS is withheld until an actual workflow run succeeds.
