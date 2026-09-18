from biupiu_ai.storage import DatasetVersion, InMemoryDatasetStore
from biupiu_ai.statistics import describe
from biupiu_ai.integrity import content_hash

def test_versions_are_monotonic():
    store = InMemoryDatasetStore()
    store.save_version(DatasetVersion("D1", 1, content_hash("a"), "2026-09-18T10:00:00Z", "user"))
    store.save_version(DatasetVersion("D1", 2, content_hash("b"), "2026-09-18T10:01:00Z", "user"))
    assert [v.version for v in store.history("D1")] == [1, 2]

def test_statistics():
    s = describe([1.0, 2.0, 3.0, 4.0])
    assert s.count == 4
    assert s.mean == 2.5
    assert round(s.sample_stddev, 6) == 1.290994

def test_integrity_hash():
    assert content_hash("biupiu") == content_hash("biupiu")
