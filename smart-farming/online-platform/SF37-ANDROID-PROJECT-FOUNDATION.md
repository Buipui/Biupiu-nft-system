# SF-37 — Android Project Foundation & Showcase Registry Integration

## Purpose
Establish the Android application foundation and connect the SF-36 showcase registry to the shared Biupiu World/mobile data layer.

Status: FOUNDATION SPECIFICATION / BUILD EXECUTION PENDING

## Application layers
- App shell
- Authentication/Profile
- Biupiu World
- Episode viewer
- Department explorer
- Research Library
- Digital Lab
- Academy
- Gallery
- Marketplace
- Intelligence Hub
- Settings

## Canonical data source
The mobile application consumes the same canonical IDs and evidence states used by the World Runtime.

Primary showcase data:
- SF36-SHOWCASE-DEVELOPMENT-MANIFEST.json
- SF36-SHOWCASE-PLACEMENT-MAP.json
- SF36-SHOWCASE-DEVELOPMENT-REGISTER.md

## Marine showcase
biu-veh-marine-001 uses the earlier Biupiu glass hydrofoil concept as a visual design reference. The application must display its current evidence status as CONCEPT and must not represent the concept image as proof of a completed physical vessel.

## Android foundation
Recommended implementation:
- Kotlin
- Jetpack Compose
- single-activity architecture
- repository/data layer for canonical manifests
- navigation layer using stable route IDs
- local cache for low-bandwidth previews
- future 3D viewer module isolated from the core application shell

## Initial routes
/home
/world
/world/episode/{episode_id}
/department/{department_id}
/research
/lab/{experiment_id}
/academy/{lesson_id}
/gallery
/marketplace
/profile

## Build gate
The first Android build should prove application launch, navigation, manifest loading and showcase rendering using lightweight metadata before heavy 3D assets are introduced.

Live commerce and live World Runtime remain disabled.
