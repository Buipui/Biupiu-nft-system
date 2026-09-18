# SF-17 — Mod-Site Asset Audit for Biupiu Department Showcases

Date: 2026-09-18

## Scope
Audited Alan Wake 2, Microsoft Flight Simulator 2020, Battlefield V, Hell Let Loose and Arma 3 mod ecosystems for later reference when creating Biupiu department advertising vehicles and environments.

## Findings

### Alan Wake 2
Nexus contains useful modding infrastructure and visual techniques, but checked asset permissions are not generally suitable for commercial cross-game reuse. One Alan Wake 2 mod requires permission for asset use and prohibits use in sold files. A separate mod loader is MIT-licensed and allows asset use/conversion under its own licence, but that does not grant rights to Remedy/game assets. 
Classification: RESEARCH / TOOLING REFERENCE; no game asset import.

### Microsoft Flight Simulator 2020
Microsoft's official SDK explicitly supports creation of original aircraft/world assets and distribution through Microsoft Marketplace or third-party distribution services. This is valuable as a reference for Biupiu's aircraft packaging, world packages, manifests and asset pipeline. Community mods remain individually licensed and must be assessed per asset.
Classification: ORIGINAL-ASSET PIPELINE REFERENCE; individual community assets require licence review.

### Battlefield V
Checked Nexus examples include Battlefield Airborne and Pacific Overhaul. Their permissions require author permission for asset use, prohibit conversion, and prohibit use in sold mods/files. 
Classification: RESEARCH-ONLY for proprietary/mod assets.

### Hell Let Loose
The official EULA grants a limited licence for personal, non-commercial use and expressly restricts reverse engineering/copying/transmission and similar activities. 
Classification: RESEARCH-ONLY; do not extract or reuse game assets.

### Arma 3
Bohemia publishes explicit content licences. The APL-ND includes noncommercial and Arma-only restrictions, and the Arma 3 EULA restricts commercial exploitation and distribution of the program. Therefore Arma assets are not automatically suitable for a commercial Biupiu World. 
Classification: RESEARCH-ONLY unless an exact asset has a separate licence compatible with Biupiu.

## Practical conclusion
No checked game/mod asset is automatically approved for Biupiu's commercial advertising world.

The useful route is:
1. Study the games for vehicle categories, world composition, aircraft presentation, boats, off-road vehicles, terrain, lighting, navigation and streaming.
2. Identify individual third-party assets only when their exact licence permits commercial use, modification and redistribution outside the original game.
3. Prefer original Biupiu models for department showcases.
4. Maintain documentary provenance and licence evidence for every external asset.

## Biupiu showcase priority
- Aircraft: original Biupiu aircraft/EVTOL concepts, using Flight Simulator SDK architecture as reference.
- Marine: original Biupiu boats/hydrofoils.
- Off-road: original Biupiu regenerative-agriculture/conservation vehicles.
- Logistics: original Biupiu low-emission fleet.
- Research: original mobile laboratories.
- Advertising: each vehicle links to its department, research, products, Academy, Digital Lab and enquiry page.

## Evidence
Nexus Mods states that copyrighted game content requires appropriate permission, and its Terms restrict commercial use of site material without a licence. citeturn0search9turn0search11
