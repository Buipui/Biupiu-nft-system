package com.biupiu.minios.federation;

import android.os.Build;
import android.graphics.RenderEffect;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.Map;

/** Capability registry for external AI, multimedia and Compose/UI federation. */
public final class AiMultimediaUiFederationRegistry {
    public enum State { NATIVE_DEPENDENCY, ADAPTER_ONLY, DEVICE_REQUIRED, LICENSE_REVIEW, PLATFORM_BOUNDARY, AVAILABLE, UNRESOLVED }
    public enum Layer { AI_RUNTIME, MULTIMEDIA, UI, NAVIGATION, RENDERING }

    public static final class Capability {
        private final String id;
        private final Layer layer;
        private final State state;
        private final String role;
        Capability(String id, Layer layer, State state, String role) {
            if (id == null || id.isBlank() || layer == null || state == null || role == null || role.isBlank())
                throw new IllegalArgumentException("invalid capability");
            this.id = id; this.layer = layer; this.state = state; this.role = role;
        }
        public String id() { return id; }
        public Layer layer() { return layer; }
        public State state() { return state; }
        public String role() { return role; }
    }

    private final Map<String, Capability> capabilities = new LinkedHashMap<>();

    public AiMultimediaUiFederationRegistry() {
        register("qualcomm.imsdk.2", Layer.MULTIMEDIA, State.PLATFORM_BOUNDARY, "Dragonwing/Qualcomm Linux multimedia+AI pipeline boundary");
        register("qualcomm.qairt", Layer.AI_RUNTIME, State.LICENSE_REVIEW, "Qualcomm AI Runtime/QNN provider boundary; SDK supplied externally");
        register("onnxruntime.android", Layer.AI_RUNTIME, State.NATIVE_DEPENDENCY, "ONNX Runtime Android inference runtime");
        register("onnxruntime.cpu", Layer.AI_RUNTIME, State.NATIVE_DEPENDENCY, "ONNX Runtime CPU execution provider");
        register("onnxruntime.xnnpack", Layer.AI_RUNTIME, State.NATIVE_DEPENDENCY, "ONNX Runtime XNNPACK execution provider");
        register("onnxruntime.nnapi", Layer.AI_RUNTIME, State.DEVICE_REQUIRED, "ONNX Runtime NNAPI execution provider");
        register("onnxruntime.qnn", Layer.AI_RUNTIME, State.LICENSE_REVIEW, "ONNX Runtime Qualcomm QNN execution provider");
        register("litert.v2", Layer.AI_RUNTIME, State.NATIVE_DEPENDENCY, "Google AI Edge LiteRT CompiledModel inference boundary");
        register("litert.compiledmodel", Layer.AI_RUNTIME, State.NATIVE_DEPENDENCY, "LiteRT CompiledModel accelerator-first inference API");
        register("tensorflow-lite.compat", Layer.AI_RUNTIME, State.ADAPTER_ONLY, "Legacy TensorFlow Lite compatibility lane; prefer LiteRT for new work");
        register("google.ai.edge", Layer.AI_RUNTIME, State.ADAPTER_ONLY, "Google AI Edge family integration boundary");
        register("huawei.hiai", Layer.AI_RUNTIME, State.DEVICE_REQUIRED, "Huawei HiAI device/NPU capability boundary");
        register("paddle-lite.ndk", Layer.AI_RUNTIME, State.ADAPTER_ONLY, "Paddle Lite Android NDK provider boundary");
        register("apache.tvm", Layer.AI_RUNTIME, State.ADAPTER_ONLY, "Apache TVM cross-compiled runtime/provider boundary");
        register("apache.tvm.runtime", Layer.AI_RUNTIME, State.ADAPTER_ONLY, "Apache TVM minimal mobile runtime boundary");
        register("compose.first", Layer.UI, State.NATIVE_DEPENDENCY, "Jetpack Compose-first UI architecture");
        register("material3", Layer.UI, State.NATIVE_DEPENDENCY, "Jetpack Compose Material 3 design system");
        register("render-effect", Layer.RENDERING, Build.VERSION.SDK_INT >= 31 ? State.AVAILABLE : State.DEVICE_REQUIRED, "Android RenderEffect API; runtime guarded by API level");
        register("navigation3", Layer.NAVIGATION, State.NATIVE_DEPENDENCY, "Compose-first Navigation 3 boundary");
    }

    private void register(String id, Layer layer, State state, String role) {
        capabilities.put(id, new Capability(id, layer, state, role));
    }
    public Map<String, Capability> snapshot() { return Collections.unmodifiableMap(capabilities); }
    public Capability require(String id) {
        Capability c = capabilities.get(id);
        if (c == null) throw new IllegalArgumentException("Unknown capability: " + id);
        return c;
    }
    public boolean isUsable(String id) {
        State s = require(id).state();
        return s == State.NATIVE_DEPENDENCY || s == State.AVAILABLE || s == State.ADAPTER_ONLY;
    }
    public boolean isRuntimeVerified(String id) { return require(id).state() == State.AVAILABLE; }
    public boolean isRenderEffectUsable() { return Build.VERSION.SDK_INT >= 31; }
}