package com.biupiu.rndos.auth

import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel

class AuthViewModel(private val store: SessionStore) : ViewModel() {
    var state: SessionState by mutableStateOf(
        SessionState(authenticated = store.read() != null, session = store.read())
    )
        private set

    fun setDevelopmentSession(token: String, userId: String, organisationId: String, expiresAt: String) {
        if (token.isBlank() || userId.isBlank() || organisationId.isBlank() || expiresAt.isBlank()) {
            state = state.copy(error = "All session fields are required")
            return
        }
        val session = DevSession(token.trim(), userId.trim(), organisationId.trim(), expiresAt.trim())
        store.save(session)
        state = SessionState(authenticated = true, session = session)
    }

    fun signOut() {
        store.clear()
        state = SessionState()
    }
}