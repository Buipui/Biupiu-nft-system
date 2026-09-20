"""MQTT adapter for the Biupiu Machine Capability boundary."""
from __future__ import annotations
import json
from typing import Any

try:
    import paho.mqtt.client as mqtt
except ImportError:
    mqtt = None

class MQTTAdapter:
    protocol = "MQTT"

    def __init__(self, capability: dict[str, Any], broker: str, port: int = 1883,
                 topic_map: dict[str, str] | None = None):
        self.capability = capability
        self.broker = broker
        self.port = port
        self.topic_map = topic_map or {}
        self.client = None
        self.connected = False

    def connect(self) -> None:
        if mqtt is None:
            raise RuntimeError("paho-mqtt is required for MQTT execution")
        self.client = mqtt.Client()
        self.client.connect(self.broker, self.port)
        self.client.loop_start()
        self.connected = True

    def disconnect(self) -> None:
        if self.client is not None:
            self.client.loop_stop()
            self.client.disconnect()
        self.client = None
        self.connected = False

    def publish_command(self, name: str, value: Any) -> None:
        if self.capability["permission_class"] == "READ_ONLY":
            raise PermissionError("READ_ONLY capability cannot actuate")
        if not self.connected or self.client is None:
            raise RuntimeError("MQTT adapter is not connected")
        topic = self.topic_map[name]
        payload = json.dumps({"value": value})
        self.client.publish(topic, payload, qos=1)
