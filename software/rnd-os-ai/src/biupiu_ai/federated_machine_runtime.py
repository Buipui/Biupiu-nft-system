"""Integrated Biupiu compute + machine-capability runtime.

Capability validation -> compute eligibility -> workload dispatch -> telemetry.
Safety-critical hardware remains behind a separate certified boundary.
"""
from dataclasses import dataclass, field
from typing import Callable, Iterable
from .compute_federation import ComputeFederation, ComputeUnit, HostTopology, Workload
from .machine_capability import CapabilityRegistry, CapabilitySample, MachineCapability

@dataclass(frozen=True)
class MachineValidation:
    sample: CapabilitySample
    accepted: bool
    reason: str

@dataclass
class FederatedMachineRuntime:
    topology: HostTopology
    capabilities: CapabilityRegistry = field(default_factory=CapabilityRegistry)

    def __post_init__(self) -> None:
        self.compute = ComputeFederation(self.topology)

    def register_capability(self, capability: MachineCapability) -> None:
        self.capabilities.register(capability)

    def validate_capability(self, capability_id: str, value: float) -> MachineValidation:
        sample = self.capabilities.validate(capability_id, value)
        return MachineValidation(sample, sample.valid, sample.reason)

    def dispatch(self, workload: Workload, runner: Callable[[Workload, ComputeUnit], object]) -> object:
        return self.compute.execute(workload, runner)

    def plan(self, workloads: Iterable[Workload]) -> dict[str, str]:
        return self.compute.plan(workloads)
