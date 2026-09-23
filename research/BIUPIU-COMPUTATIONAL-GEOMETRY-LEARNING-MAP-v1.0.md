# Biupiu Computational Geometry Learning Map v1.0

## Purpose
Logs retain raw numeric evidence while deriving graph and geometry representations so behaviour can be inspected as relationships, trajectories and state transitions rather than isolated numbers.

## Mapped dimensions
- X/Y: deterministic angular placement of task/system nodes.
- Z: combined collaboration and evidence level.
- Edges: dependency and cross-department collaboration.
- Radius: evidence strength plus recurrence.
- Time: successive map snapshots; historical states are retained.
- Faults: nodes/edges with failure-class and affected-dependency metadata.
- Learning: topology, position, recurrence and state changes.

## Fault-finding rule
Every important machine event should retain raw values, build/test evidence, dependency/failure classification, graph links, geometry-map reference, learning-state reference, provenance and version.

The geometry is a derived view and cannot overwrite authoritative raw evidence.

## Behavioural paths
DISCOVER -> ROUTE -> EXECUTE -> OBSERVE -> VERIFY -> LEARN

FAILURE -> DEPENDENCY -> AFFECTED_MODULE -> REGRESSION -> PREVENTATIVE_TEST

Each ML system can generate the same representation independently. Federation compares maps for agreement/disagreement and records the comparison as learning evidence.

## Visualisation requirement
Logs should increasingly support time-series graphs, dependency graphs, cross-department networks, computational geometry, state-vector growth and fault-propagation graphs.

A numeric-only record is incomplete for behavioural learning when a graphable relationship exists.
