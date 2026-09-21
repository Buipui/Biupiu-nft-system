"""Public-sector and academic research reference registry for Biupiu OS.

This module registers reference sources and adapter contracts only. It does not
bundle government systems, restricted datasets, proprietary OEM material, or
third-party binaries. Promotion into executable core remains fail-closed.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class ResearchSource:
    source_id: str
    institution: str
    focus: Tuple[str, ...]
    role: str
    provenance_required: bool = True
    licence_required: bool = True
    security_review_required: bool = True
    executable: bool = False


PUBLIC_RESEARCH_SOURCES = (
    ResearchSource(
        "nasa-fprime",
        "NASA",
        ("flight-software", "embedded-systems", "component-architecture"),
        "reference-and-adapter-candidate",
    ),
    ResearchSource(
        "nasa-gmat",
        "NASA",
        ("trajectory-design", "optimization", "scientific-computing"),
        "reference-and-adapter-candidate",
    ),
    ResearchSource(
        "nasa-osal",
        "NASA",
        ("os-abstraction", "posix-portability", "platform-isolation"),
        "architecture-reference",
    ),
    ResearchSource(
        "nasa-vision-workbench",
        "NASA",
        ("computer-vision", "image-processing", "3d-reconstruction"),
        "reference-and-adapter-candidate",
    ),
    ResearchSource(
        "nasa-ziggy",
        "NASA",
        ("pipeline-orchestration", "monitoring", "provenance"),
        "architecture-reference",
    ),
    ResearchSource(
        "darpa-tractor",
        "DARPA",
        ("c-to-rust-translation", "static-analysis", "dynamic-analysis"),
        "research-pattern",
    ),
    ResearchSource(
        "darpa-expmath",
        "DARPA",
        ("lemma-decomposition", "autoformalization", "formal-proof"),
        "research-pattern",
    ),
    ResearchSource(
        "darpa-dial",
        "DARPA",
        ("algorithm-discovery", "optimization", "multiphysics"),
        "research-pattern",
    ),
    ResearchSource(
        "mit-drake",
        "MIT",
        ("robotics", "planning", "simulation", "control"),
        "adapter-candidate",
    ),
    ResearchSource(
        "dhs-public-ai-research",
        "U.S. Department of Homeland Security",
        ("public-ai-research", "security-engineering", "resilience"),
        "reference-and-discovery-only",
    ),
)


def source_ids() -> Tuple[str, ...]:
    return tuple(source.source_id for source in PUBLIC_RESEARCH_SOURCES)


def sources_by_institution(institution: str) -> Tuple[ResearchSource, ...]:
    key = institution.strip().casefold()
    return tuple(
        source for source in PUBLIC_RESEARCH_SOURCES
        if source.institution.casefold() == key
    )


def executable_sources() -> Tuple[ResearchSource, ...]:
    """Return only sources explicitly marked executable.

    The current registry is intentionally empty: external research is not
    promoted into Biupiu OS without source-level licence, security,
    compatibility, regression and human-promotion evidence.
    """
    return tuple(source for source in PUBLIC_RESEARCH_SOURCES if source.executable)
