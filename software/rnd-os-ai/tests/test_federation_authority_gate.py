from biupiu_ai.federation_protocol import REQUIRED_GATES


def test_core_authority_gate_requires_core_os_validation():
    gate = next(g for g in REQUIRED_GATES if g.gate_id == "F01")
    assert "core-os-validation" in gate.required
