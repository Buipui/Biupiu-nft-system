import os
from .model_context import GroundedContext
from .model_provider import EvidenceGroundedDevelopmentProvider

class ConfiguredModelProvider:
    """Provider boundary for a future live/local model. Never stores credentials in code."""
    def __init__(self):
        self.model_name = os.getenv("BIUPIU_AI_MODEL", "development")
        self.api_base = os.getenv("BIUPIU_AI_API_BASE", "")
        self.development = EvidenceGroundedDevelopmentProvider()

    def generate(self, context: GroundedContext):
        # Until a production adapter is configured, fail closed to the deterministic provider.
        return self.development.generate(context)
