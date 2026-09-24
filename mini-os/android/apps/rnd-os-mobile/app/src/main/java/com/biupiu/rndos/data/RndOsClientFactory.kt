package com.biupiu.rndos.data

import com.biupiu.rndos.auth.DevSession

object RndOsClientFactory {
    fun create(session: DevSession?): RndOsApi {
        val transport = RndOsHttpTransport(
            baseUrl = ApiConfig.DEFAULT_BASE_URL,
            bearerToken = session?.token
        )
        return RndOsHttpApi(transport)
    }
}
