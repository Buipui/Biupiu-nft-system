from biupiu_ai.quantum_federation import (
    PromotionEvidence,
    eligible_for_quantum_promotion,
    quantum_capability_names,
)


def test_quantum_promotion_is_fail_closed():
    assert not eligible_for_quantum_promotion(PromotionEvidence())


def test_quantum_promotion_requires_all_evidence():
    evidence = PromotionEvidence(
        provenance=True,
        license_reviewed=True,
        security_reviewed=True,
        regression_passed=True,
        reproducible=True,
        human_approved=True,
    )
    assert eligible_for_quantum_promotion(evidence)


def test_hardware_path_requires_security_review():
    evidence = PromotionEvidence(
        provenance=True,
        license_reviewed=True,
        regression_passed=True,
        reproducible=True,
        human_approved=True,
    )
    assert not eligible_for_quantum_promotion(evidence, requires_hardware=True)


def test_quantum_capabilities_are_stable():
    capabilities = quantum_capability_names()
    assert capabilities == tuple(sorted(capabilities))
    assert "quantum-kernel" in capabilities
