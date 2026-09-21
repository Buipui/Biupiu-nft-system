# Biupiu Pixar/Open Animation Pipeline — Gate 2
**Status:** SOURCE IMPLEMENTATION READY / HOST EXECUTION PENDING

Gate 1 selected OpenUSD, OpenSubdiv and OpenTimelineIO as the open animation/interchange backbone. Gate 2 converts that architecture into repository-local first-party contracts and executable fixture validation.

## Completed at repository level
- Canonical minimal USDA scene fixture exists.
- Canonical OTIO timeline fixture exists.
- Static USD/OTIO validator exists.
- USDA contract comparator exists.
- Export-artifact ingestion contract exists.
- Gate 9 CI guardrail exists.
- Native Visual API now provides the first-party ABI boundary for render, animation and video jobs.
- First-party native API lifecycle smoke test and CMake target have been added.

## Runtime tasks still requiring a host
1. Build OpenUSD against the supported Windows toolchain.
2. Execute USDA parser/round-trip.
3. Execute OpenSubdiv test mesh evaluation.
4. Execute OTIO schema/API validation.
5. Produce a real external export with provenance.
6. Connect the native API to a real provider.
7. Compare provider output against canonical scene/animation expectations.

No runtime pass is claimed until those observations exist.
