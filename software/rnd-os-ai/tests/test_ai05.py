from pathlib import Path
from biupiu_ai.auth import DevelopmentTokenVerifier
from biupiu_ai.gateway import AiGatewayService
from biupiu_ai.provider import DeterministicProvider
from biupiu_ai.retrieval import RepositoryRetriever
from biupiu_ai.api import AiApi

def make_api(tmp_path):
    (tmp_path / "evidence.md").write_text("photonics evidence", encoding="utf-8")
    service = AiGatewayService(RepositoryRetriever(str(tmp_path)), DeterministicProvider())
    return AiApi(service, DevelopmentTokenVerifier("test-token"))

def test_authorized_ai_request(tmp_path: Path):
    result = make_api(tmp_path).ask("test-token", "photonics evidence")
    assert result["ok"] is True
    assert result["subject"] == "development-user"

def test_unauthorized_ai_request(tmp_path: Path):
    result = make_api(tmp_path).ask("wrong-token", "photonics evidence")
    assert result["ok"] is False
