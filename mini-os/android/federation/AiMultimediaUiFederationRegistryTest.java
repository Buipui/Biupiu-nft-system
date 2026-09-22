package com.biupiu.minios.federation;

public final class AiMultimediaUiFederationRegistryTest {
    public static void run() {
        AiMultimediaUiFederationRegistry registry = new AiMultimediaUiFederationRegistry();
        String[] required = {
            "qualcomm.imsdk.2", "qualcomm.qairt", "onnxruntime.android", "litert.v2",
            "tensorflow-lite.compat", "google.ai.edge", "huawei.hiai", "paddle-lite.ndk",
            "apache.tvm", "compose.first", "material3", "render-effect", "navigation3"
        };
        for (String id : required) {
            if (!registry.snapshot().containsKey(id)) throw new AssertionError("Missing capability: " + id);
            if (registry.require(id).role().isBlank()) throw new AssertionError("Missing role: " + id);
        }
        if (registry.isUsable("qualcomm.qairt")) throw new AssertionError("QAIRT must fail closed pending SDK/licence/runtime evidence");
        if (registry.isUsable("huawei.hiai")) throw new AssertionError("HiAI must fail closed pending target-device evidence");
        if (registry.isUsable("qualcomm.imsdk.2")) throw new AssertionError("IMSDK 2.0 is not a generic Android dependency");
        if (!registry.isUsable("onnxruntime.android")) throw new AssertionError("ONNX Runtime source integration missing");
        if (!registry.isUsable("litert.v2")) throw new AssertionError("LiteRT source integration missing");
        if (!registry.isUsable("compose.first")) throw new AssertionError("Compose-first integration missing");
        if (!registry.isUsable("material3")) throw new AssertionError("Material 3 integration missing");
        if (!registry.isUsable("navigation3")) throw new AssertionError("Navigation 3 integration missing");
        if (registry.isRuntimeVerified("onnxruntime.android")) throw new AssertionError("Dependency presence is not runtime verification");
        if (registry.isRuntimeVerified("litert.v2")) throw new AssertionError("Dependency presence is not runtime verification");

        AiProviderSelector selector = new AiProviderSelector();
        if (!selector.candidates("vision").contains("litert.compiledmodel"))
            throw new AssertionError("LiteRT CompiledModel provider missing");
        if (selector.candidates("vision").contains("onnxruntime.qnn"))
            throw new AssertionError("QNN provider crossed licence boundary");
        if (selector.candidates("vision").contains("huawei.hiai"))
            throw new AssertionError("HiAI provider crossed device boundary");
    }
}
