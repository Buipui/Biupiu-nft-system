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


def eligible_for_quantum_promotion(
    evidence: PromotionEvidence, *, requires_hardware: bool = False
) -> bool:
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
    """Return the canonical quantum capability registry in stable order."""
    return tuple(
        sorted(
            {
                "quantum-kernel",
                "quantum-neural-network",
                "hybrid-differentiation",
                "benchmarking",
            }
        )
    )


@dataclass(frozen=True)
class QuantumLearningObservation:
    """A bounded observation usable by the quantum-learning service while idle."""
    observation_id: str
    signal: str
    value: float
    confidence: float
    backend: str = "classical"
    passive: bool = True

def record_quantum_learning_observation(
    observation: QuantumLearningObservation,
) -> dict:
    """Record learning evidence without activating QPU execution.

    Passive quantum learning means the service can update its knowledge of
    workloads, baselines, simulator behaviour and provider capability while
    quantum hardware remains disabled.
    """
    if not observation.passive:
        raise ValueError("this observation path is for passive learning only")
    if not all(0.0 <= float(x) <= 1.0 for x in (observation.value, observation.confidence)):
        raise ValueError("value and confidence must be between 0 and 1")
    return {
        "observation_id": observation.observation_id,
        "signal": observation.signal,
        "value": observation.value,
        "confidence": observation.confidence,
        "backend": observation.backend,
        "execution": "PASSIVE",
        "qpu_activation": "DISABLED",
        "next_action": "REVIEW" if observation.confidence < 0.8 else "BENCHMARK",
    }


def select_quantum_candidate(
    *,
    classical_score: float,
    quantum_simulator_score: float,
    uncertainty: float,
    resource_pressure: float,
) -> str:
    """Choose whether a candidate merits later quantum validation.

    This is a routing/learning decision, not a claim of quantum advantage.
    """
    vals = (classical_score, quantum_simulator_score, uncertainty, resource_pressure)
    if not all(0.0 <= float(x) <= 1.0 for x in vals):
        raise ValueError("candidate scores must be between 0 and 1")
    if resource_pressure > 0.9:
        return "DEFER"
    if quantum_simulator_score > classical_score and uncertainty < 0.5:
        return "SIMULATOR_VALIDATE"
    return "CLASSICAL_BASELINE"
