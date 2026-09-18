# Biupiu Japan Technical Test World — Gate 2 Specification v1.0

Status: READY FOR SANDBOX IMPLEMENTATION
Purpose: validate the integration path before promoting AAA/mod-inspired techniques into production Biupiu World.

## Test scope
Build one isolated, non-production Japan scene containing:
- procedural terrain
- Japanese forest/vegetation layer
- one original settlement
- one original shrine/workshop architectural cluster
- weather and atmospheric state
- one original subscriber avatar
- one original vehicle
- basic NPC population
- world-state save/restore
- one cinematic camera sequence

## Candidate open-source/reference components

### PCG / environment
- EssentialUE5PCG — UE 5.6.1+ examples including landscape forest, paths, rocks and runtime-oriented PCG patterns. Reference candidate; licence review required before redistribution.
- Houdini Engine for Unreal — official SideFX integration; use as the procedural authoring adapter, not as a copied third-party asset bundle.
- Unreal Engine's native PCG examples/documentation — baseline implementation.

### AI / avatar
- NVIDIA ACE — research/integration reference for digital-human and avatar AI pipelines.
- Convai Unreal Engine SDK — research reference for multiplayer AI-avatar interaction and environment awareness; licensing/service terms must be reviewed.
- Ready Player Me Unreal examples — reference for avatar-creator web integration; use only if its current licensing and service availability fit Biupiu.
- OpenRigLogic — core rig-evaluation research already identified for the avatar pipeline.

### World/AAA research
- Assassin's Creed Shadows — Japan visual/environment reference only.
- Ghost of Tsushima — Japan landscape/atmosphere reference only.
- Forza Horizon 6 — modern Japan/automotive reference only.
- Red Dead Redemption 2 — weather/environment-state reference only.
- Cyberpunk 2077 — dense urban/night/material reference only.

## Compatibility rules
1. Canonical Biupiu world data remains engine-neutral where practical.
2. OpenUSD remains the preferred interchange layer.
3. Unreal is the interactive world runtime target.
4. Houdini/PCG are authoring/generation layers.
5. Third-party repositories remain sandboxed until licence and dependency checks pass.
6. Game mods are technique/reference sources; proprietary game assets do not enter the production asset registry.
7. Every test asset receives a Biupiu Asset ID and provenance record.
8. Android/mobile variants must be treated as a separate performance tier.

## Test metrics
- CPU frame time
- GPU frame time
- FPS
- memory
- VRAM
- world-cell load time
- PCG generation time
- avatar load time
- save/restore latency
- network replication cost
- cinematic render time
- final EXR size
- mobile fallback performance

## Pass criteria
PASS requires: stable scene loading; deterministic enough procedural results for reproducible builds; no rights contamination; working avatar; working weather state; working persistence; acceptable frame-time budget for the target tier; successful cinematic render; documented provenance.

## Promotion path
Sandbox → compatibility report → licence review → performance profile → Biupiu adapter → production package.

## Initial package targets
- BIUPIU-WORLD-JAPAN-FEUDAL
- BIUPIU-WORLD-JAPAN-MODERN
- BIUPIU-WORLD-JAPAN-FUTURE
- BIUPIU-AVATAR-CORE
- BIUPIU-WEATHER-CORE
- BIUPIU-PCG-WORLD-CORE
- BIUPIU-CINEMATIC-CORE