"""Capability-oriented machine I/O boundary for Biupiu OS.

Applications address machine capabilities rather than vendor-specific device
names. Hardware-specific translation remains isolated in adapters.
"""
from dataclasses import dataclass
from enum import Enum
from time import monotonic
from typing import Mapping


class Transport(str, Enum):
    CAN = "can"
    CAN_FD = "can-fd"
    LIN = "lin"
    ETHERNET = "ethernet"
    SPI = "spi"
    I2C = "i2c"
    GPIO = "gpio"
    ADC = "adc"
    VIRTUAL = "virtual"


@dataclass(frozen=True)
class MachineCapability:
    capability_id: str
    category: str
    unit: str
    transport: Transport
    minimum: float | None = None
    maximum: float | None = None
    update_hz: float = 0.0
    readable: bool = True
    writable: bool = False
    safety_class: str = "non-safety"
    redundancy_group: str | None = None
    adapter_id: str = "unbound"


@dataclass(frozen=True)
class CapabilitySample:
    capability_id: str
    value: float
    timestamp: float
    valid: bool
    reason: str = ""


class CapabilityRegistry:
    def __init__(self) -> None:
        self._capabilities: dict[str, MachineCapability] = {}

    def register(self, capability: MachineCapability) -> None:
        if capability.capability_id in self._capabilities:
            raise ValueError(f"Capability already registered: {capability.capability_id}")
        if capability.minimum is not None and capability.maximum is not None:
            if capability.minimum > capability.maximum:
                raise ValueError("Capability minimum cannot exceed maximum")
        self._capabilities[capability.capability_id] = capability

    def get(self, capability_id: str) -> MachineCapability:
        return self._capabilities[capability_id]

    def validate(self, capability_id: str, value: float, timestamp: float | None = None) -> CapabilitySample:
        capability = self.get(capability_id)
        now = monotonic() if timestamp is None else timestamp
        if not capability.readable:
            return CapabilitySample(capability_id, value, now, False, "capability-not-readable")
        if capability.minimum is not None and value < capability.minimum:
            return CapabilitySample(capability_id, value, now, False, "below-range")
        if capability.maximum is not None and value > capability.maximum:
            return CapabilitySample(capability_id, value, now, False, "above-range")
        return CapabilitySample(capability_id, value, now, True, "accepted")


def capability_manifest(registry: CapabilityRegistry) -> Mapping[str, MachineCapability]:
    return dict(registry._capabilities)
