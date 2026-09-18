package com.biupiu.rndos.ai

data class AiRequest(
    val task: String,
    val researchObjectId: String? = null,
    val context: List<String> = emptyList()
)

data class AiResponse(
    val answer: String,
    val evidenceState: String,
    val citations: List<String> = emptyList()
)

interface AiGateway {
    suspend fun ask(request: AiRequest): AiResponse
}
