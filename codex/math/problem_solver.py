from __future__ import annotations

"""Reference mathematical problem-solving orchestrator.

This module intentionally contains adapters, not an autonomous theorem generator.
External solvers are injected so the repository can remain dependency-light.
"""

from dataclasses import dataclass, field
from typing import Any, Callable, Mapping, Sequence


@dataclass
class Problem:
    statement: str
    domain: Sequence[str] = field(default_factory=tuple)
    variables: Mapping[str, Any] = field(default_factory=dict)
    constraints: Sequence[str] = field(default_factory=tuple)
    objective: str | None = None
    units: Mapping[str, str] = field(default_factory=dict)


@dataclass
class Candidate:
    name: str
    result: Any
    residual: float | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class SolveRecord:
    problem: Problem
    candidates: list[Candidate]
    verification: dict[str, Any]
    status: str


class MathSolver:
    """Coordinates independent solvers and verification without hiding uncertainty."""

    def __init__(
        self,
        solvers: Sequence[Callable[[Problem], Candidate]] = (),
        verifier: Callable[[Problem, list[Candidate]], Mapping[str, Any]] | None = None,
    ):
        self.solvers = list(solvers)
        self.verifier = verifier

    def solve(self, problem: Problem) -> SolveRecord:
        candidates: list[Candidate] = []
        failures: list[dict[str, str]] = []

        for solver in self.solvers:
            try:
                candidates.append(solver(problem))
            except Exception as exc:
                failures.append({
                    "solver": getattr(solver, "__name__", repr(solver)),
                    "error_type": type(exc).__name__,
                    "message": str(exc),
                })

        verification = dict(self.verifier(problem, candidates)) if self.verifier else {}
        verification["solver_failures"] = failures

        status = "verified_candidate" if verification.get("verified") else (
            "candidate" if candidates else "unsolved"
        )
        return SolveRecord(problem, candidates, verification, status)
