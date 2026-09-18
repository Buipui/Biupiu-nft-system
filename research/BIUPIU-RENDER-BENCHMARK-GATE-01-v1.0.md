# Biupiu Render Benchmark — Gate RENDER-02

**Status:** Benchmark specification executed / measurement pending
**Date:** 18 September 2026
**Parent:** BIUPIU-PROFESSIONAL-RENDERING-STACK-v1.0

## Objective

Create one controlled benchmark scene that can be rendered through Blender Cycles, OctaneRender, V-Ray and Unreal Engine 5 without changing the authoritative source geometry.

## Canonical test scene

Use a neutral Biupiu engineering asset containing:

- hard-surface automotive/marine geometry
- curved composite surface
- transparent component
- brushed/rough metal
- plant-fibre composite material
- resin/coating surface
- small emissive/photonic element
- neutral studio environment
- one outdoor/environment variant

The first benchmark should use a reproducible synthetic scene rather than a proprietary third-party asset.

## Required controls

Keep constant where the engine permits:

1. source geometry/version
2. object transforms
3. physical scale
4. camera position and lens/FOV
5. light positions and measured intensity assumptions
6. texture source and resolution
7. material-property assumptions
8. output resolution
9. colour-management target
10. scene naming/version

Engine-specific settings may differ where technically necessary, but every deviation must be recorded.

## Render adapters

### Cycles
Baseline reference renderer.

### Octane
GPU path-tracing benchmark.

### V-Ray
Production path-tracing comparison.

### Unreal Engine 5
Real-time/virtual-production comparison. Record whether the result uses Lumen, path tracing or another documented mode.

## Measurement sheet

Record for every engine:

- software version
- renderer version
- GPU/CPU hardware
- render mode
- samples/quality settings
- render resolution
- render time
- peak memory/VRAM if available
- output file size
- colour-management configuration
- material conversion notes
- unsupported-feature notes
- visual review notes
- reproducibility notes

Do not declare an engine superior from a single subjective visual comparison.

## Evaluation dimensions

Use separate observations for:

- geometry fidelity
- material fidelity
- lighting fidelity
- reflections/refractions
- vegetation/environment handling
- motion/cinematic suitability
- engineering annotation compatibility
- digital-twin integration
- iteration speed
- render performance
- pipeline interoperability
- provenance/auditability

## Acceptance gate

RENDER-02 is complete only when:

- [ ] one canonical scene is versioned
- [ ] four adapter configurations are documented
- [ ] each available engine produces a reproducible output
- [ ] engine/version/hardware metadata is recorded
- [ ] conversion differences are documented
- [ ] outputs are linked to the same source-model ID
- [ ] no proprietary binaries, credentials or licensed third-party assets are committed
- [ ] human visual review is recorded
- [ ] measured results are stored separately from subjective observations

## Current execution state

**Architecture:** PASS  
**Benchmark specification:** PASS  
**Repository implementation:** PASS  
**Actual render measurements:** PENDING workstation execution

The GitHub environment can define and validate the benchmark contract, but it cannot honestly claim render-time measurements without executing the renderers on a configured workstation.

## Next gate

RENDER-03 — workstation compatibility and first controlled benchmark run.
