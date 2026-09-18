# SF-39 — Android Build Workflow Activation & Artifact Verification

## Purpose
Activate the repository workflow for Android manifest/contract validation and define artifact verification.

Status: WORKFLOW READY / BUILD EXECUTION REQUIRES ANDROID PROJECT

## Checks
1. Repository checkout
2. JSON manifest validation
3. Android project presence check
4. Gradle wrapper validation
5. Compile
6. Unit/contract tests
7. Debug APK generation
8. APK existence/hash record
9. Artifact upload
10. Smoke-test handoff

## Important
SF38 currently defines the workflow contract and manifest validation. A real Android APK can only be marked VERIFIED when an actual Android project and Gradle build execute successfully.

The workflow must fail rather than fabricate a build result when the Android source project is absent or compilation fails.

## Release states
NOT_READY → WORKFLOW_VALIDATED → BUILD_RUNNING → BUILD_PASSED → ARTIFACT_VERIFIED → DEVICE_TEST_PENDING
