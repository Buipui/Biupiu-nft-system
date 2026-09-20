# Biupiu PowerShell Gateway Gate 01 — DOS-Based Host Control

Date: 20 September 2026
Status: REPOSITORY IMPLEMENTATION COMPLETE / HOST VERIFICATION OPEN

## Executed scope
- Existing Biupiu DOS compatibility/command model reused as the gateway design basis.
- Provider-neutral gateway boundary implemented.
- Default dry-run mode implemented.
- Explicit operation allowlist implemented.
- Arbitrary command/script execution denied.
- Write operations require explicit approval.
- Structured evidence output implemented.
- Deterministic policy test implemented.
- Digital Twin gateway schema registered.
- Android is represented as a future control client only; no live remote execution is claimed.

## External adapter reconciliation
- Graphics adapter boundary: COMMITTED.
- Graphics candidate manifest: COMMITTED.
- Windows host probe: COMMITTED / HOST-EXECUTION-PENDING.
- Vendor code copied into Core: NO.
- GPU/driver/CMake/CUDA/DXR/Vulkan host detection: UNVERIFIED.

## DOS relationship
PowerShell is an adapter/execution backend for approved Windows operations. It does not replace the DOS runtime and does not become the Biupiu OS authority.

## Digital Twin
OS Twin -> DOS command contract -> PowerShell Gateway Twin -> host observations/evidence -> Digital Twin.
The Digital Twin mirrors validated state and lineage. It cannot promote unverified host results into authoritative OS state.

## Status
- Repository files/read-back: COMMITTED.
- Gateway policy: IMPLEMENTED.
- Gateway source: IMPLEMENTED.
- Deterministic test: IMPLEMENTED.
- Digital Twin schema: IMPLEMENTED.
- Windows PowerShell execution: PENDING / UNVERIFIED.
- Unity/UE5/Visual Studio/VS Code host discovery through gateway: PENDING / UNVERIFIED.
- Android-to-Windows live control: NOT IMPLEMENTED.
- Production promotion: OPEN.

## Exterminate
No unrestricted execution primitive, network/download/install path or embedded credential was introduced. No third-party vendor code was copied into the gateway.

Next gate: run the gateway and graphics probe on the Windows development host, collect JSON evidence, execute named tests, reconcile evidence into the Digital Twin, and then update promotion status.