# Biupiu Professional Visualization Toolchain Matrix v1.0

| Layer | Tool | Primary role | Repository package |
|---|---|---|---|
| Master 3D | Blender | modelling, geometry, animation, simulation, Cycles rendering | blender |
| Product visualization | KeyShot Studio | CAD/product materials and high-end product rendering | keyshot |
| Rapid visualization | Twinmotion | environments, walkthroughs, rapid scene production | twinmotion |
| Interactive 3D | Unreal Engine | digital twins, real-time visualization, interactive demos | unreal |
| AI image/video | Runway | generative and transformation workflows | runway |
| AI creative | Adobe Firefly | concept imagery/video and creative iteration | firefly |
| Editorial | Premiere Pro | video assembly, sound and delivery | premiere |
| Compositing/motion | After Effects | motion graphics, compositing and titles | after-effects |

## Package principle

Each connector is provider-specific. The OS should expose a common media-job interface so applications can be swapped without changing the research-object model.

## Suggested job types

- `render.still`
- `render.turntable`
- `render.animation`
- `render.walkthrough`
- `render.digital-twin`
- `video.concept`
- `video.cinematic`
- `video.edit`
- `image.concept`
- `image.material-study`

## Evidence boundary

A render is a visualization artifact. A simulation result is an engineering evidence artifact. They must remain distinct in the R&D OS.


## V-Ray integration

V-Ray is registered as an additional professional renderer alongside Blender/Cycles, KeyShot, Twinmotion and Unreal. Use V-Ray through the connector boundary; proprietary runtime components are not redistributed.

| Job type | V-Ray role |
|---|---|
| render.still | high-quality product/concept rendering |
| render.turntable | asset presentation |
| render.animation | sequence rendering where supported |
| render.digital-twin | presentation layer, not engineering solver |
| material-study | VRayMtl/alSurface shader research |
| gltf-preview | glTF/GLB interoperability via V-Ray App SDK reference |
