package com.biupiu.rndos.auth

data class DevSession(
    val token: String,
    val userId: String,
    val organisationId: String,
    val expiresAt: String
)

interface SessionStore {
    fun read(): DevSession?
    fun save(session: DevSession)
    fun clear()
}

/**
 * Development-only in-memory store.
 * Production must use Android Keystore-backed encrypted storage.
 */
class MemorySessionStore : SessionStore {
    private var session: DevSession? = null
    override fun read(): DevSession? = session
    override fun save(session: DevSession) { this.session = session }
    override fun clear() { session = null }
}
