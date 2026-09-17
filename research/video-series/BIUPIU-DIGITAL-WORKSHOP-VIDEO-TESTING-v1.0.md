# Biupiu Digital Workshop — Video-Based Engineering Testing Protocol v1.0

**Date:** 17 September 2026  
**Status:** ACTIVE / VIRTUAL VALIDATION  
**Scope:** Biupiu R&D repository, engineering-validation video series and prototype queue

## 1. Purpose

The Digital Workshop is a virtual engineering environment for testing research hypotheses before physical prototyping. It combines AI-generated visualisations, simulation outputs, CAD/geometry, calculations, source videos and structured test records.

A video is treated as a **test input or visualisation**, not as proof of a physical result. This distinction follows the established difference between simulation and a data-synchronised digital twin: a digital twin is tied to a real-world system through specified data exchange, while a simulation can operate independently. citeturn0search3turn0search4

## 2. Video evidence classes

| Class | Use | Evidence status |
|---|---|---|
| V0 — Reference video | Third-party source used to identify a claim or design | Discovery only |
| V1 — AI concept video | Original Biupiu visualisation of a proposed design | Concept only |
| V2 — Simulation video | Animated/modelled response under stated assumptions | Computational result |
| V3 — Digital-workshop test | Controlled virtual test with logged inputs, model, parameters and outputs | Experimental-computational |
| V4 — Instrumented prototype video | Physical prototype with identifiable instrumentation and raw data | Physical evidence |
| V5 — Correlated twin video | Virtual model updated/calibrated against measured physical data | Digital-twin evidence |

## 3. Standard video test record

Every test video must log:

- Test ID and version
- Research/department IDs
- Source claim and source URL where applicable
- Creator/rights status for third-party material
- Hypothesis or engineering question
- Model/CAD version
- Geometry and material assumptions
- Boundary conditions and input values
- Software/tool/version
- Random seed where applicable
- Simulation duration and timestep/resolution
- Sensors/instrumentation if physical data are used
- Expected outcome and falsification condition
- Actual virtual result
- Uncertainty/sensitivity notes
- Raw-data location
- Reviewer status
- Disposition: repeat / modify / physical prototype / defer / falsify

## 4. Digital Workshop test loop

`VIDEO/CLAIM → DECOMPOSE → MODEL → PARAMETERISE → VIRTUAL TEST → RECORD OUTPUT → SENSITIVITY TEST → FALSIFICATION CHECK → DESIGN ITERATION → PHYSICAL TEST → CALIBRATION → DIGITAL-TWIN UPDATE`

Virtual results must never be silently promoted to physical performance claims.

## 5. Initial workshop test modules

### DW-001 — Hybrid VAWT

Test rotor geometry, blade pitch, solidity, wind speed, rotational speed, torque and generator loading. Produce comparative virtual runs and identify parameters requiring physical measurement.

### DW-002 — Low-head micro-hydro

Test head, flow, runner geometry, hydraulic losses and generator loading. Include sediment/debris assumptions and safe shutdown logic.

### DW-003 — Farm-energy controller

Model PV/wind/storage/load combinations, state of charge, peak demand, curtailment and controller responses. Test disturbance scenarios before controller-in-loop work.

### DW-004 — Hemp processing

Model/process-map decortication and fractionation variables including feedstock dimensions, moisture, throughput, yield, energy demand, dust and quality outputs. Treat simulated yield as a prediction until physically measured.

### DW-005 — Desiccant cooling

Model temperature/humidity conditions, moisture removal, regeneration heat, energy demand and coefficient of performance. Perform sensitivity tests on ambient conditions and regeneration temperature.

### DW-006 — FSO / photonics

Model optical link geometry, atmospheric attenuation/turbulence assumptions, link margin, routing alternatives and adaptive-control hypotheses. Use GIS/CAD inputs where available; deployment claims require field measurements and regulatory review.

### DW-007 — Metamaterials / structured-light concepts

Use electromagnetic or optical simulation to explore candidate geometries and wavefront/phase responses. Clearly label simulated fields as computational outputs and identify fabrication and measurement requirements.

### DW-008 — Complex geometry

Use deterministic geometry generation to test topology, symmetry, parameter changes, mesh quality and measurable geometric properties. Preserve seed, parameters and algorithm version.

## 6. AI-generated video rules

AI-generated videos may be used as original Biupiu prototype visualisations, explanatory animations and virtual-test presentations. They must carry an on-screen status such as **AI CONCEPT**, **SIMULATION**, **DIGITAL WORKSHOP TEST**, or **PHYSICAL TEST** according to the evidence class.

AI-generated footage must not depict a simulated event as if it were recorded physical evidence. If an AI reconstruction illustrates a proposed physical experiment, the narration must state that it is illustrative.

## 7. From video to physical validation

A virtual result advances to physical testing only when the test record contains:

1. Defined measurable quantity.
2. Valid model and assumptions.
3. Reproducible parameters.
4. Sensitivity/failure analysis.
5. Safety review.
6. Prior-art/IP review where relevant.
7. Instrumentation and calibration plan.
8. Raw-data capture plan.

Physical results then become calibration data for the next workshop iteration. A sufficiently synchronized model may later qualify as a digital twin; until that condition exists, call it a simulation or digital model rather than a true twin. citeturn0search5turn0search7

## 8. Video-series integration

This protocol is directly linked to `EP01-PRODUCTION-PACKAGE-v1.0.md` and the Season 1 engineering-validation series. Each episode may contain:

- claim intake clip/reference;
- original Biupiu AI concept visual;
- digital-workshop simulation;
- parameter dashboard;
- test result animation;
- falsification/sensitivity segment;
- physical prototype footage when available;
- comparison of predicted versus measured data;
- repository-linked test record.

## 9. Release gate

No video is labelled **validated** merely because it looks realistic, produces a plausible animation, or agrees with an unverified source video. Validation requires evidence appropriate to the claim class and, for physical claims, reproducible measurement.

**Digital Workshop status:** ACTIVE.  
**Physical prototype status:** separate gate; not implied by virtual testing.
