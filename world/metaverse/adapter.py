"""Biupiu World metaverse adapter primitives.

Dependency-free reference implementation. Network/XR providers are injected at runtime.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
import time


@dataclass
class EntityState:
    entity_id: str
    kind: str
    transform: Dict[str, Any]
    digital_twin_id: Optional[str] = None
    provenance: Optional[Dict[str, Any]] = None


@dataclass
class WorldState:
    world_id: str
    version: int = 0
    entities: Dict[str, EntityState] = field(default_factory=dict)

    def register(self, entity: EntityState) -> None:
        if entity.entity_id in self.entities:
            raise ValueError(f"duplicate entity: {entity.entity_id}")
        self.entities[entity.entity_id] = entity
        self.version += 1

    def snapshot(self) -> Dict[str, Any]:
        return {
            "worldId": self.world_id,
            "version": self.version,
            "timestamp": time.time(),
            "entities": [
                {
                    "id": e.entity_id,
                    "kind": e.kind,
                    "transform": e.transform,
                    "digitalTwinId": e.digital_twin_id,
                    "provenance": e.provenance,
                } for e in self.entities.values()
            ],
        }


class MetaverseAdapter:
    """Validates client proposals before authoritative World mutation."""

    def __init__(self, world: WorldState):
        self.world = world

    def propose_interaction(self, entity_id: str, action: str) -> Dict[str, Any]:
        if entity_id not in self.world.entities:
            raise KeyError(entity_id)
        if not action:
            raise ValueError("action required")
        return {"accepted_for_validation": True, "entity_id": entity_id, "action": action}
