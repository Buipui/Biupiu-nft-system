# BIUPIU GRADLE SYSTEM HARVEST — GATE 30

Date: 21 September 2026

## Objective

Deep-audit every Gradle-based Android system in the repository, establish a canonical toolchain matrix, restore missing Gradle metadata, integrate CI execution across the existing systems, and prevent version drift.

## Deep repository findings

Three independent Android Gradle systems exist:

1. `apps/android` — canonical native Biupiu R&D OS shell.
2. `smart-farming/android` — Smart Farming Android client.
3. `software/rnd-os-mobile` — newer standalone R&D OS mobile build.

They remain separate application boundaries; they are not merged by copying source trees.

## Toolchain matrix

| System | AGP | Kotlin | Gradle | JDK |
|---|---:|---:|---:|---:|
| apps/android | 8.7.3 | 2.0.21 | 8.9 | 17 |
| smart-farming/android | 8.7.3 | 2.0.21 | 8.9 | 17 |
| software/rnd-os-mobile | 8.13.0 | 2.2.20 | 8.13 | 17 |

Android's official compatibility table states AGP 8.7 requires Gradle 8.9, while AGP 8.13 uses Gradle 8.13. Gradle's official documentation recommends the Wrapper and SHA-256 distribution verification.

## Integrated controls

- Added wrapper properties for all three systems.
- Pinned official distribution SHA-256 values.
- Added a single repository Gradle-system manifest.
- Added a matrix CI gate covering all three builds.
- Pinned the canonical OEM workflow to Gradle 8.9.
- Removed the last CI dependency on an absent `gradlew` call in the emulator job.
- Added deterministic manifest/path smoke checks.

## Missing files

All three systems still lack:
- `gradlew`
- `gradlew.bat`
- `gradle/wrapper/gradle-wrapper.jar`

These are intentionally recorded as OPEN rather than replaced with an unverified binary. The official Gradle wrapper JAR must be retrieved/generated in a network-capable build environment and checksum-verified before promotion.

## Promotion

DISCOVER -> COMPATIBILITY MAP -> WRAPPER METADATA -> WRAPPER JAR VERIFY -> CI BUILD -> UNIT TEST -> EMULATOR -> OEM -> HIL -> RELEASE

## Status

- Gradle systems discovered: IMPLEMENTED
- Version matrix: IMPLEMENTED
- Distribution checksum pins: IMPLEMENTED
- CI matrix: IMPLEMENTED
- Wrapper JAR: OPEN
- Android compilation: PENDING CI
- Emulator: PENDING
- Physical OEM: PENDING
- Production release: PENDING

## Next gate

G30-A — Wrapper Completion:
1. Retrieve/generate official wrapper files.
2. Verify wrapper JAR SHA-256 against Gradle's published checksum.
3. Run every Android system through its committed wrapper.
4. Only then replace CI system-Gradle execution with wrapper execution.
