# Biupiu Animation Pipeline Tests

## Gate 2 scope

This directory contains minimal, non-proprietary test artifacts for the OpenUSD/OpenSubdiv/OpenTimelineIO integration track.

- `usd/minimal_scene.usda`: time-sampled scene with environment, vehicle placeholder and animated camera.
- `otio/biupiu_showreel_timeline.json`: editorial timeline manifest with external media reference.

## Execution checklist

1. Validate the USDA file with an OpenUSD-capable parser.
2. Open and round-trip the scene in Blender with USD support enabled.
3. Run a separate OpenSubdiv mesh test using a Biupiu-created test mesh.
4. Validate the OTIO manifest with the installed OTIO schema/API.
5. Replace the placeholder media URL only with locally generated test media.
6. Record tool versions, platform, hashes and results in a dated validation report.

## Current status

Artifacts and test plan committed. Runtime execution is **not claimed** until a configured Windows/Linux/Android environment runs the checks. No rendered media or third-party proprietary assets are included.
