from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class GatewayPolicy:
    max_input_chars: int = 12000
    max_evidence_sources: int = 50
    max_dataset_versions: int = 20
    max_cost_units: int = 1
    requests_per_minute: int = 30


@dataclass(frozen=True)
class GatewayDecision:
    accepted: bool
    reason: str


def validate_request(
    task: str,
    evidence_source_ids: list[str],
    dataset_version_ids: list[str],
    policy: GatewayPolicy,
) -> GatewayDecision:
    if not task.strip():
        return GatewayDecision(False, "empty-task")
    if len(task) > policy.max_input_chars:
        return GatewayDecision(False, "task-too-large")
    if len(evidence_source_ids) > policy.max_evidence_sources:
        return GatewayDecision(False, "too-many-evidence-sources")
    if len(dataset_version_ids) > policy.max_dataset_versions:
        return GatewayDecision(False, "too-many-dataset-versions")
    return GatewayDecision(True, "accepted")


def provider_cost_allowed(estimated_cost_units: int, policy: GatewayPolicy) -> bool:
    return 0 <= estimated_cost_units <= policy.max_cost_units


def staging_provider_allowed(
    *,
    authenticated: bool,
    transport_secure: bool,
    privacy_reviewed: bool,
    rate_limit_configured: bool,
    cost_limit_configured: bool,
    provider_enabled: bool,
) -> bool:
    return all((
        authenticated,
        transport_secure,
        privacy_reviewed,
        rate_limit_configured,
        cost_limit_configured,
        provider_enabled,
    ))
