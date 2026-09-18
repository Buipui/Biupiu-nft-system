package com.biupiu.rndos.data

import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertTrue

class RndOsHttpTransportTest {
    @Test
    fun apiExceptionCarriesStatusCode() {
        val error = RndOsApiException(401, "Unauthorized")
        assertEquals(401, error.statusCode)
        assertTrue(error.message!!.contains("Unauthorized"))
    }
}