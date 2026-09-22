# Biupui Game-Engine Federation Routing v1.1

This routing layer integrates the harvested engines as optional capability providers rather than making any engine a boot-time dependency.

## BuipuiOS
- Native lane: Cocos2d-x, Cocos Engine, raylib.
- ECS lane: Ashley-derived engine-neutral ECS concepts.
- Shared interfaces: rendering, input, assets, audio, telemetry, security and lifecycle.
- No managed or web engine is privileged system code.

## buipiu mini OS
- Native lane: Cocos2d-x, Cocos Engine, raylib.
- Managed lane: MonoGame through an optional .NET workload.
- Java lane: libGDX with Gradle dependency isolation.
- Web lanes: Three.js, GDevelop runtime and Babylon.js inside a sandboxed web/runtime boundary.
- ECS lane: shared engine-neutral ECS bridge, with Ashley as an optional implementation/reference.
- Celeste remains reference-only.

## Integration contract
Every provider must implement the shared capability model without requiring the OS to boot the provider. Provider loading is explicit, sandboxed and provenance-checked.

## Gate rule
A module is not marked SOURCE-INTEGRATED until its upstream commit/tag is pinned, dependency graph is recorded, license notices are retained, and the relevant host/Android build succeeds.
