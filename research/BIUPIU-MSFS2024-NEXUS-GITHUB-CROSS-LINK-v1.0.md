# Biupiu Microsoft Flight Simulator 2024 — Nexus Mods × GitHub Cross-Link v1.0

**Simulator:** Microsoft Flight Simulator 2024 (MSFS 2024)  
**Research streams:** AERO / CG-3D / CODEX / AI / DIGITAL-TWIN / VIDEO-SERIES / ROBOTICS  
**Status:** indexed research and integration layer; third-party assets are not redistributed.

## Nexus Mods discovery

Nexus Mods has a dedicated MSFS 2024 mod catalogue. Current indexed examples include aircraft tweaks, EFB modifications, texture tooling, aircraft livery templates, localization and visual presets. The catalogue is separate from the older Microsoft Flight Simulator catalogue, so assets must be tagged by simulator generation.

Notable current examples:
- **EzMods 2024 XCub Plus** — aircraft modification.
- **EzMods XCub Move EFB** — EFB placement modification.
- **EzMods XCub Remove EFB** — EFB removal modification.
- **Texture Converter SDK Package** — community texture-conversion tooling for MSFS 2024 KTX2 workflows.
- **Asobo C172 Livery Template** and **Asobo XCub Livery Template** — livery-authoring references.
- **MS-Milviz DeHavilland DH-2 Livery Template** and **GotFriends Drako Livery Template** — aircraft-specific authoring references.
- **MSFS 2024 Arabic Localization** — experimental localization; Nexus permissions explicitly prohibit redistribution/modification/conversion without permission, so it is a provenance-only reference.
- **Microsoft Flightsimulator 2024 ReshadePreset Yami** — visual/presentation reference; permissions also restrict redistribution/conversion.

These examples demonstrate the main resource classes to monitor: aircraft, cockpit/EFB, liveries/textures, localization, visual presets and development utilities.

## GitHub resources

### Microsoft MSFS avionics source mirror
https://github.com/microsoft/msfs-avionics-mirror

Microsoft's public avionics source mirror contains MSFS 2024 (V2) avionics source. Map to:
AERO → AVIONICS → CODEX → UI/INSTRUMENTATION.

### fsmapper
https://github.com/opiopan/fsmapper

Home-cockpit/virtual-instrument-panel software with explicit MSFS 2024 SDK build requirements. Map to:
COCKPIT → HARDWARE I/O → DIGITAL-TWIN → ROBOTICS.

### MSFS2024_AI
https://github.com/noscapect/MSFS2024_AI

Virtual first-officer project using MSFS 2024 integration and SimConnect/aircraft SDK interfaces. Map to:
AI → AERO → SIMULATION → HUMAN/MACHINE INTERFACE.

### Go SimConnect wrapper
https://github.com/mrlm-net/simconnect

Go wrapper around SimConnect.dll supporting Microsoft Flight Simulator 2020/2024, including SimVar reading/writing/streaming. Map to:
CODEX → SIMCONNECT → DIGITAL-TWIN → TELEMETRY.

### AeroMod
https://github.com/metebykl/aeromod

Open-source external addon manager supporting install/uninstall, enable/disable, integrity checking, search, presets and scenery mapping. Treat as a tooling reference; verify its current MSFS 2024 compatibility before production adoption.

## Cross-link matrix

| MSFS 2024 resource class | Nexus reference | GitHub cross-link | Biupiu destination |
|---|---|---|---|
| Aircraft mods | XCub Plus | avionics mirror / SDK research | AERO |
| EFB/cockpit | XCub EFB mods | fsmapper | COCKPIT / ROBOTICS |
| Textures | Texture Converter SDK Package | asset-pipeline research | CG-3D / MATERIALS |
| Liveries | C172/XCub/DH-2/Drako templates | avionics/asset pipeline | CG-3D / VIDEO-SERIES |
| Visuals | ReShade preset | render pipeline | VIDEO-SERIES / VISUALIZATION |
| Localization | Arabic localization | UI/avionics source | UI / CULTURAL |
| AI pilot | — | MSFS2024_AI | AI / AERO |
| Telemetry | — | SimConnect Go wrapper | DIGITAL-TWIN |
| Addon management | — | AeroMod | SOFTWARE / CODEX |

## Integration rules

1. MSFS 2024 resources remain distinct from FS2002, FS2004, FSX and MSFS 2020.
2. Nexus assets are references until provenance and permissions are verified.
3. No proprietary Microsoft, aircraft-developer or third-party game assets are copied into the repository.
4. Nexus permissions are treated as authoritative for each individual mod.
5. Open-source GitHub code is subject to its own repository licence and dependency licences.
6. Conversion between simulator generations is never assumed to be lossless.
7. Every adopted asset/tool receives simulator version, source URL, creator, licence/permission state, version and hash metadata.
8. MSFS 2024 SDK-dependent functionality remains gated until a validated MSFS 2024 development environment is connected.

## Biupiu pipeline

MSFS 2024 mod/reference → provenance/licence gate → asset/tool classification → SDK/API compatibility check → conversion/interchange manifest → Digital Twin/World asset registry → Unreal/Blender/render pipeline where appropriate → validation → approved derivative.

## Gate

**MSFS24-01 — Nexus/GitHub discovery + cross-link gate: EXECUTED**

Completed:
- MSFS 2024 Nexus catalogue verified.
- Current mod/resource classes identified.
- GitHub avionics, cockpit, AI, SimConnect and addon-management resources cross-linked.
- Licence/provenance restrictions recorded.
- Simulator-generation separation established.

Not claimed:
- No third-party Nexus assets were copied.
- No proprietary SDK/binary was redistributed.
- No live MSFS 2024 rendering or SDK build was executed from this research-only integration.
- Compatibility is not assumed where a resource is not explicitly documented for MSFS 2024.

## Source references

- Nexus MSFS 2024 catalogue: https://www.nexusmods.com/games/microsoftflightsimulator2024/mods
- Nexus MSFS 2024 top mods: https://www.nexusmods.com/microsoftflightsimulator2024/mods/top
- Microsoft avionics mirror: https://github.com/microsoft/msfs-avionics-mirror
- fsmapper: https://github.com/opiopan/fsmapper
- MSFS2024_AI: https://github.com/noscapect/MSFS2024_AI
- SimConnect Go: https://github.com/mrlm-net/simconnect
- AeroMod: https://github.com/metebykl/aeromod

**Version:** 1.0  
**Date:** 19 September 2026
