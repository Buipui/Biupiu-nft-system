from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Any, Protocol

@dataclass(frozen=True)
class AdapterSpec:
    name: str
    domain: str
    protocol: str
    status: str = "contract-only"
    external_dependency: str = ""
    notes: str = ""

class EngineAdapter(Protocol):
    spec: AdapterSpec
    def health(self) -> dict[str, Any]: ...
    def execute(self, payload: dict[str, Any]) -> dict[str, Any]: ...

class ContractAdapter:
    """Safe placeholder: records integration contract without pretending a runtime exists."""
    def __init__(self, spec: AdapterSpec):
        self.spec = spec
    def health(self):
        return {"adapter": self.spec.name, "status": self.spec.status, "runtime_available": False}
    def execute(self, payload):
        raise RuntimeError(f"{self.spec.name} runtime is not installed; adapter contract only")

def default_adapters():
    return [
        ContractAdapter(AdapterSpec("ue5-massentity", "visualization/entity", "C++ API", external_dependency="Unreal Engine MassEntity")),
        ContractAdapter(AdapterSpec("unity-entities", "visualization/entity", "C# API", external_dependency="Unity Entities/DOTS")),
        ContractAdapter(AdapterSpec("project-chrono", "multiphysics", "C++/PyChrono", external_dependency="Project Chrono")),
        ContractAdapter(AdapterSpec("gazebo-sim", "robotics/sensors", "Gazebo Transport/Protobuf", external_dependency="Gazebo Sim")),
        ContractAdapter(AdapterSpec("openfoam", "CFD", "solver/process boundary", external_dependency="OpenFOAM")),
        ContractAdapter(AdapterSpec("hardware-iot", "hardware", "MQTT/OPC-UA/Modbus", external_dependency="device gateway")),
    ]
