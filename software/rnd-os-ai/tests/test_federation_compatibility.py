from biupiu_ai.federation_compatibility import check_family_compatibility

def test_python_typescript_compatibility():
    result = check_family_compatibility("python-ml", "typescript-federation")
    assert result.compatible
    assert "json" in result.shared_interfaces

def test_unknown_family_fails_closed():
    result = check_family_compatibility("unknown", "python-ml")
    assert not result.compatible
