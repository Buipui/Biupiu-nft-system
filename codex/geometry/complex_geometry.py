"""Deterministic mathematical geometry primitives for the Biupiu CODEX.

The module contains geometry only. It does not assert any physical interpretation
of source material that inspired the shapes.
"""
from __future__ import annotations

import math
from typing import Iterable, List, Tuple

Point3 = Tuple[float, float, float]


def torus(R: float, r: float, nu: int = 64, nv: int = 32) -> List[Point3]:
    """Return a deterministic point cloud for a torus."""
    if R <= 0 or r <= 0:
        raise ValueError("R and r must be positive")
    if nu < 3 or nv < 3:
        raise ValueError("nu and nv must be >= 3")
    return [
        ((R + r * math.cos(v)) * math.cos(u),
         (R + r * math.cos(v)) * math.sin(u),
         r * math.sin(v))
        for i in range(nu)
        for j in range(nv)
        for u, v in [(2 * math.pi * i / nu, 2 * math.pi * j / nv)]
    ]


def stacked_tori(count: int, R: float, r: float, spacing: float) -> List[Point3]:
    """Create a deterministic axial stack of torus point clouds."""
    if count < 1:
        raise ValueError("count must be >= 1")
    base = torus(R, r)
    return [(x, y, z + k * spacing) for k in range(count) for x, y, z in base]


def helix(radius: float, pitch: float, turns: float, samples: int = 512) -> List[Point3]:
    """Return a deterministic 3-D helix."""
    if radius <= 0 or turns <= 0 or samples < 2:
        raise ValueError("invalid helix parameters")
    return [
        (radius * math.cos(t), radius * math.sin(t), pitch * t / (2 * math.pi))
        for t in [2 * math.pi * turns * i / (samples - 1) for i in range(samples)]
    ]


def nested_spirals(scales: Iterable[float], turns: float, samples: int = 512) -> List[List[Point3]]:
    """Generate a family of deterministic scaled helices."""
    return [helix(float(scale), 1.0, turns, samples) for scale in scales]


def hourglass(z: Iterable[float], waist: float, flare: float) -> List[Point3]:
    """Return a radial hourglass profile sampled along supplied z values."""
    if waist <= 0 or flare < 0:
        raise ValueError("waist must be positive and flare non-negative")
    return [(waist + flare * abs(float(v)), 0.0, float(v)) for v in z]


def nested_wave(x: Iterable[float], amplitudes: Iterable[float], frequencies: Iterable[float]) -> List[float]:
    """Evaluate a deterministic sum of harmonic waves."""
    amps = list(amplitudes)
    freqs = list(frequencies)
    if len(amps) != len(freqs) or not amps:
        raise ValueError("amplitudes and frequencies must have equal non-zero length")
    return [sum(a * math.sin(f * float(v)) for a, f in zip(amps, freqs)) for v in x]


def vortex_ring(radius: float, tube_radius: float, samples: int = 256) -> List[Point3]:
    """Return the centreline of a vortex ring; physics is intentionally separate."""
    if radius <= 0 or tube_radius <= 0 or samples < 3:
        raise ValueError("invalid vortex-ring parameters")
    return [(radius * math.cos(t), radius * math.sin(t), 0.0)
            for t in [2 * math.pi * i / samples for i in range(samples)]]
