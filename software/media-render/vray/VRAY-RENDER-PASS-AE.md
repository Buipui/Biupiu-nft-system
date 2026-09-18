# V-Ray Render Pass → After Effects

Register V-Ray render-pass output as an intermediate media artifact.

Pipeline:

V-Ray render → EXR/render elements → pass validation → After Effects/compositing → final media artifact

Required provenance:
- source asset hash
- scene/version
- V-Ray version
- render settings profile
- frame range
- output format
- render-pass list
- compositing software/version
- final artifact hash

This workflow is presentation/media processing only and does not alter engineering evidence.
