# Biupiu Rendering / Physics / Reconstruction Adapter Contract v1.0

## Purpose
Provide stable Biupiu interfaces so graphics, physics and reconstruction implementations can be upgraded independently.

### GraphicsAdapter
- backend selection: DX12 / Vulkan
- glTF/asset ingestion
- PBR material path
- ray-tracing capability detection
- GPU timestamp/telemetry hooks
- HDR/colour-management handoff
- deterministic resource/provenance IDs

### PhysicsAdapter
- fixed timestep
- rigid body state
- constraints and collision queries
- vehicle/rotor/flight extension hooks
- deterministic/replay mode where supported
- telemetry export
Implementations: Jolt 5.6.0 target; PhysX 5.x target; Bullet/PyBullet validation adapter; existing dependency-free private physics kernel.

### ReconstructionAdapter
- render-resolution selection
- motion-vector/depth/jitter inputs
- reactive/disocclusion masks where available
- temporal accumulation
- sharpening/post processing
- frame-generation capability reporting
- vendor-neutral fallback
Implementations: AMD FidelityFX SDK 2.3.0 / FSR 4.x documentation path; Intel XeSS 3.0.1; native engine path; OptiScaler research path only.

## Promotion gate
1. licence review; 2. exact version pin; 3. local build; 4. automated tests; 5. GPU runtime test; 6. benchmark capture; 7. provenance record; 8. explicit promotion into the applicable Biupiu package.