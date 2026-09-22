# Biupiu NFT vs World Repository Placement Audit — 2026-09-22

## Repository finding
`Buipui/Buipui-World` currently exists as a private repository but is empty at the Git repository tree level. The substantive World implementation therefore currently resides in `Buipui/Biupiu-nft-system/world/`.

This is a **repository-boundary issue, not proof of incorrect module ownership**. Moving files before the World repository has a governed structure would create duplicate authorities.

## Correct ownership model

### NFT / core repository
Keep:
- NFT contracts and blockchain integration
- provenance/certificate logic
- core OS/AI contracts
- shared simulator/federation contracts
- research evidence and manifests
- World adapter contracts
- World resource indices and integration specifications

### Biupiu World repository
Target home once initialized:
- executable World client/runtime
- UE5 project
- Blender/OpenUSD production assets
- environment builds
- World-only UI/client code
- packaged World content
- World runtime tests
- platform-specific World deployment

### Shared boundary
Never duplicate authoritative implementations. Use versioned contracts/adapters:
CORE/RESEARCH -> FEDERATION CONTRACT -> WORLD ADAPTER -> WORLD RUNTIME

## Simulator separation
Department simulators remain domain-owned. World consumes their versioned state/observations through adapters.

Do not merge:
- automotive physics into World
- marine physics into World
- farming solver into World
- NFT logic into simulator physics
- speculative World scenarios into validated engineering solvers

World may visualise/replicate results, but simulator authority stays with its domain module.

## Housekeeping actions
- Marked current World material as CORE_RESEARCH/ADAPTER vs WORLD_RUNTIME candidate.
- Added a single placement map rather than copying existing World modules.
- Kept speculative scenarios under `world/speculative/` and separate from validated simulation.
- Kept external assets behind rights/provenance classes.
- Kept NFT/accounting functions optional adapters rather than embedding financial authority in World.

## Result
No destructive moves were made because the destination repository is empty. The correct next migration gate is to initialise `Buipui/Buipui-World` with the governed contract and runtime skeleton, then migrate only files classified WORLD_RUNTIME.
