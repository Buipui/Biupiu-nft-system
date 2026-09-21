"""Persistent identity, provenance, feedback and governed handoff contracts."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Mapping


@dataclass(frozen=True)
class SpecialistIdentity:
    specialist_id: str
    version: str
    owner_domains: tuple[str, ...]
    resident: bool = True
    autonomous: bool = True


@dataclass(frozen=True)
class ModuleOwnership:
    specialist_id: str
    module_id: str
    artifact: str
    evidence_state: str
    artifact_version: str


@dataclass(frozen=True)
class LearningEvent:
    event_id: str
    specialist_id: str
    task_id: str
    outcome: str
    metrics: Mapping[str, float] = field(default_factory=dict)
    feedback: Mapping[str, Any] = field(default_factory=dict)
    model_version: str = "unpromoted"
    promotion_eligible: bool = False


@dataclass(frozen=True)
class Handoff:
    task_id: str
    source_specialist: str
    target_specialist: str
    reason: str
    artifact_ids: tuple[str, ...] = ()
    approved: bool = False


class SpecialistStateStore:
    """In-memory contract; persistence belongs to the OS/DMS implementation layer."""

    def __init__(self) -> None:
        self.identities: dict[str, SpecialistIdentity] = {}
        self.ownership: list[ModuleOwnership] = []
        self.learning_events: list[LearningEvent] = []
        self.handoffs: list[Handoff] = []

    def register_identity(self, identity: SpecialistIdentity) -> None:
        self.identities[identity.specialist_id] = identity

    def bind_module(self, binding: ModuleOwnership) -> None:
        if binding.specialist_id not in self.identities:
            raise KeyError(binding.specialist_id)
        self.ownership.append(binding)

    def record_learning(self, event: LearningEvent) -> None:
        self.learning_events.append(event)

    def request_handoff(self, handoff: Handoff) -> bool:
        if not handoff.approved:
            return False
        if handoff.source_specialist not in self.identities or handoff.target_specialist not in self.identities:
            return False
        self.handoffs.append(handoff)
        return True

    def promotable_events(self) -> tuple[LearningEvent, ...]:
        return tuple(e for e in self.learning_events if e.promotion_eligible and e.outcome == "validated")


def build_state_store() -> SpecialistStateStore:
    return SpecialistStateStore()
