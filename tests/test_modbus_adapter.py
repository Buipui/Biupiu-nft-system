import pytest
from modbus_adapter import ModbusAdapter

def capability():
    return {"identity": {"capability_id": "test.modbus"}, "permission_class": "READ_ONLY"}

def test_disconnected_read_fails_closed():
    adapter = ModbusAdapter(capability(), "127.0.0.1")
    with pytest.raises(RuntimeError):
        adapter.read_holding_register("temperature")

def test_read_only_cannot_write():
    adapter = ModbusAdapter(capability(), "127.0.0.1")
    adapter.client = object()
    with pytest.raises(PermissionError):
        adapter.write_register("start", 1)

def test_missing_dependency_fails_closed(monkeypatch):
    import modbus_adapter
    monkeypatch.setattr(modbus_adapter, "ModbusTcpClient", None)
    adapter = ModbusAdapter(capability(), "127.0.0.1")
    with pytest.raises(RuntimeError):
        adapter.connect()
