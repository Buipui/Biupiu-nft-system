# Buipui hardened_malloc Candidate — Integration Contract

## Purpose
Define a controlled compatibility candidate for GrapheneOS hardened_malloc against Buipui's Android 17 baseline.

## Source authority
GrapheneOS/hardened_malloc upstream. Exact source commit must be pinned at implementation time.

## Acceptance gates
- LICENSE/provenance recorded
- exact upstream commit recorded
- Bionic integration patch identified
- arm64 compatibility checked
- 4K page-size requirement checked
- virtual address/page-table assumptions checked
- build succeeds with warnings-as-errors
- upstream allocator tests pass
- AOSP/Bionic tests pass
- Cuttlefish boots
- SELinux audit clean for the change
- no AVB/KeyMint/Keystore regression
- CTS/VTS/security tests pass for the affected surface

## Configuration rule
Start with upstream default security configuration. Do not tune for benchmark performance before establishing security/functionality. Any light configuration is a separate measured profile.

## Rollback
Keep stock AOSP allocator configuration as a selectable baseline until all candidate gates pass.

## Federation evidence
Every build/test event must contain:
commit, source digest, toolchain, target, configuration, test command, result, log/artifact reference, security classification and promotion decision.
