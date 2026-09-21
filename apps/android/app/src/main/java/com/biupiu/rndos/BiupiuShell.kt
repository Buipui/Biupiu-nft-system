package com.biupiu.rndos

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Build
import androidx.compose.material.icons.filled.Home
import androidx.compose.material.icons.filled.Park
import androidx.compose.material.icons.filled.Settings
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp

/*
 * Gate 25: Biupiu Materiality + Colourway System.
 *
 * "Colourway" is the fashion/product-design term that best matches the
 * requested idea: a deliberate family of colours used across a collection.
 * Biupiu extends that concept into material finishes and nature-derived themes.
 */

private object BiupiuPalette {
    // Core brand anchors retained, but no longer used as the only UI colours.
    val DeepGreen = Color(0xFF08251D)
    val Verdant = Color(0xFF174A36)
    val OxidisedGold = Color(0xFFC79A35)
    val Graphite = Color(0xFF171A18)
    val Porcelain = Color(0xFFF3EFE5)

    // Distinctive colour-wheel families.
    val Copper = Color(0xFFB56A3B)
    val Patina = Color(0xFF3D8B83)
    val MineralBlue = Color(0xFF315D78)
    val Orchid = Color(0xFF76527E)
    val Clay = Color(0xFFA86F50)
    val Lichen = Color(0xFF75854A)
    val Pollen = Color(0xFFD0A83B)
    val Basalt = Color(0xFF242A28)
}

private enum class MaterialFinish(val label: String) {
    AnodisedAluminium("Anodised Aluminium"),
    BrushedTitanium("Brushed Titanium"),
    BioComposite("Bio-Composite"),
    RecycledGlass("Recycled Glass"),
    CarbonWeave("Carbon Weave"),
    LivingStone("Living Stone")
}

private data class MaterialSwatch(
    val finish: MaterialFinish,
    val base: Color,
    val accent: Color,
    val description: String
)

private val workshopMaterials = listOf(
    MaterialSwatch(MaterialFinish.AnodisedAluminium, Color(0xFF4D5B58), BiupiuPalette.Patina, "Cool machined body • subtle directional grain"),
    MaterialSwatch(MaterialFinish.BrushedTitanium, Color(0xFF6A6D68), BiupiuPalette.MineralBlue, "Low-gloss metal • fine radial brushing"),
    MaterialSwatch(MaterialFinish.BioComposite, BiupiuPalette.Verdant, BiupiuPalette.Lichen, "Plant-fibre matrix • natural layered depth"),
    MaterialSwatch(MaterialFinish.RecycledGlass, Color(0xFF344E4A), BiupiuPalette.Pollen, "Translucent mineral character • embedded highlights"),
    MaterialSwatch(MaterialFinish.CarbonWeave, Color(0xFF202522), BiupiuPalette.OxidisedGold, "Technical weave • restrained metallic accent"),
    MaterialSwatch(MaterialFinish.LivingStone, Color(0xFF514B43), BiupiuPalette.Clay, "Earth mineral surface • warm organic undertone")
)

@Composable
fun BiupiuApp() {
    var selected by rememberSaveable { mutableIntStateOf(0) }
    val destinations = listOf("Home", "Lab", "Machine", "System")
    val icons = listOf(Icons.Filled.Home, Icons.Filled.Park, Icons.Filled.Build, Icons.Filled.Settings)

    MaterialTheme {
        Scaffold(
            containerColor = BiupiuPalette.DeepGreen,
            bottomBar = {
                NavigationBar(containerColor = BiupiuPalette.Graphite) {
                    destinations.forEachIndexed { i, label ->
                        NavigationBarItem(
                            selected = selected == i,
                            onClick = { selected = i },
                            icon = { Icon(icons[i], contentDescription = label) },
                            label = { Text(label) }
                        )
                    }
                }
            }
        ) { padding ->
            when (selected) {
                0 -> HomeSurface(Modifier.padding(padding))
                1 -> LabSurface(Modifier.padding(padding))
                2 -> MachineSurface(Modifier.padding(padding))
                else -> SystemSurface(Modifier.padding(padding))
            }
        }
    }
}

@Composable
private fun Header(title: String, subtitle: String) {
    Column(Modifier.fillMaxWidth()) {
        Text("BIUPIU", color = BiupiuPalette.OxidisedGold, style = MaterialTheme.typography.labelLarge)
        Spacer(Modifier.height(4.dp))
        Text(title, color = BiupiuPalette.Porcelain, style = MaterialTheme.typography.headlineMedium)
        Spacer(Modifier.height(4.dp))
        Text(subtitle, color = BiupiuPalette.Porcelain.copy(alpha = .74f))
    }
}

@Composable
private fun HomeSurface(m: Modifier) {
    val cards = listOf(
        "System health" to "Runtime ready • session layer available",
        "Colourway studio" to "Material finishes • nature themes • controlled palette families",
        "Research workspace" to "R&D • simulation • Digital Twin",
        "Verification" to "Evidence-first actions • reversible by design"
    )
    Surface(m.fillMaxSize(), color = BiupiuPalette.DeepGreen) {
        LazyColumn(
            Modifier.fillMaxSize().padding(20.dp),
            verticalArrangement = Arrangement.spacedBy(12.dp)
        ) {
            item { Header("Command Centre", "Premium control built around colour, material and state") }
            item { StatePill("READY", BiupiuPalette.Lichen) }
            items(cards) { (a, b) -> StatusCard(a, b, BiupiuPalette.Verdant) }
        }
    }
}

@Composable
private fun LabSurface(m: Modifier) {
    Surface(m.fillMaxSize(), color = BiupiuPalette.DeepGreen) {
        Column(Modifier.fillMaxSize().padding(20.dp)) {
            Header("Biupiu Lab", "Research • simulation • Digital Twin • materials • geometry")
            Spacer(Modifier.height(20.dp))
            StatusCard("Nature-inspired themes", "Verdant Canopy • Mineral Spring • Fynbos Ember • Forest After Rain", BiupiuPalette.Patina)
            Spacer(Modifier.height(12.dp))
            StatusCard("Validation path", "PROPOSE → SIMULATE → VALIDATE → AUTHORISE → EXECUTE", BiupiuPalette.Orchid)
        }
    }
}

@Composable
private fun MachineSurface(m: Modifier) {
    Surface(m.fillMaxSize(), color = BiupiuPalette.Graphite) {
        LazyColumn(
            Modifier.fillMaxSize().padding(20.dp),
            verticalArrangement = Arrangement.spacedBy(12.dp)
        ) {
            item { Header("Biupiu Workshop", "A material-first interface: machines should feel machined, not generic") }
            item { StatePill("WORKSHOP • MATERIAL PREVIEW", BiupiuPalette.Copper) }
            items(workshopMaterials) { swatch -> MaterialCard(swatch) }
            item { StatusCard("Safety boundary", "Discovery is separated from actuation. Physical control remains gated.", BiupiuPalette.OxidisedGold) }
        }
    }
}

@Composable
private fun SystemSurface(m: Modifier) {
    Surface(m.fillMaxSize(), color = BiupiuPalette.DeepGreen) {
        Column(Modifier.fillMaxSize().padding(20.dp)) {
            Header("Biupiu System", "Security • accounts • storage • network • accessibility")
            Spacer(Modifier.height(20.dp))
            StatusCard("Colourway engine", "Brand colours remain protected; contextual colour families can change by workspace.", BiupiuPalette.MineralBlue)
            Spacer(Modifier.height(12.dp))
            StatusCard("Accessibility", "Material finishes are decorative layers. Text, state and controls retain accessible contrast.", BiupiuPalette.Lichen)
        }
    }
}

@Composable
private fun StatePill(label: String, accent: Color) {
    Row(
        Modifier
            .border(1.dp, accent.copy(alpha = .7f), RoundedCornerShape(50))
            .padding(horizontal = 12.dp, vertical = 7.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        Box(Modifier.size(8.dp).background(accent, RoundedCornerShape(50)))
        Spacer(Modifier.width(8.dp))
        Text(label, color = BiupiuPalette.Porcelain, style = MaterialTheme.typography.labelLarge)
    }
}

@Composable
private fun StatusCard(title: String, detail: String, accent: Color) {
    Card(
        Modifier.fillMaxWidth(),
        shape = RoundedCornerShape(16.dp),
        colors = CardDefaults.cardColors(containerColor = BiupiuPalette.Basalt)
    ) {
        Column(Modifier.padding(16.dp)) {
            Text(title, color = accent, style = MaterialTheme.typography.titleMedium)
            Spacer(Modifier.height(6.dp))
            Text(detail, color = BiupiuPalette.Porcelain)
        }
    }
}

@Composable
private fun MaterialCard(swatch: MaterialSwatch) {
    val finish = swatch.finish
    Card(
        Modifier.fillMaxWidth(),
        shape = RoundedCornerShape(18.dp),
        colors = CardDefaults.cardColors(containerColor = swatch.base)
    ) {
        Box(
            Modifier
                .fillMaxWidth()
                .height(108.dp)
                .background(
                    Brush.linearGradient(
                        listOf(
                            swatch.base,
                            swatch.base.copy(alpha = .78f),
                            swatch.accent.copy(alpha = .36f)
                        )
                    )
                )
                .padding(16.dp)
        ) {
            Column(Modifier.align(Alignment.BottomStart)) {
                Text(finish.label, color = BiupiuPalette.Porcelain, style = MaterialTheme.typography.titleMedium)
                Spacer(Modifier.height(4.dp))
                Text(swatch.description, color = BiupiuPalette.Porcelain.copy(alpha = .78f))
            }
        }
    }
}
