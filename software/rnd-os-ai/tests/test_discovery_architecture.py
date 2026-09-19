from biupiu_ai.discovery_architecture import (
    Autonomy, DiscoveryTask, DiscoveryTool, TaskGraph, TaskStatus,
    dependency_closure, validate_tool_use
)


def test_task_graph_ready_and_blocked():
    graph = TaskGraph()
    graph.add(DiscoveryTask("root", "retrieve evidence", TaskStatus.COMPLETE))
    graph.add(DiscoveryTask("child", "analyse evidence", dependencies=("root",)))
    assert [t.task_id for t in graph.ready()] == ["child"]
    assert graph.blocked() == []


def test_task_graph_dependency_closure():
    graph = TaskGraph()
    graph.add(DiscoveryTask("a", "a"))
    graph.add(DiscoveryTask("b", "b", dependencies=("a",)))
    graph.add(DiscoveryTask("c", "c", dependencies=("b",)))
    assert dependency_closure("c", graph) == {"a", "b", "c"}


def test_unreviewed_external_tool_fails_closed():
    tool = DiscoveryTool("external", ("search",), external=True, licence_reviewed=False)
    assert not validate_tool_use(tool, autonomy=Autonomy.FULL, human_approved=True)


def test_supervised_tool_requires_approval():
    tool = DiscoveryTool("reviewed", ("search",), external=True, licence_reviewed=True)
    assert not validate_tool_use(tool, autonomy=Autonomy.SUPERVISED, human_approved=False)
    assert validate_tool_use(tool, autonomy=Autonomy.SUPERVISED, human_approved=True)
