package com.biupiu.minios.federation;

public final class AndroidCapabilityRegistryTest {
    public static void run() {
        AndroidCapabilityRegistry r = new AndroidCapabilityRegistry();
        if (!r.isUsable("aosp.mainline")) throw new AssertionError("AOSP capability missing");
        if (!r.isUsable("android.auto.projection")) throw new AssertionError("Android Auto capability missing");
        if (r.isUsable("gsm-flags-2.0")) throw new AssertionError("Unresolved capability must fail closed");
        if (r.isUsable("vector.automotive.sil-hil")) throw new AssertionError("Licensed external framework must remain licence-gated");
        if (r.isUsable("motorola.ma2.transport")) throw new AssertionError("Physical accessory must fail closed without hardware");
        if (!r.isUsable("godot.renderingdevice")) throw new AssertionError("Godot adapter capability missing");
        if (!r.isUsable("vulkan.android-runtime")) throw new AssertionError("Vulkan adapter capability missing");
        if (r.isUsable("vulkan.validation")) throw new AssertionError("Validation layer must remain device-gated");

        String[] federated = {
            "armv8.2.fp16", "arm.neon", "opencl.compute",
            "model.qwen", "model.deepseek", "model.llama", "model.gemma",
            "tencent.ncnn", "megvii.megcc", "megvii.megengine",
            "alibaba.tinynn", "rockchip.rknn",
            "android.appfunctions-mcp", "android.aicore",
            "pytorch.executorch", "pytorch.core", "yandex.catboost",
            "dace.data-centric", "menpo", "cupy", "fastnlp",
            "iqm.quantum-sdk", "riken.quantum-simulator", "fujitsu.quantum-simulator",
            "android.agsl"
        };
        for (String id : federated) {
            if (!r.isUsable(id)) throw new AssertionError("Federated adapter missing: " + id);
        }

        if (r.isUsable("huawei.kirin.npu")) throw new AssertionError("Kirin vendor SDK requires licence/device review");
        if (r.isUsable("st.stm32cube-ai")) throw new AssertionError("STM32Cube.AI requires licence/HIL review");
        if (r.isUsable("google.aqt")) throw new AssertionError("AQT historical reference must not become runtime authority");
        if (r.isUsable("opendroid.ui-engine")) throw new AssertionError("Unresolved OpenDroid identifier must fail closed");

        if (new VulkanCapabilityAdapter(null).isAvailable()) {
            throw new AssertionError("Vulkan adapter must fail closed without Android context");
        }

        AndroidAutoTransportAdapter nullContextAdapter = new AndroidAutoTransportAdapter(null);
        if (nullContextAdapter.isAvailable()) throw new AssertionError("Android Auto adapter must not claim live availability");
    }
}
