"""Specialist-AI federation contract for Biupiu Intelligence and AI OS."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Mapping, Protocol

@dataclass(frozen=True)
class Capability:
    name: str
    version: str
    domains: tuple[str, ...]
    autonomous: bool = True
    resident: bool = True

@dataclass
class Task:
    task_id: str
    domain: str
    payload: Mapping[str, Any]
    required_capabilities: tuple[str, ...] = ()
    collaborators: tuple[str, ...] = ()

@dataclass
class Result:
    task_id: str
    specialist: str
    status: str
    output: Mapping[str, Any]
    confidence: float | None = None
    provenance: Mapping[str, Any] = field(default_factory=dict)
    handoffs: tuple[str, ...] = ()

class Specialist(Protocol):
    capability: Capability
    def execute(self, task: Task) -> Result: ...

class SpecialistRegistry:
    """Registry that keeps domain specialists resident and discoverable."""

    def __init__(self) -> None:
        self._specialists: dict[str, Specialist] = {}

    def register(self, specialist: Specialist) -> None:
        self._specialists[specialist.capability.name] = specialist

    def resident(self, domain: str) -> tuple[Specialist, ...]:
        return tuple(
            s for s in self._specialists.values()
            if domain in s.capability.domains and s.capability.resident
        )

    def can_handle(self, capability: str) -> bool:
        return capability in self._specialists

    def dispatch(self, task: Task) -> Result:
        candidates = list(self.resident(task.domain))
        for required in task.required_capabilities:
            candidates = [s for s in candidates if required in s.capability.domains or required == s.capability.name]
        if not candidates:
            return Result(task.task_id, "federation", "unresolved", {}, handoffs=())
        # Local specialist autonomy is preferred; federation selects only when needed.
        return candidates[0].execute(task)

    def capabilities(self) -> tuple[Capability, ...]:
        return tuple(s.capability for s in self._specialists.values())
