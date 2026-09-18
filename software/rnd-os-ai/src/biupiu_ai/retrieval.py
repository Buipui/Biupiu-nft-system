from pathlib import Path
from typing import Iterable, List
from .schemas import RetrievalItem

class RepositoryRetriever:
    """Minimal deterministic repository retriever for AI-02.

    Production vector search/embeddings can be added behind this interface
    without changing the AI gateway contract.
    """
    def __init__(self, root: str):
        self.root = Path(root)

    def search(self, query: str, paths: Iterable[str] = ()) -> List[RetrievalItem]:
        terms = [t.lower() for t in query.split() if len(t) > 2]
        candidates = [self.root / p for p in paths] if paths else self.root.rglob("*.md")
        hits = []
        for path in candidates:
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            score = sum(text.lower().count(t) for t in terms)
            if score:
                hits.append((score, path, text))
        hits.sort(key=lambda x: (-x[0], str(x[1])))
        return [RetrievalItem(str(p), p.name, t[:1200]) for _, p, t in hits[:10]]
