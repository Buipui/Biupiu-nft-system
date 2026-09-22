"""Optional ML backend registry for Biupiu Intelligence.

No third-party package is required to import this module. Backend availability
is probed without importing/executing the package. This keeps the Core OS and
the deterministic Intelligence foundation portable and fail-closed.
"""

from __future__ import annotations

from dataclasses import dataclass
import importlib.util
from typing import Tuple


@dataclass(frozen=True)
class BackendSpec:
    backend_id: str
    package: str
    import_name: str
    license: str
    capabilities: Tuple[str, ...]
    integration_mode: str
    source: str


BACKENDS = (
    BackendSpec(
        "SKLEARN", "scikit-learn", "sklearn", "BSD-3-Clause",
        ("classical", "classification", "regression", "clustering", "preprocessing", "evaluation"),
        "optional-adapter", "https://github.com/scikit-learn/scikit-learn",
    ),
    BackendSpec(
        "XGBOOST", "xgboost", "xgboost", "Apache-2.0",
        ("tabular", "classification", "regression", "ranking"),
        "optional-adapter", "https://github.com/dmlc/xgboost",
    ),
    BackendSpec(
        "LIGHTGBM", "lightgbm", "lightgbm", "MIT",
        ("tabular", "classification", "regression", "ranking", "distributed"),
        "optional-adapter", "https://github.com/lightgbm-org/LightGBM",
    ),
    BackendSpec(
        "RIVER", "river", "river", "BSD-3-Clause",
        ("online", "streaming", "incremental", "concept-drift"),
        "optional-adapter", "https://github.com/online-ml/river",
    ),
    BackendSpec(
        "PYTORCH", "torch", "torch", "BSD-3-Clause-plus-third-party-notices",
        ("deep-learning", "vision", "sequence", "representation-learning", "scientific-ml"),
        "optional-adapter", "https://github.com/pytorch/pytorch",
    ),
    BackendSpec(
        "TORCHRL", "torchrl", "torchrl", "MIT",
        ("reinforcement-learning", "simulation", "control"),
        "optional-adapter", "https://github.com/pytorch/rl",
    ),
    BackendSpec(
        "TRANSFORMERS", "transformers", "transformers", "Apache-2.0",
        ("nlp", "multilingual", "language-models", "representation-learning"),
        "optional-adapter", "https://github.com/huggingface/transformers",
    ),
    BackendSpec(
        "FAISS", "faiss-cpu/faiss-gpu", "faiss", "MIT",
        ("vector-search", "nearest-neighbour", "retrieval"),
        "optional-adapter", "https://github.com/facebookresearch/faiss",
    ),
    BackendSpec(
        "NETWORKX", "networkx", "networkx", "BSD-3-Clause",
        ("graphs", "knowledge-graph", "dependency-analysis"),
        "optional-adapter", "https://github.com/networkx/networkx",
    ),
    BackendSpec(
        "OPTUNA", "optuna", "optuna", "MIT",
        ("hyperparameter-optimization", "search", "study-management"),
        "optional-adapter", "https://github.com/optuna/optuna",
    ),
    BackendSpec(
        "ONNX", "onnx", "onnx", "Apache-2.0",
        ("model-interchange", "portable-inference"),
        "optional-adapter", "https://github.com/onnx/onnx",
    ),
    BackendSpec(
        "ONNXRUNTIME", "onnxruntime", "onnxruntime", "MIT",
        ("portable-inference", "edge-inference"),
        "optional-adapter", "https://github.com/microsoft/onnxruntime",
    ),
    BackendSpec(
        "MLFLOW", "mlflow", "mlflow", "Apache-2.0",
        ("experiment-tracking", "model-registry", "evaluation-lineage"),
        "optional-adapter", "https://github.com/mlflow/mlflow",
    ),
    BackendSpec(
        "OPACUS", "opacus", "opacus", "Apache-2.0",
        ("differential-privacy", "private-training"),
        "optional-adapter", "https://github.com/meta-pytorch/opacus",
    ),
    BackendSpec(
        "PYSYFT", "syft", "syft", "Apache-2.0",
        ("federated-learning", "privacy-research", "remote-data-science", "datasite-access"),
        "research-adapter", "https://github.com/OpenMined/PySyft",
    ),
    BackendSpec(
        "FLOWER", "flwr", "flwr", "Apache-2.0",
        ("federated-learning", "federated-analytics", "secure-aggregation", "simulation"),
        "research-adapter", "https://github.com/flwrlabs/flower",
    ),
    BackendSpec(
        "GYMNASIUM", "gymnasium", "gymnasium", "MIT",
        ("reinforcement-learning", "environment-interface", "simulation"),
        "optional-adapter", "https://github.com/Farama-Foundation/Gymnasium",
    ),
    # Native/mobile/edge accelerator adapters. These are capability contracts,
    # not bundled vendor SDKs; proprietary SDKs remain externally licensed.
    BackendSpec("ANDROID_AI_CORE", "Android platform AI Core", "android.ai.core", "Android platform terms",
        ("on-device-ai", "accelerated-inference", "android"), "platform-adapter", "https://developer.android.com/"),
    BackendSpec("NNAPI", "Android NNAPI", "android.nnapi", "Android platform terms",
        ("on-device-ai", "accelerated-inference", "android", "portable-inference"), "platform-adapter", "https://developer.android.com/ndk/guides/neuralnetworks"),
    BackendSpec("QUALCOMM_QNN", "Qualcomm AI Engine Direct QNN", "qnn", "Qualcomm SDK license",
        ("edge-inference", "npu", "dsp", "gpu", "android"), "vendor-adapter", "https://developer.qualcomm.com/"),
    BackendSpec("QUALCOMM_SNPE", "Qualcomm SNPE", "snpe", "Qualcomm SDK license",
        ("edge-inference", "npu", "dsp", "gpu", "android"), "vendor-adapter", "https://developer.qualcomm.com/"),
    BackendSpec("MEDIATEK_NEURON", "MediaTek NeuroPilot Neuron Runtime", "neuron", "MediaTek SDK license",
        ("edge-inference", "npu", "android"), "vendor-adapter", "https://developer.mediatek.com/"),
    BackendSpec("HUAWEI_HIAI", "Huawei HiAI Foundation/Engine", "hiai", "Huawei SDK license",
        ("edge-inference", "npu", "android"), "vendor-adapter", "https://developer.huawei.com/"),
    BackendSpec("STM32CUBE_AI", "STM32Cube.AI", "stm32cubeai", "ST SDK license",
        ("microcontroller-inference", "edge-inference", "embedded"), "vendor-adapter", "https://www.st.com/"),
    BackendSpec("NXP_EIQ", "NXP eIQ", "eiq", "NXP SDK license",
        ("edge-inference", "npu", "embedded", "automotive"), "vendor-adapter", "https://www.nxp.com/design/design-center/software/eiq-ai-development-environment.html"),
    BackendSpec("OPENVINO", "Intel OpenVINO", "openvino", "Apache-2.0",
        ("portable-inference", "edge-inference", "cpu", "gpu", "npu"), "optional-adapter", "https://github.com/openvinotoolkit/openvino"),
    BackendSpec("TENSORRT", "NVIDIA TensorRT", "tensorrt", "NVIDIA SDK license",
        ("deep-learning", "edge-inference", "gpu", "jetson"), "vendor-adapter", "https://github.com/NVIDIA/TensorRT"),
    BackendSpec("TVM", "Apache TVM", "tvm", "Apache-2.0",
        ("model-compiler", "portable-inference", "cpu", "gpu", "npu", "mobile"), "optional-adapter", "https://github.com/apache/tvm"),
    BackendSpec("JITTOR", "Jittor", "jittor", "Apache-2.0",
        ("deep-learning", "jit-compilation", "meta-operators", "mobile"), "optional-adapter", "https://github.com/Jittor/jittor"),
    BackendSpec("RAY", "Ray", "ray", "Apache-2.0",
        ("distributed", "reinforcement-learning", "training", "serving"), "optional-adapter", "https://github.com/ray-project/ray"),
    BackendSpec("FASTNLP", "FastNLP", "fastNLP", "Apache-2.0",
        ("nlp", "language-models", "training"), "optional-adapter", "https://github.com/fastnlp/fastNLP"),
    BackendSpec("FLASHATTENTION", "FlashAttention", "flash_attn", "BSD-3-Clause",
        ("attention", "llm-inference", "gpu", "memory-efficiency"), "optional-adapter", "https://github.com/Dao-AILab/flash-attention"),
    BackendSpec("TENSORFLOW", "TensorFlow", "tensorflow", "Apache-2.0",
        ("deep-learning", "training", "inference", "mobile"), "optional-adapter", "https://github.com/tensorflow/tensorflow"),
    BackendSpec("TFLITE", "TensorFlow Lite", "tflite_runtime", "Apache-2.0",
        ("mobile", "edge-inference", "android"), "optional-adapter", "https://github.com/tensorflow/tflite-micro"),
    BackendSpec("CENTUAR", "Stanford CRFM Centaur/open-weight research", "centaur", "Project-specific license",
        ("llm", "language-models", "inference"), "research-adapter", "https://crfm.stanford.edu/"),
)


def get_backend(backend_id: str) -> BackendSpec | None:
    wanted = backend_id.strip().upper()
    return next((b for b in BACKENDS if b.backend_id == wanted), None)


def probe_backend(backend_id: str) -> bool:
    backend = get_backend(backend_id)
    if backend is None:
        raise ValueError(f"unknown ML backend: {backend_id}")
    try:
        return importlib.util.find_spec(backend.import_name) is not None
    except (ImportError, ModuleNotFoundError, ValueError):
        return False
