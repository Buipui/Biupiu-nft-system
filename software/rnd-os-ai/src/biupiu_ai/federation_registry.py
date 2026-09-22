"""Fail-closed registry for native and specialist Biupiu AI adapters."""

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class AgentSystem:
    system_id: str
    role: str
    capabilities: Tuple[str, ...]
    adapter: str
    status: str = "CANDIDATE"
    trust_level: str = "UNVERIFIED"


@dataclass(frozen=True)
class FederationPolicy:
    require_provenance: bool = True
    require_license: bool = True
    require_security: bool = True
    require_regression: bool = True
    require_human_promotion: bool = True


DEFAULT_SYSTEMS = (
    AgentSystem("biupiu-intelligence", "research-orchestrator", ("retrieval", "evidence", "learning"), "native", "ACTIVE", "VERIFIED"),
    AgentSystem("biupiu-core-os", "authority", ("validation", "compatibility", "release-gates"), "native", "ACTIVE", "VERIFIED"),
    AgentSystem("biupiu-ai-os", "ai-routing", ("reasoning", "models", "adaptation"), "native"),
    AgentSystem("biupiu-adapter-registry", "interoperability", ("capability-discovery", "protocol-routing", "provenance", "adapter-contracts"), "native", "ACTIVE", "VERIFIED"),
    AgentSystem("langgraph", "workflow-orchestrator", ("state-graphs", "checkpointing", "human-approval"), "adapter"),
    AgentSystem("crewai", "role-coordination", ("role-agents", "workflow"), "adapter"),
    AgentSystem("dspy", "optimization", ("evaluation", "program-optimization"), "adapter"),
    AgentSystem("vllm", "inference", ("serving", "batching"), "adapter"),
    AgentSystem("pysyft", "privacy-federated-data", ("remote-data-science", "datasite-access", "privacy"), "research-adapter"),
    AgentSystem("flower", "federated-learning", ("federated-learning", "federated-analytics", "secure-aggregation", "simulation"), "research-adapter"),
    AgentSystem("qiskit-ml", "quantum-ml", ("quantum-kernels", "qnn"), "optional-adapter"),
    AgentSystem("pennylane", "quantum-ml", ("hybrid-circuits", "differentiation"), "optional-adapter"),
)


def eligible_for_activation(
    system: AgentSystem,
    policy: FederationPolicy,
    *,
    provenance: bool = False,
    license: bool = False,
    security: bool = False,
    regression: bool = False,
    human_approved: bool = False,
) -> bool:
    """Allow activation only when every policy-required promotion check passes."""
    if system.status == "BLOCKED":
        return False
    checks = (provenance, license, security, regression, human_approved)
    required = (
        policy.require_provenance,
        policy.require_license,
        policy.require_security,
        policy.require_regression,
        policy.require_human_promotion,
    )
    return all(value or not needed for value, needed in zip(checks, required))


def capability_names() -> Tuple[str, ...]:
    """Return the deterministic union of registered capabilities."""
    return tuple(sorted({capability for system in DEFAULT_SYSTEMS for capability in system.capabilities}))
