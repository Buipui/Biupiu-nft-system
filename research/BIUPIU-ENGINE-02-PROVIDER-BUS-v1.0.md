# ENGINE-02 — Native Provider Bus

**Status:** IMPLEMENTED at source/contract level

## Architecture
`Biupiu Engine -> Provider Bus -> Simulation | Physics | Living Systems | XR | Renderer | Asset/Provenance`

The provider bus owns registration, initialization, stepping, health state and fault isolation. Providers cannot directly mutate one another.

## Failure behaviour
A provider exception is converted into a provider FAULT record. The bus continues evaluating unaffected providers. A degraded result is retained as DEGRADED rather than promoted to VERIFIED.

## Canonical context
Each provider receives engine version, deterministic tick, simulation time and a world snapshot reference. Provider output identifies its own provenance through providerId and state.

## Current default contracts
- biupiu-simulation-core
- biupiu-physics-provider
- biupiu-living-systems
- biupiu-xr-openxr
- biupiu-render-provider
- biupiu-asset-provenance

These are integration contracts, not claims that every underlying runtime provider is installed or production-ready.

## Next gate — ENGINE-03
Connect the provider bus to the existing Simulation Core and living-system implementation, then add deterministic replay/regression fixtures and a real provider adapter for UE5/Unity/Lumion/XR.
