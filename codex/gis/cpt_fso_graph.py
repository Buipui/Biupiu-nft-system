"""Deterministic Cape Town FSO candidate graph construction.

This module converts validated public/institutional GIS observations into a
research graph. It intentionally does not decide whether a site is deployable.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import cos, radians, sqrt
from typing import Iterable


@dataclass(frozen=True)
class Node:
    node_id: str
    latitude: float
    longitude: float
    node_class: str
    source_id: str
    permission_status: str = "unknown"
    safety_status: str = "unknown"


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    distance_m: float
    status: str = "screening"


def distance_m(a: Node, b: Node) -> float:
    """Preliminary local planar distance; not a geodetic survey calculation."""
    mean_lat = radians((a.latitude + b.latitude) / 2.0)
    dy = (b.latitude - a.latitude) * 111_320.0
    dx = (b.longitude - a.longitude) * 111_320.0 * cos(mean_lat)
    return sqrt(dx * dx + dy * dy)


def candidate_edges(
    nodes: Iterable[Node],
    max_distance_m: float,
) -> list[Edge]:
    """Create deterministic undirected candidate links within a distance gate."""
    ordered = sorted(nodes, key=lambda n: n.node_id)
    edges: list[Edge] = []
    for i, left in enumerate(ordered):
        for right in ordered[i + 1 :]:
            d = distance_m(left, right)
            if d <= max_distance_m:
                edges.append(Edge(left.node_id, right.node_id, d))
    return edges


def corridor_graph(nodes: Iterable[Node], max_distance_m: float) -> dict:
    """Return a serialisable graph payload for downstream digital-twin use."""
    ordered = sorted(nodes, key=lambda n: n.node_id)
    edges = candidate_edges(ordered, max_distance_m)
    return {
        "schema_version": "1.0",
        "status": "research_screening",
        "nodes": [n.__dict__ for n in ordered],
        "edges": [e.__dict__ for e in edges],
        "validation_gates": [
            "authoritative_geometry",
            "terrain_and_building_LOS",
            "weather_visibility",
            "power_and_backhaul",
            "permission",
            "aviation",
            "optical_safety",
            "environment",
            "structural_engineering",
        ],
    }
