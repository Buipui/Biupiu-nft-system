package com.biupiu.minios.federation;

import android.content.Context;
import android.content.pm.PackageManager;

/**
 * Native capability boundaries for external graphics/engine federation.
 *
 * Godot remains an engine/provider boundary; this class does not embed Godot.
 * Vulkan availability is queried from the Android platform at runtime.
 */
public final class GraphicsCapabilityAdapters {
    private GraphicsCapabilityAdapters() {}

    public static ExternalTransportAdapter godotRenderingDevice() {
        return new ExternalTransportAdapter() {
            @Override public String id() { return "godot.renderingdevice"; }

            @Override public boolean isAvailable() {
                // Engine/runtime presence is not established by the native Mini OS source tree.
                return false;
            }

            @Override public String diagnosticState() {
                return "ENGINE_RUNTIME_REQUIRED; Godot RenderingDevice is an external provider boundary";
            }
        };
    }
}

/** Android Vulkan capability query. */
final class VulkanCapabilityAdapter implements ExternalTransportAdapter {
    private final Context context;

    VulkanCapabilityAdapter(Context context) {
        this.context = context == null ? null : context.getApplicationContext();
    }

    @Override public String id() {
        return "vulkan.android-runtime";
    }

    @Override public boolean isAvailable() {
        if (context == null) return false;
        PackageManager pm = context.getPackageManager();
        return pm != null
                && pm.hasSystemFeature(PackageManager.FEATURE_VULKAN_HARDWARE_LEVEL);
    }

    @Override public String diagnosticState() {
        if (context == null) {
            return "RUNTIME_REQUIRED; Android context unavailable; Vulkan support not claimed";
        }
        return isAvailable()
                ? "DEVICE_CAPABILITY_DETECTED; Vulkan hardware feature reported by Android"
                : "DEVICE_CAPABILITY_ABSENT; Vulkan hardware feature not reported by Android";
    }
}

/**
 * Validation-layer capability is intentionally not used as a production renderer
 * availability signal. Actual validation-layer discovery belongs to the debug/test
 * environment and must not alter renderer authority.
 */
final class VulkanValidationAdapter implements ExternalTransportAdapter {
    @Override public String id() {
        return "vulkan.validation";
    }

    @Override public boolean isAvailable() {
        return false;
    }

    @Override public String diagnosticState() {
        return "DIAGNOSTIC_ONLY; validation-layer runtime evidence must come from a debug/test execution";
    }
}
