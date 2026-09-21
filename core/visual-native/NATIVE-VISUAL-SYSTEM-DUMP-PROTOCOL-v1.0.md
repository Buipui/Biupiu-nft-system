# Biupiu Native Visual System Dump Protocol v1.0
**Gate:** VIS-NATIVE-01
**Status:** IMPLEMENTED AS CONTRACT

## Intake
1. Discover official/public releases and lawful historical dumps.
2. Discover authoritative open-source implementations.
3. Record source, commit/tag, licence and dependency metadata.
4. Classify each item as REFERENCE / ADAPTER / OPTIONAL-DEPENDENCY / NATIVE-CANDIDATE / PROHIBITED.
5. Compare against the native visual API contract.
6. Run static/schema checks.
7. Run host capability checks.
8. Run deterministic render/animation/video fixtures.
9. Record output hashes and provenance.
10. Promote only after explicit validation.

## Missing-module scan
Flag missing implementations for GPU backend abstraction, scene graph/command submission, shader/material interface, texture/image IO, animation timeline/sampling, skeletal/rig evaluation, camera, lighting/environment, render target/frame capture, video frame pipeline, codec/container boundary, audio sync, colour management, asset streaming/LOD, frame pacing, diagnostics/profiling, deterministic replay, provenance/output manifest and provider fallback.

Missing modules are OPEN, not silently substituted.

## Acceptance
REGISTERED -> STATIC_PASS -> HOST_CAPABILITY_PASS -> PROVIDER_SMOKE_PASS -> REGRESSION_PASS -> VERIFIED
