"""Deterministic learning/provenance primitives for Biupiu Intelligence.

This module records lineage; it does not train or modify an AI model.
It uses only the Python standard library so the foundation remains portable.
"""

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import hashlib
import json
from typing import Optional, Sequence


EVIDENCE_STATES = {
    "ESTABLISHED", "SUPPORTED", "PRELIMINARY", "HYPOTHESIS",
    "SPECULATIVE", "CONTRADICTED", "INCONCLUSIVE",
}
KNOWLEDGE_CLASSES = {
    "FACT", "MODEL_OUTPUT", "HYPOTHESIS", "SIMULATION_RESULT",
    "MEASUREMENT", "INTERPRETATION", "FAILURE", "REPOSITORY_CHANGE",
}
NEXT_ACTIONS = {"SIMULATE", "TEST", "REPLICATE", "CALIBRATE", "REVIEW", "HOLD", "ARCHIVE"}
DECISIONS = {"PENDING", "ACCEPTED", "REJECTED", "DEFERRED"}


def _canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_canonical(value: object) -> str:
    return hashlib.sha256(_canonical(value).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class LearningRecord:
    learning_id: str
    target_type: str
    target_id: str
    input_refs: Sequence[str]
    evidence_state: str
    knowledge_class: str
    prior_version: Optional[str]
    result_version: str
    model_version: Optional[str]
    expected_outcome: Optional[str]
    observed_outcome: str
    error: Optional[float]
    uncertainty: Optional[float]
    next_action: str
    human_decision: str
    provenance_hash: str
    parent_learning_id: Optional[str]
    created_at: str


def make_learning_record(
    learning_id: str,
    target_type: str,
    target_id: str,
    input_refs: Sequence[str],
    evidence_state: str,
    knowledge_class: str,
    result_version: str,
    observed_outcome: str,
    *,
    prior_version: Optional[str] = None,
    model_version: Optional[str] = None,
    expected_outcome: Optional[str] = None,
    error: Optional[float] = None,
    uncertainty: Optional[float] = None,
    next_action: str = "REVIEW",
    human_decision: str = "PENDING",
    parent_learning_id: Optional[str] = None,
    created_at: Optional[str] = None,
) -> LearningRecord:
    if evidence_state not in EVIDENCE_STATES:
        raise ValueError(f"invalid evidence_state: {evidence_state}")
    if knowledge_class not in KNOWLEDGE_CLASSES:
        raise ValueError(f"invalid knowledge_class: {knowledge_class}")
    if next_action not in NEXT_ACTIONS:
        raise ValueError(f"invalid next_action: {next_action}")
    if human_decision not in DECISIONS:
        raise ValueError(f"invalid human_decision: {human_decision}")

    timestamp = created_at or datetime.now(timezone.utc).isoformat()
    unsigned = {
        "learning_id": learning_id,
        "target_type": target_type,
        "target_id": target_id,
        "input_refs": list(input_refs),
        "evidence_state": evidence_state,
        "knowledge_class": knowledge_class,
        "prior_version": prior_version,
        "result_version": result_version,
        "model_version": model_version,
        "expected_outcome": expected_outcome,
        "observed_outcome": observed_outcome,
        "error": error,
        "uncertainty": uncertainty,
        "next_action": next_action,
        "human_decision": human_decision,
        "parent_learning_id": parent_learning_id,
        "created_at": timestamp,
    }
    return LearningRecord(
        **unsigned,
        provenance_hash=sha256_canonical(unsigned),
    )


def verify_learning_record(record: LearningRecord) -> bool:
    data = asdict(record)
    expected = data.pop("provenance_hash")
    return sha256_canonical(data) == expected
