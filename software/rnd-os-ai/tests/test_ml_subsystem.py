import pytest

from biupiu_ai.ml.backends import get_backend
from biupiu_ai.ml.engine import MLRequest, route_ml_request
from biupiu_ai.ml.metrics import accuracy, mse, mae, brier_score, precision_at_k, recall_at_k, population_stability_index
from biupiu_ai.ml.multilingual import build_search_profile, query_terms

def test_backend_registry():
    assert get_backend("SKLEARN").license == "BSD-3-Clause"
    assert get_backend("XGBOOST").license == "Apache-2.0"
    assert get_backend("TRANSFORMERS").license == "Apache-2.0"

def test_route_requires_evidence_and_prefers_backend():
    r = route_ml_request(MLRequest("ML-001","classification",("AI","AGRI"),("paper:001",),("en","zh"),("SKLEARN",)))
    assert r.selected_backend == "SKLEARN"

def test_metrics():
    assert accuracy([1,0,1],[1,1,1]) == 2/3
    assert mse([1,2],[2,2]) == 0.5
    assert mae([1,2],[2,4]) == 1.5
    assert brier_score([1,0],[0.8,0.2]) == pytest.approx(0.04)
    assert precision_at_k({"a","b"},["a","c","b"],2) == 0.5
    assert recall_at_k({"a","b"},["a","c","b"],2) == 0.5

def test_drift_screening():
    assert population_stability_index([1,2,3,4,5],[1,2,3,4,5]) >= 0

def test_multilingual_profile():
    p = build_search_profile("ML-001","machine learning","zh",native_terms=("机器学习",),transliterations=("jiqixuexi",),abbreviations=("ML",))
    terms = query_terms(p)
    assert "机器学习" in terms and "machine learning" in terms and "ML" in terms
