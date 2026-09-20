"""Provider-backed specialist catalog and cross-domain handoff executor.

This layer instantiates specialist identities without requiring optional provider
packages to be installed. Provider availability is declared as metadata and
runtime adapters can be attached later. Local autonomy is always preferred;
handoffs occur only when a task explicitly names collaborators.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from .specialist_federation import Capability, Result, Specialist, SpecialistRegistry, Task


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


class CatalogSpecialist:
    def __init__(self, binding: ProviderBinding):
        self.binding = binding
        self.capability = Capability(
            binding.specialist, "1.0", binding.domains, autonomous=True, resident=True
        )

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


def execute_task_graph(
    registry: SpecialistRegistry,
    tasks: Sequence[Task],
) -> tuple[Result, ...]:
    """Execute an explicit handoff chain; no implicit cross-domain takeover."""
    results: list[Result] = []
    for task in tasks:
        result = registry.dispatch(task)
        results.append(result)
        if result.status == "unresolved":
            break
    return tuple(results)
