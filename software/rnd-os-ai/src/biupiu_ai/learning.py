"""Governed learning, failure-memory and drift primitives for Biupiu Intelligence.

The module records lineage and produces bounded diagnostic signals. It does not
autonomously rewrite authoritative OS code or claim scientific validation.
Standard-library only so the deterministic core stays portable.
"""
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import hashlib, json, math
from typing import Optional, Sequence, Tuple

EVIDENCE_STATES={"ESTABLISHED","SUPPORTED","PRELIMINARY","HYPOTHESIS","SPECULATIVE","CONTRADICTED","INCONCLUSIVE"}
KNOWLEDGE_CLASSES={"FACT","MODEL_OUTPUT","HYPOTHESIS","SIMULATION_RESULT","MEASUREMENT","INTERPRETATION","FAILURE","REPOSITORY_CHANGE"}
NEXT_ACTIONS={"SIMULATE","TEST","REPLICATE","CALIBRATE","REVIEW","HOLD","ARCHIVE"}
DECISIONS={"PENDING","ACCEPTED","REJECTED","DEFERRED"}
FAILURE_CLASSES={"dependency","interface","schema","version","runtime","data","provenance","licence","resource","logic","numerical","integration","unknown"}
LEARNING_LEVELS={0:"logged",1:"classified",2:"fix_verified",3:"regression_covered",4:"reusable_pattern",5:"preventative_test_generated"}

def _canonical(value:object)->str:
    return json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False)

def sha256_canonical(value:object)->str:
    return hashlib.sha256(_canonical(value).encode()).hexdigest()

@dataclass(frozen=True)
class LearningRecord:
    learning_id:str; target_type:str; target_id:str; input_refs:Sequence[str]
    evidence_state:str; knowledge_class:str; prior_version:Optional[str]
    result_version:str; model_version:Optional[str]; expected_outcome:Optional[str]
    observed_outcome:str; error:Optional[float]; uncertainty:Optional[float]
    next_action:str; human_decision:str; provenance_hash:str
    parent_learning_id:Optional[str]; created_at:str

def make_learning_record(learning_id:str,target_type:str,target_id:str,input_refs:Sequence[str],
                         evidence_state:str,knowledge_class:str,result_version:str,observed_outcome:str,**kwargs)->LearningRecord:
    if evidence_state not in EVIDENCE_STATES: raise ValueError("invalid evidence_state")
    if knowledge_class not in KNOWLEDGE_CLASSES: raise ValueError("invalid knowledge_class")
    next_action=kwargs.get("next_action","REVIEW"); human_decision=kwargs.get("human_decision","PENDING")
    if next_action not in NEXT_ACTIONS: raise ValueError("invalid next_action")
    if human_decision not in DECISIONS: raise ValueError("invalid human_decision")
    data={"learning_id":learning_id,"target_type":target_type,"target_id":target_id,
          "input_refs":list(input_refs),"evidence_state":evidence_state,"knowledge_class":knowledge_class,
          "prior_version":kwargs.get("prior_version"),"result_version":result_version,
          "model_version":kwargs.get("model_version"),"expected_outcome":kwargs.get("expected_outcome"),
          "observed_outcome":observed_outcome,"error":kwargs.get("error"),"uncertainty":kwargs.get("uncertainty"),
          "next_action":next_action,"human_decision":human_decision,
          "parent_learning_id":kwargs.get("parent_learning_id"),
          "created_at":kwargs.get("created_at") or datetime.now(timezone.utc).isoformat()}
    return LearningRecord(**data,provenance_hash=sha256_canonical(data))

def verify_learning_record(record:LearningRecord)->bool:
    data=asdict(record); expected=data.pop("provenance_hash")
    return sha256_canonical(data)==expected

@dataclass(frozen=True)
class FailureObservation:
    target_id:str; failure_class:str; fingerprint:str; state_signature:str
    fixed:bool; regression_passed:bool; changed_components:Tuple[str,...]=()
    platform:str="unknown"; version:str=""; evidence_refs:Tuple[str,...]=()
    def __post_init__(self):
        if self.failure_class not in FAILURE_CLASSES: raise ValueError("invalid failure_class")

@dataclass(frozen=True)
class FailurePattern:
    fingerprint:str; occurrences:int; fixes_verified:int; regressions_passed:int
    platforms:Tuple[str,...]; stalled:bool; learning_level:int

def fingerprint_failure(failure_class:str,state_signature:str,*,target_id:str="",platform:str="")->str:
    if failure_class not in FAILURE_CLASSES: raise ValueError("invalid failure_class")
    return sha256_canonical({"failure_class":failure_class,"state_signature":state_signature,
                             "target_id":target_id,"platform":platform})[:24]

def summarize_failure_pattern(observations:Sequence[FailureObservation])->FailurePattern:
    if not observations: raise ValueError("at least one observation is required")
    fp=observations[0].fingerprint
    if any(x.fingerprint!=fp for x in observations): raise ValueError("fingerprints must match")
    occurrences=len(observations); fixes=sum(x.fixed for x in observations)
    regressions=sum(x.regression_passed for x in observations)
    platforms=tuple(sorted({x.platform for x in observations if x.platform}))
    stalled=occurrences>=2 and len({x.state_signature for x in observations})==1 and fixes==0 and regressions==0
    level=4 if fixes and regressions and occurrences>=2 else 3 if regressions else 2 if fixes else 1
    if stalled: level=1
    return FailurePattern(fp,occurrences,fixes,regressions,platforms,stalled,level)

@dataclass(frozen=True)
class DriftState:
    count:int; baseline_error:float; current_error:float; ewma_error:float
    drift_score:float; drift_detected:bool

def update_drift_state(state:Optional[DriftState],observed_error:float,*,alpha:float=0.2,threshold:float=0.15)->DriftState:
    if not 0<=observed_error<=1: raise ValueError("observed_error must be between 0 and 1")
    if not 0<alpha<=1: raise ValueError("alpha must be in (0,1]")
    if threshold<0: raise ValueError("threshold must be non-negative")
    if state is None: return DriftState(1,observed_error,observed_error,observed_error,0.0,False)
    ewma=(1-alpha)*state.ewma_error+alpha*observed_error
    score=abs(ewma-state.baseline_error)/max(abs(state.baseline_error),1e-9)
    return DriftState(state.count+1,state.baseline_error,observed_error,ewma,score,score>=threshold and state.count>=2)

@dataclass(frozen=True)
class CandidateScore:
    candidate_id:str; score:float; information_gain:float; uncertainty_reduction:float
    model_disagreement:float; feasibility:float; regression_safety:float

def score_learning_candidate(candidate_id:str,**signals)->CandidateScore:
    names=("information_gain","uncertainty_reduction","model_disagreement","feasibility","regression_safety")
    vals={n:float(signals.get(n,0.0)) for n in names}
    if any(not math.isfinite(v) or not 0<=v<=1 for v in vals.values()): raise ValueError("signals must be finite values between 0 and 1")
    score=.30*vals["information_gain"]+.25*vals["uncertainty_reduction"]+.15*vals["model_disagreement"]+.15*vals["feasibility"]+.15*vals["regression_safety"]
    return CandidateScore(candidate_id,round(score,6),**vals)

def can_promote_learning(
    pattern: FailurePattern,
    *,
    provenance_verified: bool,
    licence_checked: bool = True,
    human_approved: bool = False,
) -> bool:
    """Permit reuse only after verified fix, regression, provenance, licence and human approval."""
    return (
        pattern.learning_level >= 4
        and not pattern.stalled
        and provenance_verified
        and licence_checked
        and human_approved
    )


def make_multilingual_learning_record(
    learning_id: str,
    target_id: str,
    locale: str,
    source_language: str,
    observed_outcome: str,
    *,
    input_refs: Sequence[str] = (),
    result_version: str = "language-contract-v1",
    model_version: Optional[str] = None,
    expected_outcome: Optional[str] = None,
    human_decision: str = "PENDING",
) -> LearningRecord:
    """Record multilingual routing/harvest evidence without changing authority.

    Locale and source-language metadata remain explicit so future diagnostics
    can compare script/region handling and fallback behaviour.
    """
    metadata_ref = f"locale={locale};source_language={source_language}"
    refs = tuple(input_refs) + (metadata_ref,)
    return make_learning_record(
        learning_id=learning_id,
        target_type="MULTILINGUAL_ROUTING",
        target_id=target_id,
        input_refs=refs,
        evidence_state="SUPPORTED",
        knowledge_class="REPOSITORY_CHANGE",
        result_version=result_version,
        observed_outcome=observed_outcome,
        model_version=model_version,
        expected_outcome=expected_outcome,
        human_decision=human_decision,
        next_action="TEST",
    )


@dataclass(frozen=True)
class LearningEvidence:
    """Evidence inputs used to rank a learning candidate without granting authority."""
    verified_fix: float = 0.0
    regression_safety: float = 0.0
    provenance_quality: float = 0.0
    uncertainty_reduction: float = 0.0
    recurrence: float = 0.0
    drift_penalty: float = 0.0


def score_governed_learning_candidate(candidate_id: str, evidence: LearningEvidence) -> CandidateScore:
    """Score reusable-learning candidates using evidence quality and drift.

    This is a deterministic policy/selection layer, not autonomous promotion.
    Scores are bounded to [0, 1]; Core OS promotion gates remain authoritative.
    """
    values = {
        "information_gain": max(0.0, min(1.0, evidence.recurrence)),
        "uncertainty_reduction": evidence.uncertainty_reduction,
        "model_disagreement": evidence.drift_penalty,
        "feasibility": evidence.provenance_quality,
        "regression_safety": min(evidence.verified_fix, evidence.regression_safety),
    }
    if not all(math.isfinite(float(v)) and 0.0 <= float(v) <= 1.0 for v in values.values()):
        raise ValueError("learning evidence must be finite values between 0 and 1")
    base = (
        0.20 * values["information_gain"]
        + 0.20 * values["uncertainty_reduction"]
        + 0.15 * values["model_disagreement"]
        + 0.20 * values["feasibility"]
        + 0.25 * values["regression_safety"]
    )
    drift_penalty = 0.20 * max(0.0, min(1.0, evidence.drift_penalty))
    score = max(0.0, min(1.0, base - drift_penalty))
    return CandidateScore(
        candidate_id,
        round(score, 6),
        values["information_gain"],
        values["uncertainty_reduction"],
        values["model_disagreement"],
        values["feasibility"],
        values["regression_safety"],
    )


def learning_reuse_ready(pattern: FailurePattern, evidence: LearningEvidence,
                         *, provenance_verified: bool, licence_checked: bool,
                         human_approved: bool = False) -> bool:
    """Require verified fix, regression safety and provenance before reuse."""
    evidence_ready = (
        evidence.verified_fix >= 1.0
        and evidence.regression_safety >= 1.0
        and evidence.provenance_quality >= 1.0
        and evidence.drift_penalty < 0.5
    )
    return evidence_ready and can_promote_learning(
        pattern,
        provenance_verified=provenance_verified,
        licence_checked=licence_checked,
        human_approved=human_approved,
    )
