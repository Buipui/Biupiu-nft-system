package com.biupiu.rndos

data class BiupiuRequest(
    val id: String,
    val route: String,
    val payload: Map<String, String> = emptyMap()
)

data class BiupiuResponse(
    val requestId: String,
    val success: Boolean,
    val code: String,
    val message: String,
    val data: Map<String, String> = emptyMap()
)

enum class AdapterLifecycle {
    UNCONFIGURED,
    INACTIVE,
    ACTIVE,
    ERROR,
    FINALIZED
}

data class HardwareSample(
    val capabilityId: String,
    val timestampEpochMs: Long,
    val values: Map<String, Double>,
    val quality: String = "UNKNOWN",
    val unitMap: Map<String, String> = emptyMap()
)

interface BiupiuPlatformAdapter {
    fun secureStore(key: String, value: String): Boolean
    fun secureRead(key: String): String?
    fun cachePut(key: String, value: String): Boolean
    fun cacheGet(key: String): String?
    fun deviceCapability(name: String): Boolean

    fun adapterState(): AdapterLifecycle = AdapterLifecycle.UNCONFIGURED
    fun discoverHardware(): List<HardwareCapability> = emptyList()
    fun readHardware(capabilityId: String): HardwareSample? = null
    fun writeHardware(capabilityId: String, command: Map<String, String>): Boolean = false
}

interface BiupiuTransport {
    fun execute(request: BiupiuRequest): BiupiuResponse
}

object BiupiuCoreContract {
    const val CONTRACT_VERSION = "1.1"
    const val API_SCHEMA_VERSION = "1.1"
}

object BiupiuHardwareContract {
    const val CAPABILITY_SCHEMA_VERSION = "1.0"
    const val TELEMETRY_SCHEMA_VERSION = "1.0"
}
