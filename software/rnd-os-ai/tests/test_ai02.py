from pathlib import Path
from biupiu_ai.retrieval import RepositoryRetriever
from biupiu_ai.provider import DeterministicProvider
from biupiu_ai.gateway import AiGatewayService

def test_retrieval_and_gateway(tmp_path: Path):
    (tmp_path / "test.md").write_text("structured light evidence hypothesis", encoding="utf-8")
    service = AiGatewayService(RepositoryRetriever(str(tmp_path)), DeterministicProvider())
    result = service.ask("structured light evidence")
    assert result.evidence_state == "development"
    assert result.citations == ["test.md"]
