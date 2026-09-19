"""First-party ML routing and provenance boundary."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from .backends import BackendSpec, BACKENDS, get_backend, probe_backend
from biupiu_ai.learning import make_learning_record, LearningRecord


TASK_CAPABILITIES = {
    "classification": ("classical", "tabular", "deep-learning"),
    "regression": ("classical", "tabular", "deep-learning"),
    "clustering": ("clustering", "representation-learning"),
    "online": ("online", "streaming", "incremental"),
    "retrieval": ("vector-search", "knowledge-graph"),
    "nlp": ("nlp", "multilingual", "language-models"),
    "reinforcement-learning": ("reinforcement-learning", "simulation", "control"),
    "hyperparameter-optimization": ("hyperparameter-optimization", "search"),
    "portable-inference": ("portable-inference", "edge-inference"),
    "privacy": ("differential-privacy", "federated-learning", "privacy-research"),
}


@dataclass(frozen=True)
class MLRequest:
    request_id: str
    task_type: str
    departments: Tuple[str, ...]
    evidence_refs: Tuple[str, ...]
    source_languages: Tuple[str, ...] = ("en",)
    preferred_backends: Tuple[str, ...] = ()
    irreversible: bool = False


@dataclass(frozen=True)
class MLRoute:
    request_id: str
    selected_backend: str | None
    candidate_backends: Tuple[str, ...]
    requires_human_approval: bool
    reasons: Tuple[str, ...]


def _matches(backend: BackendSpec, task_type: str) -> bool:
    needs = TASK_CAPABILITIES.get(task_type, (task_type,))
    return any(cap in backend.capabilities for cap in needs)


def route_ml_request(request: MLRequest, *, only_available: bool = False) -> MLRoute:
    if not request.request_id or not request.task_type:
        raise ValueError("request_id and task_type are required")
    if not request.evidence_refs:
        raise ValueError("ML routing requires evidence_refs")

    candidates = [
        b for b in BACKENDS
        if _matches(b, request.task_type)
        and (not only_available or probe_backend(b.backend_id))
    ]
    preferred = [get_backend(x) for x in request.preferred_backends]
    preferred = [x for x in preferred if x is not None and x in candidates]
    ordered = tuple(dict.fromkeys([*(x.backend_id for x in preferred), *(x.backend_id for x in candidates)]))
    selected = ordered[0] if ordered else None

    reasons = [
        f"task={request.task_type}",
        f"departments={','.join(request.departments) or 'UNSPECIFIED'}",
        f"languages={','.join(request.source_languages)}",
        "third-party execution remains optional and separately validated",
    ]
    if only_available and not selected:
        reasons.append("no installed compatible backend detected")
    return MLRoute(
        request.request_id,
        selected,
        ordered,
        request.irreversible,
        tuple(reasons),
    )


def make_ml_learning_record(
    request: MLRequest,
    *,
    result_version: str,
    observed_outcome: str,
    model_version: str | None = None,
    error: float | None = None,
    uncertainty: float | None = None,
) -> LearningRecord:
    return make_learning_record(
        learning_id=f"ML-{request.request_id}",
        target_type="ML_RUN",
        target_id=request.request_id,
        input_refs=request.evidence_refs,
        evidence_state="PRELIMINARY",
        knowledge_class="MODEL_OUTPUT",
        result_version=result_version,
        observed_outcome=observed_outcome,
        model_version=model_version,
        error=error,
        uncertainty=uncertainty,
        next_action="REVIEW",
        human_decision="PENDING",
    )
