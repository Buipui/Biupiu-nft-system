"""Native computational-geometry learning map for machine-readable evidence."""
from __future__ import annotations
from dataclasses import dataclass
from math import cos, pi, sin, sqrt
from typing import Iterable, Tuple

@dataclass(frozen=True)
class LearningNode:
    node_id: str
    system_id: str
    task_code: str
    department: str
    evidence_level: int
    x: float
    y: float
    z: float

@dataclass(frozen=True)
class LearningEdge:
    source: str
    target: str
    relation: str
    weight: float

@dataclass(frozen=True)
class GeometryLearningMap:
    nodes: Tuple[LearningNode, ...]
    edges: Tuple[LearningEdge, ...]
    representation: str = "3D_DETERMINISTIC_FEATURE_PROJECTION"

def _clamp01(value: float) -> float:
    return max(0.0, min(1.0, float(value)))

def build_learning_map(records: Iterable[dict]) -> GeometryLearningMap:
    rows = list(records)
    nodes = []
    by_id = {}
    n = max(1, len(rows))
    for i, row in enumerate(rows):
        evidence = _clamp01(float(row.get("evidence_level", 0))) * 5.0
        collaboration = _clamp01(float(row.get("collaboration", 0)))
        recurrence = _clamp01(float(row.get("recurrence", 0)))
        radius = 1.0 + evidence / 5.0 + recurrence
        angle = (2.0 * pi * i) / n
        node = LearningNode(
            node_id=str(row["node_id"]),
            system_id=str(row["system_id"]),
            task_code=str(row["task_code"]),
            department=str(row["department"]),
            evidence_level=int(round(evidence)),
            x=round(radius * cos(angle), 8),
            y=round(radius * sin(angle), 8),
            z=round((0.6 * collaboration) + (0.4 * evidence / 5.0), 8),
        )
        nodes.append(node)
        by_id[node.node_id] = node
    edges = []
    for row in rows:
        src = str(row["node_id"])
        for target in row.get("depends_on", ()):
            if str(target) in by_id:
                a, b = by_id[src], by_id[str(target)]
                distance = sqrt((a.x-b.x)**2 + (a.y-b.y)**2 + (a.z-b.z)**2)
                edges.append(LearningEdge(src, str(target), "DEPENDENCY", round(1.0/(1.0+distance), 8)))
        for target in row.get("collaborates_with", ()):
            if str(target) in by_id:
                edges.append(LearningEdge(src, str(target), "COLLABORATION", 1.0))
    return GeometryLearningMap(tuple(nodes), tuple(edges))

def map_to_log_event(geometry: GeometryLearningMap, *, correlation_id: str) -> dict:
    return {
        "event_type": "COMPUTATIONAL_GEOMETRY_LEARNING_MAP",
        "correlation_id": correlation_id,
        "representation": geometry.representation,
        "node_count": len(geometry.nodes),
        "edge_count": len(geometry.edges),
        "nodes": [node.__dict__ for node in geometry.nodes],
        "edges": [edge.__dict__ for edge in geometry.edges],
        "raw_numeric_evidence_retained": True,
        "mapping_is_derived": True,
    }
