# SF-35 — Runtime / Android Build Test & End-to-End Integration

## Purpose
Define the end-to-end integration gate connecting Biupiu World, mobile architecture, Digital Lab, Academy, Gallery and Marketplace.

Status: E2E TEST CONTRACT / BUILD EXECUTION PENDING

## Test path
APP LAUNCH → AUTH/PROFILE → WORLD → EPISODE → SCENE → HERO ASSET → RESEARCH → DIGITAL LAB → ACADEMY → GALLERY → MARKETPLACE → PROFILE

## Android test targets
- Android app launch
- navigation and back-stack behaviour
- responsive 16:9/9:16 media
- deferred 3D loading
- low-bandwidth preview mode
- caption rendering
- stable-ID persistence
- offline/error fallback
- session restoration
- guarded commerce actions

## World-to-mobile handoff
A world scene must open its corresponding mobile route using canonical IDs without creating a second incompatible identity.

## Digital Lab handoff
Episode scenes may link to experiments through experiment_id. Experimental claims remain labelled according to the Digital Lab record.

## Release blockers
- Android build failure
- broken canonical route
- missing required context
- asset/claim mismatch
- rights guard bypass
- inaccessible critical content
- unguarded commerce action

Live publication remains disabled until actual build and device tests pass.
