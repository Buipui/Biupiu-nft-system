"""Biupiu World civilisation farming simulator v1.
Simulation only: no real-world financial or agricultural control.
Historical mechanics are parameterized and must be paired with evidence metadata.
"""
from dataclasses import dataclass, field
from typing import Dict, List
import random

@dataclass
class FarmState:
    site_id: str
    season: int = 1
    water: float = 100.0
    soil: float = 70.0
    labour: float = 50.0
    stored: Dict[str, float] = field(default_factory=dict)
    yield_units: float = 0.0
    barter_value: float = 0.0

SITE_RULES = {
    "inca_mountain": {
        "terrain": "steep_andean",
        "water_efficiency": 1.25,
        "erosion_risk": 0.25,
        "microclimate_bonus": 1.15,
        "crops": ["potato", "quinoa", "maize"],
    },
    "maya_lowland": {
        "terrain": "tropical_lowland",
        "water_efficiency": 1.0,
        "erosion_risk": 0.35,
        "milpa_rotation_bonus": 1.20,
        "crops": ["maize", "beans", "squash"],
    },
    "babylon_alluvial": {
        "terrain": "alluvial_plain",
        "water_efficiency": 1.35,
        "salinity_risk": 0.20,
        "crops": ["barley", "date", "sesame"],
    },
    "babylon_hanging_gardens_reconstruction": {
        "terrain": "elevated_terraces",
        "water_efficiency": 0.80,
        "maintenance_cost": 1.35,
        "reconstruction": True,
        "crops": ["date", "fig", "vine", "vegetable"],
    },
}

def simulate_cycle(farm: FarmState, climate_factor: float = 1.0, seed: int = 7) -> FarmState:
    """Run one abstract harvest cycle using transparent game/simulation mechanics."""
    rules = SITE_RULES[farm.site_id]
    rng = random.Random(seed + farm.season)
    base = 10.0 * climate_factor * rules.get("water_efficiency", 1.0)
    if farm.site_id == "inca_mountain":
        base *= rules["microclimate_bonus"]
    if farm.site_id == "maya_lowland":
        base *= rules["milpa_rotation_bonus"]
    if farm.site_id == "babylon_alluvial" and rng.random() < rules["salinity_risk"]:
        base *= 0.75
    if rules.get("reconstruction"):
        base /= rules["maintenance_cost"]
    water_use = min(farm.water, 20.0)
    labour_use = min(farm.labour, 10.0)
    yield_units = max(0.0, base * (water_use / 20.0) * (labour_use / 10.0))
    farm.water -= water_use
    farm.labour -= labour_use
    farm.soil = max(0.0, farm.soil - rules.get("erosion_risk", 0.1) * 5)
    farm.yield_units = round(yield_units, 3)
    crop = rules["crops"][farm.season % len(rules["crops"])]
    farm.stored[crop] = round(farm.stored.get(crop, 0) + yield_units, 3)
    farm.barter_value = round(yield_units * (1.0 + max(0.0, 70-farm.soil)/100), 3)
    farm.season += 1
    return farm

def compare_sites(climate_factor: float = 1.0) -> List[dict]:
    rows=[]
    for site_id in SITE_RULES:
        farm=FarmState(site_id=site_id)
        simulate_cycle(farm, climate_factor)
        rows.append({"site_id":site_id, "yield_units":farm.yield_units,
                     "soil_after":round(farm.soil,3), "barter_value":farm.barter_value})
    return rows

if __name__ == "__main__":
    for row in compare_sites():
        print(row)
