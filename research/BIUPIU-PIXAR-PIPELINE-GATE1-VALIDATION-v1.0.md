# Biupiu Pixar/Open Animation Pipeline — Gate 1 Validation v1.0

Date: 18 September 2026

## Gate objective

Validate the architecture before vendoring large upstream source trees. Biupiu will use upstream repositories as dependencies/references and keep Biupiu-created adapters, test assets and manifests in this repository.

## Verified upstream capabilities

### OpenUSD
Upstream: https://github.com/PixarAnimationStudios/OpenUSD

USD is an extensible scene-description system for authoring, reading and streaming time-sampled 3D scene data. The upstream project supports Windows and macOS in addition to its primary Linux development environment, and documents WebAssembly builds. Its imaging stack requires OpenSubdiv. This makes USD the central interchange candidate for the Biupiu character/world/product pipeline.

### OpenSubdiv
Upstream: https://github.com/PixarAnimationStudios/OpenSubdiv

OpenSubdiv provides high-performance subdivision-surface evaluation. Its upstream documentation lists Windows support and optional GPU APIs including DirectX, OpenGL, CUDA, OpenCL and Metal. Pixar's documentation also states that OpenSubdiv supports Android. This makes it a particularly useful geometry component for the future Android branch of the Biupiu R&D OS.

### OpenTimelineIO
Upstream: https://github.com/AcademySoftwareFoundation/OpenTimelineIO

OTIO provides an editorial timeline API/interchange format. It carries cut/timing information and references to external media; it is not a media container. The project provides Python bindings and adapter/plugin architecture.

## Gate 1 integration decisions

1. **OpenUSD = scene interchange backbone**
2. **OpenSubdiv = geometry/subdivision component**
3. **OpenTimelineIO = editorial/showreel interchange**
4. Keep upstream source external until build/version/license pinning is complete.
5. Store Biupiu integration scripts, manifests and tests in this repository.
6. Do not copy Pixar proprietary film assets, characters, textures, datasets or branding.
7. Android work should prioritize a lightweight native/OpenSubdiv path and investigate USD native/WASM runtime options separately.

## Test matrix

| Test | Target | Status |
|---|---|---|
| USD scene schema/import-export design | Windows | READY |
| OpenSubdiv build configuration | Windows | READY |
| OpenSubdiv Android feasibility | Android | RESEARCH-VALIDATED |
| OTIO timeline schema | Windows/Linux | READY |
| Blender USD interchange | Windows | NEXT |
| Unreal USD interchange | Windows | NEXT |
| Adobe/showreel OTIO handoff | Windows | NEXT |
| Android USD runtime | Android | INVESTIGATE |
| Licence/notice inventory | All | REQUIRED |

## First executable implementation

Create a minimal Biupiu test scene containing:
- one procedural/computational character mesh
- one Biupiu vehicle/aircraft/marine placeholder
- one environment
- one animated camera
- time-sampled transforms
- material placeholders
- metadata linking the scene to a Biupiu Research ID

Round-trip target:

Biupiu source geometry → Blender → USD → Blender/consumer → rendered test frame.

Second test:

subdivision-capable mesh → OpenSubdiv evaluation → visual/geometry comparison.

Third test:

rendered shot references → OTIO timeline → editorial handoff manifest.

## Acceptance criteria

- No proprietary Pixar production assets are introduced.
- Upstream source and licence provenance remain identifiable.
- USD test scene preserves scene hierarchy and animation metadata.
- OpenSubdiv test preserves intended topology and produces valid evaluated geometry.
- OTIO test preserves shot order, duration and media references.
- Windows path is documented.
- Android path is explicitly marked native, WASM or deferred after testing rather than assumed.

## Gate status

**GATE 1 — ARCHITECTURE / SOURCE VALIDATION: PASSED**

Next gate: build the first minimal USD/OpenSubdiv/OTIO test harness and connect it to the existing Biupiu Blender/Unreal/Adobe pipeline.
