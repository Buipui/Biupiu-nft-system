"""Modbus adapter for the Biupiu Machine Capability boundary."""
from __future__ import annotations
from typing import Any

try:
    from pymodbus.client import ModbusTcpClient
except ImportError:
    ModbusTcpClient = None

class ModbusAdapter:
    protocol = "MODBUS"

    def __init__(self, capability: dict[str, Any], host: str, port: int = 502,
                 register_map: dict[str, int] | None = None, unit_id: int = 1):
        self.capability = capability
        self.host = host
        self.port = port
        self.register_map = register_map or {}
        self.unit_id = unit_id
        self.client = None

    def connect(self) -> None:
        if ModbusTcpClient is None:
            raise RuntimeError("pymodbus is required for Modbus execution")
        self.client = ModbusTcpClient(self.host, port=self.port)
        if not self.client.connect():
            self.client.close()
            self.client = None
            raise ConnectionError("Modbus connection failed")

    def disconnect(self) -> None:
        if self.client is not None:
            self.client.close()
        self.client = None

    def read_holding_register(self, signal_name: str, count: int = 1):
        if self.client is None:
            raise RuntimeError("Modbus adapter is not connected")
        address = self.register_map[signal_name]
        result = self.client.read_holding_registers(address=address, count=count, slave=self.unit_id)
        if result.isError():
            raise IOError(str(result))
        return result.registers

    def write_register(self, name: str, value: int) -> None:
        if self.capability["permission_class"] == "READ_ONLY":
            raise PermissionError("READ_ONLY capability cannot actuate")
        if self.client is None:
            raise RuntimeError("Modbus adapter is not connected")
        address = self.register_map[name]
        result = self.client.write_register(address=address, value=value, slave=self.unit_id)
        if result.isError():
            raise IOError(str(result))
