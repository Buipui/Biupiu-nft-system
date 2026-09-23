from __future__ import annotations

"""Biupiu computational biology primitives.

Architecture deliberately mirrors codex/geometry/biupiu_geometry.py:
typed immutable primitives, deterministic numerical operations, explicit tolerances,
and small functions suitable for independent verification.
This is a computational-biology analogue, not a claim that biological systems are
geometrically identical.
"""

from dataclasses import dataclass
from math import inf
from typing import Iterable

EPS = 1e-12

@dataclass(frozen=True)
class BioPoint:
    sequence_id: str
    position: int

def distance(a: BioPoint, b: BioPoint) -> float:
    if a.sequence_id != b.sequence_id:
        return inf
    return float(abs(a.position - b.position))

def orientation(a: BioPoint, b: BioPoint, c: BioPoint) -> int:
    if a.sequence_id != b.sequence_id or b.sequence_id != c.sequence_id:
        raise ValueError("orientation requires one biological sequence/coordinate frame")
    det = (b.position - a.position) * (c.position - a.position)
    if det > EPS: return 1
    if det < -EPS: return -1
    return 0

def collinear(a: BioPoint, b: BioPoint, c: BioPoint) -> bool:
    return a.sequence_id == b.sequence_id == c.sequence_id

@dataclass(frozen=True)
class BioSegment:
    a: BioPoint
    b: BioPoint

def sequence_span(points: Iterable[BioPoint]) -> float:
    pts = list(points)
    if len(pts) < 2:
        return 0.0
    if len({p.sequence_id for p in pts}) != 1:
        raise ValueError("sequence_span requires one biological sequence")
    return float(max(p.position for p in pts) - min(p.position for p in pts))

def normalize_sequence(sequence: str) -> str:
    seq = sequence.strip().upper()
    if not seq:
        raise ValueError("sequence must not be empty")
    if any(base not in "ACGTUN" for base in seq):
        raise ValueError("unsupported nucleotide")
    return seq

def hamming_distance(a: str, b: str) -> int:
    a, b = normalize_sequence(a), normalize_sequence(b)
    if len(a) != len(b):
        raise ValueError("Hamming distance requires equal-length sequences")
    return sum(x != y for x, y in zip(a, b))

def gc_fraction(sequence: str) -> float:
    seq = normalize_sequence(sequence)
    return sum(base in "GC" for base in seq) / len(seq)
