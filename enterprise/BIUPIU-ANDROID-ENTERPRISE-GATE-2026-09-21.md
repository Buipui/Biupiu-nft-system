# Biupiu Enterprise Android — Harvest + Commercial Optimisation Gate 2026-09-21

## Completed
- Deep Android Enterprise capability harvest
- GitHub enterprise code/reference harvest
- Existing Biupiu DMS/OS/Intelligence cross-reference
- Enterprise tenancy and device lifecycle model
- AI enterprise governance boundary
- Commercial product-tier structure
- Security and evidence-plane separation
- Consolidation rule to prevent duplicate authorities

## Promotion decisions

KEEP-AOSP:
DevicePolicyManager, managed profiles, device-owner/fully-managed flows, managed configurations, provisioning, Mainline, Cuttlefish.

KEEP-REFERENCE:
Android Enterprise Samples, TestDPC.

RESEARCH-ONLY:
Third-party framework mirrors/wrappers and unspecified OpenBooks material until provenance/licence/compatibility/security gates pass.

REJECT:
Security bypasses, profile-boundary bypasses, AVB/SELinux weakening, unsigned privileged code, copied proprietary blobs/keys.

## Immediate implementation gate
Build a Buipui Enterprise Policy Broker around official Android Enterprise APIs, then expose it to DMS and the Multi-AI Federation through a narrow audited interface.

Policy flow:
Enterprise Policy -> Android Enterprise API/action -> observed device result -> audit event -> DMS state -> AI evidence.

No AI agent receives unrestricted DevicePolicyManager authority.
