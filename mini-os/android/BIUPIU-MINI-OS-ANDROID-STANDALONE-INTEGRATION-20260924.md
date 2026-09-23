# Biupiu Mini OS — Android Standalone Development & Integration Section

Record: BIUPIU-MINI-OS-ANDROID-STANDALONE-INTEGRATION-20260924  
Status: REGISTERED / SOURCE IMPLEMENTED / BUILD VERIFICATION OPEN  
Purpose: standalone handoff and development history for the Android Mini OS, including Federation and Biupiu Native Intelligence integration.

## 1. Canonical authority

The Android Mini OS is an endpoint/runtime surface of the wider Biupiu OS/DMS system.

HUMAN RELEASE -> CORE OS/DMS -> DOMAIN OWNER -> NATIVE INTELLIGENCE -> FEDERATION -> ADAPTER/PROVIDER -> EXTERNAL REFERENCE

Native Intelligence may observe, classify, simulate and propose. It cannot independently execute, promote, release or override Core OS/DMS authority.

## 2. Previous development carried forward

- Core OS baseline and OS/AI separation.
- DMS/control-plane and Digital Twin architecture.
- Federation capability registry and fail-closed adapter model.
- AOSP Mainline and Pixel/GKI boundaries.
- Android Auto public API boundary.
- Motorola MA2, AAWireless TWO and Carlinkit 5.0 (2Air) transport adapters.
- Vector automotive SIL/HIL boundary.
- LSPosed/ART instrumentation boundary.
- RegiStar / One Hand Operation+ / NotiStar integration.
- Android notification listener/history and accessibility gesture foundation.
- Godot RenderingDevice and Vulkan capability boundaries.
- ARMv8.2-A FP16 / NEON, OpenCL and model/NPU provider federation.
- AppFunctions/MCP, AICore, ExecuTorch and other external provider adapters.
- Quantum/simulation provider references with QPU execution separately gated.
- OpenDroid provider/module references with unresolved engine identity failing closed.
- Shared language contract and Android selector integration.
- Simulator federation and Digital Twin cross-links.
- Gate-learning, guided fault finding, provenance, quarantine and promotion controls.
- Blind baseline/self-optimisation and quantum-inspired audit protocols from 2026-09-24.

## 3. Android build integration

The Android project remains a normal Gradle application build using mini-os/android/settings.gradle, mini-os/android/build.gradle and mini-os/android/app/build.gradle.

The federation source directory is now explicitly included in the Android application's Java source set so the native federation contracts participate in the Android build rather than existing only as repository-side reference files.

This configuration change does not imply device, GPU/NPU, Android Auto, accessory, AOSP or hardware execution has been verified.

## 4. Native Intelligence + Federation bridge

New native boundary:

- mini-os/android/federation/NativeIntelligenceFederationAdapter.java
- mini-os/android/federation/NativeIntelligenceFederationAdapterTest.java

Flow:

Android Observation -> Evidence Classification -> Biupiu Native Intelligence -> Federation Routing -> OS/DMS Validation -> Domain/Adapter Execution -> Evidence -> Learning Record

The bridge intentionally returns execution and promotion authority to Core OS/DMS. Unresolved capability identifiers are quarantined.

## 5. Capability routing

AndroidCapabilityRegistry remains the canonical Android capability catalogue.

States are AVAILABLE, ADAPTER_ONLY, DEVICE_REQUIRED, LICENSE_REVIEW, HISTORICAL_REFERENCE and UNRESOLVED. No external provider is silently promoted into native authority.

## 6. Evidence and learning

Android execution events should map to the federation event contract: Timestamp, Node, Task-ID, Parent-Task, Role, Input, Action, Output, Build, Test, Evidence, Validation, Failure.

The Android layer should emit machine-readable state/evidence rather than relying on chat history. Failures remain preserved for guided diagnosis, regression and future learning.

## 7. Verification boundary

### Registered / implemented

- Android project structure and Gradle configuration.
- Native federation registry and fail-closed checks.
- External provider classification.
- Graphics/Vulkan capability boundaries.
- Simulator federation cross-links.
- Native Intelligence/Federation contract.
- Standalone development/integration record.

### Source-level verified

- Semantic fail-closed logic by source inspection.
- Existing registry assertions and authority boundaries.
- Existing architecture cross-links and provenance rules.

### Still open

- Actual Gradle/Android SDK build.
- Android emulator/device execution.
- Live Android Auto projection.
- Physical MA2 / AAWireless TWO / Carlinkit verification.
- GPU/Vulkan runtime benchmark.
- NPU/device correlation.
- Vector CAN/CAN-FD HIL.
- LSPosed/ART runtime.
- Full AOSP/Pixel platform build.
- Persistent encrypted notification store.
- Production security/signing/update gates.

## 8. Standalone handoff rule

This section is the canonical Android Mini OS handoff record. New Android work should update this record and its machine-readable companion before being considered integrated.

Source implementation != runtime verification.

## 9. Canonical cross-links

- research/BIUPIU-OS-DMS-SUBSYSTEM-MASTER-INDEX-v1.0.md
- research/BIUPIU-NATIVE-CODING-PHILOSOPHY-AND-ENGINEERING-MATRIX-v1.0.md
- research/BIUPIU-ANDROID-AOSP-AUTOMOTIVE-GATE-REGISTER-20260922.md
- research/BIUPIU-SYSTEM-CROSS-LINK-DIGEST-v1.1.md
- research/BIUPIU-GATE-LEARNING-ARCHITECTURE-v1.0.md
- research/BIUPIU-BLIND-BASELINE-SELF-OPTIMISATION-PROTOCOL-20260924.md
- research/BIUPIU-QUANTUM-INSPIRED-DEEP-AUDIT-HARVEST-20260924.md
- intelligence/BIUPIU-MASTER-SYSTEM-INDEX-AI67.md
- software/rnd-os-ai/src/biupiu_ai/federation_registry.py
- mini-os/android/federation/AndroidCapabilityRegistry.java

Current gate: ANDROID MINI OS SOURCE INTEGRATION EXPANDED / BUILD + DEVICE VERIFICATION OPEN.
