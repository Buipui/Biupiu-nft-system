from biupiu_ai.federation_protocol import REQUIRED_GATES, federation_ready
from biupiu_ai.federation_registry import DEFAULT_SYSTEMS, FederationPolicy, eligible_for_activation
from biupiu_ai.learning import (
    FailureObservation,
    can_promote_learning,
    fingerprint_failure,
    summarize_failure_pattern,
)
from biupiu_ai.promotion_router import AssetClass, propose_promotion
from simulator_adapters import SimulatorAdapter
from biupiu_ai.guided_fault_finding import fault_fix_rule, guide_fault


def test_federation_ai_stack_is_fail_closed_and_cross_linked():
    assert len(REQUIRED_GATES) >= 16
    assert {"biupiu-intelligence", "biupiu-core-os", "biupiu-ai-os"} <= {
        system.system_id for system in DEFAULT_SYSTEMS
    }

    candidate = next(system for system in DEFAULT_SYSTEMS if system.system_id == "langgraph")
    assert not eligible_for_activation(candidate, FederationPolicy(), security=True)

    proposal = propose_promotion(
        record_id="federation-test-adapter",
        asset_class=AssetClass.ADAPTER,
        licence_verified=True,
        security_checked=True,
        compatibility_checked=True,
        deterministic_tests_passed=True,
        provenance_recorded=True,
        human_approved=True,
    )
    assert proposal.digital_twin_eligible

    fp = fingerprint_failure("interface", "federation-contract", target_id="router")
    observations = [
        FailureObservation("router", "interface", fp, "federation-contract", True, True, platform="linux"),
        FailureObservation("router", "interface", fp, "federation-contract-v2", True, True, platform="windows"),
    ]
    pattern = summarize_failure_pattern(observations)
    assert can_promote_learning(pattern, provenance_verified=True, human_approved=True)

    verified = [type(g)(g.gate_id, g.component, g.required, "VERIFIED") for g in REQUIRED_GATES]
    evidence = {g.gate_id: {key: True for key in g.required} for g in verified}
    assert federation_ready(verified, evidence)

    missing = SimulatorAdapter("missing", "__biupiu_missing_executable__").probe()
    assert missing.status == "not-installed"
    assert missing.command == ()


def test_guided_fault_fix_matrix_is_deterministic_and_fail_closed():
    rule = fault_fix_rule("TRANSPORT")
    assert rule.regression_required and rule.human_promotion_required
    finding = guide_fault({"fault_id": "f1", "fault_class": "CONTRACT", "evidence_refs": ["ev1"]})
    assert finding.state == "TRIAGING"
    assert "schema/version/content-type" in finding.next_step
    try:
        fault_fix_rule("UNKNOWN")
    except ValueError:
        pass
    else:
        raise AssertionError("unknown fault class must fail closed")
