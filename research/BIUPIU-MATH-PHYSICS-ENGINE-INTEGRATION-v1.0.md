# Biupiu Mathematics + Physics Engine Integration v1.0

**Gate:** SIM-PHYS-01  
**Status:** INTEGRATED at architecture level

Biupiu OS -> Simulation Core -> Math Service / Physics Service -> Digital Twin -> Engine Adapters.

Mathematics services provide deterministic numerical checks, residuals, invariants, geometry validation and optimisation interfaces. Physics services provide dynamics, collision/interaction and domain-specific solver interfaces.

Open/free candidates identified for controlled evaluation: Jolt Physics (MIT), PROJECT CHRONO (BSD-3-Clause), MuJoCo (Apache-2.0), OpenVDB (Apache-2.0). They remain external candidates until dependency, security, compatibility and runtime gates pass.

Proprietary UE5/Unity physics remains external and replaceable. Provider results must include scenario/model version, timestep, units, coordinate system, state kind, provenance, convergence/errors and output identity.

Important scenarios can be cross-checked across providers: reference math -> provider A -> provider B -> residual comparison -> DRIFT/BLOCKED classification.

Visual rendering never becomes engineering truth merely because an engine produced an image or interactive scene.
