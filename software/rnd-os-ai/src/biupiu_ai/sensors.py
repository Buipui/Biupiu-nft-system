from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class SensorReading:
    device_id: str
    sensor_id: str
    timestamp: str
    value: float
    unit: str
    quality: str = "unclassified"
    metadata: Dict[str, Any] | None = None

class SensorIngestor:
    def validate(self, reading: SensorReading) -> list[str]:
        errors = []
        if not reading.device_id: errors.append("device_id is required")
        if not reading.sensor_id: errors.append("sensor_id is required")
        if not reading.timestamp: errors.append("timestamp is required")
        if not reading.unit: errors.append("unit is required")
        if not isinstance(reading.value, (int, float)): errors.append("value must be numeric")
        return errors

    def normalize(self, reading: SensorReading) -> dict:
        errors = self.validate(reading)
        if errors: raise ValueError("; ".join(errors))
        return {"device_id": reading.device_id, "sensor_id": reading.sensor_id, "timestamp": reading.timestamp, "value": float(reading.value), "unit": reading.unit, "quality": reading.quality, "metadata": reading.metadata or {}}
