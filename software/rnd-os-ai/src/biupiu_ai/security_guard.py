"""Fail-closed security gate for Biupiu OS/AI external resources and actions."""
from dataclasses import dataclass
from enum import Enum


class ActionClass(str, Enum):
    READ_ONLY = "read_only"
    EXTERNAL_CODE = "external_code"
    STATE_WRITE = "state_write"
    IRREVERSIBLE = "irreversible"


class ResourceClass(str, Enum):
    INTERNAL = "internal"
    EXTERNAL_REFERENCE = "external_reference"
    EXTERNAL_CODE = "external_code"
    DEPENDENCY = "dependency"
    PROHIBITED = "prohibited"


@dataclass(frozen=True)
class SecurityContext:
    licence_verified: bool = False
    security_checked: bool = False
    compatibility_checked: bool = False
    deterministic_tests_passed: bool = False
    provenance_recorded: bool = False
    human_approved: bool = False
    main_os_approved: bool = False


@dataclass(frozen=True)
class SecurityDecision:
    allowed: bool
    authoritative: bool
    reason: str
    required_controls: tuple[str, ...]


_RESOURCE_CONTROLS = (
    "licence_verified",
    "security_checked",
    "compatibility_checked",
    "deterministic_tests_passed",
    "provenance_recorded",
)


def evaluate_action(
    *,
    action: ActionClass,
    resource: ResourceClass,
    context: SecurityContext,
) -> SecurityDecision:
    """Evaluate an action without executing it; deny unsafe promotion paths."""
    if resource is ResourceClass.PROHIBITED:
        return SecurityDecision(False, False, "prohibited_resource", _RESOURCE_CONTROLS)

    if action is ActionClass.READ_ONLY:
        return SecurityDecision(True, False, "advisory_read_only", ())

    controls_ok = all(getattr(context, name) for name in _RESOURCE_CONTROLS)
    authority_ok = context.human_approved and context.main_os_approved

    if resource in {ResourceClass.EXTERNAL_CODE, ResourceClass.DEPENDENCY} and not controls_ok:
        return SecurityDecision(False, False, "external_resource_gates_incomplete", _RESOURCE_CONTROLS)

    if action in {ActionClass.STATE_WRITE, ActionClass.IRREVERSIBLE} and not authority_ok:
        return SecurityDecision(
            False,
            False,
            "authoritative_os_approval_required",
            ("human_approved", "main_os_approved"),
        )

    authoritative = action in {ActionClass.STATE_WRITE, ActionClass.IRREVERSIBLE} and authority_ok
    return SecurityDecision(True, authoritative, "approved_by_security_policy", ())
