# Biupiu Global Harvest — Android Development Update

## Harvested engineering direction
- Use Kotlin Multiplatform for shared business/domain logic where practical.
- Use Compose Multiplatform for shared UI where platform support and UX requirements justify it.
- Keep Android-specific application code separate from shared libraries.
- Preserve native adapters for secure storage, filesystem, sensors, graphics, device APIs and distribution.
- Treat Windows/macOS/Linux as explicit targets rather than assuming desktop compatibility.
- Treat Unix/POSIX as an adapter family requiring per-platform validation.
- Keep OEM stores behind the same Android release artifact and capability contract.

## Repository cross-reference
Historical Android work already contains:
- native application entry point
- runtime session
- entitlement routing
- department runtime
- department launcher
- Android CI gate
- structured error handling
- common application shell
- capability binding
- Blender/Digital Twin integration boundary

## Immediate implementation gate
Gate 20 adds a capability registry and explicit platform target matrix without forcing a risky rewrite of the existing Android application.

## Verification boundary
This gate is architectural and source-level. APK installation, device execution, OEM store submission, desktop packaging, and Unix builds remain separate verification gates.
