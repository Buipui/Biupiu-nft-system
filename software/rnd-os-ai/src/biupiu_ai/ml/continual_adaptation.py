"""Dependency-light continual/test-time adaptation primitives.

First-party, model-agnostic and fail-closed.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping, Sequence, Tuple
import math

@dataclass(frozen=True)
class AdaptationResult:
    values: Tuple[float, ...]
    adaptation_weight: float
    drift_score: float
    rollback_required: bool

def blend_predictions(base: Sequence[float], teacher: Sequence[float], *, teacher_confidence: float,
                      drift_score: float = 0.0, max_teacher_weight: float = 0.35) -> AdaptationResult:
    if len(base) != len(teacher) or not base:
        raise ValueError("base and teacher predictions must have equal non-zero length")
    if not 0.0 <= teacher_confidence <= 1.0:
        raise ValueError("teacher_confidence must be between 0 and 1")
    if drift_score < 0.0:
        raise ValueError("drift_score must be non-negative")
    if not 0.0 <= max_teacher_weight <= 1.0:
        raise ValueError("max_teacher_weight must be between 0 and 1")
    weight = min(max_teacher_weight, teacher_confidence / (1.0 + drift_score))
    result = tuple((1.0 - weight) * float(b) + weight * float(t) for b, t in zip(base, teacher))
    return AdaptationResult(result, weight, drift_score, drift_score >= 3.0)

def reference_anchored_parameter_update(current: Mapping[str, float], reference: Mapping[str, float],
    gradient: Mapping[str, float], *, learning_rate: float = 0.01, anchor_strength: float = 0.1,
    max_step: float = 0.05) -> Mapping[str, float]:
    if set(current) != set(reference) or set(current) != set(gradient):
        raise ValueError("current, reference and gradient keys must match")
    if learning_rate <= 0 or anchor_strength < 0 or max_step <= 0:
        raise ValueError("invalid adaptation parameters")

    updated = {}
    for key in current:
        current_value = float(current[key])
        raw = current_value - learning_rate * float(gradient[key]) + anchor_strength * (
            float(reference[key]) - current_value
        )
        delta = max(-max_step, min(max_step, raw - current_value))

        # Contractual bound: if the nominal endpoint would compare outside the
        # bound because of binary floating-point representation, move the
        # endpoint one ULP toward the current value.
        candidate = current_value + delta
        if abs(candidate - current_value) > max_step:
            target = current_value + math.copysign(max_step, delta)
            candidate = math.nextafter(target, current_value)
        updated[key] = candidate

    return updated
