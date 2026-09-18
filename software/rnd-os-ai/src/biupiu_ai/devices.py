from dataclasses import dataclass
from typing import Literal

DeviceType = Literal["raspberry-pi", "arduino", "esp32", "generic-iot"]

@dataclass
class DeviceRegistration:
    device_id: str
    device_type: DeviceType
    firmware_version: str
    experiment_id: str | None = None
    status: str = "registered"

class DeviceRegistry:
    def __init__(self):
        self.devices: dict[str, DeviceRegistration] = {}

    def register(self, device: DeviceRegistration) -> None:
        if device.device_id in self.devices: raise ValueError("device already registered")
        self.devices[device.device_id] = device

    def get(self, device_id: str) -> DeviceRegistration | None:
        return self.devices.get(device_id)
