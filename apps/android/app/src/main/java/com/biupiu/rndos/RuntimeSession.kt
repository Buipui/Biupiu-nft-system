package com.biupiu.rndos

data class RuntimeSession(
    val client: String = "android",
    val subscriberId: String,
    val tier: String,
    val status: String,
    val entitlements: List<String>
)

data class RuntimeRouteState(
    val route: String,
    val enterable: Boolean,
    val reason: String
)

object BiupiuRuntime {
    fun resolveRoute(session: RuntimeSession, route: String): RuntimeRouteState {
        if (session.status != "active") {
            return RuntimeRouteState(route, false, "INACTIVE_ACCOUNT")
        }
        if (route == "MAIN_HUB" || route == "RND_OS") {
            return RuntimeRouteState(route, true, "AUTHORIZED")
        }
        val entitlement = when (route) {
            "SMART_FARMING" -> "SMART_FARMING"
            "SMART_METAL_WORKSHOP" -> "SMART_METAL_WORKSHOP"
            else -> return RuntimeRouteState(route, false, "NO_ENTITLEMENT")
        }
        return RuntimeRouteState(
            route,
            session.entitlements.contains(entitlement),
            if (session.entitlements.contains(entitlement)) "AUTHORIZED" else "NO_ENTITLEMENT"
        )
    }
}
