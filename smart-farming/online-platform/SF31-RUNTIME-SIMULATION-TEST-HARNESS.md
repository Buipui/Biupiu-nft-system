# SF-31 — Runtime Simulation & Episode Package Test Harness

## Purpose
Create a deterministic simulation layer that tests the Episode 01 package before live Biupiu World activation.

Status: SIMULATION-READY / LIVE RUNTIME DISABLED

## Harness flow
LOAD MANIFEST → RESOLVE SCENES → RESOLVE HERO ASSETS → CHECK CONTEXT LINKS → CHECK CLAIM LABELS → CHECK RIGHTS STATE → CHECK DELIVERY PROFILE → REPORT

## Test cases
- RT-SIM-01: episode manifest loads
- RT-SIM-02: all five department scenes resolve
- RT-SIM-03: all registered hero vehicles resolve
- RT-SIM-04: department/research/Digital Lab/Academy context keys exist
- RT-SIM-05: claim labels match SF-26/SF-27 records
- RT-SIM-06: prohibited/unapproved asset states are blocked
- RT-SIM-07: publication state cannot bypass human approval
- RT-SIM-08: rollback metadata exists
- RT-SIM-09: delivery profiles are internally consistent
- RT-SIM-10: archive requirements are present

## Failure policy
Any missing scene, asset, claim status, rights state or required context link produces a BLOCKED result.

## Important
Simulation validates repository metadata and workflow logic. It does not prove that an actual 3D render, animation, sound mix or runtime application works until those production assets and runtime builds exist.
