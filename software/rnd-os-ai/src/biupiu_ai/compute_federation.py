"""Biupiu heterogeneous compute federation.

Capability-first scheduling across CPU performance/efficiency/vector units,
GPU and NPU resources. Hardware topology is discovered at runtime; core
counts are never hard-coded. Safety-critical execution must remain behind a
separate deterministic/safety-certified boundary.
"""
from dataclasses import dataclass, field
from enum import Enum
from time import monotonic
from typing import Callable, Iterable, Mapping, Sequence


class ComputeClass(str, Enum):
    PERFORMANCE = "performance"
    EFFICIENCY = "efficiency"
    VECTOR = "vector"
    GPU = "gpu"
    NPU = "npu"


@dataclass(frozen=True)
class ComputeUnit:
    unit_id: str
    kind: ComputeClass
    capacity: float = 1.0
    available: bool = True


@dataclass(frozen=True)
class HostTopology:
    vendor: str
    architecture: str
    units: tuple[ComputeUnit, ...]
    memory_bytes: int = 0
    simd: tuple[str, ...] = ()


@dataclass(frozen=True)
class Workload:
    workload_id: str
    cost: float
    parallelizable: bool = True
    preferred: tuple[ComputeClass, ...] = ()
    minimum: tuple[ComputeClass, ...] = ()


@dataclass(frozen=True)
class DispatchRecord:
    workload_id: str
    unit_id: str
    started: float
    finished: float
    status: str

    @property
    def duration(self) -> float:
        return max(0.0, self.finished - self.started)


@dataclass
class FederationTelemetry:
    dispatched: list[DispatchRecord] = field(default_factory=list)

    @property
    def success_rate(self) -> float:
        if not self.dispatched:
            return 1.0
        return sum(r.status == "ok" for r in self.dispatched) / len(self.dispatched)


class ComputeFederation:
    """Plan and execute workloads against discovered heterogeneous resources."""

    def __init__(self, topology: HostTopology):
        self.topology = topology
        self.telemetry = FederationTelemetry()

    def eligible_units(self, workload: Workload) -> list[ComputeUnit]:
        units = [
            u for u in self.topology.units
            if u.available and u.capacity > 0
            and (not workload.minimum or u.kind in workload.minimum)
        ]
        if workload.preferred:
            preferred = [u for u in units if u.kind in workload.preferred]
            if preferred:
                return preferred + [u for u in units if u not in preferred]
        return units

    def plan(self, workloads: Iterable[Workload]) -> dict[str, str]:
        """Return a deterministic initial plan using capacity-aware balancing."""
        loads = {u.unit_id: 0.0 for u in self.topology.units if u.available and u.capacity > 0}
        plan: dict[str, str] = {}
        for work in sorted(workloads, key=lambda w: (-w.cost, w.workload_id)):
            candidates = self.eligible_units(work)
            if not candidates:
                raise RuntimeError(f"No eligible compute unit for workload {work.workload_id}")
            unit = min(
                candidates,
                key=lambda u: (loads[u.unit_id] / u.capacity, u.unit_id),
            )
            plan[work.workload_id] = unit.unit_id
            if work.parallelizable:
                loads[unit.unit_id] += work.cost
            else:
                loads[unit.unit_id] += work.cost * 1.25
        return plan

    def execute(
        self,
        workload: Workload,
        runner: Callable[[Workload, ComputeUnit], object],
    ) -> object:
        units = self.eligible_units(workload)
        if not units:
            raise RuntimeError(f"No eligible compute unit for workload {workload.workload_id}")
        unit = units[0]
        started = monotonic()
        try:
            result = runner(workload, unit)
        except Exception:
            self.telemetry.dispatched.append(
                DispatchRecord(workload.workload_id, unit.unit_id, started, monotonic(), "failed")
            )
            raise
        self.telemetry.dispatched.append(
            DispatchRecord(workload.workload_id, unit.unit_id, started, monotonic(), "ok")
        )
        return result


def topology_from_mapping(data: Mapping[str, object]) -> HostTopology:
    """Convert a native discovery payload into the canonical federation contract."""
    raw_units = data.get("units", ())
    units: list[ComputeUnit] = []
    for raw in raw_units if isinstance(raw_units, Sequence) else ():
        if not isinstance(raw, Mapping):
            continue
        units.append(
            ComputeUnit(
                unit_id=str(raw["unit_id"]),
                kind=ComputeClass(str(raw["kind"])),
                capacity=float(raw.get("capacity", 1.0)),
                available=bool(raw.get("available", True)),
            )
        )
    return HostTopology(
        vendor=str(data.get("vendor", "unknown")),
        architecture=str(data.get("architecture", "unknown")),
        units=tuple(units),
        memory_bytes=int(data.get("memory_bytes", 0)),
        simd=tuple(str(x) for x in data.get("simd", ())),
    )
