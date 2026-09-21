package com.biupiu.rndos

/**
 * Foreign/OEM resource intelligence is metadata-first. It records reusable
 * interface patterns and provenance without importing vendor blobs, dumps,
 * proprietary assets, or unverified third-party code.
 */
enum class ResourceEvidenceClass {
    OFFICIAL_OEM,
    AOSP,
    LINEAGE_DEVICE_TREE,
    FOREIGN_LANGUAGE_REPOSITORY,
    XDA_DISCOVERY,
    OPENBOOKS_KNOWLEDGE,
    GITHUB_REFERENCE
}

enum class ResourceUse {
    DEVICE_TREE,
    VINTF_CONTRACT,
    PARTITION_BOUNDARY,
    HAL_ADAPTER,
    KERNEL_REFERENCE,
    PROPRIETARY_EXTRACTION_MANIFEST,
    LOCALISATION,
    AUDIT_PROVENANCE,
    IDEMPOTENT_WORKFLOW,
    MAINLINE_PORTABILITY
}

data class ForeignResourceModule(
    val id: String,
    val evidenceClass: ResourceEvidenceClass,
    val languages: Set<String>,
    val uses: Set<ResourceUse>,
    val authority: String,
    val integrationBoundary: String,
    val licenseOrPermissionRequired: Boolean = true,
    val runtimeVerified: Boolean = false
)

object ForeignResourceRegistry {
    val modules = listOf(
        ForeignResourceModule("aosp-treble-vintf", ResourceEvidenceClass.AOSP, setOf("en"), setOf(ResourceUse.VINTF_CONTRACT, ResourceUse.PARTITION_BOUNDARY, ResourceUse.HAL_ADAPTER), "Android Open Source Project", "platform-neutral vendor/system contract"),
        ForeignResourceModule("lineage-device-tree-and-extraction", ResourceEvidenceClass.LINEAGE_DEVICE_TREE, setOf("en"), setOf(ResourceUse.DEVICE_TREE, ResourceUse.PROPRIETARY_EXTRACTION_MANIFEST, ResourceUse.KERNEL_REFERENCE), "LineageOS project", "OEM adapter metadata; no blobs"),
        ForeignResourceModule("xiaomi-foreign-device-tree-patterns", ResourceEvidenceClass.FOREIGN_LANGUAGE_REPOSITORY, setOf("zh", "en"), setOf(ResourceUse.DEVICE_TREE, ResourceUse.PARTITION_BOUNDARY, ResourceUse.PROPRIETARY_EXTRACTION_MANIFEST, ResourceUse.KERNEL_REFERENCE), "public repository; validate against OEM/AOSP", "reference-only device profile"),
        ForeignResourceModule("sony-open-device-patterns", ResourceEvidenceClass.FOREIGN_LANGUAGE_REPOSITORY, setOf("en", "ja"), setOf(ResourceUse.DEVICE_TREE, ResourceUse.KERNEL_REFERENCE, ResourceUse.HAL_ADAPTER), "Sony Open Devices / public device trees", "reference-only device profile"),
        ForeignResourceModule("samsung-community-device-patterns", ResourceEvidenceClass.FOREIGN_LANGUAGE_REPOSITORY, setOf("ko", "en"), setOf(ResourceUse.DEVICE_TREE, ResourceUse.KERNEL_REFERENCE), "public community repository; verify against Samsung sources", "reference-only device profile"),
        ForeignResourceModule("xda-discovery-channel", ResourceEvidenceClass.XDA_DISCOVERY, setOf("en", "de", "fr", "es", "it", "pt", "ru", "ja", "ko", "zh"), setOf(ResourceUse.DEVICE_TREE, ResourceUse.HAL_ADAPTER, ResourceUse.KERNEL_REFERENCE), "discovery only", "research lead; never an authority"),
        ForeignResourceModule("openbooks-knowledge-localisation", ResourceEvidenceClass.OPENBOOKS_KNOWLEDGE, setOf("en", "fr", "es", "de", "pt-BR", "zh", "ja", "it"), setOf(ResourceUse.LOCALISATION, ResourceUse.AUDIT_PROVENANCE, ResourceUse.IDEMPOTENT_WORKFLOW), "OpenBooks project only where licensing and scope match", "conceptual workflow/knowledge reference; no code import")
    )
}
