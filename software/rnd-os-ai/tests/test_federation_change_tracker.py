from biupiu_ai.federation_change_tracker import compare_function, render_changelog


def test_function_diff_tracks_added_removed_changed_and_unchanged():
    before = {"route": "native", "timeout": 30, "security": "required"}
    after = {"route": "native", "timeout": 45, "security": "required", "trace": True}
    diff = compare_function("BPU.SYS.FEDERATION.CORE", "routing", before, after)

    assert diff.semantic_state == "CHANGED"
    assert diff.added == ("trace",)
    assert diff.removed == ()
    assert diff.changed == ("timeout",)
    assert diff.unchanged == ("route", "security")
    assert diff.from_hash != diff.to_hash
    assert "timeout" in render_changelog(diff)


def test_identical_function_is_unchanged():
    state = {"route": "native", "security": "required"}
    diff = compare_function("BPU.SYS.INTELLIGENCE.NATIVE", "retrieval", state, state)
    assert diff.semantic_state == "UNCHANGED"
    assert diff.added == ()
    assert diff.removed == ()
    assert diff.changed == ()
