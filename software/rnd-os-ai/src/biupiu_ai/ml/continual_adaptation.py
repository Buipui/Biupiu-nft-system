"""Dependency-light continual/test-time adaptation primitives.

Inspired by the 2026 trend toward continual test-time adaptation, this module
implements a reference-anchored, fail-closed adaptation boundary. It is
first-party code and deliberately model-agnostic.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence, Tuple


@dataclass(frozen=True)
class AdaptationResult:
    values: Tuple[float, ...]
    adaptation_weight: float
    drift_score: float
    rollback_required: bool


def blend_predictions(
    base: Sequence[float],
    teacher: Sequence[float],
    *,
    teacher_confidence: float,
    drift_score: float = 0.0,
    max_teacher_weight: float = 0.35,
) -> AdaptationResult:
    """Blend a base prediction with an external teacher under bounded drift.

    Higher teacher confidence increases the update, while high drift decreases
    trust in the adaptation. The function never emits an update beyond the
    configured cap and flags rollback when the observed drift is extreme.
    """
    if len(base) != len(teacher) or not base:
        raise ValueError("base and teacher predictions must have equal non-zero length")
    if not 0.0 <= teacher_confidence <= 1.0:
        raise ValueError("teacher_confidence must be between 0 and 1")
    if drift_score < 0.0:
        raise ValueError("drift_score must be non-negative")
    if not 0.0 <= max_teacher_weight <= 1.0:
        raise ValueError("max_teacher_weight must be between 0 and 1")

    # Reduce adaptation as distribution shift becomes more severe.
    drift_factor = 1.0 / (1.0 + drift_score)
    weight = min(max_teacher_weight, teacher_confidence * drift_factor)

    result = tuple(
        (1.0 - weight) * float(b) + weight * float(t)
        for b, t in zip(base, teacher)
    )
    rollback = drift_score >= 3.0
    return AdaptationResult(result, weight, drift_score, rollback)


def reference_anchored_parameter_update(
    current: Mapping[str, float],
    reference: Mapping[str, float],
    gradient: Mapping[str, float],
    *,
    learning_rate: float = 0.01,
    anchor_strength: float = 0.1,
    max_step: float = 0.05,
) -> Mapping[str, float]:
    """Bound a streaming update around a known-good reference state."""
    if set(current) != set(reference) or set(current) != set(gradient):
        raise ValueError("current, reference and gradient keys must match")
    if learning_rate <= 0 or anchor_strength < 0 or max_step <= 0:
        raise ValueError("invalid adaptation parameters")

    updated = {}
    for key in current:
        raw = (
            float(current[key])
            - learning_rate * float(gradient[key])
            + anchor_strength * (float(reference[key]) - float(current[key]))
        )
        delta = raw - float(current[key])
        delta = max(-max_step, min(max_step, delta))
        updated[key] = float(current[key]) + delta
    return updated
