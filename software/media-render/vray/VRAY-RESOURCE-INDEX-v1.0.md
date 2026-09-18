# V-Ray Resource Index v1.0

## Cross-checked resources

| Resource | Upstream | Usable Biupiu content | License/status |
|---|---|---|---|
| V-Ray glTF viewer | ChaosGroup/vray_gltf | Python parser, camera helpers, CLI render orchestration | MIT reference code; V-Ray runtime required |
| V-Ray Material GLSL | ChaosGroup/vraymtl_glsl | VRayMtl shader reference for viewport/material research | MIT |
| V-Ray App SDK | ChaosGroup/vray-app-sdk | Connector/API design reference and SDK sample architecture | MIT sample repository; commercial runtime dependency |
| alSurface | ChaosGroup/vray_al_surface | SSS/BRDF research reference for material studies | MIT |
| ThunderLoom | ThunderLoom/ThunderLoom | Woven-cloth physically based shader research | MIT |
| Maya V-Ray command docs | BigRoy/mayaVrayCommandDocs | Automation/reference snippets | Community resource; verify license before copying code |
| V-Ray pass importer | ptrojan3d/vray-pass-importer-ae | After Effects render-pass workflow reference | Verify upstream license before copying |

## Selection rule
Only source code with a clear reusable license is copied into the Biupiu repository. Proprietary V-Ray software is referenced as an external dependency rather than redistributed.

## Cross-disciplinary mapping
- Materials R&D → VRayMtl / alSurface / textile shader references
- Computational Engineering → glTF parser and render orchestration
- Media OS → render-job connector
- Digital Twin → glTF/GLB interchange and material preview
- Microturbines → high-fidelity visual asset pipeline
