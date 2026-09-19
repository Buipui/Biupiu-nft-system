"""Dependency-free evaluation metrics for the Biupiu ML gate."""

from __future__ import annotations

from math import isclose
from typing import Iterable, Sequence


def _pairs(y_true: Iterable, y_pred: Iterable):
    pairs = list(zip(y_true, y_pred))
    if not pairs:
        raise ValueError("at least one prediction is required")
    return pairs


def accuracy(y_true: Iterable, y_pred: Iterable) -> float:
    pairs = _pairs(y_true, y_pred)
    return sum(a == b for a, b in pairs) / len(pairs)


def mse(y_true: Iterable[float], y_pred: Iterable[float]) -> float:
    pairs = _pairs(y_true, y_pred)
    return sum((float(a) - float(b)) ** 2 for a, b in pairs) / len(pairs)


def mae(y_true: Iterable[float], y_pred: Iterable[float]) -> float:
    pairs = _pairs(y_true, y_pred)
    return sum(abs(float(a) - float(b)) for a, b in pairs) / len(pairs)


def brier_score(y_true: Iterable[int], y_prob: Iterable[float]) -> float:
    pairs = _pairs(y_true, y_prob)
    return sum((float(p) - int(y)) ** 2 for y, p in pairs) / len(pairs)


def precision_at_k(relevant: Iterable, ranked: Sequence, k: int) -> float:
    if k <= 0:
        raise ValueError("k must be positive")
    rel = set(relevant)
    top = list(ranked)[:k]
    if not top:
        return 0.0
    return sum(item in rel for item in top) / len(top)


def recall_at_k(relevant: Iterable, ranked: Sequence, k: int) -> float:
    if k <= 0:
        raise ValueError("k must be positive")
    rel = set(relevant)
    if not rel:
        return 0.0
    top = list(ranked)[:k]
    return sum(item in rel for item in top) / len(rel)


def population_stability_index(reference: Sequence[float],
                                current: Sequence[float],
                                buckets: int = 10) -> float:
    """Simple PSI for drift screening.

    This is a screening statistic, not a scientific verdict. Binning uses
    reference quantiles so that zero-variance or sparse data fail safely.
    """
    if not reference or not current:
        raise ValueError("reference and current samples are required")
    if buckets < 2:
        raise ValueError("buckets must be >= 2")

    ref = sorted(float(x) for x in reference)
    cur = [float(x) for x in current]
    if isclose(ref[0], ref[-1]):
        return 0.0

    edges = []
    for i in range(1, buckets):
        pos = min(len(ref) - 1, int(i * len(ref) / buckets))
        edges.append(ref[pos])

    def counts(values):
        out = [0] * buckets
        for value in values:
            idx = 0
            while idx < len(edges) and value > edges[idx]:
                idx += 1
            out[idx] += 1
        return out

    rc, cc = counts(ref), counts(cur)
    rtot, ctot = len(ref), len(cur)
    score = 0.0
    for r, c in zip(rc, cc):
        rp = max(r / rtot, 1e-12)
        cp = max(c / ctot, 1e-12)
        score += (cp - rp) * __import__("math").log(cp / rp)
    return score
