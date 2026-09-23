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
    licence_checked: bool = False,
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
        "model_disagreement": max(0.0, 1.0 - evidence.drift_penalty),
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


@dataclass(frozen=True)
class RuntimeTelemetryObservation:
    """Normalised runtime evidence suitable for passive learning."""
    module_id: str
    state: str
    path: str
    latency_ms: float
    resource_pressure: float
    success: bool
    correlation_id: str


def make_runtime_telemetry_learning_record(
    observation: RuntimeTelemetryObservation,
    *,
    learning_id: str,
    input_refs: Sequence[str] = (),
    result_version: str = "runtime-telemetry-v1",
) -> LearningRecord:
    """Convert runtime telemetry into governed evidence without promotion."""
    if observation.latency_ms < 0:
        raise ValueError("latency_ms must be non-negative")
    if not 0.0 <= observation.resource_pressure <= 1.0:
        raise ValueError("resource_pressure must be between 0 and 1")
    if not observation.correlation_id.strip():
        raise ValueError("correlation_id is required")
    refs = tuple(input_refs) + (
        f"correlation={observation.correlation_id}",
        f"path={observation.path}",
        f"state={observation.state}",
    )
    return make_learning_record(
        learning_id=learning_id,
        target_type="RUNTIME_TELEMETRY",
        target_id=observation.module_id,
        input_refs=refs,
        evidence_state="SUPPORTED",
        knowledge_class="MEASUREMENT",
        result_version=result_version,
        observed_outcome=(
            f"success={observation.success};latency_ms={observation.latency_ms:.6f};"
            f"resource_pressure={observation.resource_pressure:.6f}"
        ),
        error=0.0 if observation.success else 1.0,
        uncertainty=None,
        next_action="TEST",
    )


CODING_MATRIX_VERSION = "BIUPIU-NATIVE-CODING-PHILOSOPHY-AND-ENGINEERING-MATRIX-v1.0"
CODING_GATE_VERSION = "biupiu.ai.coding-hard-gate.v1"


def coding_learning_evidence(*, coding_matrix_checked: bool, semantic_audit_passed: bool,
                             language_test_passed: bool, regression_passed: bool,
                             provenance_verified: bool, security_passed: bool,
                             rollback_reference: str = "") -> dict:
    """Return machine-readable coding evidence without granting promotion authority."""
    return {
        "coding_matrix_version": CODING_MATRIX_VERSION,
        "coding_gate_version": CODING_GATE_VERSION,
        "coding_matrix_checked": bool(coding_matrix_checked),
        "semantic_audit_passed": bool(semantic_audit_passed),
        "language_test_passed": bool(language_test_passed),
        "regression_passed": bool(regression_passed),
        "provenance_verified": bool(provenance_verified),
        "security_passed": bool(security_passed),
        "rollback_reference": str(rollback_reference),
    }


def coding_pattern_reuse_ready(evidence: dict, *, human_approved: bool = False) -> bool:
    """Gate reusable coding knowledge; Core OS/release authority remains final."""
    required = (
        "coding_matrix_checked", "semantic_audit_passed", "language_test_passed",
        "regression_passed", "provenance_verified", "security_passed",
    )
    return bool(human_approved and evidence.get("rollback_reference") and all(evidence.get(k) for k in required))

@dataclass(frozen=True)
class ExternalFixEvidence:
    """Evidence used to learn from an external fix that was not internally implemented."""
    target_id: str
    fault_class: str
    external_fix_id: str
    internal_present: bool
    semantic_match: bool
    source_verified: bool
    licence_checked: bool
    security_checked: bool
    tests_available: bool
    regression_available: bool
    search_pass: str
    source_refs: Tuple[str, ...] = ()

def score_external_fix_gap(evidence: ExternalFixEvidence) -> CandidateScore:
    """Score an external fix gap for guided investigation, never for auto-promotion."""
    if evidence.search_pass not in {"PASS-1", "PASS-2"}:
        raise ValueError("search_pass must be PASS-1 or PASS-2")
    if not evidence.source_refs:
        raise ValueError("source_refs are required")
    values = {
        "information_gain": 1.0 if not evidence.internal_present else 0.0,
        "uncertainty_reduction": 1.0 if evidence.semantic_match else 0.0,
        "model_disagreement": 1.0 if not evidence.internal_present and evidence.semantic_match else 0.0,
        "feasibility": 1.0 if evidence.source_verified and evidence.licence_checked else 0.0,
        "regression_safety": 1.0 if evidence.tests_available and evidence.regression_available and evidence.security_checked else 0.0,
    }
    return score_learning_candidate(f"external-fix-gap:{evidence.external_fix_id}", **values)

def make_external_fix_gap_learning_record(evidence: ExternalFixEvidence, *, learning_id: str) -> LearningRecord:
    """Persist an external/internal mismatch as governed learning evidence."""
    score = score_external_fix_gap(evidence)
    outcome = (
        f"external fix {evidence.external_fix_id} absent internally; "
        f"search={evidence.search_pass}; candidate_score={score.score:.6f}; "
        f"native implementation required={not evidence.internal_present}"
    )
    return make_learning_record(
        learning_id=learning_id,
        target_type="EXTERNAL_FIX_GAP",
        target_id=evidence.target_id,
        input_refs=tuple(evidence.source_refs) + (f"external_fix_id={evidence.external_fix_id}",),
        evidence_state="SUPPORTED" if evidence.source_verified else "PRELIMINARY",
        knowledge_class="FAILURE",
        result_version="external-fix-gap-learning-v1",
        observed_outcome=outcome,
        next_action="TEST" if score.regression_safety else "REVIEW",
    )

@dataclass(frozen=True)
class HarvestComparison:
    search_id: str
    pass_one_refs: Tuple[str, ...]
    pass_two_refs: Tuple[str, ...]
    common_refs: Tuple[str, ...]
    only_first: Tuple[str, ...]
    only_second: Tuple[str, ...]
    divergence_reason: str

def compare_harvest_passes(search_id: str, pass_one_refs: Sequence[str], pass_two_refs: Sequence[str]) -> HarvestComparison:
    """Explain repeated-harvest differences without assuming the cause."""
    a, b = set(pass_one_refs), set(pass_two_refs)
    common = tuple(sorted(a & b))
    only_a, only_b = tuple(sorted(a - b)), tuple(sorted(b - a))
    if not only_a and not only_b:
        reason = "NO_DIVERGENCE"
    elif not common:
        reason = "NON_OVERLAPPING_RESULT_SET_REQUIRES_SOURCE_AND_INDEX_REVIEW"
    else:
        reason = "RESULT_SET_CHANGED_REQUIRES_RECENCY_QUERY_AND_SOURCE_INDEX_REVIEW"
    return HarvestComparison(search_id, tuple(pass_one_refs), tuple(pass_two_refs), common, only_a, only_b, reason)


@dataclass(frozen=True)
class PassiveLearningObservation:
    """Low-cost observation captured while a module is PASSIVE.

    Passive learning records observations without activating the target module
    or granting authority to modify production code.
    """
    target_id: str
    signal_type: str
    value: float
    confidence: float
    resource_state: str = "PASSIVE"
    source_ref: str = ""

def make_passive_learning_record(
    observation: PassiveLearningObservation,
    *,
    learning_id: str,
    model_version: str = "passive-learning-v1",
) -> LearningRecord:
    """Convert passive telemetry into governed learning evidence."""
    if observation.resource_state != "PASSIVE":
        raise ValueError("passive learning requires PASSIVE resource state")
    if not all(math.isfinite(float(x)) and 0.0 <= float(x) <= 1.0
               for x in (observation.value, observation.confidence)):
        raise ValueError("passive observation value/confidence must be between 0 and 1")
    refs = (observation.source_ref,) if observation.source_ref else ()
    return make_learning_record(
        learning_id=learning_id,
        target_type="PASSIVE_MODULE",
        target_id=observation.target_id,
        input_refs=refs,
        evidence_state="SUPPORTED" if observation.confidence >= 0.5 else "PRELIMINARY",
        knowledge_class="MEASUREMENT",
        result_version="passive-learning-v1",
        model_version=model_version,
        expected_outcome=None,
        observed_outcome=f"{observation.signal_type}={observation.value:.6f};confidence={observation.confidence:.6f}",
        next_action="TEST",
    )


def passive_learning_candidate(
    observation_count: int,
    *,
    uncertainty: float,
    recurrence: float,
    regression_safety: float = 0.0,
) -> CandidateScore:
    """Rank a passive observation for later active validation.

    This improves future scheduling/optimisation decisions without activating
    the module solely for learning.
    """
    if observation_count < 0:
        raise ValueError("observation_count must be non-negative")
    return score_learning_candidate(
        "passive-observation",
        information_gain=min(1.0, observation_count / 100.0),
        uncertainty_reduction=max(0.0, min(1.0, 1.0 - uncertainty)),
        model_disagreement=max(0.0, min(1.0, recurrence)),
        feasibility=1.0,
        regression_safety=max(0.0, min(1.0, regression_safety)),
    )
