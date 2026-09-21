"""Biupiu AI OS native runtime boundary.
Separate from Biupiu Core OS. Controlled AI-side runtime for repository context,
command validation, telemetry, learning hooks and safe promotion.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from time import time
from typing import Any, Callable, Dict, Optional

class ActionClass(str, Enum):
    READ = "read"
    SIMULATE = "simulate"
    WRITE = "write"
    PRIVILEGED = "privileged"

@dataclass(frozen=True)
class AIRequest:
    request_id: str
    action: str
    action_class: ActionClass
    payload: Dict[str, Any] = field(default_factory=dict)
    requires_approval: bool = True

@dataclass
class AIResult:
    request_id: str
    status: str
    output: Dict[str, Any] = field(default_factory=dict)
    error: Optional[str] = None
    timestamp: float = field(default_factory=time)

class NativeAIOSRuntime:
    def __init__(self, repository_reader: Callable[[str], Dict[str, Any]],
                 command_executor: Callable[[AIRequest], Dict[str, Any]],
                 learner: Callable[[Dict[str, Any]], Dict[str, Any]]) -> None:
        self.repository_reader = repository_reader
        self.command_executor = command_executor
        self.learner = learner
        self.approval_required = {ActionClass.WRITE, ActionClass.PRIVILEGED}

    def observe(self, topic: str) -> Dict[str, Any]:
        return self.repository_reader(topic)

    def execute(self, request: AIRequest, approved: bool = False) -> AIResult:
        if request.action_class in self.approval_required and not approved:
            return AIResult(request.request_id, "approval_required",
                            error="Privileged/write action requires explicit approval")
        try:
            return AIResult(request.request_id, "executed",
                            output=self.command_executor(request))
        except Exception as exc:
            return AIResult(request.request_id, "failed", error=str(exc))

    def learn(self, observation: Dict[str, Any]) -> Dict[str, Any]:
        return self.learner(observation)
