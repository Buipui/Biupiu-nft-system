# Biupiu Blender Engine Registry v1.0

## Windows
- Engine: official Blender upstream
- Source: https://github.com/blender/blender
- Role: primary desktop authoring, Digital Twin visualization, environment/character production and showreel rendering.
- Update rule: pin a verified release or commit before production use.

## Android
- Engine: reviewed Blender Android fork
- Source: https://github.com/Wanderson-Magalhaes/blender_for_android
- Role: mobile modelling, inspection, lightweight rendering and Digital Twin interaction.
- Update rule: pin a verified commit and run Android build/runtime gates.

## Architecture rule
The two engines share Biupiu Digital Twin contracts and asset provenance, but remain independently deployable. Blender is an engine layer, not the canonical research database.
