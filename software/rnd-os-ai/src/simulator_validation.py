"""Deterministic validation of the simulator adapter layer.

This module performs local, non-executing checks only. It does not install,
launch, or load third-party simulation backends.
"""
from dataclasses import asdict, dataclass
from typing import Any

from simulator_adapters import backend_matrix


@dataclass(frozen=True)
class ValidationRecord:
    backend: str
    available: bool
    status: str
    executable: str | None


def validate_backends() -> dict[str, Any]:
    records = [
        ValidationRecord(
            backend=result.backend,
            available=result.available,
            status=result.status,
            executable=result.executable,
        )
        for result in backend_matrix().values()
    ]
    return {
        "gate": "SIM-OSS-03",
        "mode": "non-executing-local-probe",
        "records": [asdict(record) for record in records],
        "production_approved": False,
        "reason": "Environment-specific smoke, dependency, security and Digital Twin tests remain required.",
    }
