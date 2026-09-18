package com.biupiu.rndos.auth

import androidx.lifecycle.ViewModel

class AuthViewModel(private val store: SessionStore = MemorySessionStore()) : ViewModel() {
    var state: SessionState = SessionState(authenticated = store.read() != null)
        private set

    fun setDevelopmentSession(token: String, userId: String, organisationId: String, expiresAt: String) {
        if (token.isBlank() || userId.isBlank() || organisationId.isBlank() || expiresAt.isBlank()) {
            state = state.copy(error = "All session fields are required")
            return
        }
        val session = DevSession(token, userId, organisationId, expiresAt)
        store.save(session)
        state = SessionState(authenticated = true, session = session)
    }

    fun signOut() {
        store.clear()
        state = SessionState()
    }
}
