# Biupiu KeyShot GitHub Resource Audit v1.0

Date: 2026-09-18

## Stage 1 — Discovery
Reviewed GitHub search results for KeyShot, materials, HDRI, plugins, scripts and rendering integrations.

### Findings
- GitHub contains multiple repositories using the KeyShot name, but several appear to be unofficial distribution/marketing repositories. These are not adopted as dependencies.
- The useful category is workflow documentation, configuration, scripts, API/integration examples and independently licensed utilities.
- KeyShot remains a licensed desktop dependency rather than a repository-bundled renderer.

## Stage 2 — Candidate resource classes
1. KeyShot integration/API examples
2. Material and HDRI workflow references
3. CAD-to-KeyShot pipeline documentation
4. Batch/render automation concepts
5. Open-source showroom/material-preview utilities

## Stage 3 — Initial candidates
- keyshot-dev/configurations — configuration-oriented reference; inspect further before reuse.
- keyshot-dev/scripts — script-oriented reference; inspect further before reuse.
- keyshot-dev/integration-api-examples — integration examples; inspect further before reuse.
- SimonTek27/kseditor — community project surfaced with showroom, HDRI, material override and render-queue concepts. Reference only until source/license verification.
- jasonengcc/KeyShot-Studio-Materials — KeyShot-oriented material/HDRI documentation. Not treated as authoritative or as a bundled asset source.

## Exclusion policy
Exclude cracks, unauthorized installers, license bypasses, passwords, pirated binaries and assets whose redistribution rights are unclear.

## Biupiu decision
Use a connector architecture:
Blender/CAD -> KeyShot -> professional still/animation output.
Unreal Engine 5/Twinmotion remain the interactive/cinematic world layer.
KeyShot is the product/material validation and presentation layer.

No proprietary KeyShot files are copied into this repository.

## Next gates
- Verify the three keyshot-dev repositories and licenses.
- Inspect kseditor source/license.
- Define material/HDRI provenance metadata.
- Add render-profile schemas for automotive, marine, eVTOL/helicopter, microturbine, biomaterials and product showcase scenes.
