# Biupiu Engine Execution Index v1.0

## Gate E1 — Graphics-first prototype

Objective: establish the first runnable renderer-oriented architecture for immersive Biupiu World and commercial product visualization.

### Priority
1. Renderable scene/runtime shell.
2. Product/showroom scene.
3. High-fidelity material and lighting pipeline.
4. Cinematic camera and deterministic frame capture.
5. Asset manifest and CAD-to-render lineage.
6. Performance/quality benchmark hooks.
7. Digital Twin/AI/OS adapter interfaces.

### Required interfaces
- Scene/entity API
- Render abstraction API
- Asset registry API
- CAD source/derived asset lineage API
- Camera/capture API
- Digital Twin entity/state API
- Biupiu OS lifecycle/permission API
- Intelligence/AI request-and-approval API

### Graphics target
The engine should support progressively higher detail rather than imposing one fixed quality level:
- Preview
- Real-time production
- Cinematic
- Offline/high-quality render

### Product visualization rule
A product asset can have multiple representations:
CAD source -> master geometry -> visual high-detail mesh -> runtime optimized mesh -> cinematic variant.

The source CAD remains separately identifiable and is never silently overwritten by render optimization.

### First demonstrator
Create a small immersive Biupiu World showroom/industrial environment with:
- terrain/floor
- architectural shell
- product display area
- physically based materials
- configurable lighting
- cinematic camera
- asset metadata
- render capture
- one Digital Twin entity

### Verification
E1 is not complete merely because files exist. Completion requires:
- project/runtime build succeeds;
- renderer starts;
- scene loads;
- product asset renders;
- camera capture produces deterministic output;
- asset manifest validates;
- smoke tests pass;
- results are recorded.

## Future gates
E2 — asset import/CAD conversion and material pipeline.
E3 — world streaming, LOD and vegetation.
E4 — physics/simulation.
E5 — editor and production tooling.
E6 — AI + Intelligence + Digital Twin.
E7 — complete vertical slice.
E8 — release qualification.

## Third-party boundary
Existing engines and open-source projects are research/integration candidates only. License, dependency, security, compatibility and build validation precede production integration. Proprietary AAA engine code/assets are excluded.

## Status
E1 architecture: initiated.
E1 runtime implementation: pending verification.
