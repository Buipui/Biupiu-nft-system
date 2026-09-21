from biupiu_ai.federation_protocol import REQUIRED_GATES, gate_passes, federation_ready, required_components

def test_required_components_are_stable():
    assert required_components() == (
        "core-authority","ai-ml-algorithms","multilingual","federated-learning",
        "quantum-ml","specialist-ai","nasa-darpa-research","failure-learning","ci-runtime",
    )

def test_gate_is_fail_closed():
    g=REQUIRED_GATES[0]
    assert gate_passes(g, {k: True for k in g.required}) is False
    verified=type(g)(g.gate_id,g.component,g.required,"VERIFIED")
    assert gate_passes(verified,{k: True for k in verified.required}) is True

def test_federation_requires_every_gate():
    verified=[type(g)(g.gate_id,g.component,g.required,"VERIFIED") for g in REQUIRED_GATES]
    evidence={g.gate_id:{k:True for k in g.required} for g in verified}
    assert federation_ready(verified,evidence) is True
    evidence["F09"]["test-results"]=False
    assert federation_ready(verified,evidence) is False
