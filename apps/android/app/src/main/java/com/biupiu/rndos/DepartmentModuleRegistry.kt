package com.biupiu.rndos

data class DepartmentModuleTarget(
    val route: String,
    val packageName: String,
    val launchUri: String,
    val screenId: String
)

object DepartmentModuleRegistry {
    fun resolve(route: String): DepartmentModuleTarget? = when (route) {
        "SMART_FARMING" -> DepartmentModuleTarget(route, "@biupiu/smart-farming", "biupiu://department/smart-farming", "FARMING_WORLD")
        "SMART_METAL_WORKSHOP" -> DepartmentModuleTarget(route, "@biupiu/smart-metallurgy", "biupiu://department/smart-metal-workshop", "METAL_MAKING_WORLD")
        "RND_OS" -> DepartmentModuleTarget(route, "@biupiu/rnd-os", "biupiu://department/rnd-os", "RND_OS_HOME")
        "CREATIVE_AI" -> DepartmentModuleTarget(route, "@biupiu/firefly", "biupiu://department/creative-ai", "CREATIVE_AI_HOME")
        else -> null
    }
}
