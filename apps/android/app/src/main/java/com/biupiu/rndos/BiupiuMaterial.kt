package com.biupiu.rndos

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp

/**
 * Lightweight material language for Biupiu OS.
 *
 * This is a procedural visual approximation, not physically based rendering.
 * Keep the effect quiet: finish should communicate quality without competing
 * with information.
 */
enum class BiupiuMaterial {
    ANODISED_ALUMINIUM,
    BRUSHED_TITANIUM,
    BIO_COMPOSITE,
    RECYCLED_GLASS,
    CARBON_WEAVE,
    LIVING_STONE
}

private data class MaterialSpec(
    val base: Color,
    val highlight: Color,
    val label: String
)

private fun BiupiuMaterial.spec(): MaterialSpec = when (this) {
    BiupiuMaterial.ANODISED_ALUMINIUM ->
        MaterialSpec(Color(0xFFA6AAA5), Color(0xFFD7DAD5), "Anodised Aluminium")
    BiupiuMaterial.BRUSHED_TITANIUM ->
        MaterialSpec(Color(0xFF70736F), Color(0xFFB7BBB6), "Brushed Titanium")
    BiupiuMaterial.BIO_COMPOSITE ->
        MaterialSpec(Color(0xFF465449), Color(0xFF738477), "Bio-Composite")
    BiupiuMaterial.RECYCLED_GLASS ->
        MaterialSpec(Color(0xFF68736F), Color(0xFFAAB5AF), "Recycled Glass")
    BiupiuMaterial.CARBON_WEAVE ->
        MaterialSpec(Color(0xFF242826), Color(0xFF565C57), "Carbon Weave")
    BiupiuMaterial.LIVING_STONE ->
        MaterialSpec(Color(0xFF666057), Color(0xFFA49B89), "Living Stone")
}

@Composable
fun BiupiuMaterialSurface(
    material: BiupiuMaterial,
    modifier: Modifier = Modifier,
    showLabel: Boolean = true
) {
    val spec = material.spec()
    Box(
        modifier
            .fillMaxWidth()
            .height(92.dp)
            .background(
                Brush.linearGradient(
                    listOf(spec.base, spec.highlight.copy(alpha = 0.42f), spec.base)
                )
            )
            .padding(16.dp)
    ) {
        if (showLabel) {
            Text(
                text = spec.label,
                color = MaterialTheme.colorScheme.onSurface,
                style = MaterialTheme.typography.titleMedium
            )
        }
    }
}
