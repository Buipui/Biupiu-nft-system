# Biupui Federation Harvest — Game Engines Matrix v1.0

**Status:** SOURCE-INTEGRATION DESIGN / IMPLEMENTATION PENDING
**Target tracks:** BuipuiOS (AOSP/native) and buipiu mini OS (Android/mobile)
**Branch:** `integration/federation-game-engines`

## Scope

Harvest and evaluate reusable modules from:

- Cocos2d-x / Cocos engine
- MonoGame and Celeste (reference implementation only; do not copy game assets or proprietary content)
- libGDX and Ashley ECS
- raylib
- Three.js
- GDevelop
- Babylon.js

## Integration rule

Do not embed complete engines into the Android system image by default. Use a capability-based federation layer with isolated adapters. Engine runtimes are optional packages, while shared services are exposed through Biupui interfaces:

1. `IBiupuiRenderBackend` — GLES/Vulkan/WebGPU capability negotiation
2. `IBiupuiInput` — touch, keyboard, gamepad and sensor input
3. `IBiupuiAssetProvider` — sandboxed asset loading and lifecycle
4. `IBiupuiScene` — scene graph and/or ECS bridge
5. `IBiupuiAudio` — audio device and focus integration
6. `IBiupuiTelemetry` — performance, crash and resource metrics
7. `IBiupuiSecurityBoundary` — permissions, process isolation and content provenance

## Proposed package lanes

| Lane | Candidate modules | Target |
|---|---|---|
| Native 2D | Cocos2d-x, raylib | BuipuiOS + mini OS via NDK where compatible |
| Managed 2D | MonoGame, Celeste reference patterns | mini OS app/runtime; separate .NET workload |
| Java 2D/3D | libGDX, Ashley ECS | mini OS app/runtime; Gradle dependency isolation |
| Web/embedded | Three.js, Babylon.js, GDevelop runtime | sandboxed WebView/Web runtime; not privileged system code |
| ECS core | Ashley concepts plus engine-neutral ECS contract | shared Biupui simulation layer |

## Licensing and provenance gate

Every harvested component must retain upstream license, copyright notices, version/commit pin, checksum, source URL and modification record. Celeste is treated as a gameplay/architecture reference; its assets, code and content are not imported without explicit rights verification.

## Required validation gates

- DESIGNED: adapter contracts and package ownership documented
- SOURCE-INTEGRATED: pinned source/dependency manifests and notices present
- COMPILED: host and Android ABI builds pass
- BOOT-VERIFIED: no engine package required for OS boot
- FUNCTION-VERIFIED: smoke scene, input, asset and lifecycle tests pass
- SECURITY-VERIFIED: sandbox, permissions, dependency and license scans pass
- DEVICE-VERIFIED: tested on target hardware and documented separately

**Current result:** design artifact only. No engine source has been claimed as compiled, boot-verified, function-verified, security-verified or device-verified in this commit.
