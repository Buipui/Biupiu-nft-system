"""Deterministic native-ML federation function difference/changelog tracker.

The tracker compares two governed snapshots for one AI-federation system/function.
It produces a machine-readable diff without granting execution or promotion authority.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Mapping, Sequence
import hashlib
import json


def canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def content_hash(value: Any) -> str:
    return hashlib.sha256(canonical(value).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class FunctionDiff:
    system_id: str
    function_id: str
    from_hash: str
    to_hash: str
    added: tuple[str, ...]
    removed: tuple[str, ...]
    changed: tuple[str, ...]
    unchanged: tuple[str, ...]
    semantic_state: str
    evidence_state: str = "SOURCE_COMPARISON_ONLY"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _keys(value: Mapping[str, Any]) -> set[str]:
    return {str(k) for k in value.keys()}


def compare_function(
    system_id: str,
    function_id: str,
    before: Mapping[str, Any],
    after: Mapping[str, Any],
) -> FunctionDiff:
    before_keys = _keys(before)
    after_keys = _keys(after)
    added = sorted(after_keys - before_keys)
    removed = sorted(before_keys - after_keys)
    changed = sorted(
        k for k in before_keys & after_keys
        if canonical(before[k]) != canonical(after[k])
    )
    unchanged = sorted(
        k for k in before_keys & after_keys
        if canonical(before[k]) == canonical(after[k])
    )
    semantic_state = "UNCHANGED"
    if added or removed or changed:
        semantic_state = "CHANGED"
    return FunctionDiff(
        system_id=system_id,
        function_id=function_id,
        from_hash=content_hash(before),
        to_hash=content_hash(after),
        added=tuple(added),
        removed=tuple(removed),
        changed=tuple(changed),
        unchanged=tuple(unchanged),
        semantic_state=semantic_state,
    )


def compare_registry_function(
    system_id: str,
    function_id: str,
    before_registry: Mapping[str, Mapping[str, Any]],
    after_registry: Mapping[str, Mapping[str, Any]],
) -> FunctionDiff:
    return compare_function(
        system_id,
        function_id,
        before_registry.get(function_id, {}),
        after_registry.get(function_id, {}),
    )


def render_changelog(diff: FunctionDiff) -> str:
    d = diff.to_dict()
    lines = [
        f"# Federation Function Changelog: {d['system_id']} / {d['function_id']}",
        "",
        f"- semantic_state: {d['semantic_state']}",
        f"- evidence_state: {d['evidence_state']}",
        f"- from_hash: {d['from_hash']}",
        f"- to_hash: {d['to_hash']}",
        f"- added: {', '.join(d['added']) or 'none'}",
        f"- removed: {', '.join(d['removed']) or 'none'}",
        f"- changed: {', '.join(d['changed']) or 'none'}",
        f"- unchanged: {', '.join(d['unchanged']) or 'none'}",
    ]
    return "\n".join(lines)


__all__ = [
    "FunctionDiff",
    "canonical",
    "content_hash",
    "compare_function",
    "compare_registry_function",
    "render_changelog",
]
