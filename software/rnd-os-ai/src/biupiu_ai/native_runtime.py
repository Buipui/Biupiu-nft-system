"""Biupiu native AI runtime boundary.
First-party, dependency-light orchestration over existing Biupiu Intelligence,
continual adaptation, multilingual discovery and federation controls.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from hashlib import sha256
import json
from typing import Any, Mapping, Sequence
from .intelligence_core import AgentTask, route_task, validate_agent_result
from .federation_registry import DEFAULT_SYSTEMS, FederationPolicy, eligible_for_activation
from .ml.continual_adaptation import blend_predictions

@dataclass(frozen=True)
class NativeResult:
    task_id: str
    status: str
    route: tuple[str, ...]
    digest: str
    evidence_state: str
    promotion_allowed: bool

class NativeAIRuntime:
    def __init__(self, *, policy: FederationPolicy | None = None):
        self.policy = policy or FederationPolicy()

    def execute(self, task: AgentTask, *, evidence_state: str = "PRELIMINARY",
                evidence_refs: Sequence[str] = (), payload: Mapping[str, Any] | None = None,
                human_approved: bool = False) -> NativeResult:
        route = route_task(task)
        allowed = validate_agent_result(
            evidence_refs=evidence_refs or task.evidence_refs,
            evidence_state=evidence_state,
            human_approved=human_approved,
            irreversible=task.irreversible,
        )
        record = {"task": asdict(task), "route": route.domains,
                  "evidence_state": evidence_state,
                  "evidence_refs": tuple(evidence_refs or task.evidence_refs),
                  "payload": payload or {}, "promotion_allowed": allowed}
        digest = sha256(json.dumps(record, sort_keys=True, default=str).encode()).hexdigest()
        return NativeResult(task.task_id, "COMPLETE" if allowed else "FLAGGED_AI",
                            route.domains, digest, evidence_state, allowed)

    @staticmethod
    def bounded_learning(base: Sequence[float], teacher: Sequence[float], *,
                          confidence: float, drift: float = 0.0) -> dict[str, Any]:
        return asdict(blend_predictions(base, teacher, teacher_confidence=confidence,
                                        drift_score=drift))

    def activation_matrix(self) -> dict[str, bool]:
        return {s.system_id: eligible_for_activation(
            s, self.policy, provenance=False, license=False,
            security=False, regression=False, human_approved=False)
            for s in DEFAULT_SYSTEMS}
