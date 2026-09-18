from dataclasses import dataclass
from typing import List

@dataclass
class ExperimentResult:
    outcome: str  # supported | unsupported | inconclusive
    summary: str
    limitations: List[str]
    next_test: str

def classify_result(observed_effect: float, uncertainty: float, predicted_direction: str, threshold: float = 0.0) -> ExperimentResult:
    if uncertainty < 0:
        raise ValueError("uncertainty cannot be negative")
    if observed_effect == 0 or abs(observed_effect) <= uncertainty:
        return ExperimentResult("inconclusive", "Observed effect is not distinguishable from stated uncertainty.", ["Insufficient signal-to-uncertainty separation."], "Repeat with improved measurement precision or sample size.")
    direction_ok = (predicted_direction == "positive" and observed_effect > threshold) or (predicted_direction == "negative" and observed_effect < -threshold)
    if direction_ok:
        return ExperimentResult("supported", "Observed effect is directionally consistent with the prediction.", ["This classification does not establish causality or general validity."], "Replicate under an independent condition.")
    return ExperimentResult("unsupported", "Observed effect does not match the predicted direction.", ["Check assumptions, controls and measurement validity."], "Review the model and test an alternative hypothesis.")
