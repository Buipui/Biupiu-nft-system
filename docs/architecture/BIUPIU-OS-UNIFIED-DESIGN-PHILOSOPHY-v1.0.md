# BIUPIU OS UNIFIED DESIGN PHILOSOPHY v1.0

**Gate:** 26  
**Status:** IMPLEMENTED — source architecture and Android shell updated; runtime/device visual verification pending.

## Principle

Biupiu OS and every Biupiu subsystem must feel **premium without becoming complicated**.

Pagani and Ferrari are reference points for restrained luxury, high-quality material finishes, neutral colour foundations, deliberate configuration, clear presentation of choices, craftsmanship and precision. They are design references, not templates. No proprietary branding, assets or interface is copied.

## Biupiu rule

**Neutral base → material finish → restrained nature accent → clear information.**

The default interface should rely on graphite, titanium, aluminium, warm white, stone and muted bronze/green tones. Strong colour is reserved for semantic state, important actions, or a deliberately selected workspace colourway. The system must not become a rainbow interface.

## Universal rules

1. **Premium through restraint.** Avoid visual clutter, unnecessary gradients, decorative panels and excessive animation.
2. **Neutral first.** A subsystem should remain professional and legible even with all decorative accents removed.
3. **Material conveys character.** Surface finish can suggest aluminium, titanium, carbon, glass, bio-composite or stone without pretending to be physically accurate PBR.
4. **Nature is an accent family.** Botanical/mineral themes may influence colourway, imagery and material language, but do not overpower information.
5. **Semantic colour is protected.** Warnings, errors, success, permissions and system state retain explicit accessible meaning.
6. **One visual language.** OS, DMS, Intelligence, Lab, Workshop, Digital Twin, simulators, configurators and departmental systems inherit the same base tokens.
7. **Simple interaction.** Prefer a small number of obvious actions, progressive disclosure and reversible changes.
8. **Configuration should feel deliberate.** Show the current selection, effect and ability to review/revert before commitment.
9. **Legibility overrides ornament.** Typography, contrast, touch targets and state visibility are functional requirements.
10. **No false physicality.** A visual material treatment is labelled as a visual approximation until measured/rendered and verified.

## Architecture rule

The visual system is a shared design contract, not a screen-by-screen style.

BIUPIU DESIGN TOKENS → PLATFORM THEME → COMPONENTS → SUBSYSTEM SHELLS → DOMAIN WORKSPACES

Platform implementations may adapt controls to Android, desktop, embedded or simulator contexts while preserving the same visual principles.

## Colourway rule

A colourway is a controlled family, not an arbitrary colour picker. Each colourway records a base neutral, secondary neutral, material finish, restrained accent, semantic state colours, contrast/accessibility requirements and workspace/domain purpose.

## Canonical neutral family

- Deep Green — brand/environment anchor
- Graphite — primary dark surface
- Titanium — technical neutral
- Aluminium — light technical neutral
- Warm White — readable light surface/text
- Sand/Stone — natural neutral
- Bronze — restrained premium accent
- Patina/Nature — restrained biological/environmental accent

## Verification boundary

Source implementation does not prove visual quality on every device. Required later gates include Android emulator/device rendering, contrast/accessibility tests, tablet/desktop adaptation, simulator/workshop rendering, performance/motion testing, screenshot/regression comparison and cross-platform token conformance.

**Rule for future gates:** Do not add visual complexity merely to demonstrate capability. Every new visual element must justify itself through usability, information hierarchy, material clarity or verified domain function.
