from biupiu_ai.promotion_router import AssetClass, propose_promotion

def test_proposal_is_fail_closed():
    p = propose_promotion(record_id="world-engine-1", asset_class=AssetClass.ADAPTER)
    assert p.main_os_approval_required
    assert not p.digital_twin_eligible

def test_validated_adapter_can_reach_digital_twin():
    p = propose_promotion(
        record_id="world-engine-1",
        asset_class=AssetClass.ADAPTER,
        departments=("CG-3D", "RENDER", "CG-3D"),
        licence_verified=True,
        security_checked=True,
        compatibility_checked=True,
        deterministic_tests_passed=True,
        provenance_recorded=True,
        human_approved=True,
    )
    assert p.digital_twin_eligible
    assert p.departments == ("CG-3D", "RENDER")

def test_prohibited_never_promotes():
    p = propose_promotion(
        record_id="proprietary-source",
        asset_class=AssetClass.PROHIBITED,
        licence_verified=True,
        security_checked=True,
        compatibility_checked=True,
        deterministic_tests_passed=True,
        provenance_recorded=True,
        human_approved=True,
    )
    assert not p.digital_twin_eligible
