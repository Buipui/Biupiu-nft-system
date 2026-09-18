from dataclasses import asdict
from .experiments import ExperimentPlan

def serialize_experiment(plan: ExperimentPlan) -> dict:
    return asdict(plan)

def validate_experiment(plan: ExperimentPlan) -> list[str]:
    errors = []
    if not plan.hypothesis.strip():
        errors.append("hypothesis is required")
    if not plan.independent_variables:
        errors.append("at least one independent variable is required")
    if not plan.dependent_variables:
        errors.append("at least one dependent variable is required")
    if not plan.controls:
        errors.append("at least one control is required")
    if not plan.procedure:
        errors.append("procedure is required")
    if not plan.falsification_criteria:
        errors.append("falsification criteria are required")
    return errors
