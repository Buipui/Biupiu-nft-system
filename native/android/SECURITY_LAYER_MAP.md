# Buipui Security Layer Map

Status: MAPPED / IMPLEMENTATION PENDING

## Kernel layer
Candidate classes:
- kernel hardening
- memory/exploit mitigations
- driver isolation
- attack-surface reduction
- secure boot chain dependencies
- kernel integrity and audit hooks

Rule: only code with a justified kernel responsibility is admitted here.

## Android platform layer
Candidate classes:
- SELinux policy
- permissions and identity boundaries
- sandboxing
- verified boot / integrity
- keystore/cryptographic services
- system-service isolation
- update and rollback integrity

## Buipui native layer
Candidate classes:
- system integrity monitoring
- configuration/repository integrity
- anomaly detection
- service health monitoring
- multi-AI security arbitration
- audit/event pipeline
- failure-learning with security boundaries

## APK layer
Candidate classes:
- user-facing security controls
- diagnostics
- policy/status dashboards
- non-privileged management functions

## Intake rule
Every collected library/module is classified as:
KEEP-KERNEL | KEEP-AOSP | KEEP-NATIVE | KEEP-SYSTEM-APK | KEEP-APK | RESEARCH-ONLY | REJECT

Before integration, record:
- license
- source/provenance
- Android/AOSP compatibility
- architecture/ABI
- privilege requirements
- maintenance status
- known CVEs/security posture
- build/test evidence
- duplication with existing AOSP capability

No unverified security library is promoted into the kernel merely because it is security-related.
