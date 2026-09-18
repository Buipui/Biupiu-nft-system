from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class ExperimentPlan:
    hypothesis: str
    independent_variables: List[str]
    dependent_variables: List[str]
    controls: List[str]
    procedure: List[str]
    expected_observations: List[str]
    falsification_criteria: List[str]
    assumptions: List[str] = field(default_factory=list)
    safety_review_required: bool = True
    research_object_id: Optional[str] = None

class ExperimentGenerator:
    """Creates structured, falsifiable experiment plans from hypotheses."""

    def generate(self, hypothesis: str, research_object_id: Optional[str] = None) -> ExperimentPlan:
        return ExperimentPlan(
            hypothesis=hypothesis,
            independent_variables=["parameter_to_vary"],
            dependent_variables=["measured_response"],
            controls=["baseline/control condition", "measurement procedure"],
            procedure=[
                "Define the baseline and measurement method.",
                "Change one primary independent variable at a time.",
                "Record raw measurements and environmental conditions.",
                "Repeat the measurement according to the protocol.",
                "Compare results with the predefined falsification criteria.",
            ],
            expected_observations=["A measurable response consistent with the hypothesis, if supported."],
            falsification_criteria=[
                "No reproducible effect above the predefined measurement threshold.",
                "Observed effect contradicts the stated directional prediction.",
            ],
            assumptions=["Measurement uncertainty and instrument limits must be recorded."],
            research_object_id=research_object_id,
        )
