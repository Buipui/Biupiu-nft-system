# Biupiu G32-C — Controlled GitHub Actions Pinning

## Status
IMPLEMENTED_NOT_VERIFIED

## Scope
Establish an evidence-preserving action-integrity gate before changing the repository-wide workflow surface.

## Verified upstream evidence
- actions/checkout v4.4.0 is a signed GitHub release.
- actions/setup-java v4.9.1 is an immutable signed release.
- Current upstream documentation indicates newer major releases exist; this gate does not perform an unrelated major-version migration.

## Controls
1. Discover every workflow action reference.
2. Resolve owner/repository and exact release provenance.
3. Pin only when the exact immutable commit SHA is verified.
4. Never fabricate or infer SHAs.
5. Keep workflow permissions least-privilege.
6. Re-run security and supply-chain audits after every controlled mutation.
7. Treat build success separately from runtime, OEM, HIL, and production verification.

## Current boundary
The repository-wide action set is not yet fully SHA-pinned. No blanket replacement is performed.

## Next gate
G32-D — Android Keystore/runtime validation and controlled completion of the verified action allowlist.
