# V-Ray Integration Gate v1.0

## Gate status
**CLOSED — architecture and source integration verified.**

### Verification checklist
- [x] V-Ray registered as a Media Render OS provider.
- [x] Proprietary runtime kept outside the repository.
- [x] Open-source/reference source copied only from verified upstream repositories.
- [x] glTF/GLB interoperability path documented.
- [x] Material/shader research path documented.
- [x] Textile/hemp material research path separated from engineering evidence.
- [x] Render-pass/compositing path documented.
- [x] Provenance and evidence boundary defined.
- [x] Existing toolchain matrix updated.

## Gate boundary

**Authoritative engineering assets**
→ canonical asset registry  
→ glTF/GLB exchange  
→ V-Ray adapter  
→ render output  
→ provenance/hash  
→ Media OS

V-Ray output remains **VISUALIZATION_ONLY** unless independently validated by the relevant engineering simulation/experiment workflow.

## Next gate

Build the provider-neutral render-job adapter and automated media QA layer. The adapter should accept the existing Render Job Schema, select V-Ray/Blender/KeyShot/Twinmotion/Unreal through a common interface, capture renderer metadata, and prevent unverified render output from entering engineering-evidence records.
