package com.biupiu.minios.federation;

import java.util.EnumSet;
import java.util.Collections;
import java.util.Set;

/**
 * Provider-neutral OpenDroid federation boundary.
 *
 * OpenDroid is an autonomous Android agent, not a standalone UI rendering engine.
 * Its UI surface is Compose-based; automation is AccessibilityService-driven.
 * This adapter records capabilities without importing external application code.
 */
public final class OpenDroidCapabilityAdapter implements ExternalTransportAdapter {
    public enum Module {
        ACCESSIBILITY_AUTOMATION,
        ACTION_DISPATCH,
        AGENT_LOOP,
        LLM_PROVIDER_ROUTING,
        MEMORY,
        SECURITY_KEYSTORE,
        FOREGROUND_SERVICE,
        NOTIFICATION_LISTENER,
        VOICE,
        ROOM_DATABASE,
        DATASTORE_REPOSITORY,
        HILT_DI,
        COMPOSE_UI,
        VIEWMODEL
    }

    private final Set<Module> declaredModules = EnumSet.allOf(Module.class);

    @Override
    public String id() {
        return "opendroid.android-agent";
    }

    public Set<Module> modules() {
        return Collections.unmodifiableSet(EnumSet.copyOf(declaredModules));
    }

    @Override
    public boolean isAvailable() {
        // Source registration is not runtime proof. A real OpenDroid integration
        // requires the external project, dependency/licence review, build and device tests.
        return false;
    }

    @Override
    public String diagnosticState() {
        return "EXTERNAL_AGENT_BOUNDARY; runtime/build/device integration required";
    }
}
