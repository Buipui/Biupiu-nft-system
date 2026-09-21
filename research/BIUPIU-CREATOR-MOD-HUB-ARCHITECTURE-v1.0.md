# Biupiu Creator Mod Hub Architecture v1.0

## Purpose

Establish the free community modding layer discussed for Biupiu World.

The principle is:

**Free to create -> free to submit -> rights-aware validation -> discoverable community content -> optional commercial creator/professional paths.**

## Engine strategy

Biupiu initially supports:

- Unreal Engine
- Unity
- Biupiu-native formats

Unreal and Unity are compatibility/distribution ecosystems. Biupiu Engine is the long-term native target.

## Core pipeline

Creator -> Biupiu Creator Identity -> Upload -> Metadata -> Licence Declaration -> Dependency Scan -> Rights/Provenance Gate -> Compatibility Test -> Security Scan -> Community Review -> Mod Hub -> Biupiu World

## Mod package record

Every mod should carry:

- creator ID
- creator display name
- engine
- engine version
- platform
- package version
- dependencies
- licence
- third-party assets
- commercial-use declaration
- source/provenance
- content hash
- update history
- compatibility result
- security result
- moderation state

## Community principles

The free layer is intended as Biupiu's give-back mechanism to the modding community.

Creators retain the rights they actually own. Biupiu receives only the permissions required by the explicit publishing licence.

No automatic transfer of creator IP.

## Native Biupiu advantages

The Mod Hub should eventually provide native:

- asset packaging
- version control
- dependency resolution
- cross-engine metadata
- automated compatibility checks
- provenance
- creator attribution
- safe rollback
- ratings/reviews
- analytics
- update notifications
- optional monetisation
- educational/tutorial publishing
- verified creator badges

## Marketing/acquisition role

The free modding system is an audience-acquisition and retention mechanism, not merely a feature.

Target flywheel:

Free tools -> creators -> mods -> players -> Biupiu World -> social discovery -> more creators -> more content -> professional users -> simulation/CAD demand -> Biupiu Engine adoption.

No revenue forecast is implied by this architecture.

## Safety and security

Never execute arbitrary uploaded code merely because a package is marked as a mod.

Future runtime isolation should include:

- package validation
- signed manifests
- dependency allowlists
- sandboxing where technically appropriate
- permission declarations
- malware scanning
- resource limits
- rollback
- version pinning
- audit logs

## Verification gates

### REGISTERED
Architecture and creator-rights model recorded.

### IMPLEMENTED
Upload, metadata and validation prototype exists.

### VERIFIED
End-to-end mod submission, scanning, compatibility and rollback are tested.

### RELEASED
Community distribution operates under published creator and content policies.

**Current status: REGISTERED.**
