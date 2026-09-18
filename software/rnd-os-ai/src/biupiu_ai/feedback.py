from dataclasses import dataclass
from .datasets import ExperimentDataset
from .timeseries import summarize

@dataclass
class ExperimentFeedback:
    dataset_id: str
    summary: dict
    next_action: str

def analyze_dataset(dataset: ExperimentDataset) -> ExperimentFeedback:
    errors = dataset.validate()
    if errors:
        raise ValueError("; ".join(errors))
    summary = summarize([p.value for p in dataset.points])
    return ExperimentFeedback(
        dataset.dataset_id,
        {"count": summary.count, "mean": summary.mean, "minimum": summary.minimum, "maximum": summary.maximum},
        "Review measurements against the predefined hypothesis and uncertainty before generating the next test.",
    )
