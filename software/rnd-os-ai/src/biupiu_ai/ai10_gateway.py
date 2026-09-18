from .model_context import GroundedContext
from .model_provider import ModelProvider

class GroundedAiService:
    def __init__(self, provider: ModelProvider):
        self.provider = provider

    def answer(self, task: str, dataset_versions=None, evidence=None):
        context = GroundedContext(task, dataset_versions or [], evidence or [])
        return self.provider.generate(context)
