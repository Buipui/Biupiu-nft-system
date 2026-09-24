# Biupiu Digital Twin Simulation Benchmark — 2026-09-24

**Task-ID:** DT-SIM-BENCH-20260924  
**Status:** EXECUTED — SCREENING BENCHMARK  
**Evidence class:** plausible_model  
**Validation:** screening  
**Promotion:** research_only  
**Execution:** isolated local Python runtime; no physical hardware, HIL, QPU or UE5 runtime.

## Purpose

Establish a deterministic digital benchmark that can later be compared against controlled physical measurements. The benchmark is deliberately a reduced-order cantilever fixture rather than a certification model.

The benchmark follows the existing Biupiu Digital Twin boundary:

`MATERIAL → GEOMETRY → LOAD CASE → STRUCTURAL RESPONSE → MODAL/BUCKLING → UNCERTAINTY → PHYSICAL CORRELATION`

The synthetic screening material cards are **not measured material allowables** and must be replaced by traceable Biupiu coupon/test data before design claims.

## Runner

`research/simulators/test_digital_twin_benchmark_20260924.py`

Geometry:
- length = 1.0 m
- width = 0.1 m
- thickness = 0.01 m
- fixed-free boundary
- safety factor = 2.5
- loads = 50 / 100 / 150 N
- SI units

Solver model:
- Euler-Bernoulli cantilever static response
- Euler first-mode frequency
- Euler fixed-free buckling proxy
- deterministic arithmetic benchmark

## Candidate baseline results

| ID | Synthetic E | Density | Mass kg | Tip deflection @100 N mm | Stress MPa | f1 Hz | Buckling margin |
|---|---:|---:|---:|---:|---:|---:|---:|
| BMG-H01 | 25 GPa | 1250 kg/m³ | 1.250 | 160.000 | 60.0 | 7.2243 | 2.0562 |
| BMG-F01 | 30 GPa | 1200 kg/m³ | 1.200 | 133.333 | 60.0 | 8.0770 | 2.4674 |
| BMG-HF01 | 32 GPa | 1220 kg/m³ | 1.220 | 125.000 | 60.0 | 8.2732 | 2.6319 |
| BMG-HFB01 | 40 GPa | 1350 kg/m³ | 1.350 | 100.000 | 60.0 | 8.7931 | 3.2899 |

These values are **benchmark outputs only**. They are not evidence that any listed material has those exact properties.

## Repeatability / execution measurements

Each candidate was evaluated for 10,000 iterations.

| ID | Iterations | Mean runtime | Deterministic | Failures |
|---|---:|---:|---|---:|
| BMG-H01 | 10,000 | 6.1536431 µs | PASS | 0 |
| BMG-F01 | 10,000 | 5.8149772 µs | PASS | 0 |
| BMG-HF01 | 10,000 | 5.7706955 µs | PASS | 0 |
| BMG-HFB01 | 10,000 | 6.8295132 µs | PASS | 0 |

## Load-line benchmark

H01 at the three reference loads produced:

- 50 N → 80 mm tip deflection / 30 MPa stress / 4.1123 buckling margin
- 100 N → 160 mm / 60 MPa / 2.0562
- 150 N → 240 mm / 90 MPa / 1.3708

The static fixture therefore provides a simple later correlation test for load-response linearity. Frequency is independent of applied static load in this reduced-order model.

## Uncertainty sweep

For every candidate:
- E multiplier: 0.90 / 1.00 / 1.10
- density multiplier: 0.95 / 1.00 / 1.05
- 9 combinations per candidate

This creates a first uncertainty envelope for mass, deflection, frequency and buckling margin. The JSON evidence file retains the sweep definition; measured material uncertainty must replace the synthetic bounds for physical correlation.

## Physical-test handoff

First measurements to capture against this benchmark:

1. specimen/component mass
2. static load versus tip displacement
3. strain/stress response
4. first natural frequency
5. safe stability/buckling observations where applicable
6. temperature and moisture/conditioning state
7. specimen geometry and manufacturing revision
8. sensor/test-system calibration metadata

Calibration and independent validation datasets must remain separate. Failed tests remain in the evidence set and are classified rather than removed.

## Evidence boundary

**PASS**
- deterministic simulation execution
- repeatability benchmark
- common geometry/load fixture
- four candidate records instantiated
- load sweep executed
- uncertainty sweep executed
- machine-readable evidence logged

**OPEN**
- measured material cards
- coupon correlation
- component correlation
- rotating subassembly correlation
- HIL
- physical sensor validation
- production/certification evidence

The simulation is a benchmark for later physical testing, **not physical truth, certification, qualification, or an authorisation to actuate hardware**.

## Provenance

Primary architectural references:
- `research/BIUPIU-BLADE-SIMULATION-RUNNER-SPEC-v1.0.md`
- `research/BIUPIU-BIO-COMPOSITE-DIGITAL-TWIN-v1.0.md`
- `research/BIUPIU-BLADE-MATERIAL-GENOME-v1.0.md`
- `research/BIUPIU-DIGITAL-TWIN-ACTIVE-LEARNING-SPEC-v1.0.md`
- `research/BIUPIU-DIGITAL-TWIN-PROMOTION-CONTRACT-v1.0.md`

**Conclusion:** DIGITAL SIMULATION BENCHMARK PASS → PHYSICAL CORRELATION GATE OPEN.
