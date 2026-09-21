package com.biupiu.rndos

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Typography
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

/**
 * Biupiu OS design-system authority.
 *
 * Principle: neutral, premium, legible. Material finish and restrained
 * nature accents provide character; they never replace semantic UI colour.
 */
object BiupiuUiTheme {
    const val DEEP_GREEN = "#0B241B"
    const val DEEP_GREEN_2 = "#102F24"
    const val METALLIC_GOLD = "#C9A227"
    const val GRAPHITE = "#141716"
    const val SOFT_WHITE = "#F4F1E8"

    const val CORNER_SMALL_DP = 10
    const val CORNER_MEDIUM_DP = 16
    const val TOUCH_TARGET_MIN_DP = 48
    const val ANIMATION_FAST_MS = 160
    const val ANIMATION_STANDARD_MS = 240
}

private val BiupiuDarkScheme = darkColorScheme(
    primary = Color(0xFFBFA06B),
    onPrimary = Color(0xFF171A18),
    primaryContainer = Color(0xFF3B3426),
    onPrimaryContainer = Color(0xFFF1EEE6),
    secondary = Color(0xFF8F9A94),
    onSecondary = Color(0xFF171A18),
    secondaryContainer = Color(0xFF303733),
    onSecondaryContainer = Color(0xFFE4E7E3),
    tertiary = Color(0xFF718078),
    onTertiary = Color(0xFF171A18),
    background = Color(0xFF10261F),
    onBackground = Color(0xFFF1EEE6),
    surface = Color(0xFF1B1D1C),
    onSurface = Color(0xFFF1EEE6),
    surfaceVariant = Color(0xFF3A3E3B),
    onSurfaceVariant = Color(0xFFD0D3CE),
    outline = Color(0xFF8D928C),
    error = Color(0xFFD9A6A0),
    onError = Color(0xFF2A1110)
)

@Composable
fun BiupiuUiTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = BiupiuDarkScheme,
        typography = Typography(),
        content = content
    )
}
