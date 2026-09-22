package com.biupiu.minios.federation;

import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.Map;

public final class AndroidCapabilityRegistry {
    public enum State { AVAILABLE, ADAPTER_ONLY, DEVICE_REQUIRED, LICENSE_REVIEW, HISTORICAL_REFERENCE, UNRESOLVED }

    private final Map<String, State> capabilities = new LinkedHashMap<>();

    public AndroidCapabilityRegistry() {
        capabilities.put("aosp.mainline", State.AVAILABLE);
        capabilities.put("pixel.gki.vendor-separation", State.ADAPTER_ONLY);
        capabilities.put("android.auto.projection", State.AVAILABLE);
        capabilities.put("motorola.ma2.transport", State.DEVICE_REQUIRED);
        capabilities.put("aawireless.two.transport", State.DEVICE_REQUIRED);
        capabilities.put("carlinkit.2air.transport", State.DEVICE_REQUIRED);
        capabilities.put("vector.automotive.sil-hil", State.LICENSE_REVIEW);
        capabilities.put("lsposed.art-instrumentation", State.LICENSE_REVIEW);
        capabilities.put("gsm-flags-2.0", State.UNRESOLVED);
        capabilities.put("godot.renderingdevice", State.ADAPTER_ONLY);
        capabilities.put("vulkan.android-runtime", State.ADAPTER_ONLY);
        capabilities.put("vulkan.validation", State.DEVICE_REQUIRED);

        // Deep external federation: CPU/GPU/model/NPU/ML providers.
        capabilities.put("armv8.2.fp16", State.ADAPTER_ONLY);
        capabilities.put("arm.neon", State.ADAPTER_ONLY);
        capabilities.put("opencl.compute", State.ADAPTER_ONLY);
        capabilities.put("model.qwen", State.ADAPTER_ONLY);
        capabilities.put("model.deepseek", State.ADAPTER_ONLY);
        capabilities.put("model.llama", State.ADAPTER_ONLY);
        capabilities.put("model.gemma", State.ADAPTER_ONLY);
        capabilities.put("tencent.ncnn", State.ADAPTER_ONLY);
        capabilities.put("megvii.megcc", State.ADAPTER_ONLY);
        capabilities.put("megvii.megengine", State.ADAPTER_ONLY);
        capabilities.put("alibaba.tinynn", State.ADAPTER_ONLY);
        capabilities.put("huawei.kirin.npu", State.LICENSE_REVIEW);
        capabilities.put("rockchip.rknn", State.ADAPTER_ONLY);
        capabilities.put("android.appfunctions-mcp", State.ADAPTER_ONLY);
        capabilities.put("android.aicore", State.ADAPTER_ONLY);
        capabilities.put("pytorch.executorch", State.ADAPTER_ONLY);
        capabilities.put("pytorch.core", State.ADAPTER_ONLY);
        capabilities.put("st.stm32cube-ai", State.LICENSE_REVIEW);
        capabilities.put("yandex.catboost", State.ADAPTER_ONLY);
        capabilities.put("dace.data-centric", State.ADAPTER_ONLY);
        capabilities.put("menpo", State.ADAPTER_ONLY);
        capabilities.put("cupy", State.ADAPTER_ONLY);
        capabilities.put("fastnlp", State.ADAPTER_ONLY);

        // Quantum/simulation and graphics.
        capabilities.put("google.aqt", State.HISTORICAL_REFERENCE);
        capabilities.put("iqm.quantum-sdk", State.ADAPTER_ONLY);
        capabilities.put("riken.quantum-simulator", State.ADAPTER_ONLY);
        capabilities.put("fujitsu.quantum-simulator", State.ADAPTER_ONLY);
        capabilities.put("android.agsl", State.ADAPTER_ONLY);
        capabilities.put("opendroid.ui-engine", State.UNRESOLVED);
    }

    public Map<String, State> snapshot() {
        return Collections.unmodifiableMap(capabilities);
    }

    public boolean isUsable(String capability) {
        State s = capabilities.get(capability);
        return s == State.AVAILABLE || s == State.ADAPTER_ONLY;
    }
}
