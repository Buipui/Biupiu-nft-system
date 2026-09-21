"""Biupiu Architecture Simulator: manifest-driven research prototype.

Keeps simulation state separate from rendering and enforces a rights-aware asset gate.
This is an architecture-layer prototype, not a UE runtime implementation.
"""
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

ALLOWED_FOR_BUILD = {"GREEN"}
REVIEW = {"BLUE", "YELLOW", "ORANGE", "GREY"}
BLOCKED = {"RED"}

@dataclass
class Asset:
    asset_id: str
    source: str
    license: str
    rights_class: str
    formats: List[str] = field(default_factory=list)
    country_tags: List[str] = field(default_factory=list)
    modules: List[str] = field(default_factory=list)

@dataclass
class SiteState:
    crs: str
    latitude: float
    longitude: float
    elevation_m: float = 0.0
    terrain_source: str = ""
    parcel_ids: List[str] = field(default_factory=list)
    buildings: List[Dict] = field(default_factory=list)

class ArchitectureSimulator:
    def __init__(self):
        self.assets: Dict[str, Asset] = {}
        self.site: SiteState | None = None

    def register_asset(self, asset: Asset) -> None:
        self.assets[asset.asset_id] = asset

    def import_site(self, site: SiteState) -> None:
        if not site.crs:
            raise ValueError("CRS is required for GIS-safe simulation")
        self.site = site

    def eligible_assets(self, country: str | None = None) -> List[Asset]:
        items = [a for a in self.assets.values() if a.rights_class in ALLOWED_FOR_BUILD]
        if country:
            items = [a for a in items if not a.country_tags or country in a.country_tags]
        return items

    def propose_massing(self, footprint_m2: float, levels: int, bay_m: float = 6.0) -> Dict:
        if footprint_m2 <= 0 or levels < 1 or bay_m <= 0:
            raise ValueError("Invalid architectural parameters")
        width = footprint_m2 ** 0.5
        bays = max(1, round(width / bay_m))
        return {
            "footprint_m2": footprint_m2,
            "levels": levels,
            "structural_bays": bays,
            "estimated_gfa_m2": footprint_m2 * levels,
        }

    def validate(self) -> Tuple[bool, List[str]]:
        errors: List[str] = []
        if self.site is None:
            errors.append("No GIS site imported")
        for a in self.assets.values():
            if a.rights_class in BLOCKED:
                errors.append(f"Blocked asset registered: {a.asset_id}")
        return (not errors, errors)
