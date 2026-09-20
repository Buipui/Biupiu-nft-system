"""Provider-backed specialist catalog and cross-domain handoff executor."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Sequence

from .specialist_federation import Capability, Result, SpecialistRegistry, Task


@dataclass(frozen=True)
class ProviderBinding:
    specialist: str
    providers: tuple[str, ...]
    domains: tuple[str, ...]


CATALOG: tuple[ProviderBinding, ...] = (
    ProviderBinding("quantum-ai", ("Cirq", "QuTiP", "OQD", "Qiskit", "PennyLane"), ("quantum", "simulation")),
    ProviderBinding("federated-ai", ("Flower", "PySyft"), ("federated-learning", "privacy")),
    ProviderBinding("vision-geometry-ai", ("OpenCV", "computational-geometry"), ("vision", "geometry", "spatial")),
    ProviderBinding("engineering-simulation-ai", ("engineering-simulators",), ("engineering", "materials", "structures", "vehicles", "energy")),
    ProviderBinding("agriculture-ai", ("agriculture-simulators", "sensor-stack"), ("agriculture", "water", "soil", "crops")),
    ProviderBinding("robotics-embedded-ai", ("Raspberry-Pi", "Arduino"), ("robotics", "embedded", "sensors", "control")),
    ProviderBinding("language-research-ai", ("multilingual-retrieval", "translation"), ("language", "research", "multilingual")),
    ProviderBinding("knowledge-provenance-ai", ("repository-index", "provenance-graph"), ("knowledge", "provenance", "repository")),
    ProviderBinding("media-rendering-ai", ("graphics", "rendering"), ("media", "rendering", "assets")),
    ProviderBinding("security-health-ai", ("monitoring", "anomaly-detection"), ("security", "health", "diagnostics", "failure")),
)


# First-thread department assignment. "FOUND" means a corresponding repository
# module/resource was located during this gate; "TRACK" means the specialist
# identity exists but a department-specific implementation still needs discovery.
DEPARTMENT_ASSIGNMENTS: dict[str, tuple[str, str, tuple[str, ...]]] = {
    "AGRI": ("agriculture-ai", "FOUND", ("Farming Simulation Architecture", "Farming Simulator Resource Registry")),
    "BIO": ("agriculture-ai", "TRACK", ("plant biology", "biotechnology")),
    "BIO-GEN": ("agriculture-ai", "TRACK", ("genetics", "seed breeding")),
    "HEMP": ("agriculture-ai", "FOUND", ("farming simulation", "precision agriculture")),
    "BIOCARBON": ("engineering-simulation-ai", "TRACK", ("carbon materials", "advanced materials")),
    "BIOCHEM": ("engineering-simulation-ai", "FOUND", ("microturbine/energy simulation cross-division track",)),
    "MATERIALS": ("engineering-simulation-ai", "FOUND", ("bio-composite digital twin", "CAD/BEM/CFD/FEA chain")),
    "TEXTILES": ("engineering-simulation-ai", "FOUND", ("AI-enabled smart-textile research",)),
    "AUTO": ("engineering-simulation-ai", "FOUND", ("vehicle simulation pipeline", "microturbine cross-division track")),
    "AERO": ("engineering-simulation-ai", "FOUND", ("flight/aeroelastic digital-twin pipeline",)),
    "MARINE": ("engineering-simulation-ai", "FOUND", ("marine controls/hydrodynamics pipeline", "microturbine cross-division track")),
    "ROBOTICS": ("robotics-embedded-ai", "FOUND", ("MoveIt 2 robotics adapter contract",)),
    "MATH": ("engineering-simulation-ai", "FOUND", ("OR-Tools optimisation", "computational geometry", "mathematical verification", "Digital Twin interface")),
    "PHOTONICS": ("vision-geometry-ai", "TRACK", ("structured light", "OAM", "optical computing")),
    "BIUPIU-OS": ("knowledge-provenance-ai", "FOUND", ("repository index", "provenance", "security architecture")),
    "MEDIA": ("media-rendering-ai", "FOUND", ("Blender/graphics/rendering architecture",)),
    "LANG": ("language-research-ai", "FOUND", ("multilingual research/translation architecture",)),
}


class CatalogSpecialist:
    def __init__(self, binding: ProviderBinding):
        self.binding = binding
        self.capability = Capability(binding.specialist, "1.0", binding.domains, autonomous=True, resident=True)

    def execute(self, task: Task) -> Result:
        return Result(
            task.task_id,
            self.capability.name,
            "completed",
            {"domain": task.domain, "payload": dict(task.payload), "providers": self.binding.providers},
            confidence=1.0,
            provenance={"provider_catalog": self.binding.providers, "mode": "adapter-contract"},
        )


def build_specialist_registry() -> SpecialistRegistry:
    registry = SpecialistRegistry()
    for binding in CATALOG:
        registry.register(CatalogSpecialist(binding))
    return registry


def departments_with_found_modules() -> tuple[str, ...]:
    return tuple(name for name, (_, status, _) in DEPARTMENT_ASSIGNMENTS.items() if status == "FOUND")


def execute_task_graph(registry: SpecialistRegistry, tasks: Sequence[Task]) -> tuple[Result, ...]:
    """Execute an explicit handoff chain; no implicit cross-domain takeover."""
    results: list[Result] = []
    for task in tasks:
        result = registry.dispatch(task)
        results.append(result)
        if result.status == "unresolved":
            break
    return tuple(results)
