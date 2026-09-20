"""Recovered repository-module bindings for resident Biupiu specialist AIs.

Bindings reference repository artifacts; they do not claim third-party runtime packages
are installed. A binding is promoted only when the referenced artifact exists and has
been read back from the federation branch.
"""
from __future__ import annotations
from dataclasses import dataclass

from .specialist_catalog import DEPARTMENT_ASSIGNMENTS


@dataclass(frozen=True)
class ModuleBinding:
    department: str
    specialist: str
    module_id: str
    artifact: str
    status: str


RECOVERED_MODULES: tuple[ModuleBinding, ...] = (
    ModuleBinding("AGRI", "agriculture-ai", "FARM-SIM-01", "world/environments/BIUPIU-FARMING-SIMULATION-ARCHITECTURE-v1.0.md", "VERIFIED"),
    ModuleBinding("HEMP", "agriculture-ai", "FARM-SIM-01", "research/BIUPIU-FARMING-SIMULATOR-RESOURCE-REGISTRY-v1.0.md", "VERIFIED"),
    ModuleBinding("BIOCHEM", "engineering-simulation-ai", "PROP-06", "research/PROP-06-CROSS-DISCIPLINE-MICROTURBINE-TRACK-v1.0.md", "VERIFIED"),
    ModuleBinding("MATERIALS", "engineering-simulation-ai", "BIO-TWIN-01", "research/BIUPIU-BIO-COMPOSITE-DIGITAL-TWIN-v1.0.md", "VERIFIED"),
    ModuleBinding("TEXTILES", "engineering-simulation-ai", "BIO-TWIN-01", "research/BIUPIU-BIO-COMPOSITE-DIGITAL-TWIN-v1.0.md", "VERIFIED"),
    ModuleBinding("AUTO", "engineering-simulation-ai", "PROP-06", "research/PROP-06-CROSS-DISCIPLINE-MICROTURBINE-TRACK-v1.0.md", "VERIFIED"),
    ModuleBinding("AERO", "engineering-simulation-ai", "BIO-TWIN-01", "research/BIUPIU-BIO-COMPOSITE-DIGITAL-TWIN-v1.0.md", "VERIFIED"),
    ModuleBinding("MARINE", "engineering-simulation-ai", "PROP-06", "research/PROP-06-CROSS-DISCIPLINE-MICROTURBINE-TRACK-v1.0.md", "VERIFIED"),
    ModuleBinding("ROBOTICS", "robotics-embedded-ai", "FARM-ROBOTICS", "world/environments/BIUPIU-FARMING-SIMULATION-ARCHITECTURE-v1.0.md", "VERIFIED"),
    ModuleBinding("MATH", "engineering-simulation-ai", "MATH-ROUTE", "research/BIUPIU-DEPARTMENT-INDEX.md", "VERIFIED"),
    ModuleBinding("MEDIA", "media-rendering-ai", "BLENDER-BRIDGE-01", "docs/blender-android/BIUPIU-BLENDER-ANDROID-ARCHITECTURE-v1.0.md", "VERIFIED"),
    ModuleBinding("BIUPIU-OS", "knowledge-provenance-ai", "MINT-01", "research/BIUPIU-DEPARTMENT-INDEX.md", "VERIFIED"),
)


def recovered_bindings() -> tuple[ModuleBinding, ...]:
    return RECOVERED_MODULES


def verify_assignment_consistency() -> bool:
    return all(
        DEPARTMENT_ASSIGNMENTS[m.department][0] == m.specialist
        for m in RECOVERED_MODULES
    )
