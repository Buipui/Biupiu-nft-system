from dataclasses import dataclass
from typing import Callable, Optional

from .model_context import GroundedContext
from .schemas import AiResult


@dataclass(frozen=True)
class ProviderHarnessPolicy:
    timeout_seconds: float = 15.0
    max_cost_units: int = 1
    require_citations: bool = True


@dataclass(frozen=True)
class ProviderHarnessResult:
    ok: bool
    error: Optional[str]
    result: Optional[AiResult]


class ProviderTestHarness:
    """Deterministic provider boundary test harness.

    It accepts an injected callable rather than performing network I/O. This
    makes authentication, timeout and failure behavior testable without
    storing credentials or contacting a live model during repository tests.
    """

    def __init__(self, policy: ProviderHarnessPolicy):
        self.policy = policy

    def invoke(
        self,
        context: GroundedContext,
        provider_call: Callable[[GroundedContext], AiResult],
    ) -> ProviderHarnessResult:
        try:
            result = provider_call(context)
        except Exception as exc:
            return ProviderHarnessResult(False, f"provider-error:{type(exc).__name__}", None)

        if self.policy.require_citations and not result.citations:
            return ProviderHarnessResult(False, "missing-citations", result)

        return ProviderHarnessResult(True, None, result)
