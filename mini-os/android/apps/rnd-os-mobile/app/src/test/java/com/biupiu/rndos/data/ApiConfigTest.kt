package com.biupiu.rndos.data

import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertFailsWith

class ApiConfigTest {
    @Test
    fun developmentHttpEndpointIsAcceptedWhenExplicitlyAllowed() {
        assertEquals(
            "http://10.0.2.2:3000",
            ApiConfig.validateBaseUrl("http://10.0.2.2:3000/", allowInsecureHttp = true)
        )
    }

    @Test
    fun productionRejectsHttp() {
        assertFailsWith<IllegalArgumentException> {
            ApiConfig.validateBaseUrl("http://example.test", allowInsecureHttp = false)
        }
    }

    @Test
    fun productionAcceptsHttps() {
        assertEquals(
            "https://api.example.test",
            ApiConfig.validateBaseUrl("https://api.example.test/", allowInsecureHttp = false)
        )
    }
}
