from .provider import AiProvider
from .retrieval import RepositoryRetriever
from .schemas import AiContext

class AiGatewayService:
    def __init__(self, retriever: RepositoryRetriever, provider: AiProvider):
        self.retriever = retriever
        self.provider = provider

    def ask(self, task: str, research_object_id=None):
        evidence = self.retriever.search(task)
        return self.provider.generate(AiContext(task, research_object_id, evidence))
