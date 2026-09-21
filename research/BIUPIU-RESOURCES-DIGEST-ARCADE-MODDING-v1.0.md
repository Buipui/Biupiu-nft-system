# Biupiu Resources Digest — Arcade, Modding & Native Runtime v1.0

**Date:** 21 September 2026

## Purpose

Cross-reference official upstream resources and convert them into Biupiu-native development targets. This digest is a research index, not an approval to redistribute third-party games or execute untrusted packages.

## Official reference resources

| Resource | Official reference | Biupiu use | Boundary |
|---|---|---|---|
| MAME | https://github.com/mamedev/mame | Arcade and multi-system emulation study; adapter candidate | Emulator licence does not grant ROM rights; MAME trademark restrictions apply |
| DOSBox Staging | https://github.com/dosbox-staging/dosbox-staging | Legacy PC/DOS runtime study | GPL-2.0-or-later plus third-party licence review; games remain separate |
| ScummVM | https://github.com/scummvm/scummvm | Adventure/legacy runtime study | GPL obligations and individual game-data rights |
| OpenTTD | https://github.com/OpenTTD/OpenTTD | Open-source simulation reference and possible showcase | Review core and baseset licences before packaging |
| GitHub licensing guidance | https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository | Licence detection and repository policy | Dependencies and absent licences require separate review |

## OpenBooks / open-resource cross-reference

The research process should search open-book and open-access material for:

- emulator architecture and preservation
- game-engine design
- virtual economies and multiplayer sessions
- modding governance and creator licensing
- software supply-chain security
- digital preservation and museum interfaces
- open-source licensing and SPDX identifiers

No single open-book catalogue is treated as a licence authority. Each source is recorded with URL, author/publisher, date, licence/access terms, evidence class and intended use.

## Native Biupiu systems to build

1. `NativeResourceRegistry` — resource metadata and rights states.
2. `BiupiuArcadeRuntime` interface — platform-neutral launch/session contract.
3. `BiupiuModdingStation` — creator project wizard and submission workflow.
4. `RightsGate` — fail-closed commercial-use and redistribution checks.
5. `CompatibilityGate` — engine/platform/version checks.
6. `SecurityGate` — static inspection, capability declarations and future sandbox boundary.
7. `ProvenanceLedger` — creator, source, dependency, version and hash lineage.
8. `SessionManager` — avatar, cabinet, controller and multiplayer session lifecycle.
9. `ModHubAdapter` — Unreal, Unity and future Biupiu Engine metadata adapters.
10. `DigitalMuseumIndex` — historical title metadata without unlicensed game binaries.

## Proposed native data flow

`Creator/Curator -> Resource Registry -> Licence Declaration -> Static Validation -> Dependency Check -> Compatibility Check -> Security Review -> Human Approval -> Isolated Preview -> Publication -> Versioned Provenance`

## Promotion gates

- **REGISTERED:** resource or architecture recorded.
- **IMPLEMENTED:** code exists and local tests are added.
- **VERIFIED:** rights, security, compatibility and runtime tests pass.
- **RELEASED:** approved content is distributed under documented terms.

## Current state

- Architecture: REGISTERED.
- Native TypeScript contracts: IMPLEMENTED PARTIAL.
- In-memory registry: IMPLEMENTED PARTIAL.
- Unreal/Unity runtime adapters: NOT IMPLEMENTED.
- Sandbox execution: NOT IMPLEMENTED.
- External game redistribution clearance: NONE CLAIMED.
- Independent tests and CI: PENDING.

## Source notes

The official MAME repository describes MAME as a multi-purpose emulation framework and identifies GPL-2.0+ licensing with additional per-file licences. DOSBox Staging documents GPL-2.0-or-later and third-party exceptions. OpenTTD documents GPL-2.0 with additional component licences. GitHub documentation warns that a public repository without a licence remains under default copyright rules.
