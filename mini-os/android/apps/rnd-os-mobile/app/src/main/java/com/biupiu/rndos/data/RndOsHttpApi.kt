package com.biupiu.rndos.data

class RndOsHttpApi(private val transport: RndOsHttpTransport) : RndOsApi {
    override suspend fun health(): String = transport.get("/api/health")
    override suspend fun dashboard(): DashboardSnapshot {
        val json = transport.get("/api/dashboard")
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
}
