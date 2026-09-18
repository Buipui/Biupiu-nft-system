# Biupiu Redshift Validation Gate — RED-02

**Status:** ENVIRONMENT VALIDATION GATE DEFINED — LIVE HOST NOT CONNECTED
**Date:** 18 September 2026

## Objective
Validate the Redshift adapter before any claim of production rendering.

## Official compatibility baseline
Maxon currently documents Redshift across NVIDIA CUDA/OptiX, Apple Silicon Metal, AMD Windows/HIP RT and CPU rendering. Maxon states 8 GB VRAM as the minimum and 16 GB+ as recommended for production comfort.

## RED-02 test matrix

1. **Host detection**
   - Detect installed host: Cinema 4D, Maya, 3ds Max, Houdini/Solaris, Blender, Katana or other supported host.
   - Record exact host/version.

2. **Redshift detection**
   - Detect Redshift installation and exact version.
   - Record plugin/renderer availability.

3. **Compute-device validation**
   - Record GPU model(s), VRAM and driver/runtime information.
   - Confirm Redshift can enumerate the intended compute device.
   - Record CPU availability for CPU or hybrid fallback.

4. **Shader validation**
   - Compile/load a licensed Redshift OSL test set.
   - Minimum tests: SpaceTransform, UberConstant, ColorShuffle, TextureNoTile and ThinFilmInterference.
   - Record pass/fail and source licence.

5. **Material validation**
   - Build a deterministic Biupiu test material.
   - Target material classes: advanced composite, coated metal, glass/optical, carbon-fibre-like weave and bio-based resin appearance.
   - Appearance is visualisation only and must not be treated as measured material properties.

6. **Render validation**
   - Run one deterministic still and one animation/frame-sequence test.
   - Record render settings, host, renderer version, device, scene hash and output hash.

7. **Pipeline validation**
   - Confirm asset-registry provenance survives:
     source asset → Redshift scene → render output → research/showcase record.

## Acceptance criteria

RED-02 passes only when:
- a supported host is detected;
- Redshift is detected;
- a compute device or CPU fallback is usable;
- the test shader set loads successfully;
- a deterministic test render completes;
- provenance metadata is preserved;
- failures are logged rather than silently bypassed.

## Current state

**BLOCKED ON LIVE-HOST ACCESS.** The repository connector can update architecture and test specifications, but it cannot establish that Redshift is installed on the user's workstation. No live render is claimed.

## Next executable gate

Connect/validate a Redshift-capable workstation or CI/render node, then execute RED-02 and record the hardware/software environment and test results.
