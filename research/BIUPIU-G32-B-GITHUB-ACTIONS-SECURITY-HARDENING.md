# BIUPIU G32-B — GITHUB ACTIONS SECURITY & SUPPLY-CHAIN HARDENING

Date: 21 September 2026

## Objective
Audit the repository-wide GitHub Actions surface before allowing workflow/action pinning to become a verified security control.

## Implemented
- Dedicated repository-wide workflow action reference audit.
- Least-privilege permission policy recorded.
- Full-length SHA pinning treated as the promotion target.
- Action upgrades/pinning are not applied blindly: every SHA must be resolved against the action repository and release/tag provenance first.
- Existing Android security gate remains green after its self-scan defect was corrected.

## Current finding
The repository contains a large historical workflow set and many action references. Therefore G32-B separates:
1. discovery,
2. provenance verification,
3. controlled pinning,
4. regression verification.

No action SHA is fabricated.

## Promotion rules
- Unknown action owner/repository: FAIL CLOSED.
- Floating tag/branch: NOT VERIFIED.
- Full-length immutable SHA with verified upstream provenance: ELIGIBLE.
- Local/self-authored workflow: review independently.
- Third-party action: license/security/provenance review required.
- Permissions must remain no broader than required.
- Secret values must never enter workflow source.

## Verification boundary
Action-SHA compliance is repository CI policy, not proof that the Android application or physical OEM target is secure.

## Next gate
G32-C — controlled action pinning for the verified action set, followed by repository-wide CI regression and Android runtime/Keystore verification.
