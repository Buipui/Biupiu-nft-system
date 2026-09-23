from biupiu_ai.quantum_state_growth_model import evolve_state, state_evidence

def test_growth_state_remains_normalized():
    first = evolve_state(None, system_size=2)
    second = evolve_state(first, system_size=4, signal=1.0)
    assert abs(sum(a*a for a in second.amplitudes) - 1.0) < 1e-8
    assert second.system_size == 4
    assert second.growth_ratio == 2.0
    assert "not quantum hardware evidence" in state_evidence(second)["interpretation"]
