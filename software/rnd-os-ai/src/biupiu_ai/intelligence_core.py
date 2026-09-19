"""Core deterministic intelligence primitives.

Architecture patterns are implemented independently rather than copied from
third-party repositories. This module provides evidence relations, confidence
normalisation and impact-trace primitives for the Biupiu Intelligence layer.
"""

from dataclasses import dataclass
from typing import Iterable


EVIDENCE_STATES = (
    "ESTABLISHED", "SUPPORTED", "PRELIMINARY", "HYPOTHESIS",
    "SPECULATIVE", "CONTRADICTED", "INCONCLUSIVE", "UNSUPPORTED",
)

RELATIONS = (
    "SUPPORTS", "CONTRADICTS", "REFINES", "BUILDS_ON",
    "DERIVED_FROM", "TESTS", "PRODUCES", "DEPENDS_ON",
)


@dataclass(frozen=True)
class EvidenceEdge:
    source_id: str
    target_id: str
    relation: str
    evidence_state: str
    provenance_refs: tuple[str, ...] = ()


def make_edge(source_id: str, target_id: str, relation: str,
              evidence_state: str, provenance_refs: Iterable[str] = ()) -> EvidenceEdge:
    if not source_id or not target_id:
        raise ValueError("source_id and target_id are required")
    if relation not in RELATIONS:
        raise ValueError(f"invalid relation: {relation}")
    if evidence_state not in EVIDENCE_STATES:
        raise ValueError(f"invalid evidence_state: {evidence_state}")
    return EvidenceEdge(
        source_id=source_id,
        target_id=target_id,
        relation=relation,
        evidence_state=evidence_state,
        provenance_refs=tuple(provenance_refs),
    )


def grounded(edge: EvidenceEdge) -> bool:
    """True only when the relation is backed by an acceptable evidence state."""
    return edge.evidence_state in {"ESTABLISHED", "SUPPORTED", "PRELIMINARY"}


def dependency_closure(root: str, edges: Iterable[EvidenceEdge]) -> set[str]:
    """Return downstream objects reachable through DEPENDS_ON/PRODUCES edges."""
    adjacency: dict[str, set[str]] = {}
    for edge in edges:
        if edge.relation not in {"DEPENDS_ON", "PRODUCES"}:
            continue
        adjacency.setdefault(edge.source_id, set()).add(edge.target_id)

    seen: set[str] = set()
    stack = [root]
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        stack.extend(adjacency.get(node, ()))
    return seen
