# UE5-INTEGRATION-GATE-v1.0

## Status
Foundation architecture executed. No Unreal Engine source is copied or redistributed by this gate.

## Scope
This gate establishes Unreal Engine 5 as an external engine/runtime integration for Biupiu R&D OS, with explicit mappings for World, Digital Twin, Research, Simulation and Showcase.

## Execution rules
1. Keep UE5 source/toolchain external and EULA-compliant.
2. Keep canonical research and validated numerical simulation data outside UE.
3. Use UE5 for visualization, interactive worlds, digital-twin presentation and cinematic/product showcase.
4. Preserve third-party asset provenance and licence metadata.
5. Pin exact UE5/toolchain versions before release builds.
6. Treat Android as a packaged runtime target; Windows remains the primary UE development target.

## Cross-package mapping
| Existing Biupiu area | UE5 integration |
|---|---|
| biupiu-main-hub | launcher/control integration |
| biupiu-rnd-os | core data/API bridge |
| biupiu-research-lab | research visualization |
| biupiu-showcase | cinematic/showcase runtime |
| biupiu-civilisation-world | interactive world |
| biupiu-smart-farming | regenerative-farming digital twins |
| biupiu-smart-metallurgy | materials/manufacturing visualization |
| biupiu-nft-studio | 3D asset/NFT presentation |
| biupiu-access | access boundary |
| biupiu-shared | schemas/contracts |
| digital-twin | UE adapter layer |
| simulators | simulation-result visualization |
| world | levels/environments |
| showcase | asset/render pipeline |

## Gate result
The repository now has a documented UE5 integration boundary and adapter structure. Actual UE projects/plugins and packaged binaries remain a subsequent implementation gate.
