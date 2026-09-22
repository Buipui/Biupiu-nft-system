from biupiu_ai.authority_hierarchy import (
    CANONICAL_HIERARCHY,
    AuthorityLevel,
    assert_no_ai_escalation,
    authority_level,
    can_control,
    promotion_requires_core_os,
)


def test_canonical_hierarchy_places_core_os_above_intelligence():
    assert CANONICAL_HIERARCHY.index("CORE_OS_DMS") < CANONICAL_HIERARCHY.index("INTELLIGENCE")
    assert AuthorityLevel.CORE_OS_DMS < AuthorityLevel.INTELLIGENCE


def test_ai_cannot_control_core_os():
    assert not can_control("INTELLIGENCE", "CORE_OS_DMS")
    try:
        assert_no_ai_escalation("INTELLIGENCE", "CORE_OS_DMS")
    except PermissionError:
        pass
    else:
        raise AssertionError("AI authority escalation was not blocked")


def test_core_os_can_validate_intelligence_proposals():
    assert can_control("CORE_OS_DMS", "INTELLIGENCE")


def test_promotion_stays_blocked_until_core_os_validation():
    assert promotion_requires_core_os({"ai_proposal": True, "core_os_validated": False})
    assert not promotion_requires_core_os({"ai_proposal": True, "core_os_validated": True})
