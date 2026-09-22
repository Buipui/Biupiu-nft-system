# Biupiu Game-Engine Federation Routing v1.2

## BuipuiOS
Native adapters: Cocos2d-x, Cocos Engine, raylib.
ECS: engine-neutral bridge with Ashley as an optional implementation/reference.
Managed/web runtimes are not privileged boot dependencies.

## buipiu mini OS
Native: Cocos2d-x, Cocos Engine, raylib.
Managed: MonoGame via optional .NET workload.
Java: libGDX via dependency isolation.
Web: Three.js, GDevelop and Babylon.js through sandboxed runtime boundaries.
ECS: shared ECS bridge; Ashley optional.
Celeste: reference-only.

## Contract
Providers implement shared rendering, input, asset, scene, audio, telemetry, security and lifecycle contracts. Provider presence does not establish device/runtime availability.

## Promotion gate
No provider becomes SOURCE-INTEGRATED until an upstream tag/commit is pinned, dependency graph and notices are recorded, and host/Android builds plus relevant runtime/security tests succeed.
