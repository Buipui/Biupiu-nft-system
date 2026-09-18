# Biupiu Pixar Open Animation Technology Stack v1.0

## Purpose

Integrate legally usable open-source animation and scene-interchange technology originating from or maintained by the Pixar/open animation ecosystem into the Biupiu R&D animation, computational-art, character, environment and showreel pipeline.

## Primary components

### 1. OpenUSD
Repository: https://github.com/PixarAnimationStudios/OpenUSD

Use as the principal scene-description/interchange layer for:
- characters and rigs
- environments
- vehicles, aircraft, marine and eVTOL concepts
- cameras and animation
- materials and scene composition
- cross-application asset interchange

OpenUSD is supported on Windows, macOS and Linux and can also be built for WebAssembly and selected Apple targets.

### 2. OpenSubdiv
Repository: https://github.com/PixarAnimationStudios/OpenSubdiv

Use for high-quality subdivision surfaces and smooth production geometry, especially:
- character meshes
- product/vehicle surfaces
- aircraft and marine forms
- complex computational geometry

OpenUSD's build configuration directly integrates OpenSubdiv.

### 3. OpenTimelineIO
Repository: https://github.com/AcademySoftwareFoundation/OpenTimelineIO

Use as the editorial interchange layer for:
- animation sequences
- shot/timeline metadata
- render-to-edit handoff
- showreels
- future Premiere/After Effects integration

OTIO is an interchange/API layer rather than a media container.

## Biupiu integration architecture

Research / computational geometry
        ↓
Blender / modelling / animation
        ↓
OpenSubdiv geometry
        ↓
OpenUSD scene + asset interchange
        ↓
Rendering / simulation / Unreal / other DCC tools
        ↓
Rendered shots
        ↓
OpenTimelineIO editorial timeline
        ↓
Premiere / After Effects / final showreel

## Repository policy

Do NOT copy Pixar films, characters, proprietary assets, textures, branding or other copyrighted/proprietary production material.

The Biupiu repository stores:
- references and integration documentation
- build/integration configuration
- Biupiu-created adapters/scripts
- licence and attribution records
- tests
- links to upstream projects

Upstream source remains under its original repository and licence unless a specific dependency is intentionally vendored and its licence permits that use.

## Compatibility gates

### Windows
Priority target for the Biupiu Windows-based OS/rendering environment.

### Android
OpenUSD should initially be treated as an R&D/portable-runtime target rather than assuming the full desktop toolchain can run directly on Android. Investigate native library builds, WebAssembly and lightweight asset-viewer approaches separately.

### Blender
Use USD as the interchange layer around the Blender pipeline where practical.

### Unreal
Use USD for scene/asset interchange where supported, while keeping Unreal-specific project assets in their native project structure.

### Adobe
Use OpenTimelineIO as an editorial interchange/reference layer around the Adobe showreel pipeline rather than assuming every Adobe application directly consumes OTIO.

## Biupiu application streams

- Character development
- Biupiu World environments
- Product-development visualisation
- Automotive
- Marine
- Aircraft
- eVTOL
- Helicopter
- Microturbine visualisation
- Computational-art/NFT artwork
- Research visualisation
- Investor/showreel production

## Legal/IP gate

Before commercial redistribution, confirm each dependency's current licence, notices and attribution requirements. Do not imply Pixar endorsement or affiliation.

## Upstream references

- OpenUSD: https://github.com/PixarAnimationStudios/OpenUSD
- OpenSubdiv: https://github.com/PixarAnimationStudios/OpenSubdiv
- OpenTimelineIO: https://github.com/AcademySoftwareFoundation/OpenTimelineIO

## Status

**INTEGRATION STATUS: Indexed + architecture integrated.**

Next implementation gate:
1. inspect existing Biupiu Blender/Unreal/Adobe pipeline
2. add USD interchange test assets
3. add OpenSubdiv geometry test
4. add OTIO showreel timeline test
5. run Windows build/integration validation
6. investigate Android-compatible runtime path
7. record licences and dependency versions
