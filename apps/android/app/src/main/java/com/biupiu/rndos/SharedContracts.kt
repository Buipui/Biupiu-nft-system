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

interface BiupiuPlatformAdapter {
    fun secureStore(key: String, value: String): Boolean
    fun secureRead(key: String): String?
    fun cachePut(key: String, value: String): Boolean
    fun cacheGet(key: String): String?
    fun deviceCapability(name: String): Boolean
}

interface BiupiuTransport {
    fun execute(request: BiupiuRequest): BiupiuResponse
}

object BiupiuCoreContract {
    const val CONTRACT_VERSION = "1.0"
    const val API_SCHEMA_VERSION = "1.0"
}
