package com.biupiu.rndos

data class DepartmentLaunchResult(
    val route: String,
    val packageName: String,
    val started: Boolean,
    val reason: String
)

object DepartmentLauncher {
    fun launch(session: RuntimeSession, route: String): DepartmentLaunchResult {
        val runtime = DepartmentRuntime.resolve(session, route)
        return DepartmentLaunchResult(
            route,
            runtime.target.packageName,
            runtime.canStart,
            if (runtime.canStart) "STARTED" else runtime.reason
        )
    }
}
