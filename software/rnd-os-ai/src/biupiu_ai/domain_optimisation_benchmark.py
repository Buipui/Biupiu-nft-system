"""Controlled geometry-vs-biology optimisation benchmark.

The benchmark intentionally uses the same deterministic search budget and records
objective evaluations, best score, convergence, and verification. It does not
claim to measure an AI model's intelligence or quantum advantage; it measures the
shared optimiser implementation on two domain encodings.
"""

from dataclasses import dataclass
from typing import Callable, Iterable

@dataclass(frozen=True)
class BenchmarkResult:
    domain: str
    evaluations: int
    best_score: float
    verified: bool

def grid_search(domain: str, candidates: Iterable[float], objective: Callable[[float], float],
                target: float, tolerance: float = 1e-9) -> BenchmarkResult:
    best = float("inf")
    evaluations = 0
    for candidate in candidates:
        score = abs(objective(candidate) - target)
        evaluations += 1
        best = min(best, score)
    return BenchmarkResult(domain, evaluations, best, best <= tolerance)
