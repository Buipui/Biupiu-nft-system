"""Source-level invariants for the AI system cross-link manifest."""
from biupiu_ai.ai_system_crosslinks import AI_SYSTEM_LINKS, link_for, system_ids


def run() -> None:
    assert len(AI_SYSTEM_LINKS) == len(system_ids())
    assert len(system_ids()) == len(set(system_ids()))
    assert link_for("biupiu-core-os").authority == "native"
    assert link_for("qualcomm.qairt").promotion_state == "FAIL_CLOSED"
    assert link_for("huawei.hiai").promotion_state == "FAIL_CLOSED"
    assert "runtime" in link_for("onnxruntime.android").evidence_required
    assert "regression" in link_for("litert.v2").evidence_required
    for link in AI_SYSTEM_LINKS:
        assert link.system_id
        assert link.authority
        assert link.role
        assert link.consumers
        assert link.evidence_required


if __name__ == "__main__":
    run()
    print("PASS ai-system-crosslinks")
