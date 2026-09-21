package com.biupiu.rndos

/** Curated OEM resource classes discovered through public developer/community research.
 * XDA is treated as a discovery/reference channel; vendor SDKs and licenses remain authoritative.
 */
enum class OemResourceClass {
    DEVICE_TREE_REFERENCE,
    KERNEL_SOURCE_REFERENCE,
    VENDOR_HAL_REFERENCE,
    POWER_BACKGROUND_BEHAVIOUR,
    CAMERA_MEDIA_STACK,
    CONNECTIVITY_BLUETOOTH_WIFI,
    USB_DEVICE_MODE,
    NFC_SECURE_ELEMENT,
    SENSOR_HARDWARE,
    BOOT_RECOVERY_REFERENCE,
    GMS_ALTERNATIVE_DISTRIBUTION,
    OEM_SECURITY_ATTESTATION
}

data class OemResourceModule(
    val family: OemFamily,
    val resourceClass: OemResourceClass,
    val adapterBoundary: String,
    val validationRequired: Boolean = true
)

object OemResourceRegistry {
    val modules = OemCompatibilityRegistry.profiles.flatMap { profile ->
        listOf(
            OemResourceModule(profile.family, OemResourceClass.POWER_BACKGROUND_BEHAVIOUR, "OemCompatibilityProfile"),
            OemResourceModule(profile.family, OemResourceClass.CONNECTIVITY_BLUETOOTH_WIFI, "HardwareCapabilityRegistry")
        )
    } + listOf(
        OemResourceModule(OemFamily.GENERIC_ANDROID, OemResourceClass.DEVICE_TREE_REFERENCE, "PlatformTarget"),
        OemResourceModule(OemFamily.GENERIC_ANDROID, OemResourceClass.KERNEL_SOURCE_REFERENCE, "PlatformTarget"),
        OemResourceModule(OemFamily.GENERIC_ANDROID, OemResourceClass.VENDOR_HAL_REFERENCE, "BiupiuPlatformAdapter"),
        OemResourceModule(OemFamily.GENERIC_ANDROID, OemResourceClass.CAMERA_MEDIA_STACK, "HardwareCapabilityRegistry"),
        OemResourceModule(OemFamily.GENERIC_ANDROID, OemResourceClass.USB_DEVICE_MODE, "HardwareCapabilityRegistry"),
        OemResourceModule(OemFamily.GENERIC_ANDROID, OemResourceClass.NFC_SECURE_ELEMENT, "HardwareCapabilityRegistry"),
        OemResourceModule(OemFamily.GENERIC_ANDROID, OemResourceClass.SENSOR_HARDWARE, "HardwareCapabilityRegistry"),
        OemResourceModule(OemFamily.GENERIC_ANDROID, OemResourceClass.BOOT_RECOVERY_REFERENCE, "PlatformTarget"),
        OemResourceModule(OemFamily.HUAWEI, OemResourceClass.GMS_ALTERNATIVE_DISTRIBUTION, "DistributionShell"),
        OemResourceModule(OemFamily.GENERIC_ANDROID, OemResourceClass.OEM_SECURITY_ATTESTATION, "SecureSession")
    )
}
