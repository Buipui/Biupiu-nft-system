import pytest
from mqtt_adapter import MQTTAdapter

def capability():
    return {"identity": {"capability_id": "test.mqtt"}, "permission_class": "READ_ONLY"}

def test_disconnected_command_fails_closed():
    adapter = MQTTAdapter(capability(), "127.0.0.1")
    with pytest.raises(RuntimeError):
        adapter.publish_command("start", True)

def test_read_only_cannot_publish_actuation():
    adapter = MQTTAdapter(capability(), "127.0.0.1")
    adapter.connected = True
    class Fake: pass
    adapter.client = Fake()
    with pytest.raises(PermissionError):
        adapter.publish_command("start", True)
