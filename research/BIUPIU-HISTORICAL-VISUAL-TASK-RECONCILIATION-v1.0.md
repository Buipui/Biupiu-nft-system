# Biupiu Historical Visual Task Reconciliation v1.0

**Date:** 2026-09-21
**Priority:** P0
**Status:** AUDIT COMPLETE / OPEN WORK PRESERVED

## Scope
Recovered repository work relating to Pixar/OpenUSD, OpenSubdiv, OTIO, Blender, UE5, Firefly, Lumion, KeyShot, Twinmotion, visual asset provenance, Biupiu World, avatars, procedural worlds, showreels and holographic/photonic visualisation.

## Findings
The repository is rich in architecture and contracts. The recurring gap is runtime evidence: several documents correctly distinguish repository/static implementation from real host execution. This reconciliation therefore does not convert architecture into false runtime claims.

## Historical clusters
- Pixar/Open Animation: OpenUSD/OpenSubdiv/OTIO stack exists; real Blender/UE5/DCC round-trip remains an execution gate.
- Biupiu World: shared world, manifests, avatar/interaction contracts and procedural build specifications exist; destination loading, authentication and production runtime remain open in the world client.
- Visual production: render pipeline/provider matrix exists across Blender, UE5, Twinmotion, KeyShot, Firefly and editorial tools; actual provider execution is host-dependent.
- AeroBlade GT: visual production/render queue is specification-ready; render execution remains pending.
- Holographic/photonic visualisation: research and benchmark contracts exist; numerical/optical runtime validation remains separate from cinematic rendering.
- Unity: adapter architecture exists, but installation/package/build/visual regression is host-dependent and must follow native foundation work.

## Priority decision
Native Biupiu visual functionality is P0. External engines become provider adapters. Historical runtime tasks are resumed through evidence-backed gates.

## Promotion policy
No item is VERIFIED without a real execution artifact, producing application/version, timestamp, input/output hashes and comparator/test result where applicable.
