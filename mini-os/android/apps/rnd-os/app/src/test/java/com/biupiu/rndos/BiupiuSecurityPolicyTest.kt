package com.biupiu.rndos

import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class BiupiuSecurityPolicyTest {
    @Test
    fun acceptsActiveSessionWithSubscriberId() {
        val session = RuntimeSession(
            subscriberId = "subscriber-test",
            tier = "RND",
            status = "active",
            entitlements = listOf("RND_OS")
        )
        assertTrue(BiupiuSecurityPolicy.validateRuntimeSession(session))
    }

    @Test
    fun rejectsInactiveSession() {
        val session = RuntimeSession(
            subscriberId = "subscriber-test",
            tier = "RND",
            status = "inactive",
            entitlements = listOf("RND_OS")
        )
        assertFalse(BiupiuSecurityPolicy.validateRuntimeSession(session))
    }

    @Test
    fun rejectsBlankSubscriberId() {
        val session = RuntimeSession(
            subscriberId = "   ",
            tier = "RND",
            status = "active",
            entitlements = listOf("RND_OS")
        )
        assertFalse(BiupiuSecurityPolicy.validateRuntimeSession(session))
    }

    @Test
    fun networkAndBackupPolicyAreFailClosed() {
        assertFalse(BiupiuSecurityPolicy.CLEAR_TEXT_NETWORK_ALLOWED)
        assertFalse(BiupiuSecurityPolicy.BACKUP_SENSITIVE_DATA_ALLOWED)
        assertFalse(BiupiuSecurityPolicy.EXPORTED_DEPARTMENT_ACTIVITIES_ALLOWED)
        assertTrue(BiupiuSecurityPolicy.KEYSTORE_PROVIDER == "AndroidKeyStore")
    }
}
