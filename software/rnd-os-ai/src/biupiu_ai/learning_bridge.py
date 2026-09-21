"""Bridge specialist federation events into the verified Biupiu learning contract."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping, Any

from .specialist_state import LearningEvent, SpecialistStateStore
from .specialist_federation import Result


@dataclass(frozen=True)
class Evaluation:
    specialist_id: str
    task_id: str
    evidence_class: str
    drift_status: str
    regression_status: str
    provenance_ok: bool
    validation_status: str


def evaluate_result(result: Result, *, evidence_class: str = "MODEL_OUTPUT",
                    drift_status: str = "not_run",
                    regression_status: str = "not_run",
                    provenance_ok: bool = True,
                    validation_status: str = "screening") -> Evaluation:
    return Evaluation(
        result.specialist, result.task_id, evidence_class, drift_status,
        regression_status, provenance_ok, validation_status
    )


def ingest_result(store: SpecialistStateStore, result: Result, evaluation: Evaluation) -> LearningEvent:
    validated = (
        result.status == "completed"
        and evaluation.provenance_ok
        and evaluation.validation_status in {"correlated", "independently_reviewed"}
        and evaluation.drift_status in {"pass", "not_run"}
        and evaluation.regression_status in {"pass", "not_run"}
    )
    event = LearningEvent(
        event_id=f"{result.specialist}:{result.task_id}",
        specialist_id=result.specialist,
        task_id=result.task_id,
        outcome="validated" if validated else "candidate",
        metrics={"confidence": result.confidence or 0.0},
        feedback={
            "evidence_class": evaluation.evidence_class,
            "drift_status": evaluation.drift_status,
            "regression_status": evaluation.regression_status,
            "validation_status": evaluation.validation_status,
        },
        model_version=str(result.provenance.get("model_version", "unversioned")),
        promotion_eligible=validated,
    )
    store.record_learning(event)
    return event
