# BIUPIU Commercial Mobility Render QA Gate v1.0

Status: IN PROGRESS
Scope: Automotive / Jet / eVTOL
Authority: Biupiu design brief and repository visual-system requirements

## Objective
Bring automotive, jet and eVTOL visualisation to the same commercial presentation standard being established for Marine. Photorealism alone is not sufficient; product geometry, engineering details, materials, lighting and branding must remain legible.

## Common render requirements
- Preserve Biupiu design language: stealth geometry, Golden Mean/proportion studies where specified, deep green/deep ocean, carbon black, solar gold, graphite grey and restrained nature/sage accents.
- Preserve the authoritative Biupiu logo/wordmark in approved branding locations.
- Use physically based materials and controlled reflections.
- Maintain readable fine geometry at hero and technical-view distances.
- Avoid excessive bloom, fog, depth-of-field or contrast that obscures engineering features.
- Produce consistent lighting and material response across a vehicle family.
- Record asset provenance, source/licence status, scene/build identifier and render settings for every approved render.
- Separate concept visualisation from engineering validation; safety-critical claims require engineering analysis/testing.

## Automotive render acceptance views
1. Hero 3/4 front
2. Hero 3/4 rear
3. Side elevation
4. Front/rear detail
5. Wheel/brake/suspension detail
6. Aero/body-panel detail
7. Interior/cockpit
8. Underbody/technology detail where applicable
9. Studio technical presentation
10. Dynamic test-track environment

Required clarity: body surfacing, glazing, aero surfaces, lighting elements, wheels, tyres, panel transitions and propulsion/technology interfaces.

## Jet render acceptance views
1. Hero airborne 3/4
2. Ground/tarmac 3/4
3. Side elevation
4. Top/planform
5. Front/rear
6. Wing/control-surface details
7. Propulsion/intake/exhaust detail
8. Cockpit/cabin
9. Landing-gear detail
10. Technical studio render

Required clarity: aerodynamic surfaces, propulsion architecture, control surfaces, canopy, landing gear, surface transitions and Biupiu technology interfaces.

## eVTOL render acceptance views
1. Hero airborne
2. Hover/vertical-takeoff
3. Ground/landing-pad
4. Top/planform
5. Front/rear
6. Rotor/duct/bioblade detail
7. Propulsion-arm/nacelle detail
8. Cabin/interior
9. Landing gear
10. Technical studio render

Required clarity: rotor/duct geometry, propulsion interfaces, cabin glazing, fuselage, landing system, control surfaces and technology modules.

## Commercial Render QA
A render is presentation-ready only when:
- geometry is clearly readable;
- fine details are not lost;
- materials are distinguishable;
- lighting reveals rather than hides form;
- reflections do not obscure surfaces;
- environmental scale is credible;
- branding is correct;
- image resolution supports intended use;
- technical views are consistent with the hero view;
- provenance is recorded.

## Gate sequence
G1 Design-brief extraction: COMPLETE for current repository evidence.
G2 Vehicle-specific visual specification: COMPLETE for current design-board evidence.
G3 Scene/asset pipeline mapping: IN PROGRESS.
G4 High-detail geometry/material implementation: PENDING verification.
G5 Lighting/environment/simulation implementation: PENDING verification.
G6 Render provenance and reproducibility: PENDING.
G7 Commercial Render QA: PENDING.
G8 Cross-platform consistency (Blender/UE/Digital Twin/render adapters): PENDING.
G9 Approved benchmark renders: PENDING.
G10 Repository archival/closure: PENDING.

This gate does not claim that a generated concept render is an engineering-certified design.
