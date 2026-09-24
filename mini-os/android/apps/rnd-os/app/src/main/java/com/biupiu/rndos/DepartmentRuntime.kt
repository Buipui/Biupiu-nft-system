package com.biupiu.rndos

data class DepartmentRuntimeTarget(
    val route: String,
    val packageName: String,
    val scope: String?
)

data class DepartmentRuntimeState(
    val target: DepartmentRuntimeTarget,
    val canStart: Boolean,
    val reason: String
)

object DepartmentRuntime {
    fun resolve(session: RuntimeSession, route: String): DepartmentRuntimeState {
        if (session.status != "active") {
            return DepartmentRuntimeState(target(route), false, "INACTIVE_ACCOUNT")
        }

        val allowed = route == "RND_OS" || session.entitlements.contains(route)
        return DepartmentRuntimeState(
            target(route),
            allowed,
            if (allowed) "AUTHORIZED" else "NO_ENTITLEMENT"
        )
    }

    private fun target(route: String): DepartmentRuntimeTarget = when (route) {
        "SMART_FARMING" -> DepartmentRuntimeTarget(route, "@biupiu/smart-farming", "SMART_FARMING")
        "SMART_METAL_WORKSHOP" -> DepartmentRuntimeTarget(route, "@biupiu/smart-metallurgy", "SMART_METAL_WORKSHOP")
        "RND_OS" -> DepartmentRuntimeTarget(route, "@biupiu/rnd-os", null)
        else -> DepartmentRuntimeTarget(route, "UNRESOLVED", null)
    }
}
