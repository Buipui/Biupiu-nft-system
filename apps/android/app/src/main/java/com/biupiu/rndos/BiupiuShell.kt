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
 * Biupiu OS visual principle:
 * premium quality through material finish, proportion and restraint.
 * Pagani/Ferrari are reference points for craftsmanship and configuration,
 * not visual templates. Biupiu uses its own neutral colour system.
 */

private object BiupiuPalette {
    val DeepGreen = Color(0xFF10261F)
    val Graphite = Color(0xFF1B1D1C)
    val Graphite2 = Color(0xFF252826)
    val Titanium = Color(0xFF70736F)
    val Aluminium = Color(0xFFA6AAA5)
    val WarmWhite = Color(0xFFF1EEE6)
    val Sand = Color(0xFFC8BFAE)
    val Bronze = Color(0xFF9B7951)
    val Patina = Color(0xFF64766F)
    val Nature = Color(0xFF526255)
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
    MaterialSwatch(MaterialFinish.AnodisedAluminium, BiupiuPalette.Aluminium, BiupiuPalette.Titanium, "Clean machined surface • restrained directional grain"),
    MaterialSwatch(MaterialFinish.BrushedTitanium, BiupiuPalette.Titanium, BiupiuPalette.Aluminium, "Cool satin metal • fine controlled brushing"),
    MaterialSwatch(MaterialFinish.BioComposite, Color(0xFF465449), BiupiuPalette.Nature, "Plant-fibre character • quiet natural depth"),
    MaterialSwatch(MaterialFinish.RecycledGlass, Color(0xFF68736F), BiupiuPalette.Sand, "Mineral translucency • restrained highlight"),
    MaterialSwatch(MaterialFinish.CarbonWeave, BiupiuPalette.Graphite, BiupiuPalette.Bronze, "Technical weave • subtle metallic edge"),
    MaterialSwatch(MaterialFinish.LivingStone, Color(0xFF666057), BiupiuPalette.Sand, "Mineral surface • warm natural undertone")
)

@Composable
fun BiupiuApp() {
    var selected by rememberSaveable { mutableIntStateOf(0) }
    val destinations = listOf("Home", "Lab", "Workshop", "System")
    val icons = listOf(Icons.Filled.Home, Icons.Filled.Park, Icons.Filled.Build, Icons.Filled.Settings)

    BiupiuUiTheme {
        Scaffold(
            containerColor = MaterialTheme.colorScheme.background,
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
                2 -> WorkshopSurface(Modifier.padding(padding))
                else -> SystemSurface(Modifier.padding(padding))
            }
        }
    }
}

@Composable
private fun Header(title: String, subtitle: String) {
    Column(Modifier.fillMaxWidth()) {
        Text("BIUPIU", color = BiupiuPalette.Bronze, style = MaterialTheme.typography.labelLarge)
        Spacer(Modifier.height(4.dp))
        Text(title, color = MaterialTheme.colorScheme.onBackground, style = MaterialTheme.typography.headlineMedium)
        Spacer(Modifier.height(4.dp))
        Text(subtitle, color = MaterialTheme.colorScheme.onSurfaceVariant)
    }
}

@Composable
private fun HomeSurface(m: Modifier) {
    val cards = listOf(
        "System health" to "Runtime ready • session layer available",
        "Colourway" to "Neutral palettes • material finishes • nature accents",
        "Research workspace" to "R&D • simulation • Digital Twin",
        "Verification" to "Evidence-first actions • reversible by design"
    )
    Surface(m.fillMaxSize(), color = MaterialTheme.colorScheme.background) {
        LazyColumn(
            Modifier.fillMaxSize().padding(20.dp),
            verticalArrangement = Arrangement.spacedBy(12.dp)
        ) {
            item { Header("Command Centre", "Premium through restraint, clarity and material quality") }
            item { StatePill("READY", BiupiuPalette.Nature) }
            items(cards) { (title, detail) -> StatusCard(title, detail, BiupiuPalette.Bronze) }
        }
    }
}

@Composable
private fun LabSurface(m: Modifier) {
    Surface(m.fillMaxSize(), color = MaterialTheme.colorScheme.background) {
        Column(Modifier.fillMaxSize().padding(20.dp)) {
            Header("Biupiu Lab", "Research • simulation • Digital Twin • materials • geometry")
            Spacer(Modifier.height(20.dp))
            StatusCard("Nature themes", "Use nature as a restrained accent family, not as a full-screen colour wash.", BiupiuPalette.Nature)
            Spacer(Modifier.height(12.dp))
            StatusCard("Validation path", "PROPOSE → SIMULATE → VALIDATE → AUTHORISE → EXECUTE", BiupiuPalette.Bronze)
        }
    }
}

@Composable
private fun WorkshopSurface(m: Modifier) {
    Surface(m.fillMaxSize(), color = BiupiuPalette.Graphite) {
        LazyColumn(
            Modifier.fillMaxSize().padding(20.dp),
            verticalArrangement = Arrangement.spacedBy(12.dp)
        ) {
            item { Header("Biupiu Workshop", "Material quality first • simple controls • clear state") }
            item { StatePill("MATERIAL PREVIEW", BiupiuPalette.Bronze) }
            items(workshopMaterials) { MaterialCard(it) }
            item { StatusCard("Safety boundary", "Discovery is separated from actuation. Physical control remains gated.", BiupiuPalette.Bronze) }
        }
    }
}

@Composable
private fun SystemSurface(m: Modifier) {
    Surface(m.fillMaxSize(), color = MaterialTheme.colorScheme.background) {
        Column(Modifier.fillMaxSize().padding(20.dp)) {
            Header("Biupiu System", "Security • accounts • storage • network • accessibility")
            Spacer(Modifier.height(20.dp))
            StatusCard("Design system", "Neutral base + controlled material finish + restrained nature accent.", BiupiuPalette.Bronze)
            Spacer(Modifier.height(12.dp))
            StatusCard("Accessibility", "Finish and decoration never carry meaning alone. Text, state and controls remain explicit.", BiupiuPalette.Nature)
        }
    }
}

@Composable
private fun StatePill(label: String, accent: Color) {
    Row(
        Modifier
            .border(1.dp, accent.copy(alpha = .75f), RoundedCornerShape(50))
            .padding(horizontal = 12.dp, vertical = 7.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        Box(Modifier.size(8.dp).background(accent, RoundedCornerShape(50)))
        Spacer(Modifier.width(8.dp))
        Text(label, color = MaterialTheme.colorScheme.onSurface, style = MaterialTheme.typography.labelLarge)
    }
}

@Composable
private fun StatusCard(title: String, detail: String, accent: Color) {
    Card(
        Modifier.fillMaxWidth(),
        shape = RoundedCornerShape(14.dp),
        colors = CardDefaults.cardColors(containerColor = BiupiuPalette.Graphite2)
    ) {
        Column(Modifier.padding(16.dp)) {
            Text(title, color = accent, style = MaterialTheme.typography.titleMedium)
            Spacer(Modifier.height(6.dp))
            Text(detail, color = BiupiuPalette.WarmWhite)
        }
    }
}

@Composable
private fun MaterialCard(swatch: MaterialSwatch) {
    Card(
        Modifier.fillMaxWidth(),
        shape = RoundedCornerShape(14.dp),
        colors = CardDefaults.cardColors(containerColor = swatch.base)
    ) {
        Column {
            BiupiuMaterialSurface(
                material = when (swatch.finish) {
                    MaterialFinish.AnodisedAluminium -> BiupiuMaterial.ANODISED_ALUMINIUM
                    MaterialFinish.BrushedTitanium -> BiupiuMaterial.BRUSHED_TITANIUM
                    MaterialFinish.BioComposite -> BiupiuMaterial.BIO_COMPOSITE
                    MaterialFinish.RecycledGlass -> BiupiuMaterial.RECYCLED_GLASS
                    MaterialFinish.CarbonWeave -> BiupiuMaterial.CARBON_WEAVE
                    MaterialFinish.LivingStone -> BiupiuMaterial.LIVING_STONE
                },
                showLabel = true
            )
            Text(
                swatch.description,
                color = BiupiuPalette.WarmWhite.copy(alpha = .80f),
                modifier = Modifier.padding(start = 16.dp, end = 16.dp, bottom = 14.dp)
            )
        }
    }
}
