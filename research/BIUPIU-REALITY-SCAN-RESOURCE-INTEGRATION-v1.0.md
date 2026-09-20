# Biupiu Reality Scan & Resource Integration v1.0

**Gate:** REALITY-SCAN-01  
**Status:** IMPLEMENTED — repository evidence layer  
**Promotion rule:** DISCOVERED -> LICENSE-CHECKED -> RELEVANCE-CHECKED -> ISOLATED -> TESTED -> INTEGRATED -> VERIFIED

## Evidence layers
1. Repository evidence — source, commit, tests, manifests.
2. Open-source evidence — authoritative project/licence/security documentation.
3. Open-book evidence — legally reusable reference material; licence is recorded separately from software.
4. Runtime evidence — workstation/build/hardware tests.
5. Promotion evidence — reproducible contract and regression results.

## Candidate inventory
| Candidate | Domain | Licence | Biupiu role | State |
|---|---|---|---|---|
| Khronos OpenXR SDK | XR | Apache-2.0 | OpenXR loader/API boundary | LICENSE-CHECKED |
| Jolt Physics | Physics | MIT | rigid-body/collision provider candidate | LICENSE-CHECKED |
| Project Chrono | Multiphysics | BSD-3-Clause | high-fidelity multibody/multiphysics provider candidate | LICENSE-CHECKED |
| MuJoCo | Physics/control | Apache-2.0 | robotics/control/physics provider candidate | LICENSE-CHECKED |
| OpenEXR | Imaging | BSD-3-Clause | HDR/render interchange | LICENSE-CHECKED |
| Khronos glTF | Asset interchange | mixed repository licensing; file-level rules apply | runtime asset interchange | LICENSE-CHECKED |
| OpenStax Physics | Reference | CC BY 4.0 | non-code physics reference/knowledge source | LICENSE-CHECKED |

## Safety and provenance rules
- No dependency is promoted solely because it is free.
- No binary-only dependency is promoted without provenance.
- Licence ambiguity blocks code integration.
- Security-critical code requires upstream security evidence and local regression coverage.
- External engines remain providers; Biupiu remains the canonical state/validation layer.
- Repository integration does not prove workstation, GPU, XR-headset, UE5, Unity or Lumion runtime compatibility.

## Open-book separation
OpenStax Physics is CC BY 4.0, while many other OpenStax textbooks are CC BY-NC-SA. Therefore the repository records the exact title/licence rather than treating all OpenStax material as interchangeable.

## Verification boundary
This gate establishes a traceable resource inventory and promotion policy. It does not claim that every candidate has been compiled or executed on the user's workstation.
