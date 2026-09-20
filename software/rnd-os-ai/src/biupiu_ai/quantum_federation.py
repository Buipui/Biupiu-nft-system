"""Quantum-ready federation contracts with fail-closed promotion.

This module defines framework-neutral contracts. It does not activate external
quantum hardware or claim quantum advantage; all providers remain sandboxed
until independent verification and human promotion are complete.
"""
from dataclasses import dataclass, field
from typing import Mapping, Tuple


@dataclass(frozen=True)
class QuantumCapability:
    capability_id: str
    provider: str
    execution_mode: str  # simulator, hardware, classical-emulation
    requires_hardware: bool = False
    status: str = "CANDIDATE"


@dataclass(frozen=True)
class QuantumExperiment:
    experiment_id: str
    feature_map: str
    classical_baseline: str
    backend: str
    shots: int = 0
    circuit_depth: int = 0
    metrics: Mapping[str, float] = field(default_factory=dict)


@dataclass(frozen=True)
class PromotionEvidence:
    provenance: bool = False
    license_reviewed: bool = False
    security_reviewed: bool = False
    regression_passed: bool = False
    reproducible: bool = False
    human_approved: bool = False


def eligible_for_quantum_promotion(evidence: PromotionEvidence, *, requires_hardware: bool = False) -> bool:
    """Return True only when every mandatory evidence gate is satisfied."""
    required = (
        evidence.provenance,
        evidence.license_reviewed,
        evidence.security_reviewed,
        evidence.regression_passed,
        evidence.reproducible,
        evidence.human_approved,
    )
    if requires_hardware and not evidence.security_reviewed:
        return False
    return all(required)


def quantum_capability_names() -> Tuple[str, ...]:
    return ("quantum-kernel", "quantum-neural-network", "hybrid-differentiation", "benchmarking")
