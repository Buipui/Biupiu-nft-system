# BIUPIU GATE 25 — MATERIALITY & COLOURWAY SYSTEM

Status: IMPLEMENTED — BUILD/DEVICE VERIFICATION PENDING

## Design direction
Biupiu now treats colour as a designed **colourway**: a coordinated family of colours used as a collection, extended with material finishes, surface character and nature-derived themes.

The goal is not to make every screen green. The brand anchors remain protected, while each workspace can have its own controlled colour/material family.

## Material language
Workshop Simulator now has conceptual material surfaces for:
- Anodised Aluminium
- Brushed Titanium
- Bio-Composite
- Recycled Glass
- Carbon Weave
- Living Stone

These are currently UI material treatments, not physically measured PBR materials.

## Nature colour families
Registered families include:
- Verdant Canopy
- Mineral Spring
- Fynbos Ember
- Forest After Rain

The palette uses colour-wheel relationships and controlled tonal contrast rather than generic application colours.

## Hard design rule
Material appearance must never replace information clarity. State, warnings, labels and controls retain accessible contrast and semantic meaning.

## Technical boundary
Material 3 supports custom ColorScheme, typography and shapes, making a custom Biupiu design system appropriate rather than relying on default Android colours. Android's current documentation also supports custom brand colour schemes and tonal palettes. citeturn0search0turn0search5

## Verification
Implemented in source.
Build, emulator/device rendering and colour-contrast testing remain pending.
