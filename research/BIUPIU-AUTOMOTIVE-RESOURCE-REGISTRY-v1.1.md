# Biupiu Automotive / Car Mechanic Simulator Resource Registry v1.1

**Date:** 21 September 2026  
**Status:** HARVESTED / CROSS-LINKED / RIGHTS-GATED

## 1. Search scope

The 2022–2026 research pass covered public GitHub, Steam Workshop/Nexus-style mod ecosystems, automotive digital-twin projects, foreign-language discovery and open engineering references. The registry records reusable ideas, interfaces and licence-compatible source candidates—not wholesale game assets.

## 2. Car Mechanic Simulator 2021

- Steam Workshop: current community categories include cars, configs, liveries, texture packs, maps, bonus parts and localisation. citeturn0search10
- Nexus Mods: active CMS 2021 mod catalogue. citeturn1search0
- GitHub examples include GPL-3.0 TransferAll and MIT RealShop/CMS21-Together projects. These are useful for studying inventory automation, repair/economy rules and multiplayer boundaries, subject to licence and dependency review. citeturn1search10turn1search14turn1search11
- Integration target: diagnosis -> parts graph -> work order -> disassembly/assembly -> repair risk -> inventory -> validation -> Digital Twin.

## 3. Racing/game families

### Assetto Corsa
Open tooling demonstrates extraction/analysis of car data and suspension configuration. AssettoCorsaTools and assetto-tools are MIT-licensed examples. citeturn2search8turn2search13

### Gran Turismo
Public modding guides expose structured data/script workflows for PS3-era GT5/GT6 and related toolchains. They remain research references; proprietary game data is not imported. citeturn0search4turn2search11

### Need for Speed
NFSTools provides public tooling for Speed-engine NFS games, including VaultLib and Attribulator for VLT/AttribSys data. citeturn2search3

### Crash Team Racing
CTR-tools provides a C mod SDK/decompilation project; ctr-native demonstrates a native Windows/Linux port with a clean platform boundary and static SDL3 build. This is a useful architectural reference for Biupiu native portability. citeturn2search0turn2search4

### GTA
Public tooling exists for vehicle metadata/package workflows, including tools for combining GTA V vehicle meta files. These are reference-only unless individual licences and game terms permit reuse. citeturn2search14

### Forza
The Forza Mods GitHub organisation publishes open-source mod tooling including Forza-Mods-AIO and SaveTools. These remain external tooling references, not embedded dependencies. citeturn0search1

## 4. Open vehicle / Digital Twin stack

- CARLA provides open-source vehicle/sensor simulation and open digital assets under its published licensing model; the current project has UE5.5 and UE4.26 development branches. citeturn0search5
- OpenADS/OpenADSim provides an open modular simulation framework around CARLA. citeturn2search6turn2search9
- CARLA Digital Twins provides a UE5 plugin with OpenDRIVE/map workflows and Python/editor integration. citeturn0search6
- McSCert Automotive-Digital-Twin implements an ISO 23247-based architecture and is Apache-2.0. citeturn1search15

## 5. Foreign-language lane

Search routing was added for Chinese, German, Italian, Japanese, French, Spanish, Portuguese and Russian terminology around vehicle repair, vehicle dynamics, mechatronics, digital twins, CAD, telemetry and simulation.

Language is discovery metadata only. It does not confer authority, correctness or redistribution rights.

## 6. Biupiu native integration

The following source-level native boundary is now registered:

`core/multilang/include/biupiu_automotive_sim.h`  
`core/multilang/cpp/automotive_sim.cpp`  
`core/multilang/cpp/automotive_sim_smoke.cpp`

The initial kernel is a deterministic longitudinal force-balance model with validation of inputs and explicit output state. It is intentionally dependency-light so it can sit beneath UE5, Digital Twin and simulator adapters.

## 7. Rights / safety boundary

Do not copy or redistribute proprietary game binaries, extracted game assets, copyrighted vehicle models/textures/audio, manufacturer manuals or manufacturer IP. Build clean-room interfaces and original Biupiu assets around documented behaviour where licence status is uncertain.

No simulator output authorises real-world vehicle repair. Real maintenance remains governed by approved service data and qualified personnel.

## 8. Promotion state

**HARVESTED:** external resource families cross-linked.  
**INTEGRATED:** native automotive contract and deterministic core source added.  
**RUNTIME VERIFIED:** not yet claimed; host build, unit execution, UE5 integration, third-party backend execution and HIL remain open gates.
