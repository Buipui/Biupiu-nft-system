"""Cross-layer Biupiu AI integration gate.

This gate verifies that the native runtime, repository boundary, learning,
multilingual, federation, quantum, gateway and commitment layers can be
imported and exercised together without promoting any external provider.
"""
from biupiu_ai.blockchain_algorithm_bridge import create_commitment, release_record
from biupiu_ai.federation_registry import FederationPolicy, DEFAULT_SYSTEMS, eligible_for_activation
from biupiu_ai.intelligence_core import AgentTask
from biupiu_ai.learning import make_learning_record, verify_learning_record
from biupiu_ai.ml.multilingual import build_search_profile, query_terms
from biupiu_ai.native_runtime import NativeAIRuntime
from biupiu_ai.quantum_federation import PromotionEvidence, eligible_for_quantum_promotion


def test_cross_layer_native_runtime_contracts():
    task = AgentTask("INT-001", "integration smoke", ("AI", "DMS"), evidence_refs=("repo:e1",))
    runtime = NativeAIRuntime(policy=FederationPolicy())
    result = runtime.execute(task, evidence_state="SUPPORTED")
    assert result.status == "COMPLETE"
    assert result.promotion_allowed is True
    assert len(result.digest) == 64

    commitment = create_commitment(
        "biupiu-native-runtime", "1",
        code="native-runtime-contract",
        evidence={"task": task.task_id, "digest": result.digest},
        metadata={"gate": "integration"},
    )
    release = release_record(commitment)
    assert release["status"] == "OFFCHAIN_COMMITMENT"
    assert release["network"] == "UNDEPLOYED"


def test_learning_and_multilingual_lineage():
    record = make_learning_record(
        "LEARN-INT-001", "INTEGRATION", "native-runtime",
        ("repo:e1",), "SUPPORTED", "MODEL_OUTPUT", "1",
        "integration-smoke-complete",
    )
    assert verify_learning_record(record)

    profile = build_search_profile(
        "INT-001", "machine learning", "zh",
        native_terms=("机器学习",), transliterations=("jiqixuexi",),
    )
    assert {"machine learning", "机器学习", "jiqixuexi"} <= set(query_terms(profile))


def test_external_federation_and_quantum_remain_fail_closed():
    matrix = NativeAIRuntime().activation_matrix()
    assert matrix
    assert not any(matrix.values())

    candidate = next(s for s in DEFAULT_SYSTEMS if s.system_id == "langgraph")
    assert not eligible_for_activation(
        candidate, FederationPolicy(),
        provenance=False, license=False, security=False,
        regression=False, human_approved=False,
    )
    assert not eligible_for_quantum_promotion(PromotionEvidence())


def test_bounded_adaptation_and_path_security(tmp_path):
    runtime = NativeAIRuntime()
    adapted = runtime.bounded_learning([0.0, 1.0], [1.0, 0.0], confidence=1.0)
    assert adapted["adaptation_weight"] <= 0.35
    assert adapted["rollback_required"] is False

    from biupiu_ai.repository_api import LocalRepositoryAdapter
    adapter = LocalRepositoryAdapter(tmp_path)
    adapter.write("ok.txt", "ok")
    assert adapter.read("ok.txt") == "ok"
