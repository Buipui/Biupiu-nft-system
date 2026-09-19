# Biupiu FS2002 Nexus Mods × GitHub Cross-Link v1.0

**Research stream:** CODEX / COMPUTE / CG-3D / AERO / DIGITAL-TWIN / VIDEO-SERIES  
**Simulator:** Microsoft Flight Simulator 2002 (FS2002)  
**Status:** indexed research/resource layer; no third-party assets copied or redistributed.

## Scope

This record cross-links historically relevant FS2002 modification/content-creation material found through Nexus Mods with open-source GitHub tooling that can support preservation, analysis, conversion, cockpit/input integration, scenery inspection, and future Biupiu digital-twin/world-building workflows.

## Nexus Mods findings

A direct Nexus Mods FS2002 game-mod catalogue was not identified in the current Nexus index. Nexus currently exposes a dedicated Microsoft Flight Simulator catalogue, but that catalogue is for the modern Microsoft Flight Simulator product rather than the 2002 simulator. Therefore modern MSFS Nexus mods must **not** be treated as FS2002-compatible assets.

A historically relevant Nexus-hosted reference was found: the Nexus GMax documentation identifies **Microsoft Flight Simulator 2002 Pro Edition** as a GMax-ready game. This is useful as a content-authoring/pipeline reference rather than evidence of a current FS2002 mod package.

Reference:
- Nexus Mods GMax documentation: https://www.nexusmods.com/oblivion/mods/13260?tab=docs

## GitHub cross-links

### 1. MakeRunways
Repository: https://github.com/jldowson/MakeRunways

Purpose:
- Reads active scenery from SCENERY.CFG.
- Produces airport/scenery data for multiple flight-sim utilities.
- Explicitly supports FS2002, FS2004, FSX, P3D and MSFS.
- Useful as a legacy-scenery metadata extraction/validation component.

Biupiu mapping:
`FS2002 → SCENERY.CFG → airport/scenery metadata → CODEX/DIGITAL-TWIN`

### 2. FS2XPlane
Repository: https://github.com/Marginal/FS2XPlane

Purpose:
- Processes legacy Microsoft Flight Simulator scenery.
- Includes explicit handling for FS2002-era BGL scenery.
- Useful for studying legacy BGL structures and conversion limitations.

Biupiu mapping:
`FS2002 BGL → legacy scenery parser/converter → CG-3D / DIGITAL-TWIN`

### 3. OpenXPUIPC
Repository: https://github.com/1090MHz/OpenXPUIPC

Purpose:
- Contains FSUIPC offset/protocol work.
- Includes FS2002/FS2004 compatibility notes and simulation-state mappings.
- Useful for researching interoperability with older simulator state interfaces.

Biupiu mapping:
`FS2002 state/FSUIPC → interoperability adapter → CODEX / SIMULATION`

### 4. OpenTrack
Repository: https://github.com/opentrack/opentrack

Purpose:
- Head/pose tracking.
- Its supported-game data explicitly contains Microsoft Flight Simulator 2002.
- Useful for legacy cockpit/view-control experiments.

Biupiu mapping:
`FS2002 → OpenTrack → camera/view input → COCKPIT / IMMERSION`

### 5. Crosswind
Repository: https://github.com/cdahmedeh/Crosswind

Purpose:
- Modern bridge tooling for older flight simulators.
- Its compatibility table explicitly lists Microsoft Flight Simulator 2002 through FSUIPC2, although FS2002 is currently marked untested.
- Useful as a research lead for legacy-simulator interoperability, not as a validated FS2002 production dependency.

Biupiu mapping:
`FS2002/FSUIPC2 → modern flight-planning interoperability research`

### 6. Microsoft KB archive references
Repository: https://github.com/jeffpar/kbarchive

Relevant indexed material includes historical Microsoft Knowledge Base entries concerning FS2002 autopilot behaviour and scenery-read errors. These are useful as period technical documentation for preservation/debugging.

Biupiu mapping:
`period documentation → compatibility/failure knowledge → FAILURE / CODEX`

## Cross-link matrix

| FS2002 area | Nexus/GMax reference | GitHub resource | Biupiu stream |
|---|---|---|---|
| 3D content creation | GMax FS2002-ready reference | FS2XPlane | CG-3D / AERO |
| Scenery | Historical authoring context | MakeRunways | DIGITAL-TWIN / CG-3D |
| BGL analysis | Historical FS2002 pipeline | FS2XPlane | CODEX |
| Simulator state | — | OpenXPUIPC | COMPUTE / SIMULATION |
| Head tracking | — | OpenTrack | COCKPIT / IMMERSION |
| Flight-planning bridge | — | Crosswind | CODEX |
| Legacy troubleshooting | — | Microsoft KB archive | FAILURE |

## Compatibility rules

1. FS2002 assets must remain separately classified from FS2004, FSX, MSFS 2020 and MSFS 2024 assets.
2. A modern MSFS Nexus mod is not automatically portable to FS2002.
3. GitHub code is reusable only according to its repository licence and dependency licences.
4. Third-party aircraft, scenery, textures, meshes and proprietary game files must not be copied into the Biupiu repository without rights/licence review.
5. Conversion tools may be indexed and tested without redistributing copyrighted source assets.
6. Any future converted asset receives source, author, licence, original simulator, target simulator, conversion tool/version and hash metadata.
7. FS2002 research is a preservation/interoperability track; it does not override the repository's modern Unreal/Blender/render-pipeline architecture.

## Proposed integration path

`FS2002 source/mod reference → provenance/licence check → asset-type classification → BGL/model/texture/input analysis → compatible open-source tooling → conversion test → hash + manifest → Biupiu Digital Twin / World asset registry`

## Gate status

**FS2K2-01 — discovery/cross-link gate: EXECUTED**

Completed:
- Nexus FS2002 availability checked.
- Nexus GMax/FS2002 authoring reference identified.
- GitHub FS2002-relevant tooling identified.
- Compatibility boundaries documented.
- Cross-link matrix created.

Not claimed:
- No FS2002 Nexus mod was identified as a verified current downloadable FS2002 package.
- No third-party game files were imported.
- No compatibility with a live FS2002 installation has been tested.
- No conversion or visual-equivalence result has been claimed.

## Sources

- Nexus Mods GMax documentation: https://www.nexusmods.com/oblivion/mods/13260?tab=docs
- MakeRunways: https://github.com/jldowson/MakeRunways
- FS2XPlane: https://github.com/Marginal/FS2XPlane
- OpenXPUIPC: https://github.com/1090MHz/OpenXPUIPC
- OpenTrack: https://github.com/opentrack/opentrack
- Crosswind: https://github.com/cdahmedeh/Crosswind
- Microsoft KB archive: https://github.com/jeffpar/kbarchive

**Version:** 1.0  
**Date:** 19 September 2026
