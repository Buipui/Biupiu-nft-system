# Mini-OS G02 — Federated Compute Contract
## Status
IMPLEMENTED_NOT_VERIFIED
## Implemented
- CPU/vector/GPU/NPU compute classes.
- Minimum compute-class requirement is fail-closed.
- Preferred class is selected when available.
- Capacity is fallback selection signal.
- C++ and Rust tests.
## Verification boundary
CI/native compilation and physical accelerator discovery remain open.
