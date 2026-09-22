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

    # 2026-09-22 deep external federation: CPU/GPU/LLM/NPU.
    AgentSystem("arm-edge", "cpu-acceleration", ("armv8.2-fp16", "arm-neon"), "capability-adapter"),
    AgentSystem("opencl", "gpu-compute", ("opencl",), "capability-adapter"),
    AgentSystem("edge-llm-families", "model-routing", ("qwen", "deepseek", "llama", "gemma"), "model-adapter"),
    AgentSystem("tencent-ncnn", "edge-inference", ("android", "arm", "neon", "vulkan"), "provider-adapter"),
    AgentSystem("megvii-edge", "edge-ml", ("megcc", "megengine", "arm", "android"), "provider-adapter"),
    AgentSystem("alibaba-tinynn", "model-optimization", ("pruning", "quantization", "tflite-conversion"), "provider-adapter"),
    AgentSystem("kirin-npu", "vendor-npu", ("kirin", "npu"), "vendor-adapter", "CANDIDATE", "LICENSE_REVIEW"),
    AgentSystem("rockchip-rknn", "vendor-npu", ("rknn", "rknpu", "npu"), "provider-adapter"),
    AgentSystem("android-ai", "android-ai-runtime", ("appfunctions-mcp", "aicore"), "platform-adapter"),
    AgentSystem("pytorch-edge", "edge-ml", ("pytorch", "executorch", "android", "npu", "vulkan"), "provider-adapter"),
    AgentSystem("stm32cube-ai", "mcu-ai", ("stm32", "cube-ai"), "vendor-adapter", "CANDIDATE", "LICENSE_REVIEW"),
    AgentSystem("catboost", "ml", ("catboost", "tree-models"), "provider-adapter"),
    AgentSystem("dace", "data-centric-optimization", ("sdfg", "cpu", "gpu", "fpga"), "provider-adapter"),
    AgentSystem("menpo-cupy", "scientific-vision-compute", ("menpo", "cupy", "gpu"), "research-adapter"),
    AgentSystem("fastnlp", "nlp", ("nlp", "data", "training"), "provider-adapter"),

    # Quantum and graphics providers.
    AgentSystem("google-aqt", "quantization-reference", ("aqt", "quantization"), "historical-adapter", "CANDIDATE", "HISTORICAL_REFERENCE"),
    AgentSystem("iqm-quantum", "quantum-provider", ("quantum-sdk", "circuits"), "provider-adapter"),
    AgentSystem("riken-fujitsu-quantum", "quantum-simulation", ("riken", "fujitsu", "simulation"), "simulation-adapter"),
    AgentSystem("android-agsl", "graphics-shader", ("agsl", "runtimeshader"), "platform-adapter"),
    # OpenDroid identity correction: external autonomous Android agent; Compose is its UI surface.
    AgentSystem("opendroid-ui", "ui-engine", ("opendroid-ui",), "unresolved-adapter", "BLOCKED", "UNRESOLVED"),
    AgentSystem("opendroid-android-agent", "android-agent", ("accessibility", "actions", "agent-loop", "llm-routing"), "provider-adapter"),
    AgentSystem("opendroid-memory-security", "agent-state", ("memory", "keystore", "room", "datastore"), "provider-adapter"),
    AgentSystem("opendroid-services-voice", "android-services", ("foreground-service", "notification-listener", "voice", "tts"), "platform-adapter"),
    AgentSystem("opendroid-compose-ui", "ui-surface", ("compose-ui", "viewmodel", "theme", "components"), "ui-adapter"),
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
