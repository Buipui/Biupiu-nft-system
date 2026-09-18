from dataclasses import dataclass
from math import sqrt

@dataclass
class DescriptiveStats:
    count: int
    mean: float
    sample_stddev: float | None
    standard_error: float | None

def describe(values: list[float]) -> DescriptiveStats:
    n = len(values)
    if n == 0:
        raise ValueError("values cannot be empty")
    mean = sum(values) / n
    if n < 2:
        return DescriptiveStats(n, mean, None, None)
    variance = sum((x - mean) ** 2 for x in values) / (n - 1)
    sd = sqrt(variance)
    return DescriptiveStats(n, mean, sd, sd / sqrt(n))
