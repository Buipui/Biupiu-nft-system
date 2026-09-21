# Biupiu Modding Station v0.1

## User experience

Avatar enters a Biupiu World Modding Station and can:

1. Create or import a project.
2. Select Unreal, Unity or Biupiu-native target.
3. Declare licence and third-party dependencies.
4. Run metadata, package, compatibility and security checks.
5. Submit for community review.
6. Publish to the Mod Hub only after approval.
7. Test in an isolated preview session.
8. Roll back to a previously approved version.

## Native tools to build

- Project wizard
- Asset/package manifest generator
- Licence declaration form
- Dependency graph and allowlist
- Content hash generator
- Static package inspection
- Compatibility profile checker
- Permission/capability declaration
- Sandbox/isolated preview boundary
- Human/community review queue
- Version and rollback manager
- Creator attribution and changelog
- Cross-engine metadata translator
- Analytics with privacy controls

## Engine adapters

Unreal and Unity are initial adapters. The repository format must not depend on either engine's proprietary project structure. A neutral manifest is the canonical record, while engine-specific files remain adapter payloads.

## Safety rule

Uploaded packages must be treated as untrusted. Do not execute arbitrary scripts, native binaries, shaders or plugins during ingestion. Validation should begin with static inspection and declared capabilities; execution requires a separately designed sandbox and explicit approval.

## Give-back model

The basic station and community submission path is intended to remain free. Optional professional features may later support paid services without removing creator ownership or attribution.

## Gate state

**REGISTERED — IMPLEMENTATION PROTOTYPE PARTIAL — SECURITY/ENGINE TESTING PENDING.**
