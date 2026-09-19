# BIUPIU MATHEMATICAL PROBLEM-SOLVING SYSTEM v1.0

**Date:** 19 September 2026  
**Status:** Active architecture specification

## Mission

Provide a reusable mathematical reasoning and verification pipeline for Biupiu R&D. The system combines theorem retrieval, symbolic mathematics, numerical optimisation, geometry, formal verification, uncertainty analysis and digital-twin feedback.

It is a **solver/orchestrator**, not an autonomous authority: results require validation appropriate to the problem.

## Architecture

`INPUT → CLASSIFY → NORMALIZE → RETRIEVE → DECOMPOSE → SOLVE → VERIFY → SIMULATE → SENSITIVITY → DIGITAL-TWIN → VALIDATE → RECORD`

### 1. Input and classification

Classify each problem into one or more domains:

- algebra
- analysis/calculus
- differential equations
- optimisation/control
- probability/statistics
- geometry/topology
- graph theory
- numerical methods
- mechanics/physics
- materials/engineering
- AI/ML
- biomedical/biological modelling

Capture variables, units, constraints, objective, boundary/initial conditions and evidence requirements.

### 2. Theorem and method retrieval

Search by mathematical structure rather than wording alone.

Primary research layers:

- Math-Net.Ru
- ITMO OpenBooks
- multilingual institutional repositories
- arXiv/formal-math literature
- theorem/lemma semantic indexes
- GitHub implementations

The system should preserve original-language titles and translations.

### 3. Problem decomposition

Break complex problems into:

`MAIN PROBLEM → SUBPROBLEMS → LEMMAS/MODELS → SOLVERS → INTERFACES → VERIFICATION`

Candidate lemmas are tagged as:
- known/result-backed;
- candidate;
- derived;
- unverified.

Never label a newly generated statement a theorem until proof/verification supports it.

### 4. Solver portfolio

Select or combine:

- symbolic algebra;
- numerical linear algebra;
- nonlinear/root finding;
- constrained optimisation;
- mixed-integer/constraint programming;
- graph algorithms;
- ODE/PDE methods;
- control/trajectory optimisation;
- geometry algorithms;
- probabilistic/statistical methods;
- surrogate and multi-fidelity optimisation.

The portfolio should support multiple independent formulations when a result is consequential.

### 5. Verification

Verification layers:

1. dimensional/unit consistency;
2. symbolic simplification;
3. numerical residual;
4. constraint satisfaction;
5. independent solver cross-check;
6. sensitivity/conditioning;
7. uncertainty propagation;
8. formal proof where practical;
9. engineering simulation;
10. physical experiment where required.

A solver's convergence is not proof of model correctness.

### 6. Digital-twin interface

Mathematical models expose a common interface:

`STATE, PARAMETERS, INPUTS, OUTPUTS, CONSTRAINTS, UNCERTAINTY, VERSION, PROVENANCE`

Digital twins can feed measured state/telemetry back into model calibration and can return predicted states, sensitivities and optimisation candidates to engineering simulators.

### 7. Engineering routing

MATH automatically supports:

- AERO — trajectory, aerodynamics, optimisation, stability;
- MARINE — hydrodynamics, geometry, optimisation;
- ENERGY — conversion, storage, control and degradation models;
- MATERIALS/COMPOSITES — constitutive models, optimisation, uncertainty;
- PHOTONICS/ELECTROMAG — propagation, inverse problems, optimisation;
- ROBOTICS — kinematics, dynamics, planning and control;
- ADV-MFG — process optimisation, scheduling and geometry;
- AGRI/WATER — hydrology, optimisation and resource models;
- BIOMED — quantitative modelling and device/diagnostic analysis;
- AI — training objectives, optimisation, evaluation and uncertainty;
- DIGITAL-TWIN — model calibration and predictive simulation.

### 8. Workshop simulator integration

Every engineering simulator may expose a MATH adapter:

`SIMULATOR ↔ DIGITAL-TWIN ↔ MATH SOLVER ↔ PARAMETER UPDATE`

The adapter must record:
- simulator version;
- model version;
- solver version;
- parameters;
- initial state;
- boundary conditions;
- random seed where applicable;
- result hash;
- validation status.

## Current research-informed capabilities

The 2026 research scan identifies several useful directions:

- AI-assisted formal mathematics and research-agent workflows;
- semantic retrieval over very large theorem corpora;
- multilingual mathematical problem retrieval;
- formal theorem proving with Lean;
- geometry theorem proving;
- multi-fidelity optimisation under uncertainty;
- generalisable algorithm discovery;
- two-level stochastic optimisation;
- nonconvex ε-optimality conditions;
- higher-order state-constrained optimal control.

These are **research directions and integration targets**, not claims that Biupiu has independently reproduced their results.

## Open-source candidate adapters

- Google OR-Tools — combinatorial optimisation, CP-SAT, LP, routing and graph algorithms.
- AlphaGeometry / AlphaGeometry2 — geometry theorem proving and DDAR.
- MathNet — multilingual mathematical problem/retrieval benchmark.
- MathAdv — Lean theorem-proving evaluation resources.
- Symath-MCP — symbolic mathematical tool interface.
- NASA Dantzig-Wolfe solver — linear-program decomposition.
- SciPy / SymPy / SciML — numerical and symbolic scientific computing.

Each candidate remains external until licence, provenance, dependency, security and compatibility checks pass.

## Failure-learning protocol

Every failed solve creates a structured record:

`PROBLEM → ATTEMPT → FAILURE TYPE → ROOT CAUSE → CORRECTION → TEST → REUSABLE LESSON`

Failure records must not be deleted during housekeeping. They become training/retrieval material after review.

## Research integrity

The system distinguishes:
- source theorem;
- independently derived result;
- computational observation;
- simulation result;
- conjecture;
- engineering measurement.

No category is silently promoted into another.

## Safety

Engineering outputs are advisory until appropriate domain validation is completed. The system must not autonomously deploy changes to physical systems from mathematical optimisation alone.
