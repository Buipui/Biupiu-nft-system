package com.biupiu.rndos

object CapabilityRouter {
    fun route(session: RuntimeSession, capability: String): RuntimeRouteState {
        val direct = BiupiuRuntime.resolveRoute(session, capability)
        if (direct.enterable) return direct

        val registered = CapabilityRegistry.core.any { it.id == capability }
        return if (registered) {
            RuntimeRouteState(capability, false, "REGISTERED_NOT_ENTITLED")
        } else {
            RuntimeRouteState(capability, false, "UNKNOWN_CAPABILITY")
        }
    }
}
