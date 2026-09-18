from biupiu_ai.retrieval_benchmark import RetrievalBenchmark, RetrievalCase

def test_retrieval_recall():
    case = RetrievalCase("C1", "photonics", ["S1", "S2"])
    result = RetrievalBenchmark().score(case, ["S1", "S3"])
    assert result.recall == 0.5
