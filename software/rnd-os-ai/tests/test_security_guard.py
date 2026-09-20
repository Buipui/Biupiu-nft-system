import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from biupiu_ai.security_guard import (
    ActionClass,
    ResourceClass,
    SecurityContext,
    evaluate_action,
)


def test_read_only_external_reference_allowed_advisory():
    d = evaluate_action(
        action=ActionClass.READ_ONLY,
        resource=ResourceClass.EXTERNAL_REFERENCE,
        context=SecurityContext(),
    )
    assert d.allowed and not d.authoritative


def test_external_code_requires_all_gates():
    d = evaluate_action(
        action=ActionClass.EXTERNAL_CODE,
        resource=ResourceClass.EXTERNAL_CODE,
        context=SecurityContext(),
    )
    assert not d.allowed
    assert "security_checked" in d.required_controls


def test_fully_gated_external_code_allowed_but_not_authoritative():
    c = SecurityContext(True, True, True, True, True, True, False)
    d = evaluate_action(
        action=ActionClass.EXTERNAL_CODE,
        resource=ResourceClass.EXTERNAL_CODE,
        context=c,
    )
    assert d.allowed and not d.authoritative


def test_state_write_requires_main_os_and_human_approval():
    c = SecurityContext(True, True, True, True, True, True, False)
    d = evaluate_action(
        action=ActionClass.STATE_WRITE,
        resource=ResourceClass.INTERNAL,
        context=c,
    )
    assert not d.allowed

    c2 = SecurityContext(True, True, True, True, True, True, True)
    d2 = evaluate_action(
        action=ActionClass.STATE_WRITE,
        resource=ResourceClass.INTERNAL,
        context=c2,
    )
    assert d2.allowed and d2.authoritative


def test_prohibited_resource_is_blocked():
    c = SecurityContext(*(True for _ in range(7)))
    d = evaluate_action(
        action=ActionClass.READ_ONLY,
        resource=ResourceClass.PROHIBITED,
        context=c,
    )
    assert not d.allowed
