# Biupiu Arcade & Emulation Resource Architecture v1.0

## Purpose

Create a rights-aware foundation for future Biupiu World virtual arcades, retro-computing rooms, console rooms, PC rooms, museums and developer showcases.

This document converts the current emulator/modding research into a **Biupiu-native architecture**. External emulators and legacy games are treated as compatibility/reference resources, not as the permanent core of Biupiu World.

## Core principle

**Biupiu owns and develops the environment, orchestration, metadata, provenance, rights registry, creator system and future native runtime.**

External software may be an adapter/resource where its licence permits.

Target flow:

`Biupiu World -> Biupiu Arcade Runtime Interface -> Rights/Provenance Gate -> Platform Adapter -> Licensed Game/Native Game`

## Platform abstraction

Initial adapter targets:

- Arcade
- DOS/legacy PC
- Adventure/SCUMM-style legacy systems
- Open-source PC games
- Retro console systems where a lawful redistribution/runtime path is established
- Unreal community content
- Unity community content
- Future Biupiu Engine content

The platform adapter must never assume that an emulator licence grants rights to the game data.

## Rights states

Every external title/resource receives one state:

- GREEN — redistribution/use rights verified for the intended Biupiu use
- BLUE — free/open but licence scope requires review
- YELLOW — identifiable rights holder; permission/licence required
- ORANGE — ownership/chain-of-title investigation required
- RED — no approved Biupiu use
- GREY — research/reference only

No title enters a distributable Biupiu build without a GREEN determination or documented legal approval.

## Native conversion strategy

External ecosystems are used to learn requirements and test interaction models.

Biupiu-native replacements should progressively cover:

1. Arcade cabinet interaction framework
2. Game launcher/session manager
3. Virtual coin/token/session logic
4. Controller/input abstraction
5. Save/state interface
6. Multiplayer/session discovery
7. Leaderboards
8. Mod loading
9. Creator identity
10. Asset/version/dependency registry
11. Rights/provenance registry
12. Telemetry/analytics with privacy controls
13. Digital museum metadata
14. Biupiu Engine runtime adapter

The goal is not to reproduce proprietary game code. The goal is to build **Biupiu-owned infrastructure around legally usable content**.

## Virtual arcade interaction

Reference interaction:

Avatar approaches cabinet -> cabinet identifies available title -> rights gate checks entitlement -> runtime adapter launches title -> session starts -> player exits -> result/state is recorded.

For a native Biupiu game:

Avatar -> Biupiu Arcade Runtime -> native executable/module -> Biupiu DMS/session layer.

## Emulator policy

Approved open-source emulators may be evaluated as development/compatibility components subject to their individual licences.

Examples investigated:

- MAME
- DOSBox
- ScummVM
- Open-source/open-game runtimes

The repository must store the exact upstream version, licence, source URL, build configuration, patches and compatibility status for every adopted component.

## No abandonware shortcut

Publisher closure, bankruptcy, lack of sales, age of a game or availability on an archive does not by itself establish public-domain or commercial redistribution rights.

Unknown ownership remains UNKNOWN.

## Biupiu-native long-term target

**Biupiu Arcade SDK**

- IArcadeCabinet
- IGamePackage
- IGameRuntime
- IInputProfile
- ISession
- ILeaderboard
- IModPackage
- ICreator
- IRightsRecord
- IProvenanceRecord

The same interfaces should work inside Unreal, Unity and eventually Biupiu Engine.

## Verification gates

### REGISTERED
Architecture, rights states and adapter interfaces documented.

### IMPLEMENTED
A native prototype can register a game package, verify metadata and launch an approved runtime.

### VERIFIED
The complete flow has passed licence, dependency, compatibility, security and runtime tests.

### RELEASED
Only rights-cleared content and approved software versions are shipped.

**Current status: REGISTERED.**
