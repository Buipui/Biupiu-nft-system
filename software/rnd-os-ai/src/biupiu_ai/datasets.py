from dataclasses import dataclass, field
from typing import List

@dataclass
class DataPoint:
    timestamp: str
    value: float
    unit: str
    quality: str = "unclassified"

@dataclass
class ExperimentDataset:
    dataset_id: str
    experiment_id: str
    sensor_id: str
    points: List[DataPoint] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)

    def add(self, point: DataPoint) -> None:
        self.points.append(point)

    def validate(self) -> list[str]:
        errors = []
        if not self.dataset_id: errors.append("dataset_id is required")
        if not self.experiment_id: errors.append("experiment_id is required")
        if not self.sensor_id: errors.append("sensor_id is required")
        if not self.points: errors.append("dataset requires at least one point")
        for p in self.points:
            if not p.timestamp: errors.append("timestamp is required")
            if not p.unit: errors.append("unit is required")
        return errors
