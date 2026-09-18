from dataclasses import asdict
from .auth import DevelopmentTokenVerifier
from .gateway import AiGatewayService

class AiApi:
    """Framework-neutral API boundary for the Android client."""

    def __init__(self, service: AiGatewayService, verifier: DevelopmentTokenVerifier):
        self.service = service
        self.verifier = verifier

    def ask(self, token: str, task: str, research_object_id=None) -> dict:
        context = self.verifier.verify(token)
        if context is None or "ai:read" not in context.scopes:
            return {"ok": False, "error": "unauthorized"}
        result = self.service.ask(task, research_object_id)
        return {"ok": True, "result": asdict(result), "subject": context.subject}
