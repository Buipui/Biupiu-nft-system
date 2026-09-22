package com.biupiu.rndos

import java.util.Locale

/**
 * Native Biupiu language-selection contract.
 * BCP-47-compatible locale identity is retained; fallback is deterministic.
 * Translation providers are outside this selector's authority.
 */
data class BiupiuLocale(
    val languageTag: String,
    val displayName: String,
    val supportLevel: String = "SELECTION"
)

object BiupiuLanguageRegistry {
    val supportedTags: Set<String> = setOf(
        "en","af","xh","zu","st","tn","ts","ar","de","fr","es","pt",
        "it","nl","ru","uk","pl","tr","fa","ur","hi","bn","ta","te",
        "kn","ml","mr","gu","pa","si","ne","zh","ja","ko","th","vi",
        "id","ms","fil","sw","am","ha","ig","yo","he","sr","hr","bg",
        "cs","da","fi","el","hu","is","lt","lv","no","ro","sk","sl","sv"
    )

    fun normalise(tag: String): String {
        val cleaned = tag.trim().replace('_','-')
        require(cleaned.isNotEmpty()) { "language tag must not be empty" }
        val locale = Locale.forLanguageTag(cleaned)
        val canonical = locale.toLanguageTag()
        require(canonical != "und") { "unsupported language tag: $tag" }
        return canonical
    }

    fun isSupported(tag: String): Boolean =
        runCatching { normalise(tag).substringBefore('-') in supportedTags }.getOrDefault(false)

    fun fallbackChain(tag: String): List<String> {
        val canonical = normalise(tag)
        val parts = canonical.split('-')
        val result = linkedSetOf(canonical)
        if (parts.size > 1) result += parts.first()
        result += "en"
        return result.toList()
    }

    fun profile(tag: String): BiupiuLocale {
        val canonical = normalise(tag)
        require(isSupported(canonical)) { "unsupported Biupiu locale: $tag" }
        return BiupiuLocale(
            languageTag = canonical,
            displayName = Locale.forLanguageTag(canonical).getDisplayName(Locale.ENGLISH),
            supportLevel = "SELECTION"
        )
    }
}
