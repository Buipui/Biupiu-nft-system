"""Biupiu Plant Intelligence Engine prototype.

Local-first catalogue and recommendation layer. Recommendations are advisory;
validated protocols remain explicitly versioned and condition-bound.
"""
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Dict, List

@dataclass
class PlantProfile:
    plant_id: str
    common_name: str
    scientific_name: str
    stages: List[str]
    metrics: List[str]
    compatible_products: List[str]
    evidence_level: str = "L0"
    version: str = "0.1"

class PlantIntelligence:
    def __init__(self):
        self.catalogue: Dict[str, PlantProfile] = {}
        self.cycles = []
        self.experiments = []

    def add_profile(self, profile: PlantProfile):
        self.catalogue[profile.plant_id] = profile

    def start_cycle(self, plant_id: str, zone_id: str, stage: str):
        if plant_id not in self.catalogue:
            raise KeyError("Plant profile not found")
        cycle = {"id": f"cycle-{len(self.cycles)+1:04d}",
                 "plant_id": plant_id, "zone_id": zone_id, "stage": stage,
                 "started_at": datetime.now(timezone.utc).isoformat()}
        self.cycles.append(cycle)
        return cycle

    def compatibility(self, plant_id: str):
        p = self.catalogue[plant_id]
        return {"plant_id": plant_id, "products": p.compatible_products,
                "metrics": p.metrics, "evidence_level": p.evidence_level}

    def create_experiment(self, plant_id: str, hypothesis: str, variables: List[str]):
        exp = {"id": f"exp-{len(self.experiments)+1:04d}", "plant_id": plant_id,
               "hypothesis": hypothesis, "variables": variables,
               "status": "planned", "created_at": datetime.now(timezone.utc).isoformat()}
        self.experiments.append(exp)
        return exp

    def export_catalogue(self):
        return [asdict(p) for p in self.catalogue.values()]

if __name__ == "__main__":
    engine = PlantIntelligence()
    engine.add_profile(PlantProfile(
        plant_id="example-crop-001", common_name="Example Crop",
        scientific_name="Example species", stages=["establishment", "development", "production", "maturity"],
        metrics=["soil_moisture", "soil_temperature", "air_temperature", "humidity", "light"],
        compatible_products=["SF-01", "SF-02"]))
    print(engine.compatibility("example-crop-001"))
