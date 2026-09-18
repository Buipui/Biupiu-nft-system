# SF-38 — Android Source Scaffold & Manifest Ingestion

## Purpose
Define the first source scaffold for the Biupiu Android application and establish manifest ingestion from the shared World/showcase contracts.

Status: SOURCE SCAFFOLD / BUILD WORKFLOW READY

## Project structure
app/
  src/main/java/com/biupiu/world/
    MainActivity.kt
    navigation/
    data/
    model/
    repository/
    ui/
    guards/
  src/main/res/
  build.gradle.kts
  AndroidManifest.xml

## Data flow
SF36 showcase manifests
→ parser/repository
→ canonical domain models
→ navigation
→ showcase cards/detail views
→ World/Digital Lab/Academy deep links.

## First-screen acceptance
The first test build must display:
- Biupiu World entry
- department list
- showcase development list
- marine hydrofoil showcase card
- evidence/claim status
- navigation to Research/Digital Lab/Academy
- disabled/guarded commerce action

## Hydrofoil display rule
The earlier glass hydrofoil concept image is a visual design reference. The UI must identify it as a concept/design reference and never imply that the physical vessel is already built.

## Build workflow
1. Android SDK/Gradle setup
2. dependency resolution
3. compile
4. unit/contract tests
5. debug APK
6. emulator/device smoke test
7. QA report

This repository stage defines the scaffold and workflow; it does not claim an APK has been built unless a build artifact is produced and verified.
