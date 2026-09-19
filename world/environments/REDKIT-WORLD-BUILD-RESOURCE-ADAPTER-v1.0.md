# REDkit / WolvenKit World-Build Resource Adapter v1.0

## Purpose
Use the open Witcher 3 world-building ecosystem as a **method/reference layer** for Biupiu World asset construction, not as a source of copied proprietary game assets.

## Verified references
- CD PROJEKT RED REDkit: new-world workflow, terrain, vegetation, lighting, water, navigation and scene workflows.
- WolvenKit-7: open-source research/modding toolkit for REDengine 3 file formats.
- Witcher3-Blender-Tools: Blender interoperability and asset inspection workflow.

## Biupiu use
Translate reusable *methods* into Biupiu-native assets:
- terrain tiles -> deterministic Biupiu terrain generator
- vegetation painting -> procedural vegetation placement
- world scene -> modular environment manifest
- navigation data -> Biupiu navigation/collision metadata
- lighting/weather -> renderer-neutral environment parameters
- object placement -> modular prop blueprints
- reference-level workflow -> internal asset validation scene

## IP boundary
Do not copy or rehost Witcher 3 proprietary meshes, textures, audio, characters, animations, world files or extracted game assets. Third-party repositories remain external references until licence/security/compatibility review. Biupiu assets created from these methods must be original.

## Next gate
Generate original Main Hub/Farming/Metal-Making prop blueprints and procedural terrain/material specifications from the adapter contract.
