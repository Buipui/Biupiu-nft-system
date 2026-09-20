import json
from pathlib import Path
import pytest
from protocol_adapter_boundary import InMemoryTransportAdapter

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "schemas/fixtures/machine-capability-v1.0.example.json"

def capability():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))

def test_transport_boundary_connect_read_disconnect():
    adapter = InMemoryTransportAdapter(capability())
    connected = adapter.connect()
    assert connected.connected and connected.simulated
    assert adapter.read_capability()["identity"]["capability_id"] == "example.sensor.temperature"
    disconnected = adapter.disconnect()
    assert not disconnected.connected and disconnected.simulated

def test_transport_boundary_fails_when_disconnected():
    adapter = InMemoryTransportAdapter(capability())
    with pytest.raises(RuntimeError):
        adapter.read_capability()

def test_transport_boundary_preserves_permission_boundary():
    adapter = InMemoryTransportAdapter(capability())
    adapter.connect()
    with pytest.raises(PermissionError):
        adapter.write_command("start", True)
