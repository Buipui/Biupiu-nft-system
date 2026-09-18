package com.biupiu.rndos.data

import java.net.HttpURLConnection
import java.net.URL

class RndOsHttpTransport(private val baseUrl: String, private val bearerToken: String? = null) {
    fun get(path: String): String {
        val connection = (URL(baseUrl.trimEnd('/') + path).openConnection() as HttpURLConnection).apply {
            requestMethod = "GET"
            connectTimeout = 5000
            readTimeout = 5000
            setRequestProperty("Accept", "application/json")
            bearerToken?.let { setRequestProperty("Authorization", "Bearer $it") }
        }
        return connection.use {
            val status = it.responseCode
            val stream = if (status in 200..299) it.inputStream else it.errorStream
            val body = stream?.bufferedReader()?.use { reader -> reader.readText() } ?: ""
            if (status !in 200..299) throw RndOsApiException(status, body.ifBlank { "HTTP $status" })
            body
        }
    }
}

class RndOsApiException(val statusCode: Int, message: String) : Exception(message)
