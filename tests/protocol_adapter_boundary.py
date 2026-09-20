"""Transport-neutral protocol adapter boundary for Biupiu capabilities."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Protocol

@dataclass(frozen=True)
class AdapterResult:
    protocol: str
    capability_id: str
    connected: bool
    simulated: bool
    message: str

class CapabilityTransportAdapter(Protocol):
    protocol: str
    def connect(self) -> AdapterResult: ...
    def disconnect(self) -> AdapterResult: ...
    def read_capability(self) -> dict[str, Any]: ...
    def write_command(self, name: str, value: Any) -> AdapterResult: ...

class InMemoryTransportAdapter:
    """Conformance-only transport; no physical I/O."""
    protocol = "SIMULATED"

    def __init__(self, capability: dict[str, Any]):
        self.capability = capability
        self.connected = False

    def connect(self) -> AdapterResult:
        self.connected = True
        return AdapterResult(self.protocol, self.capability["identity"]["capability_id"], True, True, "simulated connection")

    def disconnect(self) -> AdapterResult:
        self.connected = False
        return AdapterResult(self.protocol, self.capability["identity"]["capability_id"], False, True, "simulated disconnect")

    def read_capability(self) -> dict[str, Any]:
        if not self.connected:
            raise RuntimeError("adapter is not connected")
        return self.capability

    def write_command(self, name: str, value: Any) -> AdapterResult:
        if self.capability["permission_class"] == "READ_ONLY":
            raise PermissionError("READ_ONLY capability cannot accept commands")
        return AdapterResult(self.protocol, self.capability["identity"]["capability_id"], True, True, f"simulated command {name}")
