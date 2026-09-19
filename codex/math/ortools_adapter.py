from __future__ import annotations
"""Optional OR-Tools bridge; Biupiu remains dependency-light when unavailable."""
from dataclasses import dataclass
from typing import Sequence

@dataclass(frozen=True)
class Assignment:
    worker: int
    task: int
    cost: float

def solve_assignment(costs: Sequence[Sequence[float]]) -> list[Assignment]:
    try:
        from ortools.linear_solver import pywraplp
    except ImportError as exc:
        raise RuntimeError("Reviewed OR-Tools dependency is not installed.") from exc
    if not costs or not costs[0]: return []
    workers, tasks = len(costs), len(costs[0])
    solver = pywraplp.Solver.CreateSolver("SCIP")
    if solver is None: raise RuntimeError("No reviewed OR-Tools backend available.")
    x={(w,t): solver.BoolVar(f"x_{w}_{t}") for w in range(workers) for t in range(tasks)}
    for w in range(workers): solver.Add(sum(x[w,t] for t in range(tasks)) <= 1)
    for t in range(tasks): solver.Add(sum(x[w,t] for w in range(workers)) == 1)
    solver.Minimize(sum(costs[w][t]*x[w,t] for w in range(workers) for t in range(tasks)))
    status=solver.Solve()
    if status != pywraplp.Solver.OPTIMAL: raise RuntimeError(f"Non-optimal assignment status: {status}")
    return [Assignment(w,t,float(costs[w][t])) for w in range(workers) for t in range(tasks) if x[w,t].solution_value() > .5]
