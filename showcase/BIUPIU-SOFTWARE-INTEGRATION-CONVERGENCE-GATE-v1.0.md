# Biupiu R&D OS — Software Integration Convergence Gate v1.0

## Objective
Complete the software/toolchain integration layer before locking the final photorealistic Biupiu World showreel. The concept-board design lock is now separate from the runtime/render implementation so later integration work does not force redesign of the approved product family.

## Current repository gate state — 2026-09-19
| Gate / PR | Area | Repository state | Production implication |
|---|---|---|---|
| PR #5 | Blender Android R&D OS layer | Open; mergeable | Blender integration is structurally ready for convergence |
| PR #6 | KeyShot visualization | Open; conflict state | Resolve into current main before final render pipeline |
| PR #7 | UE5 integration boundary | Open; conflict state; draft | Converge UE5 adapter contracts |
| PR #8 | UE5 project/plugin foundation | Open; conflict state; draft | Converge after UE5 boundary |
| PR #9 | KeyShot render-job contract | Open; conflict state | Converge with current renderer pipeline |
| PR #10 | UE5 native skeleton | Open; conflict state; draft | Converge with current UE5 foundation |
| PR #11 | Showreel production gate | Open; conflict state; draft | Keep as production specification; rebase/converge after integration |
| PR #12 | KeyShot Windows adapter/render profiles | Open; conflict state | Converge with execution pipeline |
| PR #13 | UE5 digital twin/simulation | Open; conflict state; draft | Converge after core UE5 contracts |
| PR #14 | R&D OS CI diagnostic | Open; conflict state; draft | Re-run verification after convergence |
| PR #15 | KeyShot Windows execution pipeline | Open; conflict state | Converge before final render execution |
| PR #16 | UE5 propulsion/vehicle visualization | Open; conflict state; draft | Converge after UE5 foundation and digital-twin contracts |

## Integration order
1. Establish the current main branch as the convergence base.
2. Converge Blender Android integration and its package/licence boundary.
3. Converge UE5 integration boundary.
4. Converge UE5 project/plugin foundation and native skeleton.
5. Converge UE5 digital-twin/simulation contracts.
6. Converge propulsion/vehicle visualization mappings for BL-01, MR-01, MR-02, EV-01, HC-01 and AX-01.
7. Converge KeyShot render-job contract, local adapter, Windows execution pipeline and render profiles.
8. Re-run CI/R&D OS verification after the combined integration state is assembled.
9. Only then promote the Episode 01 showreel from specification to render execution.
10. Generate approved stills first; then animation, sequencing and derivative exports.

## Design continuity rule
The user-supplied Biupiu Regenerative Technology Ecosystem.png is the approved styling reference for future photorealistic reconstruction. It defines silhouettes, proportions, product-family relationships and presentation language. It is not an engineering source model.

The authoritative Biupiu logo remains the supplied logo reference. Downstream AI/image generation must not redraw or substitute the wordmark.

## Render architecture
- Blender: canonical mesh preparation, modelling, asset cleanup and approved animation preparation.
- Unreal Engine 5: world assembly, digital-twin presentation and cinematic sequencing.
- KeyShot: controlled product visualization/render profiles where the licensed runtime is installed.
- Other renderer integrations: remain provider-specific adapters and must consume the same canonical asset/material/camera metadata.
- AI/video tools: enhancement and controlled creative support only; they do not replace canonical 3D geometry or engineering source data.

## Completion criteria
The integration gate is complete only when:
- repository contracts converge on current main;
- CI verification passes;
- Blender/UE5 package boundaries are coherent;
- renderer adapters consume the same asset metadata;
- provenance/licensing records are present;
- canonical product IDs map consistently across the showcase;
- the concept-board design lock is referenced by the render manifest;
- at least one end-to-end test render path is executable in the intended local runtime.

## Important limitation
Repository integration can establish contracts, adapters, schemas and automation. Proprietary desktop runtimes such as KeyShot, and Unreal/Blender executable environments, still require their respective installed/licensed runtime environments for actual local rendering. No proprietary binaries or credentials should be committed to the repository.