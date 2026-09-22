package com.biupiu.minios.federation;

import java.util.ArrayList;
import java.util.List;

/** Fail-closed provider selector. Runtime evidence is separate from dependency presence. */
public final class AiProviderSelector {
    private final List<AiExecutionProvider> providers = new ArrayList<>();

    public AiProviderSelector() {
        providers.add(new SimpleProvider("litert.compiledmodel", AiMultimediaUiFederationRegistry.State.NATIVE_DEPENDENCY));
        providers.add(new SimpleProvider("onnxruntime.cpu", AiMultimediaUiFederationRegistry.State.NATIVE_DEPENDENCY));
        providers.add(new SimpleProvider("onnxruntime.nnapi", AiMultimediaUiFederationRegistry.State.DEVICE_REQUIRED));
        providers.add(new SimpleProvider("onnxruntime.qnn", AiMultimediaUiFederationRegistry.State.LICENSE_REVIEW));
        providers.add(new SimpleProvider("apache.tvm.runtime", AiMultimediaUiFederationRegistry.State.ADAPTER_ONLY));
        providers.add(new SimpleProvider("huawei.hiai", AiMultimediaUiFederationRegistry.State.DEVICE_REQUIRED));
        providers.add(new SimpleProvider("paddle-lite.ndk", AiMultimediaUiFederationRegistry.State.ADAPTER_ONLY));
    }

    public List<String> candidates(String workload) {
        List<String> result = new ArrayList<>();
        for (AiExecutionProvider provider : providers) {
            if (provider.supports(workload) &&
                (provider.state() == AiMultimediaUiFederationRegistry.State.NATIVE_DEPENDENCY ||
                 provider.state() == AiMultimediaUiFederationRegistry.State.AVAILABLE ||
                 provider.state() == AiMultimediaUiFederationRegistry.State.ADAPTER_ONLY)) {
                result.add(provider.id());
            }
        }
        return result;
    }

    private static final class SimpleProvider implements AiExecutionProvider {
        private final String id;
        private final AiMultimediaUiFederationRegistry.State state;
        SimpleProvider(String id, AiMultimediaUiFederationRegistry.State state) {
            this.id = id;
            this.state = state;
        }
        public String id() { return id; }
        public AiMultimediaUiFederationRegistry.State state() { return state; }
        public boolean supports(String workload) { return workload != null && !workload.isBlank(); }
    }
}
