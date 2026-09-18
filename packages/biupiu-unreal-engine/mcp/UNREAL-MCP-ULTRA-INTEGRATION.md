# Unreal-MCP-Ultra Integration

## Source
- Upstream: https://github.com/hoodtronik/Unreal-MCP-Ultra
- Reference PR: https://github.com/hoodtronik/Unreal-MCP-Ultra/pull/5
- PR: dual-engine UE 5.6.1 / UE 5.8.1 compatibility groundwork
- Current integration mode: external dependency/reference; no upstream source is copied into Biupiu.

## Biupiu role
Unreal-MCP-Ultra is mapped as the AI/editor automation bridge between the Biupiu R&D OS and an installed Unreal Engine 5 environment.

Biupiu R&D OS -> MCP adapter -> Unreal Editor -> Digital Twin / Product Visualization / Simulation

## Compatibility contract
The referenced PR establishes a shared-source compatibility direction for UE 5.6.1 and UE 5.8.1. Its documented gates include:
1. UBT compile
2. link
3. real editor load
4. MCP server startup/binding
5. TypeScript test suite
6. tool registration
7. Blueprint read/mutation smoke
8. DataAsset/UserDefinedStruct smoke
9. material validation smoke
10. animation mutation smoke
11. PIE/runtime tool smoke
12. vision/capture smoke

The upstream PR explicitly states that compile/link success alone is not sufficient for merge readiness.

## Known compatibility points
- Engine/UserDefinedStruct.h -> StructUtils/UserDefinedStruct.h
- UMaterial::GetMaterialResource() requires version-aware handling because the signature differs before/after UE 5.7.
- UE 5.8 JSON FSharedString keys require compatible rebuilding at affected TMap::Add sites.
- Mass/MassCore is an engine-version-sensitive dependency and must not be assumed present on UE 5.6.

## Biupiu integration rules
- Keep Unreal Engine itself external and EULA-compliant.
- Do not copy Epic engine source or restricted binaries into this repository.
- Keep the MCP adapter/version manifest under Biupiu control.
- Treat upstream PR #5 as compatibility evidence, not as permission to bulk-import the upstream fork.
- Prefer one shared Biupiu integration contract with engine-specific adapters/configuration.
- Require runtime validation before marking an engine target verified.

## Intended Biupiu consumers
- Digital-twin scenes
- regenerative-farming environments
- Biupiu World
- biomaterials/product visualization
- microturbine engineering visualization
- marine/automotive/eVTOL concept visualization
- AI-assisted environment and character workflows
- simulation and capture pipelines
