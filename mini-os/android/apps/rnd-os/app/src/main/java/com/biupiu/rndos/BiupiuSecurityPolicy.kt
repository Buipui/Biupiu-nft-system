package com.biupiu.rndos

/**
 * Central security invariants for the native Android shell.
 * These are policy boundaries; cryptographic material never belongs in source.
 */
object BiupiuSecurityPolicy {
    const val MIN_TLS = "TLS"
    const val KEYSTORE_PROVIDER = "AndroidKeyStore"
    const val CLEAR_TEXT_NETWORK_ALLOWED = false
    const val BACKUP_SENSITIVE_DATA_ALLOWED = false
    const val EXPORTED_DEPARTMENT_ACTIVITIES_ALLOWED = false

    fun validateRuntimeSession(session: RuntimeSession): Boolean =
        session.status == "active" && session.subscriberId.isNotBlank()
}
