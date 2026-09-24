package com.biupiu.rndos.ai

/**
 * Android-side contract for the authenticated AI gateway.
 * Networking implementation is intentionally deferred until the server
 * API base URL, production identity provider and certificate strategy are fixed.
 */
interface AiGatewayClient {
    suspend fun ask(
        bearerToken: String,
        request: AiRequest
    ): AiResponse
}
