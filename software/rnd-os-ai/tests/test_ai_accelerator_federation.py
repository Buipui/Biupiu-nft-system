from biupiu_ai.ml.backends import BACKENDS, get_backend, probe_backend
from biupiu_ai.quantum_providers import provider_registry


REQUIRED_ACCELERATORS = {
    "ANDROID_AI_CORE", "NNAPI", "QUALCOMM_QNN", "QUALCOMM_SNPE",
    "MEDIATEK_NEURON", "HUAWEI_HIAI", "STM32CUBE_AI", "NXP_EIQ",
    "OPENVINO", "TENSORRT", "TVM", "JITTOR", "RAY", "FASTNLP",
    "FLASHATTENTION", "TENSORFLOW", "TFLITE", "CENTUAR",
}


def test_required_accelerator_registry_is_present():
    ids = {b.backend_id for b in BACKENDS}
    assert REQUIRED_ACCELERATORS <= ids


def test_accelerator_registry_has_no_duplicate_ids():
    ids = [b.backend_id for b in BACKENDS]
    assert len(ids) == len(set(ids))


def test_vendor_adapters_are_non_installing_contracts():
    for backend_id in REQUIRED_ACCELERATORS:
        backend = get_backend(backend_id)
        assert backend is not None
        assert backend.integration_mode in {
            "platform-adapter", "vendor-adapter", "optional-adapter", "research-adapter"
        }


def test_missing_optional_backend_is_safe():
    # A missing third-party package must be represented as unavailable,
    # not as an import-time failure.
    result = probe_backend("TVM")
    assert isinstance(result, bool)


def test_quantum_registry_contains_ir_and_qpu_boundaries():
    ids = {p.provider_id for p in provider_registry()}
    assert {"qir", "openqasm", "aws-braket", "azure-quantum", "dwave-leap", "pytket"} <= ids
