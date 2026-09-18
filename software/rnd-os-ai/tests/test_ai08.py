from biupiu_ai.datasets import DataPoint, ExperimentDataset
from biupiu_ai.timeseries import summarize
from biupiu_ai.feedback import analyze_dataset

def dataset():
    return ExperimentDataset("D1", "E1", "temperature-01", [
        DataPoint("2026-09-18T10:00:00Z", 20.0, "C"),
        DataPoint("2026-09-18T10:01:00Z", 22.0, "C"),
        DataPoint("2026-09-18T10:02:00Z", 24.0, "C"),
    ])

def test_dataset_validation():
    assert dataset().validate() == []

def test_timeseries_summary():
    s = summarize([20.0, 22.0, 24.0])
    assert s.count == 3
    assert s.mean == 22.0

def test_feedback_loop():
    result = analyze_dataset(dataset())
    assert result.summary["mean"] == 22.0
    assert "hypothesis" in result.next_action
