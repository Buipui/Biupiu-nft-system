"""Biupiu adaptation of Microsoft Discovery architectural patterns.

Independent implementation of compatible concepts; no Microsoft source code is copied.
Provides deterministic task-DAG, autonomy policy, agent/tool registration and governed
promotion boundaries for Biupiu Intelligence, AI OS and Core OS integration.
"""
from dataclasses import dataclass, field
from enum import Enum


class TaskStatus(str, Enum):
    NEW="new"; EXECUTING="executing"; EXECUTION_DONE="executionDone"; COMPLETE="complete"
    ON_HOLD="onHold"; FAILED="failed"; INCOMPLETE="incomplete"; STALE="stale"
    FLAGGED_HUMAN="flaggedHuman"; FLAGGED_AI="flaggedAi"; REMOVED="removed"


class Autonomy(str, Enum):
    FULL="Full"; SUPERVISED="Supervised"; LOCKED="Locked"


@dataclass(frozen=True)
class DiscoveryTask:
    task_id: str
    objective: str
    status: TaskStatus = TaskStatus.NEW
    dependencies: tuple[str, ...] = ()
    owner: str = "biupiu-intelligence"
    purpose: str = ""
    evidence_refs: tuple[str, ...] = ()


@dataclass(frozen=True)
class DiscoveryAgent:
    agent_id: str
    domains: tuple[str, ...]
    tools: tuple[str, ...] = ()
    autonomy: Autonomy = Autonomy.SUPERVISED


@dataclass(frozen=True)
class DiscoveryTool:
    tool_id: str
    capabilities: tuple[str, ...]
    reversible: bool = True
    external: bool = True
    licence_reviewed: bool = False


@dataclass
class TaskGraph:
    tasks: dict[str, DiscoveryTask] = field(default_factory=dict)

    def add(self, task: DiscoveryTask) -> None:
        if not task.task_id or not task.objective:
            raise ValueError("task_id and objective are required")
        if task.task_id in self.tasks:
            raise ValueError(f"duplicate task: {task.task_id}")
        missing = set(task.dependencies) - self.tasks.keys()
        if missing:
            raise ValueError(f"missing dependencies: {sorted(missing)}")
        if task.task_id in task.dependencies:
            raise ValueError("task cannot depend on itself")
        self.tasks[task.task_id] = task

    def ready(self) -> list[DiscoveryTask]:
        return [t for t in self.tasks.values()
                if t.status in {TaskStatus.NEW, TaskStatus.FLAGGED_AI}
                and all(self.tasks[d].status in {TaskStatus.COMPLETE, TaskStatus.EXECUTION_DONE}
                        for d in t.dependencies)]

    def branch(self, task_id: str, *new_tasks: DiscoveryTask) -> None:\n        """Spawn dependent research branches without discarding the parent."""\n        if task_id not in self.tasks:\n            raise ValueError(f"unknown parent task: {task_id}")\n        for task in new_tasks:\n            if task_id not in task.dependencies:\n                raise ValueError("branch task must depend on its parent")\n            self.add(task)\n\n    def blocked(self) -> list[DiscoveryTask]:
        return [t for t in self.tasks.values()
                if t.status in {TaskStatus.NEW, TaskStatus.FLAGGED_AI}
                and any(self.tasks[d].status not in {TaskStatus.COMPLETE, TaskStatus.EXECUTION_DONE}
                       for d in t.dependencies)]


def validate_tool_use(tool: DiscoveryTool, *, autonomy: Autonomy,
                      human_approved: bool) -> bool:
    if tool.external and not tool.licence_reviewed:
        return False
    if not tool.reversible and not human_approved:
        return False
    if autonomy == Autonomy.SUPERVISED and not human_approved:
        return False
    return True


def route_agent(agent: DiscoveryAgent, requested_domain: str) -> bool:
    return requested_domain in agent.domains


def dependency_closure(root: str, graph: TaskGraph) -> set[str]:
    seen: set[str] = set()
    stack = [root]
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        task = graph.tasks.get(node)
        if task:
            stack.extend(task.dependencies)
    return seen
