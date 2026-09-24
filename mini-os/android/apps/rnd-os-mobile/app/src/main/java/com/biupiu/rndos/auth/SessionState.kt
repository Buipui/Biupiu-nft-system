package com.biupiu.rndos.auth

data class SessionState(
    val authenticated: Boolean = false,
    val session: DevSession? = null,
    val error: String? = null
)
