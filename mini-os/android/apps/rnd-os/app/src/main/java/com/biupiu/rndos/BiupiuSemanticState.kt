package com.biupiu.rndos

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.unit.dp

/** Semantic state is independent from decorative colourways/material finishes. */
enum class BiupiuSemanticState(val label: String) {
    READY("Ready"),
    INFO("Information"),
    WARNING("Warning"),
    ERROR("Error"),
    OFFLINE("Offline")
}

private val Ready = Color(0xFF7E9B82)
private val Info = Color(0xFF8B9CA6)
private val Warning = Color(0xFFC1A36B)
private val Error = Color(0xFFD9A6A0)
private val Offline = Color(0xFF8D928C)

fun BiupiuSemanticState.color(): Color = when (this) {
    BiupiuSemanticState.READY -> Ready
    BiupiuSemanticState.INFO -> Info
    BiupiuSemanticState.WARNING -> Warning
    BiupiuSemanticState.ERROR -> Error
    BiupiuSemanticState.OFFLINE -> Offline
}

@Composable
fun BiupiuSemanticStateIndicator(
    state: BiupiuSemanticState,
    modifier: Modifier = Modifier
) {
    Row(
        modifier = modifier.semantics {
            contentDescription = "System state: " + state.label
        },
        verticalAlignment = Alignment.CenterVertically
    ) {
        Spacer(
            Modifier
                .size(8.dp)
                .background(state.color(), RoundedCornerShape(50))
        )
        Spacer(Modifier.width(8.dp))
        Text(
            text = state.label,
            color = MaterialTheme.colorScheme.onSurface,
            style = MaterialTheme.typography.labelLarge
        )
    }
}
