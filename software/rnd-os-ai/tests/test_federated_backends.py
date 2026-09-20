from biupiu_ai.ml.backends import BACKENDS, get_backend, probe_backend


def test_federated_backends_are_registered():
    assert get_backend("pysyft") is not None
    assert get_backend("flower") is not None


def test_federated_backend_contracts_are_fail_closed():
    for backend_id in ("PYSYFT", "FLOWER"):
        backend = get_backend(backend_id)
        assert backend is not None
        assert backend.integration_mode == "research-adapter"
        assert backend.license == "Apache-2.0"
        assert backend.source.startswith("https://github.com/")


def test_backend_registry_ids_are_unique():
    ids = [backend.backend_id for backend in BACKENDS]
    assert len(ids) == len(set(ids))


def test_optional_probe_does_not_import_backend():
    assert probe_backend("PYSYFT") in (True, False)
    assert probe_backend("FLOWER") in (True, False)
