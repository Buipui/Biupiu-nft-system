"""Deterministic LiDAR/street-planning primitives.

These functions operate on normalized terrain/road records. They intentionally
avoid claiming survey-grade accuracy or construction approval.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import hypot


@dataclass(frozen=True)
class TerrainPoint:
    point_id: str
    x: float
    y: float
    elevation_m: float


@dataclass(frozen=True)
class RoadNode:
    node_id: str
    x: float
    y: float
    elevation_m: float


def elevation_delta(a: TerrainPoint | RoadNode, b: TerrainPoint | RoadNode) -> float:
    return b.elevation_m - a.elevation_m


def horizontal_distance_m(a: TerrainPoint | RoadNode, b: TerrainPoint | RoadNode) -> float:
    return hypot(b.x - a.x, b.y - a.y)


def grade_fraction(a: TerrainPoint | RoadNode, b: TerrainPoint | RoadNode) -> float:
    distance = horizontal_distance_m(a, b)
    if distance == 0:
        raise ValueError("grade is undefined for coincident points")
    return elevation_delta(a, b) / distance


def planning_record(a: RoadNode, b: RoadNode) -> dict[str, object]:
    distance = horizontal_distance_m(a, b)
    return {
        "from_node": a.node_id,
        "to_node": b.node_id,
        "horizontal_distance_m": distance,
        "elevation_delta_m": elevation_delta(a, b),
        "grade_fraction": grade_fraction(a, b),
        "los_status": "unresolved",
        "survey_status": "not_surveyed",
        "engineering_status": "not_validated",
    }
