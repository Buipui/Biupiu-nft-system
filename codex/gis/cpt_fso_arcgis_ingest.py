"""Normalize City of Cape Town ArcGIS building features into FSO nodes.

The adapter intentionally drops street-address text from the graph payload.
Source object IDs and suburb names remain for reproducibility and auditing.
"""

from __future__ import annotations

from typing import Any, Iterable

PUBLIC_USAGE = {
    "OFFICE", "FIRE STATION", "LIBRARY", "HALL", "CLINIC", "DEPOT",
    "LAW ENFORCEMENT", "MUNICIPAL POOL", "RESERVOIR", "SPORT FACILITY",
    "TRAFFIC DEPARTMENT", "WORKSHOP", "COMMUNITY CENTRE",
}


def _usage(value: Any) -> str:
    return str(value or "").strip().upper()


def feature_to_node(feature: dict[str, Any], source_layer: str) -> dict[str, Any] | None:
    attrs = feature.get("attributes", {})
    geometry = feature.get("geometry", {})
    usage = _usage(attrs.get("BLDG_USG"))
    if usage not in PUBLIC_USAGE:
        return None
    if "x" not in geometry or "y" not in geometry:
        return None
    object_id = attrs.get("OBJECTID")
    return {
        "node_id": f"CCT-{source_layer}-{object_id}",
        "source_layer": source_layer,
        "source_object_id": object_id,
        "suburb": attrs.get("SBRB"),
        "name": attrs.get("NAME"),
        "node_class": usage,
        "x": geometry["x"],
        "y": geometry["y"],
        "permission_status": "unknown",
        "safety_status": "unknown",
        "aviation_status": "unknown",
        "environment_status": "unknown",
        "height_status": "unresolved",
        "los_status": "unresolved",
    }


def ingest_features(features: Iterable[dict[str, Any]], source_layer: str) -> list[dict[str, Any]]:
    nodes = [feature_to_node(f, source_layer) for f in features]
    return [n for n in nodes if n is not None]
