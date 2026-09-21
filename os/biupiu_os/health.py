from __future__ import annotations
from .adapters import default_adapters

def system_health(kernel):
    adapters = default_adapters()
    return {
        "kernel": kernel.health(),
        "adapters": [a.health() for a in adapters],
        "existing_capabilities": kernel.registry.as_dict(),
        "verification_policy": {
            "validated_requires_measurement": True,
            "certified_requires_review": True,
            "external_runtimes_verified": False,
        },
    }
