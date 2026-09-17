package com.biupiu.rndos.data

/** API boundary; network implementation is deferred until server auth/session is production-reviewed. */
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
