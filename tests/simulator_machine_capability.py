"""Deterministic, transport-neutral machine-capability simulation adapter."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class TelemetryEnvelope:
    capability_id: str
    twin_id: str
    value: float
    unit: str
    quality: str
    state_class: str
    provenance_id: str

class ReadOnlyCapabilitySimulator:
    def __init__(self, capability: dict[str, Any]):
        self.capability = capability
        self.identity = capability["identity"]
        self.twin = capability["digital_twin"]
        self.provenance = capability["provenance"]
        self.permission = capability["permission_class"]

    def sample(self, value: float) -> TelemetryEnvelope:
        output = self.capability["outputs"][0]
        limits = self.capability["operating_limits"]
        if not isinstance(value, (int, float)):
            raise ValueError("invalid telemetry value")
        if value < limits["min_degC"] or value > limits["max_degC"]:
            raise ValueError("telemetry outside operating limits")
        return TelemetryEnvelope(
            capability_id=self.identity["capability_id"],
            twin_id=self.twin["twin_id"],
            value=float(value),
            unit=output["unit"],
            quality="GOOD",
            state_class="simulated",
            provenance_id=self.provenance["version"],
        )

    def actuate(self, *_: Any) -> None:
        if self.permission == "READ_ONLY":
            raise PermissionError("READ_ONLY capability cannot actuate")
        raise NotImplementedError("actuation is not implemented by this simulator")
