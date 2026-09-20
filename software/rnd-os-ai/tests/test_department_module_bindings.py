from biupiu_ai.department_module_bindings import recovered_bindings, verify_assignment_consistency


def test_recovered_bindings_are_consistent():
    bindings = recovered_bindings()
    assert len(bindings) == 12
    assert all(b.status == "VERIFIED" for b in bindings)
    assert verify_assignment_consistency()


def test_cross_domain_reuse_is_explicit():
    bindings = recovered_bindings()
    assert any(b.department == "AUTO" and b.module_id == "PROP-06" for b in bindings)
    assert any(b.department == "MARINE" and b.module_id == "PROP-06" for b in bindings)
