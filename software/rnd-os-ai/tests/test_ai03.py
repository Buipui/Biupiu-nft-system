from biupiu_ai.experiments import ExperimentGenerator
from biupiu_ai.experiment_schema import serialize_experiment, validate_experiment
from biupiu_ai.result_analysis import classify_result

def test_experiment_generation_and_validation():
    plan = ExperimentGenerator().generate("Geometry A reduces drag relative to Geometry B")
    assert not validate_experiment(plan)
    data = serialize_experiment(plan)
    assert data["hypothesis"].startswith("Geometry A")

def test_result_classification():
    assert classify_result(2.0, 0.2, "positive").outcome == "supported"
    assert classify_result(-2.0, 0.2, "positive").outcome == "unsupported"
    assert classify_result(0.1, 0.2, "positive").outcome == "inconclusive"
