from dataclasses import dataclass
from typing import Dict

@dataclass
class DatasetVersion:
    dataset_id: str
    version: int
    content_hash: str
    created_at: str
    author: str
    note: str = ""

class InMemoryDatasetStore:
    """Development store with immutable version history."""
    def __init__(self):
        self._versions: Dict[str, list[DatasetVersion]] = {}

    def save_version(self, version: DatasetVersion) -> None:
        history = self._versions.setdefault(version.dataset_id, [])
        if history and version.version <= history[-1].version:
            raise ValueError("dataset version must increase")
        history.append(version)

    def history(self, dataset_id: str) -> list[DatasetVersion]:
        return list(self._versions.get(dataset_id, []))
