package com.biupiu.rndos

enum class OemFamily {
    GOOGLE,
    SAMSUNG,
    XIAOMI,
    OPPO,
    VIVO,
    ONEPLUS,
    MOTOROLA,
    HUAWEI,
    GENERIC_ANDROID
}

data class OemCompatibilityProfile(
    val family: OemFamily,
    val baseline: String,
    val customApiBoundary: Boolean,
    val notes: String
)

/**
 * OEM differences are treated as adapter/profile concerns.
 * The common Biupiu capability contract remains vendor-neutral.
 */
object OemCompatibilityRegistry {
    val profiles = listOf(
        OemCompatibilityProfile(OemFamily.GOOGLE, "Android API baseline", false, "Reference Android behaviour"),
        OemCompatibilityProfile(OemFamily.SAMSUNG, "Android API baseline", true, "Enterprise/custom APIs isolated behind adapter"),
        OemCompatibilityProfile(OemFamily.XIAOMI, "Android API baseline", true, "OEM power/background behaviour must be profiled"),
        OemCompatibilityProfile(OemFamily.OPPO, "Android API baseline", true, "OEM power/background behaviour must be profiled"),
        OemCompatibilityProfile(OemFamily.VIVO, "Android API baseline", true, "OEM power/background behaviour must be profiled"),
        OemCompatibilityProfile(OemFamily.ONEPLUS, "Android API baseline", true, "OEM power/background behaviour must be profiled"),
        OemCompatibilityProfile(OemFamily.MOTOROLA, "Android API baseline", false, "Validate device-specific hardware permissions"),
        OemCompatibilityProfile(OemFamily.HUAWEI, "Android API baseline", true, "Validate non-GMS distribution and device services"),
        OemCompatibilityProfile(OemFamily.GENERIC_ANDROID, "Android API baseline", true, "Best-effort compatibility; capability discovery required")
    )
}
