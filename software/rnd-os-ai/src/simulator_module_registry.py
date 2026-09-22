"""Rights-gated registry for simulator modules and public integration targets.

The registry separates discovery from executable activation. It records candidate
modules without downloading, installing, importing, or executing third-party code.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class SimulatorModule:
    module_id: str
    family: str
    integration_boundary: str
    status: str
    executable_activation: bool
    required_gates: Tuple[str, ...]
    design_contract: str = "docs/architecture/BIUPIU-DESIGN-LANGUAGE-CODE-CONTRACT-v1.0.json"
    interaction_contract: str = "research/BIUPIU-UI-SEMANTIC-ACTION-CONTRACT-v1.0.md"


MODULES: Tuple[SimulatorModule, ...] = (
    SimulatorModule(
        "gazebo",
        "robotics_simulation",
        "local-executable-adapter",
        "ADAPTER_REGISTERED",
        False,
        ("provenance", "licence", "dependency", "security", "smoke", "regression"),
    ),
    SimulatorModule(
        "mujoco",
        "multibody_dynamics",
        "provider-neutral-adapter",
        "DISCOVERED_REFERENCE",
        False,
        ("provenance", "licence", "dependency", "security", "smoke", "regression"),
    ),
    SimulatorModule(
        "openusd",
        "scene_interchange",
        "file-format-adapter",
        "DISCOVERED_REFERENCE",
        False,
        ("provenance", "licence", "dependency", "security", "roundtrip", "regression"),
    ),
    SimulatorModule(
        "3dgs",
        "neural_scene_representation",
        "data-pipeline-adapter",
        "DISCOVERED_REFERENCE",
        False,
        ("provenance", "licence", "dependency", "security", "dataset", "regression"),
    ),
)


def module_matrix() -> dict[str, SimulatorModule]:
    """Return the immutable candidate registry without activating external code."""
    return {module.module_id: module for module in MODULES}


def activation_candidates() -> tuple[str, ...]:
    """Return only modules explicitly eligible for a future review gate.

    No candidate is executable merely because it appears in this registry.
    """
    return tuple(
        module.module_id
        for module in MODULES
        if module.status == "ADAPTER_REGISTERED" and module.executable_activation
    )
