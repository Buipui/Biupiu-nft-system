"""System-wide AI cross-link manifest for Biupiu Intelligence.

This module is deliberately additive: it does not replace federation_registry.py.
It provides one deterministic, machine-readable map between native AI systems,
provider boundaries, coding governance and verification states.
"""
from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class AISystemLink:
    system_id: str
    authority: str
    role: str
    consumers: Tuple[str, ...]
    evidence_required: Tuple[str, ...]
    promotion_state: str


AI_SYSTEM_LINKS = (
    AISystemLink(
        "biupiu-intelligence", "native", "research/evidence/learning",
        ("dms", "ai-ml", "federation", "digital-twin"),
        ("provenance", "security", "regression", "human"),
        "ACTIVE_GOVERNANCE",
    ),
    AISystemLink(
        "biupiu-core-os", "native", "validation/authority/release-gates",
        ("dms", "federation", "android", "simulators"),
        ("semantic-audit", "security", "regression", "human"),
        "ACTIVE_GOVERNANCE",
    ),
    AISystemLink(
        "biupiu-ai-os", "native", "reasoning/models/adaptation",
        ("core-os", "dms", "federation", "ml"),
        ("contract", "provenance", "security", "regression"),
        "REGISTERED",
    ),
    AISystemLink(
        "onnxruntime.android", "provider", "android-inference",
        ("biupiu-ai-os", "mini-os-android"),
        ("dependency", "build", "runtime", "regression"),
        "SOURCE_INTEGRATED_RUNTIME_OPEN",
    ),
    AISystemLink(
        "onnxruntime.qnn-plugin", "vendor-provider", "qualcomm-accelerated-onnx",
        ("onnxruntime.android", "federation", "mini-os-android"),
        ("sdk-provenance", "license", "build", "device", "runtime", "regression"),
        "FAIL_CLOSED",
    ),
    AISystemLink(
        "litert.v2", "provider", "android-inference",
        ("biupiu-ai-os", "mini-os-android"),
        ("dependency", "build", "runtime", "regression"),
        "SOURCE_INTEGRATED_RUNTIME_OPEN",
    ),
    AISystemLink(
        "litert.qualcomm-qnn", "vendor-provider", "litert-qualcomm-npu",
        ("litert.v2", "federation", "mini-os-android"),
        ("sdk-provenance", "license", "build", "device", "runtime", "regression"),
        "FAIL_CLOSED",
    ),
    AISystemLink(
        "qualcomm.qairt", "vendor-provider", "qualcomm-ai-npu",
        ("federation", "mini-os-android"),
        ("sdk-provenance", "license", "device", "runtime", "regression"),
        "FAIL_CLOSED",
    ),
    AISystemLink(
        "huawei.hiai", "vendor-provider", "huawei-npu",
        ("federation", "mini-os-android"),
        ("device-capability", "sdk-provenance", "runtime", "regression"),
        "FAIL_CLOSED",
    ),
    AISystemLink(
        "paddle-lite.ndk", "provider", "android-ndk-inference",
        ("federation", "mini-os-android"),
        ("license", "build", "runtime", "regression"),
        "ADAPTER_ONLY",
    ),
    AISystemLink(
        "apache.tvm", "provider", "compiled-runtime",
        ("federation", "accelerator-layer"),
        ("license", "target-build", "runtime", "regression"),
        "ADAPTER_ONLY",
    ),
    AISystemLink(
        "executorch.hexagon", "vendor-provider", "pytorch-edge-qualcomm",
        ("federation", "mini-os-android", "biupiu-ai-os"),
        ("license", "sdk-provenance", "device", "runtime", "regression"),
        "ADAPTER_ONLY",
    ),
    AISystemLink(
        "mediatek.neuropilot", "vendor-provider", "mediatek-npu",
        ("litert.v2", "federation", "mini-os-android"),
        ("license", "device-capability", "sdk-provenance", "runtime", "regression"),
        "FAIL_CLOSED",
    ),
    AISystemLink(
        "samsung.exynos-ailitecore", "vendor-provider", "samsung-npu",
        ("litert.v2", "federation", "mini-os-android"),
        ("license", "device-capability", "sdk-provenance", "runtime", "regression"),
        "FAIL_CLOSED",
    ),
    AISystemLink(
        "google.tensor.npu", "vendor-provider", "google-tensor-npu",
        ("litert.v2", "federation", "mini-os-android"),
        ("device-capability", "sdk-provenance", "runtime", "regression"),
        "FAIL_CLOSED",
    ),
    AISystemLink(
        "android.camerax", "platform-provider", "camera-capture-and-vision-input",
        ("mini-os-android", "multimedia", "ai-ml"),
        ("api-level", "build", "device", "runtime", "regression"),
        "ADAPTER_ONLY",
    ),
    AISystemLink(
        "android.media3", "platform-provider", "media-playback-and-effects",
        ("mini-os-android", "multimedia", "ui"),
        ("api-level", "build", "runtime", "regression"),
        "ADAPTER_ONLY",
    ),
    AISystemLink(
        "google.mlkit", "platform-provider", "on-device-vision-and-ml-services",
        ("mini-os-android", "camera", "ai-ml"),
        ("license", "dependency", "device", "runtime", "regression"),
        "ADAPTER_ONLY",
    ),
    AISystemLink(
        "flower", "research-adapter", "federated-learning",
        ("ml", "learning-federation"),
        ("privacy", "security", "tests", "regression"),
        "ADAPTER_ONLY",
    ),
    AISystemLink(
        "nvflare", "research-adapter", "federated-learning",
        ("ml", "learning-federation"),
        ("license", "security", "tests", "regression"),
        "ADAPTER_ONLY",
    ),
    AISystemLink(
        "qiskit-ml", "optional-adapter", "quantum-ml",
        ("quantum-federation", "ml"),
        ("provenance", "classical-baseline", "tests", "regression"),
        "OPTIONAL",
    ),
    AISystemLink(
        "pennylane", "optional-adapter", "quantum-ml",
        ("quantum-federation", "ml"),
        ("provenance", "classical-baseline", "tests", "regression"),
        "OPTIONAL",
    ),
)


def system_ids() -> Tuple[str, ...]:
    return tuple(link.system_id for link in AI_SYSTEM_LINKS)


def link_for(system_id: str) -> AISystemLink:
    for link in AI_SYSTEM_LINKS:
        if link.system_id == system_id:
            return link
    raise KeyError(f"Unknown AI system: {system_id}")


def promotion_evidence(system_id: str) -> Tuple[str, ...]:
    return link_for(system_id).evidence_required
