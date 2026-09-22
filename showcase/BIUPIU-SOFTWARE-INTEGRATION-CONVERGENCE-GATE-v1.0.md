# Biupiu R&D OS — Software Integration Convergence Gate v1.0

## Objective
Complete the software/toolchain integration layer before locking the final photorealistic Biupiu World showreel. The concept-board design lock is separate from runtime/render implementation so later integration work does not force redesign of the approved product family.

## Integration order
1. Establish current main as the convergence base.
2. Converge Blender Android integration and package/licence boundary.
3. Converge UE5 integration boundary.
4. Converge UE5 project/plugin foundation and native skeleton.
5. Converge UE5 digital-twin/simulation contracts.
6. Converge propulsion/vehicle visualization mappings for BL-01, MR-01, MR-02, EV-01, HC-01 and AX-01.
7. Converge KeyShot render-job contract, local adapter, Windows execution pipeline and render profiles.
8. Re-run CI/R&D OS verification after the combined integration state is assembled.
9. Promote Episode 01 from specification to render execution only after the above gates pass.
10. Generate approved stills first; then animation, sequencing and derivative exports.

## Design continuity rule
The user-supplied Biupiu Regenerative Technology Ecosystem.png is the approved styling reference for future photorealistic reconstruction. It defines silhouettes, proportions, product-family relationships and presentation language. It is not an engineering source model.

The authoritative Biupiu logo remains the supplied logo reference. Downstream AI/image generation must not redraw or substitute the wordmark.

## Render architecture
- Blender: canonical mesh preparation, modelling, asset cleanup and approved animation preparation.
- Unreal Engine 5: world assembly, digital-twin presentation and cinematic sequencing.
- KeyShot: controlled product visualization/render profiles where the licensed runtime is installed.
- Other renderer integrations: provider-specific adapters consuming common asset/material/camera metadata.
- AI/video tools: controlled creative support; they do not replace canonical 3D geometry or engineering source data.

## Completion criteria
- repository contracts converge on current main;
- CI verification passes;
- Blender/UE5 package boundaries are coherent;
- renderer adapters consume the same asset metadata;
- provenance/licensing records are present;
- canonical product IDs map consistently across the showcase;
- the concept-board design lock is referenced by the render manifest;
- at least one end-to-end test render path is executable in the intended local runtime.

## Runtime boundary
Repository integration can establish contracts, adapters, schemas and automation. Proprietary desktop runtimes and external Unreal/Blender executable environments still require their installed/licensed runtime environments for actual local rendering. No proprietary binaries or credentials should be committed to the repository.
