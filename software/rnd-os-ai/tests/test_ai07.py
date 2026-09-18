import pytest
from biupiu_ai.devices import DeviceRegistry, DeviceRegistration
from biupiu_ai.sensors import SensorIngestor, SensorReading
from biupiu_ai.lab_ingest import LabIngestService

def test_sensor_ingestion():
    registry = DeviceRegistry()
    registry.register(DeviceRegistration("pi-001", "raspberry-pi", "dev"))
    result = LabIngestService(registry, SensorIngestor()).ingest(SensorReading("pi-001","temperature-01","2026-09-18T00:00:00Z",23.5,"C"))
    assert result["value"] == 23.5 and result["unit"] == "C"

def test_unknown_device_rejected():
    registry = DeviceRegistry()
    with pytest.raises(PermissionError):
        LabIngestService(registry, SensorIngestor()).ingest(SensorReading("unknown","temperature-01","2026-09-18T00:00:00Z",23.5,"C"))
