from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class SimulationRequest:
    module: str
    inputs: dict[str, Any]
    requested_evidence_state: str = "simulated"
    environment: dict[str, Any] = field(default_factory=dict)

@dataclass
class SimulationResponse:
    module: str
    status: str
    outputs: dict[str, Any]
    evidence_state: str
    warnings: list[str] = field(default_factory=list)
    provenance: list[str] = field(default_factory=list)

def validate_request(req: SimulationRequest):
    if not req.module.strip():
        raise ValueError("module is required")
    if not isinstance(req.inputs, dict):
        raise TypeError("inputs must be a mapping")
    return req
