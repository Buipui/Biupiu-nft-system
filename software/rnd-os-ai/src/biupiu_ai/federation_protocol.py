"""Canonical Biupiu federation gate protocol.

The federation coordinates native and specialist systems without allowing an
external adapter to become authoritative. Every gate is fail-closed.
"""
from dataclasses import dataclass
from typing import Tuple

@dataclass(frozen=True)
class FederationGate:
    gate_id: str
    component: str
    required: Tuple[str, ...]
    status: str = "PENDING"

REQUIRED_GATES = (
    FederationGate("F01","core-authority",("provenance","license","security","regression","human")),
    FederationGate("F02","ai-ml-algorithms",("tests","regression")),
    FederationGate("F03","multilingual",("native-source","provenance","translation-boundary","tests")),
    FederationGate("F04","federated-learning",("privacy","aggregation","security","tests")),
    FederationGate("F05","quantum-ml",("classical-baseline","simulator","provenance","tests")),
    FederationGate("F06","specialist-ai",("adapter-contract","provenance","license","security","tests")),
    FederationGate("F07","nasa-darpa-research",("source-provenance","license","security","human")),
    FederationGate("F08","failure-learning",("failure-record","rollback","regression")),
    FederationGate("F09","ci-runtime",("runner","test-results")),
    FederationGate("F10","multicore-compute",("topology-discovery","scheduler-tests","fail-closed","telemetry")),
    FederationGate("F11","machine-capability",("capability-registry","range-validation","adapter-boundary","safety-boundary")),
    FederationGate("F12","spatial-vr-compute",("simulation-authority","gpu-path","endpoint-contract","frame-timing")),
    FederationGate("F13","native-platform-federation",("x86_64","arm64","apple-silicon","windows","macos","linux","android")),
)

def gate_passes(gate: FederationGate, evidence: dict[str, bool]) -> bool:
    return gate.status == "VERIFIED" and all(evidence.get(k, False) for k in gate.required)

def federation_ready(gates, evidence_by_gate) -> bool:
    gates = tuple(gates)
    return bool(gates) and all(gate_passes(g, evidence_by_gate.get(g.gate_id, {})) for g in gates)

def required_components() -> Tuple[str, ...]:
    return tuple(g.component for g in REQUIRED_GATES)
