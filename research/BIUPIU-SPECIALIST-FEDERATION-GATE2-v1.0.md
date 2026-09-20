# Biupiu Specialist Federation Gate 2 — Provider Registry and Task Flow

## Status
- Implemented: provider-backed specialist catalog contract.
- Implemented: ten resident/autonomous specialist identities.
- Implemented: explicit sequential task-graph handoff.
- Verified at repository level: source and tests written to the federation branch.
- Runtime package execution: pending in an environment with the repository dependencies.

## Architecture
Each specialist remains resident on its assigned system and owns its local domain. The
catalog records provider stacks without silently importing or installing optional packages.
Biupiu Intelligence can explicitly compose specialists into a task graph. A task is not
automatically handed to another domain: collaboration must be explicit.

## Provider families
Quantum (Cirq/QuTiP/OQD/Qiskit/PennyLane); Federated/Privacy (Flower/PySyft);
Vision/Geometry; Engineering Simulation; Agriculture; Robotics/Embedded;
Language/Research; Knowledge/Provenance; Media/Rendering; Security/Health.

## Verification target
The included tests cover resident/autonomous registration, a quantum -> engineering ->
agriculture cross-domain chain, and fail-closed behavior for an unknown domain.

## Boundary
This gate does not claim provider packages are installed, does not submit jobs to
physical quantum hardware, and does not silently promote learned models.
