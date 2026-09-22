from .models import VALID_EVIDENCE
def guard_evidence(record):
    errors=[]; state=record.get("evidence_state")
    if state not in VALID_EVIDENCE: errors.append("INVALID_EVIDENCE_STATE")
    if state in ("validated","certified"):
        if record.get("measured_evidence_complete") is not True: errors.append("VALIDATED_REQUIRES_MEASURED_EVIDENCE")
        if record.get("review_passed") is not True: errors.append("VALIDATED_REQUIRES_REVIEW")
    return {"valid":not errors,"errors":errors}
def challenge_inputs(inputs):
    warnings=[]
    for key,value in inputs.items():
        if isinstance(value,(int,float)):
            if value!=value: warnings.append(f"NAN:{key}")
            elif value in (float("inf"),float("-inf")): warnings.append(f"INFINITE:{key}")
    return warnings
