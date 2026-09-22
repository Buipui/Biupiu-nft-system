"""Canonical authority hierarchy for Biupiu native AI/federation.

AI and federation coordinate and propose; they never outrank the owning
Core OS/DMS/domain authority or release authority.
"""
from enum import IntEnum


class AuthorityLevel(IntEnum):
    HUMAN_RELEASE = 0
    CORE_OS_DMS = 1
    DOMAIN_OWNER = 2
    INTELLIGENCE = 3
    FEDERATION = 4
    ADAPTER_PROVIDER = 5
    EXTERNAL_REFERENCE = 6


CANONICAL_HIERARCHY = (
    "HUMAN_RELEASE",
    "CORE_OS_DMS",
    "DOMAIN_OWNER",
    "INTELLIGENCE",
    "FEDERATION",
    "ADAPTER_PROVIDER",
    "EXTERNAL_REFERENCE",
)


def authority_level(name: str) -> AuthorityLevel:
    key = str(name).strip().upper().replace("-", "_").replace(" ", "_")
    try:
        return AuthorityLevel[key]
    except KeyError as exc:
        raise ValueError(f"unknown authority: {name}") from exc


def can_control(actor: str, target: str) -> bool:
    """Return True only when actor is equal/lower in authority rank.

    Lower numeric levels are more authoritative. AI/federation therefore
    cannot control Core OS/DMS or human release authority.
    """
    return authority_level(actor) <= authority_level(target)


def assert_no_ai_escalation(actor: str, target: str) -> None:
    if not can_control(actor, target):
        raise PermissionError(
            f"authority escalation blocked: {actor!r} cannot control {target!r}"
        )


def promotion_requires_core_os(record: dict) -> bool:
    """AI may propose; executable promotion requires Core OS/DMS validation."""
    return (
        bool(record.get("ai_proposal"))
        and not bool(record.get("core_os_validated"))
    )
