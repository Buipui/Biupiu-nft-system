from dataclasses import dataclass
from statistics import mean

@dataclass
class TimeSeriesSummary:
    count: int
    mean: float | None
    minimum: float | None
    maximum: float | None

def summarize(values: list[float]) -> TimeSeriesSummary:
    if not values:
        return TimeSeriesSummary(0, None, None, None)
    return TimeSeriesSummary(len(values), mean(values), min(values), max(values))
