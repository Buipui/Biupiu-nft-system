# Pixar / Open Animation Resources

## Core upstream projects

| Resource | Upstream | Biupiu role |
|---|---|---|
| OpenUSD | https://github.com/PixarAnimationStudios/OpenUSD | Scene description and interchange backbone |
| OpenSubdiv | https://github.com/PixarAnimationStudios/OpenSubdiv | Production subdivision geometry |
| OpenTimelineIO | https://github.com/AcademySoftwareFoundation/OpenTimelineIO | Editorial/timeline interchange |

## Selection rationale

OpenUSD is the primary integration target because it provides scalable time-sampled scene description and interchange and supports Windows, macOS and Linux. OpenUSD also exposes integrations for OpenSubdiv and other imaging/material systems.

OpenSubdiv is the geometry-quality target for smooth character and product surfaces.

OpenTimelineIO is the editorial target for connecting animation/render output to the Biupiu showreel workflow.

## Related ecosystem to evaluate later

- MaterialX
- OpenColorIO
- OpenImageIO
- OpenVDB
- Ptex
- Alembic
- Draco
- Embree

These appear in OpenUSD's dependency/integration configuration and should be evaluated individually rather than automatically imported.

## Licence rule

Every upstream dependency must retain its original licence and notices. Biupiu-created integration code remains separately documented.

## Source verification

Reviewed against the upstream GitHub repositories on 18 September 2026.

## Status

**Indexed for Biupiu R&D integration.**
