package com.biupiu.rndos.data

object ApiConfig {
    // Emulator-only development endpoint. Production callers must inject HTTPS.
    const val DEFAULT_BASE_URL = "http://10.0.2.2:3000"

    fun validateBaseUrl(baseUrl: String, allowInsecureHttp: Boolean): String {
        val normalized = baseUrl.trim().trimEnd('/')
        require(normalized.isNotBlank()) { "API base URL is required" }
        val isHttps = normalized.startsWith("https://", ignoreCase = true)
        val isHttp = normalized.startsWith("http://", ignoreCase = true)
        require(isHttps || (allowInsecureHttp && isHttp)) {
            "Production API endpoints must use HTTPS"
        }
        return normalized
    }
}
