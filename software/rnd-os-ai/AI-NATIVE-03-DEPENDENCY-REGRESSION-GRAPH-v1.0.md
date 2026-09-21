# AI-NATIVE-03 — Cross-Gate Dependency / Regression Graph v1.0
**Status:** REGISTERED + IMPLEMENTED / HOST VERIFICATION PENDING

## Purpose
Use the Multi-AI architecture-builder protocol to harvest and challenge dependencies among Native OS proving-ground gates before promotion to Main OS.

## Initial harvested graph
VIS-NATIVE-19 -> VIS-NATIVE-20 -> VIS-NATIVE-21 -> VIS-NATIVE-22 -> VIS-NATIVE-23

Additional dependency:
VIS-NATIVE-19 -> VIS-NATIVE-22
VIS-NATIVE-22 -> VIS-NATIVE-23

Interpretation:
- memory ownership is foundational to shader/material and asset runtime work;
- shader execution precedes material runtime;
- asset runtime depends on memory and material contracts;
- render graph depends on asset/resource readiness.

## Challenge rules
- Missing dependency = BLOCKED.
- Cycle = rejected.
- External authoritative ownership = CONFLICT.
- Deterministic topological order is required.
- Promotion requires host test + regression evidence; source implementation alone is insufficient.

## Protocol
HARVEST -> MAP -> CHALLENGE -> PROPOSE -> IMPLEMENT -> VERIFY -> REGRESS -> AUDIT -> PROMOTE
