# BIUPIU GATE 24 — NATIVE COMPOSE OS SHELL

Status: IMPLEMENTED — BUILD/DEVICE VERIFICATION PENDING

Gate 24 establishes the first real Android Compose presentation shell for Biupiu OS.

Implemented:
- Native Compose MainActivity entry point.
- Kotlin 2.0.21 Compose compiler plugin.
- Material 3 dependency baseline.
- Home, Lab, Machine and System surfaces.
- Biupiu deep-green / metallic-gold / soft-white visual language.
- Evidence-first status language.
- Explicit discovery-versus-actuation boundary.

Not yet verified:
- CI/build execution.
- Emulator/device smoke test.
- OEM certification.
- Physical hardware compatibility.
- Desktop/iOS/Web builds.
- KMP shared-core extraction.

Next gate: connect the shell to the existing capability/runtime registries and extract the shared contract/domain layer into a dedicated multiplatform module.
