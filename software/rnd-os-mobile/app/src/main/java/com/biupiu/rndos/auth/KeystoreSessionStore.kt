package com.biupiu.rndos.auth

import android.content.Context
import android.security.keystore.KeyGenParameterSpec
import android.security.keystore.KeyProperties
import org.json.JSONObject
import java.nio.charset.StandardCharsets
import java.security.KeyStore
import javax.crypto.Cipher
import javax.crypto.KeyGenerator
import javax.crypto.SecretKey
import javax.crypto.spec.GCMParameterSpec

class KeystoreSessionStore(context: Context) : SessionStore {
    private val preferences = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
    private val keyStore = KeyStore.getInstance(ANDROID_KEYSTORE).apply { load(null) }

    override fun read(): DevSession? {
        val ciphertext = preferences.getString(KEY_CIPHERTEXT, null) ?: return null
        val iv = preferences.getString(KEY_IV, null) ?: return null
        return runCatching {
            val cipher = Cipher.getInstance(TRANSFORMATION)
            cipher.init(Cipher.DECRYPT_MODE, secretKey(), GCMParameterSpec(128, decode(iv)))
            val json = String(cipher.doFinal(decode(ciphertext)), StandardCharsets.UTF_8)
            val obj = JSONObject(json)
            DevSession(obj.getString("token"), obj.getString("userId"), obj.getString("organisationId"), obj.getString("expiresAt"))
        }.getOrNull()
    }

    override fun save(session: DevSession) {
        val json = JSONObject()
            .put("token", session.token)
            .put("userId", session.userId)
            .put("organisationId", session.organisationId)
            .put("expiresAt", session.expiresAt)
            .toString()
        val cipher = Cipher.getInstance(TRANSFORMATION)
        cipher.init(Cipher.ENCRYPT_MODE, secretKey())
        preferences.edit()
            .putString(KEY_CIPHERTEXT, encode(cipher.doFinal(json.toByteArray(StandardCharsets.UTF_8))))
            .putString(KEY_IV, encode(cipher.iv))
            .apply()
    }

    override fun clear() {
        preferences.edit().remove(KEY_CIPHERTEXT).remove(KEY_IV).apply()
    }

    private fun secretKey(): SecretKey {
        (keyStore.getKey(KEY_ALIAS, null) as? SecretKey)?.let { return it }
        val generator = KeyGenerator.getInstance(KeyProperties.KEY_ALGORITHM_AES, ANDROID_KEYSTORE)
        generator.init(
            KeyGenParameterSpec.Builder(
                KEY_ALIAS,
                KeyProperties.PURPOSE_ENCRYPT or KeyProperties.PURPOSE_DECRYPT
            ).setBlockModes(KeyProperties.BLOCK_MODE_GCM)
             .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
             .setUserAuthenticationRequired(false)
             .build()
        )
        return generator.generateKey()
    }

    private fun encode(value: ByteArray) = android.util.Base64.encodeToString(value, android.util.Base64.NO_WRAP)
    private fun decode(value: String) = android.util.Base64.decode(value, android.util.Base64.NO_WRAP)

    private companion object {
        const val ANDROID_KEYSTORE = "AndroidKeyStore"
        const val KEY_ALIAS = "biupiu.rndos.session.aes"
        const val TRANSFORMATION = "AES/GCM/NoPadding"
        const val PREFS_NAME = "biupiu_rndos_secure_session"
        const val KEY_CIPHERTEXT = "ciphertext"
        const val KEY_IV = "iv"
    }
}