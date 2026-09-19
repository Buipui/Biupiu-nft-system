# BIUPIU RUSSIAN-LANGUAGE RESEARCH & CODE SEARCH PROTOCOL v1.0

**Date:** 19 September 2026  
**Status:** Active / permanent source-routing layer

## Purpose

Biupiu Main must search Russian-language technical literature as a first-class research layer where relevant. Russian material is searchable in the original language, translated for synthesis, and cross-linked to English-language and open-source implementation sources.

## Hard-coded source families

1. **ITMO OpenBooks** — robotics, control, simulation, optics/photonics, algorithms, optimization, computer vision and digital-twin research.
2. **Math-Net.Ru** — numerical methods, mathematics, optimization, control, simulation, aerospace and robotics methods.
3. **IPU RAS** — control theory, cyber-physical systems, robotics, optimization, task allocation, diagnostics and AI/control systems.
4. **MedSoc / Medical Sociology Online (BSA Medical Sociology Group)** — medical sociology, health systems, digital-health and human-system research.

Machine-readable registry: `research/source-protocols/BIUPIU-RUSSIAN-SOURCE-PROTOCOL-v1.json`.

## Mandatory search sequence

`RUSSIAN ORIGINAL → ENGLISH TECHNICAL EQUIVALENT → SOURCE METADATA → FULL TEXT → METHOD/ALGORITHM EXTRACTION → CODE/DATA SEARCH → LICENCE/PROVENANCE → REPRODUCTION → DEPARTMENT ROUTING → CODEX → TEST`

## Code integration rule

A publication is **not** code merely because it contains an algorithm.

Executable integration requires:

- implementation identified;
- licence verified;
- dependencies recorded;
- version/commit recorded;
- API/interface compatibility checked;
- security/provenance checked;
- tests added or mapped;
- results compared with the publication's stated assumptions.

Where no implementation exists, Biupiu may create an independent implementation from the published method, clearly labelled as a Biupiu implementation rather than source code from the authors.

## Initial verified research targets

- OpenBooks: autonomous multi-agent terrain monitoring using leader-follower control and gradient-descent trajectory smoothing.
- OpenBooks: UAV control with robotic manipulator using feedback linearisation, PD control, real-time inertia/centre-of-mass updates and reactive-torque compensation.
- OpenBooks: simulation environment architecture for intelligent/multi-agent systems with sensor modelling and socket-based agent communication.
- OpenBooks: analytical/simulation modelling of flexible joints for mechatronic and robotic systems.
- Math-Net.Ru: evolutionary-algorithm comparison for UAV route optimisation.
- Math-Net.Ru: manipulator modelling using Denavit-Hartenberg kinematics, Levenberg-Marquardt inverse kinematics, Newton-Euler dynamics and adaptive neuro-fuzzy methods.
- IPU RAS: cyber-physical and collaborative robotics research, including information-processing algorithms and decentralized/group robotics.
- IPU RAS: task-allocation and work-distribution algorithms with simulation tooling for collaborative robotic systems.

These are **research/algorithm integration candidates**, not claims that the original authors released reusable code.

## Safety / scope

Aerospace and robotics material remains civilian/dual-use and is limited to public research, simulation, efficiency, control, materials and benign engineering. Classified or restricted material is excluded.

## Version control

Every future Russian-source integration must record:
`RU Source ID → Original title → Translation → DOI/URL → Publication year → Claim/algorithm → Code/data status → Licence → Department → CODEX queue → Test status`.
