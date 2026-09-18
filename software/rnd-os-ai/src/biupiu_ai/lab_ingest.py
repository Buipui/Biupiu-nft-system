from .devices import DeviceRegistry
from .sensors import SensorIngestor, SensorReading

class LabIngestService:
    def __init__(self, registry: DeviceRegistry, ingestor: SensorIngestor):
        self.registry, self.ingestor = registry, ingestor

    def ingest(self, reading: SensorReading) -> dict:
        if self.registry.get(reading.device_id) is None: raise PermissionError("device is not registered")
        return self.ingestor.normalize(reading)
