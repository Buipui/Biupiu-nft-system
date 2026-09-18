# Mod Index Integration

The Mod Index is treated as the sandbox content-control layer for civilisation environments.

The current repository search did not expose a standalone Mod Index source file, so this phase defines a compatible adapter contract rather than inventing missing source data.

## Adapter contract
Each environment package may expose:
- environment_id
- mod_id
- asset_manifest
- allowed_interactions
- evidence_class
- reconstruction
- dependencies
- version
- permissions

## Sandbox rule
Mods can add models, quests, crops, tools, educational objects or scenarios without modifying the historical source record.

## Validation
1. schema validation
2. dependency check
3. evidence classification
4. asset provenance check
5. interaction permission check
6. performance tier check

Speculative mods inherit the SPECULATIVE badge.
