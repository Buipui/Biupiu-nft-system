"""OPC UA adapter for the Biupiu Machine Capability boundary."""
from __future__ import annotations
from typing import Any
try:
    from asyncua import Client
except ImportError:
    Client = None

class OPCUAAdapter:
    protocol = "OPC_UA"
    def __init__(self, capability: dict[str, Any], endpoint: str, node_map: dict[str, str] | None = None):
        self.capability = capability
        self.endpoint = endpoint
        self.node_map = node_map or {}
        self._client = None
        self.connected = False

    async def connect(self) -> None:
        if Client is None:
            raise RuntimeError("asyncua is required for OPC UA execution")
        self._client = Client(url=self.endpoint)
        await self._client.connect()
        self.connected = True

    async def disconnect(self) -> None:
        if self._client is not None:
            await self._client.disconnect()
        self._client = None
        self.connected = False

    async def read(self, signal_name: str) -> Any:
        if not self.connected or self._client is None:
            raise RuntimeError("OPC UA adapter is not connected")
        return await self._client.get_node(self.node_map[signal_name]).read_value()

    async def write_command(self, name: str, value: Any) -> None:
        if self.capability["permission_class"] == "READ_ONLY":
            raise PermissionError("READ_ONLY capability cannot actuate")
        if not self.connected or self._client is None:
            raise RuntimeError("OPC UA adapter is not connected")
        await self._client.get_node(self.node_map[name]).write_value(value)
