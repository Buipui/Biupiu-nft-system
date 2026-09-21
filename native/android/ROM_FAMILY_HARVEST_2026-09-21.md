# Buipui Native Android — ROM Family Harvest 2026-09-21

## Scope
Official/public source harvest for LineageOS, crDroid, GrapheneOS and CalyxOS. Sources are treated as upstream references, not as permission to copy project branding, proprietary material, signing keys, device blobs, or code without license review.

## Promotion protocol
DISCOVER -> OFFICIAL SOURCE -> PROVENANCE -> LICENSE -> AOSP/ANDROID17 COMPATIBILITY -> SECURITY REVIEW -> BUILD/TEST -> PROMOTE

### LineageOS
KEEP-REFERENCE / selective source promotion:
- device-support requirements: SELinux enforcing, userdebug, GKI/source-built modules where feasible, CVE maintenance, recovery/updater discipline, proprietary-file provenance.
- upstream repo manifest/device-tree patterns.
- device support and reproducible extraction discipline.
Source: LineageOS/android and LineageOS/charter.

### crDroid
KEEP-REFERENCE / selective source promotion:
- modular Settings/SystemUI customization architecture.
- configurable status bar, QS, lockscreen, gestures, theming, GameSpace, sandbox/app-isolation concepts and OTA/update UX.
- maintainer rules requiring public source, clean dependency declarations, testing and official documentation.
Do NOT promote Integrity/attestation spoofing or bypass mechanisms into Buipui security architecture.
Source: crdroidandroid/android, crDroid Settings, crDroid feature manifest, maintainer rules.

### GrapheneOS
HIGH-PRIORITY SECURITY RESEARCH / selective source promotion:
- hardened_malloc integration model for Bionic/Android.
- memory hardening, quarantine, zero-on-free, MTE-aware protections and aggressive allocator sanity checks.
- Vanadium hardening architecture as a reference for a hardened browser/WebView component.
- stable-tag-first build discipline and explicit source manifest.
Source: GrapheneOS/hardened_malloc, GrapheneOS/Vanadium, GrapheneOS build/source documentation.
Compatibility must be demonstrated against the locked Buipui Android 17/GKI target before promotion.

### CalyxOS
KEEP-REFERENCE / selective source promotion:
- SeedVault encrypted backup architecture.
- Datura firewall / per-app network-control concept.
- public GitLab/GitHub development and Gerrit workflow.
- reproducible AOSP-style build/install workflow and separate handling of components built outside the main tree.
Do not import stale Android-13-only code directly; rebase/port and test against current Android 17 APIs.

## Foreign-language / XDA lane
Foreign-language search and XDA are discovery/corroboration inputs only. No code is promoted from forum posts, mirrors, translations, repacks or unofficial builds unless the canonical upstream repository, license and exact commit can be established.

## OpenBooks lane
No unique authoritative OpenBooks codebase was established for these four ROM projects in this harvest. Keep OpenBooks material RESEARCH-ONLY until canonical provenance, license and compatibility are established.

## Security exclusions
- no SELinux weakening
- no AVB/rollback bypass
- no KeyMint/Keystore bypass
- no Play Integrity spoofing/bypass
- no unsigned privileged components
- no copied private keys
- no unverified proprietary blobs
- no kernel changes without kernel-specific review

## Current state
HARVESTED: YES
SOURCE-INTEGRATED: REFERENCE/POLICY ONLY
COMPILED: NOT VERIFIED
BOOT-VERIFIED: NOT VERIFIED
FUNCTION-VERIFIED: NOT VERIFIED
SECURITY-VERIFIED: NOT VERIFIED
DEVICE-VERIFIED: NOT VERIFIED
