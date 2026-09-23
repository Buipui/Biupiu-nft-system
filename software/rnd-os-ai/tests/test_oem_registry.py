from biupiu_ai.oem_registry import canonical_registry


def test_canonical_registry_has_cross_vendor_adapters():
    registry = canonical_registry()
    families = {x.family for x in registry.manifest()}
    assert {"Qualcomm", "Intel", "NVIDIA", "AMD", "Epic", "Khronos"} <= families


def test_registry_is_deterministic_and_fallbacks_exist():
    registry = canonical_registry()
    manifest = registry.manifest()
    assert manifest == registry.manifest()
    assert all(x.fallback for x in manifest)
    assert all(x.evidence_status == "REGISTERED" for x in manifest)


def test_qnn_binding_is_explicitly_platform_scoped():
    binding = canonical_registry().get("Qualcomm", "ONNX Runtime QNN EP")
    assert binding.platforms == ("Android", "Windows")
    assert "NPU" in binding.acceleration
