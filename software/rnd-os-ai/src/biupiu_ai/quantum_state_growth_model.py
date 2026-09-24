"""Dependency-free quantum-state-inspired growth model."""
from __future__ import annotations
from dataclasses import dataclass
from math import sqrt
from typing import Tuple

@dataclass(frozen=True)
class QuantumGrowthState:
    step: int
    system_size: int
    amplitudes: Tuple[float, ...]
    growth_ratio: float
    model: str = "NORMALIZED_STATE_VECTOR_GROWTH_V1"

def _normalise(values):
    norm = sqrt(sum(float(v) * float(v) for v in values))
    if norm == 0.0:
        return tuple(0.0 for _ in values)
    return tuple(round(float(v) / norm, 10) for v in values)

def evolve_state(previous: QuantumGrowthState | None, *, system_size: int, signal: float = 1.0) -> QuantumGrowthState:
    if system_size < 1:
        raise ValueError("system_size must be >= 1")
    if signal < 0:
        raise ValueError("signal must be non-negative")
    if previous is None:
        return QuantumGrowthState(0, system_size, _normalise([1.0] * system_size), 1.0)
    raw = list(previous.amplitudes)
    if system_size > len(raw):
        raw.extend([0.0] * (system_size - len(raw)))
    elif system_size < len(raw):
        raw = raw[:system_size]
    growth_ratio = system_size / max(1, previous.system_size)
    raw = [a * (1.0 / sqrt(max(growth_ratio, 1e-12))) for a in raw]
    raw[-1] += float(signal) * min(1.0, growth_ratio)
    return QuantumGrowthState(previous.step + 1, system_size, _normalise(raw), growth_ratio)

def state_evidence(state: QuantumGrowthState) -> dict:
    return {
        "model": state.model,
        "step": state.step,
        "system_size": state.system_size,
        "growth_ratio": round(state.growth_ratio, 10),
        "amplitude_norm": round(sum(a*a for a in state.amplitudes), 10),
        "amplitudes": list(state.amplitudes),
        "interpretation": "quantum-state-inspired mathematical learning representation; not quantum hardware evidence",
    }
