# Biupiu World — AAA Game & Mod Development Research Index v1.0

Purpose: Track AAA games and community modifications that can teach Biupiu how to build original world, rendering, character, vehicle, weather and immersion systems.

## Rule
Use game/mod projects as technical and visual references. Do not copy or redistribute proprietary game assets, extracted maps, characters, textures, sounds or other protected material unless rights explicitly permit it.

## Priority reference matrix
| Reference | Study for | Biupiu implementation |
|---|---|---|
| Assassin's Creed Shadows | Japan terrain, settlements, architecture, vegetation, historical atmosphere | Original Japan biome + architecture generator |
| Ghost of Tsushima | wind, grass, fog, weather, colour, Japanese landscape cinematography | Japan atmosphere/weather/vegetation system |
| Forza Horizon 6 | Tokyo/modern Japan, roads, traffic, urban/suburban/industrial presentation | Modern Japan + automotive world package |
| Red Dead Redemption 2 | weather state, environmental persistence, vegetation, wetness, fog, sky/light transitions | Global weather/season/environment-state system |
| Cyberpunk 2077 | dense urban night lighting, signage, props, Japanese/cyber-urban presentation | Biupiu future-city visual/lighting system |
| Skyrim / Fallout mod ecosystems | plugin/mod architecture, world extensions, NPC/quest/environment frameworks | Sandbox/mod manager research |
| Unreal open-world projects | World Partition, PCG, streaming, runtime systems | Biupiu World runtime architecture |

## Mod techniques to extract
### Visual
- tone mapping
- ReShade/shader pipelines
- colour grading
- fog density
- volumetrics
- reflections
- wet surfaces
- shadow quality
- LOD/geometry detail
- vegetation density
- sky/cloud systems

### World
- biome rules
- population/scattering
- procedural roads
- settlement generation
- world streaming
- dynamic world state
- seasonal transitions

### Characters
- model replacement workflows
- rigging
- facial animation
- clothing/material variants
- NPC population
- avatar customisation

### Vehicles
- vehicle handling architecture
- traffic population
- camera/photo mode
- damage/visual states
- automotive environment composition

### Immersion
- weather
- time of day
- ambient audio
- wildlife
- NPC routines
- environmental interaction
- persistent state

## Current concrete findings
Ghost of Tsushima: community visual work includes photorealistic presets and shader/tone-map adjustments; one package describes reducing heavy darkening and adding asset definition. These are useful references for Biupiu's Japan cinematic look.

Red Dead Redemption 2: current community weather/visual projects demonstrate persistent weather profiles, smooth transitions, localized climate behaviour, fog/cloud evolution, wind, rain/snow effects, wetness and lighting changes. These techniques are relevant to a reusable Biupiu World climate system.

Cyberpunk 2077: current mod examples show texture/prop replacement workflows and Japanese-themed urban presentation; permissions can explicitly prohibit asset reuse/conversion, so these are reference-only unless permissions say otherwise.

Unreal mod platforms: open-source projects such as Aurora demonstrate PAK/Lua/Blueprint-oriented mod-loading concepts for Unreal Engine games and are useful as mod architecture references.

## Research output format
For each reference: Game; Mod/tool; System being studied; Technical mechanism; Licence/rights; Biupiu equivalent; Integration target; Test scene; Performance impact; Production status.

## Priority
P0 — Unreal/PCG/Houdini/open-world foundations
P1 — Japan environment/weather/vegetation/vehicle systems
P1 — avatar/character/animation systems
P1 — cinematic rendering/lighting/materials
P2 — multiplayer/persistence/mod manager
P2 — XR/Pixel Streaming
P3 — experimental techniques