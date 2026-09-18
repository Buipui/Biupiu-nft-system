package com.biupiu.rndos.data

interface RndOsApi {
    suspend fun health(): String
    suspend fun dashboard(): DashboardSnapshot
}

data class DashboardSnapshot(
    val projects: Int = 0,
    val research: Int = 0,
    val hypotheses: Int = 0,
    val experiments: Int = 0,
    val failures: Int = 0,
    val ip: Int = 0,
    val relationships: Int = 0
)

data class ApiError(val statusCode: Int? = null, val message: String, val retryable: Boolean = false)

class RndOsHttpApi(
    private val baseUrl: String,
    private val bearerToken: String? = null
) : RndOsApi {
    override suspend fun health(): String = request("/api/health")
    override suspend fun dashboard(): DashboardSnapshot {
        val json = request("/api/dashboard")
        fun value(key: String): Int {
            val marker = "\"" + key + "\""
            val start = json.indexOf(marker)
            if (start < 0) return 0
            val colon = json.indexOf(':', start)
            if (colon < 0) return 0
            return json.substring(colon + 1).trim().takeWhile { it.isDigit() }.toIntOrNull() ?: 0
        }
        return DashboardSnapshot(value("projects"), value("research"), value("hypotheses"), value("experiments"), value("failures"), value("ip"), value("relationships"))
    }
    private suspend fun request(path: String): String {
        throw UnsupportedOperationException("HTTP transport adapter is isolated for the next Android implementation gate.")
    }
}
