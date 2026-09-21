import pytest
from biupiu_ai.intelligence_core import AgentTask
from biupiu_ai.native_runtime import NativeAIRuntime
from biupiu_ai.repository_api import LocalRepositoryAdapter, BiupiuRepositoryAPI
from biupiu_ai.blockchain_algorithm_bridge import create_commitment

def test_native_runtime_blocks_unproven_result():
    task=AgentTask("t1","test",("research",))
    r=NativeAIRuntime().execute(task,evidence_state="PRELIMINARY",evidence_refs=("e1",))
    assert r.status=="COMPLETE" and r.promotion_allowed

def test_native_runtime_blocks_missing_evidence():
    task=AgentTask("t2","test",("research",))
    r=NativeAIRuntime().execute(task,evidence_state="PRELIMINARY")
    assert r.status=="FLAGGED_AI" and not r.promotion_allowed

def test_irreversible_requires_human():
    task=AgentTask("t3","test",("release",),irreversible=True,evidence_refs=("e1",))
    r=NativeAIRuntime().execute(task)
    assert not r.promotion_allowed
    r=NativeAIRuntime().execute(task,human_approved=True)
    assert r.promotion_allowed

def test_bounded_learning():
    r=NativeAIRuntime.bounded_learning([0,1],[1,0],confidence=1,drift=0)
    assert 0 < r["adaptation_weight"] <= .35
    assert not r["rollback_required"]
    r=NativeAIRuntime.bounded_learning([0,1],[1,0],confidence=1,drift=3)
    assert r["rollback_required"]

def test_repository_path_confinement(tmp_path):
    api=BiupiuRepositoryAPI(LocalRepositoryAdapter(tmp_path))
    api.adapter.write("a.txt","hello")
    assert api.inventory()[0].size==5
    with pytest.raises(ValueError): api.adapter.read("../outside")

def test_algorithm_commitment_is_deterministic():
    a=create_commitment("x","1",code="c",evidence={"e":1},metadata={"m":2})
    b=create_commitment("x","1",code="c",evidence={"e":1},metadata={"m":2})
    assert a.commitment==b.commitment


def test_unsupported_and_contradicted_evidence_are_blocked():
    task=AgentTask("t4","test",("research",),evidence_refs=("e1",))
    for state in ("UNSUPPORTED","CONTRADICTED"):
        r=NativeAIRuntime().execute(task,evidence_state=state)
        assert r.status=="FLAGGED_AI"
        assert not r.promotion_allowed

def test_learning_rejects_invalid_inputs():
    with pytest.raises(ValueError):
        NativeAIRuntime.bounded_learning([0],[1],confidence=1.1)
    with pytest.raises(ValueError):
        NativeAIRuntime.bounded_learning([0],[1],confidence=1,drift=-1)

def test_activation_is_fail_closed_by_default():
    matrix=NativeAIRuntime().activation_matrix()
    assert matrix
    assert not any(matrix.values())
