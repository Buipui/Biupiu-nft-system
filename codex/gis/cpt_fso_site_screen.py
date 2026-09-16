"""Deterministic screening tools for Cape Town FSO candidate sites.

This module intentionally avoids making deployment decisions. It computes transparent
screening metrics from user-supplied, authoritative GIS / weather / infrastructure data.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from math import hypot
from typing import Iterable, Optional


@dataclass(frozen=True)
class SiteObservation:
    site_id: str
    latitude_deg: float
    longitude_deg: float
    structure_height_m: float
    fibre_available: bool
    power_available: bool
    permission_status: str
    maintenance_access: bool
    environmental_constraint: bool = False
    aviation_constraint: bool = False

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class LinkObservation:
    source_id: str
    target_id: str
    distance_m: float
    clear_line_of_sight: bool
    visibility_km: Optional[float] = None
    wind_mps: Optional[float] = None

    def to_dict(self) -> dict:
        return asdict(self)


def normalised(value: float, low: float, high: float) -> float:
    """Clamp and linearly normalise a value into [0, 1]."""
    if high <= low:
        raise ValueError("high must be greater than low")
    return max(0.0, min(1.0, (value - low) / (high - low)))


def straight_line_distance_m(a: SiteObservation, b: SiteObservation) -> float:
    """Approximate local planar distance from latitude/longitude.

    Intended only for preliminary screening; authoritative geodesic/GIS calculations
    should replace this in production studies.
    """
    lat_m = 111_320.0
    lon_m = 111_320.0
    dx = (b.longitude_deg - a.longitude_deg) * lon_m
    dy = (b.latitude_deg - a.latitude_deg) * lat_m
    return hypot(dx, dy)


def site_screen_score(site: SiteObservation) -> float:
    """Return a transparent 0-100 screening score.

    Permission and safety-related constraints are gates, not compensated by the score.
    Unknown/conditional permissions therefore remain non-deployable.
    """
    if site.permission_status.lower() not in {"clear", "approved", "research"}:
        return 0.0
    if site.aviation_constraint or site.environmental_constraint:
        return 0.0

    score = 0.0
    score += 20.0 if site.fibre_available else 0.0
    score += 15.0 if site.power_available else 0.0
    score += 15.0 if site.maintenance_access else 0.0
    score += 20.0 * normalised(site.structure_height_m, 5.0, 60.0)
    # Remaining points intentionally reserved for populated authoritative datasets.
    return round(score, 3)


def candidate_links(sites: Iterable[SiteObservation], max_distance_m: float) -> list[LinkObservation]:
    """Generate bidirectional candidate pairs within a screening distance."""
    site_list = list(sites)
    links: list[LinkObservation] = []
    for i, source in enumerate(site_list):
        for target in site_list[i + 1 :]:
            distance = straight_line_distance_m(source, target)
            if distance <= max_distance_m:
                links.append(
                    LinkObservation(
                        source_id=source.site_id,
                        target_id=target.site_id,
                        distance_m=round(distance, 3),
                        clear_line_of_sight=False,
                    )
                )
    return links
