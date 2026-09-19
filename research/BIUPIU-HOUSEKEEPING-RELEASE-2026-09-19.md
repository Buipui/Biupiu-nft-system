# Biupiu Housekeeping Release — 2026-09-19

## Release intent

This release records the repository housekeeping gate requested for the Biupiu intelligence/R&D system.

## Repository audit observations

- Default branch: `main`.
- Repository contains active AI, R&D OS, Android, world, smart-farming, animation/rendering and provenance-related tracks.
- Existing audit infrastructure was located in the R&D API, AI audit store and research audit records.
- Existing CI workflows provide multiple validation boundaries.
- Existing repository material includes both first-party Biupiu work and vendor/third-party assets.

## Cleanup policy applied

### Code
- Add a repeatable housekeeping contract rather than making speculative source changes.
- Treat TODO/FIXME findings as review items.
- Do not rewrite vendor code solely to remove TODO markers.
- Preserve existing audit/provenance boundaries.

### Research
- Preserve historical and current material.
- Record provenance and dates.
- Flag conflicts/duplicates rather than silently deleting records.
- Keep visualization-only evidence distinct from validated engineering evidence.

### Bugs
- Housekeeping is a gate for identifying and recording defects.
- Only defects supported by repository evidence should be fixed automatically.
- Runtime/build failures require CI or executable test evidence before being marked resolved.

## Current known review items

1. Vendor rendering sources contain TODO comments; these are retained as upstream/vendor work items.
2. The repository has a significant number of open issues; they remain the authoritative defect queue until individually verified.
3. CI/workflow presence is not itself proof that every workflow has recently executed successfully.
4. Research records should continue to be deduplicated and cross-linked as new sources arrive.

## Next housekeeping gate

Run repository-native CI/build checks, review open issues, reconcile indexes/manifests, then record only verified fixes in the next release.
