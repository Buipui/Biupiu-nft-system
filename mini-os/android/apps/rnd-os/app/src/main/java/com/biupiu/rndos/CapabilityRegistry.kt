package com.biupiu.rndos

data class Capability(
    val id: String,
    val minimumTier: String,
    val nativeRequired: Boolean,
    val platformNotes: String
)

object CapabilityRegistry {
    val core = listOf(
        Capability("RND_OS", "CORE", false, "Shared runtime contract"),
        Capability("SMART_FARMING", "FARMING", false, "Department capability surface"),
        Capability("SMART_METAL_WORKSHOP", "ADVANCED", false, "Department capability surface"),
        Capability("DIGITAL_TWIN", "ADVANCED", true, "Rendering/3D adapter required"),
        Capability("SECURE_SESSION", "CORE", true, "Android Keystore; platform-specific secure storage elsewhere"),
        Capability("OFFLINE_CACHE", "CORE", false, "Shared data contract; platform storage adapter"),
        Capability("DIAGNOSTICS", "CORE", false, "Structured errors and health state"),
        Capability("MULTILINGUAL", "CORE", false, "Shared locale/message contract")
    )

    fun resolve(session: RuntimeSession): List<Capability> =
        core.filter { it.id == "RND_OS" || session.entitlements.contains(it.id) ||
            (it.id == "SECURE_SESSION" && session.status == "active") }
}
