# V-Ray glTF Pipeline v1.0

The cross-checked Chaos glTF reference demonstrates a command-line path from glTF/GLB to V-Ray rendering through the V-Ray App SDK.

## Supported reference features
- glTF 2.0
- KHR_texture_transform
- PBR specular-glossiness
- transmission
- clearcoat
- sheen
- KHR_lights_punctual (with documented limitations)
- limited transform animation

## Biupiu pipeline
1. Export canonical asset as glTF/GLB.
2. Validate geometry, transforms, materials and units.
3. Submit to V-Ray adapter.
4. Render still/sequence.
5. Record scene and renderer metadata.
6. Hash outputs.
7. Route output to Media OS/compositing.

Morph/skin deformation support must be treated as a compatibility check rather than assumed capability.
