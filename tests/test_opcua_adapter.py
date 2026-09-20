import pytest
from opcua_adapter import OPCUAAdapter

def capability():
    return {"identity": {"capability_id": "test.opcua"}, "permission_class": "READ_ONLY"}

@pytest.mark.asyncio
async def test_disconnected_read_fails_closed():
    adapter = OPCUAAdapter(capability(), "opc.tcp://127.0.0.1:4840")
    with pytest.raises(RuntimeError):
        await adapter.read("temperature")

@pytest.mark.asyncio
async def test_read_only_cannot_actuate():
    adapter = OPCUAAdapter(capability(), "opc.tcp://127.0.0.1:4840")
    with pytest.raises(PermissionError):
        await adapter.write_command("start", True)
