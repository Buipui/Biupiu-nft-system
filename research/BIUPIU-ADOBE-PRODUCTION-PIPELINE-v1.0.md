# Biupiu Adobe Production Pipeline v1.0

**Status:** Architecture/integration layer
**Updated:** 18 September 2026

## Purpose

Integrate Adobe Premiere Pro and After Effects as external professional media-production applications for the Biupiu R&D OS, Digital Twin, Biupiu World and engineering showcase pipeline.

This repository stores the integration contracts, provenance rules and adapters. Adobe applications remain separately installed desktop applications; the repository does not redistribute Adobe software.

## Architecture

`Biupiu R&D OS → Media Asset Registry → Adobe Adapter Layer → After Effects / Premiere Pro → Render/Export → Provenance + Release Record`

### Premiere Pro

Primary integration target: **UXP**, not new CEP development.

The official Adobe UXP samples provide:
- project and sequence operations
- markers and metadata
- effects/transitions/keyframes
- source-monitor workflows
- import/export and encoder operations
- transcripts
- AAF/FCPXML/OTIO conversion
- TypeScript declarations and linting support

Minimum versions and manifest requirements must be read from the installed Adobe sample/version at integration time.

### After Effects

After Effects is the motion-graphics/VFX/compositing layer:
- engineering visualization overlays
- product animations
- digital-twin callouts
- title/branding systems
- compositing and VFX
- procedural/motion-graphics sequences
- render-queue workflows

Legacy CEP/ExtendScript samples are retained as compatibility/reference material. New integrations should isolate legacy APIs behind an adapter so the core R&D OS is not coupled to CEP.

## Biupiu media asset contract

Every generated media asset should carry:
- Research ID
- Project ID
- Department
- Asset ID/version
- source model/reference IDs
- software/toolchain
- Adobe application/version
- plugin/adapter version
- input asset hashes where applicable
- output hash
- render/export preset
- evidence classification
- licence/provenance state
- IP firewall state
- creation commit/release record

## Pipeline tracks

1. **Engineering Showcase** — turbines, blades, marine, automotive, eVTOL and helicopter concepts.
2. **Digital Twin** — model → simulation result → annotated visualization → rendered media.
3. **Biupiu World** — environments, characters and historical/reconstruction/speculative layers.
4. **Product Development Showreel** — controlled product-development sequences.
5. **Research Evidence Video** — source/evidence overlays, experiment footage and validation records.

## Licensing boundary

Do not copy Adobe-owned code or redistribute Adobe binaries into Biupiu. Third-party GitHub examples are inspected for architecture and API usage; implementation must respect each repository's licence and Adobe's SDK/UXP terms.

## Gate ADOBE-01

**Executed:** repository architecture and provenance contract added.

Next gate: implement the concrete UXP adapter skeletons and deterministic media-job schema, then connect them to the existing R&D OS job/event model without claiming live Adobe execution until Premiere Pro/After Effects are installed and tested on the target Windows workstation.
