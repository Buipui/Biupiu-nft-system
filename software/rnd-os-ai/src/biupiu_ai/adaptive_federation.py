"""Adaptive, fail-closed resource federation for Digital Twins and AI modules.

The controller is deliberately hardware-neutral. It selects an execution path
from capability, resource pressure and policy evidence; it never claims that a
physical accelerator was validated merely because a provider is registered.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Mapping, Sequence


class ModuleState(str, Enum):
    PASSIVE = "PASSIVE"
    READY = "READY"
    ACTIVE = "ACTIVE"
    DEGRADED = "DEGRADED"
    FAILED = "FAILED"


class ExecutionPath(str, Enum):
    CPU = "CPU"
    VECTOR = "VECTOR"
    GPU = "GPU"
    NPU = "NPU"
    SPECIAL = "SPECIAL"
    FALLBACK = "FALLBACK"


@dataclass(frozen=True)
class ModuleContract:
    module_id: str
    capabilities: tuple[str, ...] = ()
    preferred_paths: tuple[ExecutionPath, ...] = (ExecutionPath.CPU,)
    fallback_path: ExecutionPath = ExecutionPath.CPU
    passive_allowed: bool = True
    authoritative: bool = False


@dataclass(frozen=True)
class ResourceSnapshot:
    cpu: float = 1.0
    vector: float = 0.0
    gpu: float = 0.0
    npu: float = 0.0
    special: float = 0.0
    thermal_pressure: float = 0.0
    power_pressure: float = 0.0

    def __post_init__(self) -> None:
        values = (self.cpu, self.vector, self.gpu, self.npu, self.special,
                  self.thermal_pressure, self.power_pressure)
        if any(not 0.0 <= float(v) <= 1.0 for v in values):
            raise ValueError("resource values must be between 0 and 1")


@dataclass(frozen=True)
class CapabilityEvidence:
    capabilities: frozenset[str] = frozenset()
    validated_paths: frozenset[ExecutionPath] = frozenset()
    provenance_verified: bool = False
    regression_passed: bool = False
    safety_passed: bool = False


@dataclass(frozen=True)
class DispatchDecision:
    module_id: str
    state: ModuleState
    path: ExecutionPath
    reason: str


@dataclass(frozen=True)
class TelemetryEvent:
    module_id: str
    state: ModuleState
    path: ExecutionPath
    latency_ms: float
    resource_pressure: float
    success: bool
    correlation_id: str


_PATH_PRESSURE = {
    ExecutionPath.CPU: "cpu",
    ExecutionPath.VECTOR: "vector",
    ExecutionPath.GPU: "gpu",
    ExecutionPath.NPU: "npu",
    ExecutionPath.SPECIAL: "special",
}


def _pressure(snapshot: ResourceSnapshot, path: ExecutionPath) -> float:
    return float(getattr(snapshot, _PATH_PRESSURE[path]))


def select_path(
    contract: ModuleContract,
    snapshot: ResourceSnapshot,
    evidence: CapabilityEvidence,
    *,
    workload_required: bool = True,
) -> DispatchDecision:
    """Select the least-cost eligible path while preserving fail-closed policy."""
    if not workload_required and contract.passive_allowed:
        return DispatchDecision(contract.module_id, ModuleState.PASSIVE,
                                contract.fallback_path, "workload-not-required")

    if not evidence.safety_passed or not evidence.provenance_verified:
        return DispatchDecision(contract.module_id, ModuleState.DEGRADED,
                                contract.fallback_path, "evidence-gate-not-passed")

    missing = set(contract.capabilities) - set(evidence.capabilities)
    if missing:
        return DispatchDecision(contract.module_id, ModuleState.DEGRADED,
                                contract.fallback_path, "capability-missing")

    candidates = [p for p in contract.preferred_paths if p in evidence.validated_paths]
    if not candidates:
        if contract.fallback_path in evidence.validated_paths:
            return DispatchDecision(contract.module_id, ModuleState.DEGRADED,
                                    contract.fallback_path, "fallback-path")
        return DispatchDecision(contract.module_id, ModuleState.FAILED,
                                contract.fallback_path, "no-validated-execution-path")

    path = min(candidates, key=lambda p: (_pressure(snapshot, p), p.value))
    pressure = _pressure(snapshot, path)
    if pressure >= 0.95:
        if contract.fallback_path in evidence.validated_paths and contract.fallback_path != path:
            return DispatchDecision(contract.module_id, ModuleState.DEGRADED,
                                    contract.fallback_path, "resource-pressure-fallback")
        return DispatchDecision(contract.module_id, ModuleState.DEGRADED,
                                path, "resource-pressure")

    return DispatchDecision(contract.module_id, ModuleState.ACTIVE, path,
                            "validated-path-selected")


def record_telemetry(
    decision: DispatchDecision,
    *,
    latency_ms: float,
    resource_pressure: float,
    success: bool,
    correlation_id: str,
) -> TelemetryEvent:
    """Create a bounded telemetry event for the learning/observability layer."""
    if latency_ms < 0:
        raise ValueError("latency_ms must be non-negative")
    if not 0.0 <= resource_pressure <= 1.0:
        raise ValueError("resource_pressure must be between 0 and 1")
    if not correlation_id.strip():
        raise ValueError("correlation_id is required")
    return TelemetryEvent(
        decision.module_id, decision.state, decision.path, float(latency_ms),
        float(resource_pressure), bool(success), correlation_id.strip()
    )


def compatibility_manifest(
    modules: Sequence[ModuleContract],
    evidence_by_module: Mapping[str, CapabilityEvidence],
) -> tuple[DispatchDecision, ...]:
    """Build a deterministic passive-first manifest without activating modules."""
    return tuple(
        select_path(module, ResourceSnapshot(), evidence_by_module.get(module.module_id, CapabilityEvidence()),
                    workload_required=False)
        for module in sorted(modules, key=lambda x: x.module_id)
    )
