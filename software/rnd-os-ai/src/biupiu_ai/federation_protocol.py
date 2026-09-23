"""Canonical, fail-closed federation gate protocol.

The federation coordinates native and specialist systems without becoming an
authority bypass. Gate evidence is explicit and evaluated deterministically.
"""

from dataclasses import dataclass
from typing import Mapping, Sequence, Tuple


@dataclass(frozen=True)
class FederationGate:
    gate_id: str
    component: str
    required: Tuple[str, ...]
    status: str = "PENDING"


REQUIRED_GATES = (
    FederationGate("F01", "core-authority", ("provenance", "license", "security", "regression", "core-os-validation", "human")),
    FederationGate("F02", "ai-ml-algorithms", ("tests", "regression")),
    FederationGate("F03", "multilingual", ("native-source", "provenance", "translation-boundary", "tests")),
    FederationGate("F04", "federated-learning", ("privacy", "aggregation", "security", "tests")),
    FederationGate("F05", "quantum-ml", ("classical-baseline", "simulator", "provenance", "tests")),
    FederationGate("F06", "specialist-ai", ("adapter-contract", "provenance", "license", "security", "tests")),
    FederationGate("F07", "nasa-darpa-research", ("source-provenance", "license", "security", "human")),
    FederationGate("F08", "failure-learning", ("failure-record", "rollback", "regression")),
    FederationGate("F09", "ci-runtime", ("runner", "test-results")),
    FederationGate("F10", "multicore-compute", ("topology-discovery", "scheduler-tests", "fail-closed", "telemetry")),
    FederationGate("F11", "machine-capability", ("capability-registry", "range-validation", "adapter-boundary", "safety-boundary")),
    FederationGate("F12", "spatial-vr-compute", ("simulation-authority", "gpu-path", "endpoint-contract", "frame-timing")),
    FederationGate("F13", "native-platform-federation", ("x86_64", "arm64", "apple-silicon", "windows", "macos", "linux", "android")),
    FederationGate("F14", "design-language", ("design-contract", "semantic-actions", "visual-regression")),
    FederationGate("F15", "digital-twin-learning", ("twin-events", "learning-log", "rollback", "regression")),
    FederationGate("F16", "simulator-learning-federation", ("simulator-registry", "observation-schema", "learning-bridge", "provenance")),
    FederationGate("F17", "capability-discovery", ("capability-registry", "version-negotiation", "fail-closed")),
    FederationGate("F18", "federation-observability", ("trace-context", "correlation-id", "health", "queue-depth")),
    FederationGate("F19", "schema-governance", ("schema-ref", "content-type", "schema-hash", "compatibility")),
    FederationGate("F20", "delivery-resilience", ("delivery-policy", "retry", "ttl", "backpressure", "dead-letter")),
    FederationGate("F21", "industrial-adapters", ("opcua-boundary", "mqtt-boundary", "oem-boundary", "transport-neutral")),
    FederationGate("F22", "world-repository-boundary", ("core-world-separation", "simulator-authority", "provenance", "migration-plan")),
    FederationGate("F23", "digital-twin-performance-federation", ("twin-schema", "module-capability-map", "performance-policy", "passive-state", "acceleration-policy", "deceleration-policy", "telemetry", "regression")),
    FederationGate("F24", "oem-shared-development-resources", ("oem-family-registry", "sdk-adapter-registry", "runtime-version-matrix", "shared-resource-policy", "provenance")),
    FederationGate("F25", "cross-matrix-scalability", ("capability-matrix", "dependency-graph", "resource-budget", "backpressure", "fail-closed")),
)


def gate_passes(gate: FederationGate, evidence: Mapping[str, bool]) -> bool:
    """Return True only when the gate is explicitly VERIFIED and all evidence passes."""
    return gate.status == "VERIFIED" and all(evidence.get(key, False) for key in gate.required)


def federation_ready(
    gates: Sequence[FederationGate],
    evidence_by_gate: Mapping[str, Mapping[str, bool]],
) -> bool:
    """Return readiness only when every supplied federation gate passes."""
    gate_set = tuple(gates)
    return bool(gate_set) and all(
        gate_passes(gate, evidence_by_gate.get(gate.gate_id, {})) for gate in gate_set
    )


def required_components() -> Tuple[str, ...]:
    """Return canonical component names in gate order."""
    return tuple(gate.component for gate in REQUIRED_GATES)
