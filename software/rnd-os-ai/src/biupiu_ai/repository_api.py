"""Repository-linked API primitives for Biupiu AI."""
from __future__ import annotations
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from typing import Any, Protocol
import json

class RepositoryAdapter(Protocol):
    def read(self, path: str) -> str: ...
    def write(self, path: str, content: str) -> None: ...
    def list(self, prefix: str = "") -> list[str]: ...

@dataclass(frozen=True)
class RepositoryRecord:
    path: str
    sha256: str
    size: int

class LocalRepositoryAdapter:
    def __init__(self, root: str | Path):
        self.root = Path(root).resolve()
    def _safe(self, path: str) -> Path:
        target = (self.root / path).resolve()
        if self.root not in target.parents and target != self.root:
            raise ValueError("repository path escapes configured root")
        return target
    def read(self, path: str) -> str:
        return self._safe(path).read_text(encoding="utf-8")
    def write(self, path: str, content: str) -> None:
        target = self._safe(path); target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
    def list(self, prefix: str = "") -> list[str]:
        base = self._safe(prefix)
        if base.is_file(): return [str(base.relative_to(self.root))]
        return sorted(str(p.relative_to(self.root)) for p in base.rglob("*") if p.is_file())

class BiupiuRepositoryAPI:
    def __init__(self, adapter: RepositoryAdapter):
        self.adapter = adapter
    def inventory(self, prefix: str = "") -> list[RepositoryRecord]:
        out = []
        for path in self.adapter.list(prefix):
            data = self.adapter.read(path).encode("utf-8")
            out.append(RepositoryRecord(path, sha256(data).hexdigest(), len(data)))
        return out
    def append_jsonl(self, path: str, record: dict[str, Any]) -> None:
        try: existing = self.adapter.read(path)
        except FileNotFoundError: existing = ""
        self.adapter.write(path, existing + json.dumps(record, sort_keys=True, default=str) + "\n")
