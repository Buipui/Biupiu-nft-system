"""Hard-coded governed learning/federation bridge for Biupiu Intelligence.

Learning is append-only and proposal-based. It may adapt bounded model parameters
or routing preferences, but it never rewrites authoritative OS code or performs
physical actuation. Promotion remains gated by validation, provenance, regression
and human approval.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import hashlib, json, math
from pathlib import Path
from typing import Mapping, Optional, Sequence, Tuple

from .learning import FailureObservation, summarize_failure_pattern, fingerprint_failure
from .ml.continual_adaptation import reference_anchored_parameter_update

EVENTS = {"OBSERVATION","FAILURE","SIMULATION_RESULT","TEST_RESULT","DESIGN_CHANGE","DIGITAL_TWIN_UPDATE","FEDERATION_EVENT","ADAPTATION_PROPOSAL","ADAPTATION_REJECTED","ADAPTATION_APPLIED"}
ADAPTATION_TARGETS = {"MODEL_PARAMETER","ROUTING_POLICY","SIMULATOR_PARAMETER","DESIGN_TOKEN"}
@dataclass(frozen=True)
class LearningEvent:
    event_id: str
    event_type: str
    source_id: str
    target_id: str
    model_version: str
    payload: Mapping[str, object]
    evidence_refs: Tuple[str, ...]
    provenance_hash: str
    created_at: str

@dataclass(frozen=True)
class AdaptationProposal:
    proposal_id: str
    target_type: str
    target_id: str
    prior_version: str
    candidate_version: str
    changes: Mapping[str, float]
    reason: str
    rollback_version: str
    validation_required: bool = True
    human_approval_required: bool = True
    status: str = "PROPOSED"

def _canonical(v: object) -> str:
    return json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def _hash(v: object) -> str:
    return hashlib.sha256(_canonical(v).encode("utf-8")).hexdigest()

def make_event(event_type: str, source_id: str, target_id: str, model_version: str,
               payload: Mapping[str, object], evidence_refs: Sequence[str]) -> LearningEvent:
    if event_type not in EVENTS:
        raise ValueError("invalid event_type")
    if not source_id.strip() or not target_id.strip() or not model_version.strip():
        raise ValueError("source_id, target_id and model_version are required")
    if not evidence_refs:
        raise ValueError("evidence_refs are required")
    data={"event_id":f"learn_evt_{_hash((event_type,source_id,target_id,model_version,payload,evidence_refs))[:24]}",
          "event_type":event_type,"source_id":source_id,"target_id":target_id,
          "model_version":model_version,"payload":dict(payload),
          "evidence_refs":tuple(evidence_refs),
          "created_at":datetime.now(timezone.utc).isoformat()}
    return LearningEvent(**data, provenance_hash=_hash(data))

class AppendOnlyLearningLog:
    def __init__(self, path: str | Path):
        self.path=Path(path)

    def append(self, event: LearningEvent) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(_canonical(asdict(event))+"\n")

    def read(self) -> Tuple[LearningEvent, ...]:
        if not self.path.exists():
            return ()
        result=[]
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if not line.strip(): continue
            raw=json.loads(line)
            expected=raw.pop("provenance_hash")
            if _hash(raw)!=expected:
                raise ValueError("learning log provenance mismatch")
            result.append(LearningEvent(**raw, provenance_hash=expected))
        return tuple(result)

def observe_change(log: AppendOnlyLearningLog, *, source_id: str, target_id: str,
                   model_version: str, change: Mapping[str, object], evidence_refs: Sequence[str]) -> LearningEvent:
    event=make_event("DESIGN_CHANGE",source_id,target_id,model_version,change,evidence_refs)
    log.append(event)
    return event

def learn_from_failure(log: AppendOnlyLearningLog, *, source_id: str, target_id: str,
                       failure_class: str, state_signature: str, platform: str,
                       fixed: bool, regression_passed: bool, evidence_refs: Sequence[str]) -> dict:
    fp=fingerprint_failure(failure_class,state_signature,target_id=target_id,platform=platform)
    obs=FailureObservation(target_id,failure_class,fp,state_signature,fixed,regression_passed,platform=platform,evidence_refs=tuple(evidence_refs))
    pattern=summarize_failure_pattern([obs])
    event=make_event("FAILURE",source_id,target_id,"failure-learning-v1",
                     {"fingerprint":fp,"learning_level":pattern.learning_level,
                      "fixed":fixed,"regression_passed":regression_passed},
                     evidence_refs)
    log.append(event)
    return {"event_id":event.event_id,"fingerprint":fp,"learning_level":pattern.learning_level,
            "adaptation_allowed":bool(fixed and regression_passed and pattern.learning_level>=3)}

def propose_parameter_adaptation(log: AppendOnlyLearningLog, *, source_id: str,
                                  target_id: str, prior_version: str,
                                  current: Mapping[str,float], reference: Mapping[str,float],
                                  gradient: Mapping[str,float], reason: str) -> AdaptationProposal:
    changes=reference_anchored_parameter_update(current,reference,gradient)
    if any(not math.isfinite(v) for v in changes.values()):
        raise ValueError("non-finite adaptation rejected")
    proposal=AdaptationProposal(
        proposal_id=f"adapt_{_hash((target_id,prior_version,changes,reason))[:24]}",
        target_type="MODEL_PARAMETER",target_id=target_id,
        prior_version=prior_version,candidate_version=prior_version+"+candidate",
        changes=dict(changes),reason=reason,rollback_version=prior_version)
    log.append(make_event("ADAPTATION_PROPOSAL",source_id,target_id,proposal.candidate_version,
                           {"proposal":asdict(proposal)},(proposal.prior_version,)))
    return proposal

def approve_adaptation(proposal: AdaptationProposal, *, validation_passed: bool,
                       regression_passed: bool, provenance_verified: bool,
                       human_approved: bool) -> AdaptationProposal:
    if not all((validation_passed,regression_passed,provenance_verified,human_approved)):
        return AdaptationProposal(**{**asdict(proposal),"status":"REJECTED"})
    return AdaptationProposal(**{**asdict(proposal),"status":"APPROVED"})
