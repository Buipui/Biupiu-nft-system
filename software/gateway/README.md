# Biupiu PowerShell Gateway v1.0

Purpose: controlled Windows-host execution adapter for Biupiu OS, built on the existing Biupiu DOS command/compatibility model.

Boundary:
Biupiu OS Core -> DOS command/permission contract -> PowerShell Gateway -> allowlisted host operations -> evidence/audit -> Digital Twin

Rules:
- Biupiu OS remains authoritative for identity, permissions, validation, promotion and recovery.
- Default mode is DRY-RUN.
- Arbitrary command strings and arbitrary script paths are denied.
- Network, download and install operations are denied by the base policy.
- Write operations require explicit approval.
- Every operation emits structured JSON evidence.
- Credentials and secrets are never embedded.
- Digital Twin mirrors validated evidence; it cannot promote host state to authoritative OS state.
- Android is a future control client only; no implicit remote execution path is included.

Initial allowlist: HOST.CAPABILITIES, REPOSITORY.STATUS, REPOSITORY.DIRECTORY, TEST.NAMED, REPOSITORY.WRITE.TEST.

PowerShell is an execution substrate, not the OS authority. Microsoft documents PowerShell as a cross-platform automation platform and PowerShell 7 as a separate product from Windows PowerShell 5.1. The gateway records edition/version and does not assume module compatibility.

Verification boundary: repository implementation can be verified here; Windows host execution, GPU/driver inspection and Unity/UE5/Visual Studio/VS Code discovery remain host-dependent until desktop evidence is collected.

## CI Gate 02 trigger
This marker records that the gateway contract is under automated Windows-runner regression validation.
