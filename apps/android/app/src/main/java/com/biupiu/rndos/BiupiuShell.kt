package com.biupiu.rndos

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Build
import androidx.compose.material.icons.filled.Home
import androidx.compose.material.icons.filled.Settings
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp

private val Green = Color(0xFF0B241B)
private val Green2 = Color(0xFF102F24)
private val Gold = Color(0xFFC9A227)
private val White = Color(0xFFF4F1E8)

@Composable
fun BiupiuApp() {
    var selected by rememberSaveable { mutableIntStateOf(0) }
    val destinations = listOf("Home", "Lab", "Machine", "System")
    val icons = listOf(Icons.Filled.Home, Icons.Filled.Build, Icons.Filled.Build, Icons.Filled.Settings)
    MaterialTheme {
        Scaffold(
            containerColor = Green,
            bottomBar = {
                NavigationBar(containerColor = Green2) {
                    destinations.forEachIndexed { i, label ->
                        NavigationBarItem(selected = selected == i, onClick = { selected = i },
                            icon = { Icon(icons[i], contentDescription = label) }, label = { Text(label) })
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

@Composable private fun Header(title: String, subtitle: String) {
    Column(Modifier.fillMaxWidth()) {
        Text("BIUPIU", color = Gold, style = MaterialTheme.typography.labelLarge)
        Spacer(Modifier.height(4.dp))
        Text(title, color = White, style = MaterialTheme.typography.headlineMedium)
        Spacer(Modifier.height(4.dp))
        Text(subtitle, color = White.copy(alpha = .72f))
    }
}

@Composable private fun HomeSurface(m: Modifier) {
    val cards = listOf(
        "System health" to "Runtime ready • session layer available",
        "Research workspace" to "R&D • simulation • Digital Twin",
        "Machine state" to "Hardware discovery boundary registered",
        "Verification" to "Evidence-first actions • reversible by design"
    )
    Surface(m.fillMaxSize(), color = Green) {
        LazyColumn(Modifier.fillMaxSize().padding(20.dp), verticalArrangement = Arrangement.spacedBy(12.dp)) {
            item { Header("Command Centre", "Premium control without hiding system state") }
            item {
                Row(verticalAlignment = Alignment.CenterVertically) {
                    Box(Modifier.size(10.dp).background(Gold, RoundedCornerShape(50)))
                    Spacer(Modifier.width(8.dp))
                    Text("READY", color = Gold, style = MaterialTheme.typography.labelLarge)
                }
            }
            items(cards) { (a, b) -> StatusCard(a, b) }
        }
    }
}

@Composable private fun LabSurface(m: Modifier) {
    Surface(m.fillMaxSize(), color = Green) {
        Column(Modifier.fillMaxSize().padding(20.dp)) {
            Header("Biupiu Lab", "Research • simulation • Digital Twin • materials • geometry")
            Spacer(Modifier.height(20.dp))
            StatusCard("Next action", "Select a research department or simulation workspace.")
            Spacer(Modifier.height(12.dp))
            StatusCard("Validation path", "PROPOSE → SIMULATE → VALIDATE → AUTHORISE → EXECUTE")
        }
    }
}

@Composable private fun MachineSurface(m: Modifier) {
    Surface(m.fillMaxSize(), color = Green) {
        Column(Modifier.fillMaxSize().padding(20.dp)) {
            Header("Biupiu Machine", "Devices • sensors • telemetry • diagnostics")
            Spacer(Modifier.height(20.dp))
            StatusCard("Hardware registry", "USB • BLE • Wi‑Fi • Ethernet • CAN/CAN-FD • serial")
            Spacer(Modifier.height(12.dp))
            StatusCard("Safety boundary", "Discovery is separated from actuation. Physical control remains gated.")
        }
    }
}

@Composable private fun SystemSurface(m: Modifier) {
    Surface(m.fillMaxSize(), color = Green) {
        Column(Modifier.fillMaxSize().padding(20.dp)) {
            Header("Biupiu System", "Security • accounts • storage • network • accessibility")
            Spacer(Modifier.height(20.dp))
            StatusCard("Security", "Secure-session architecture registered.")
            Spacer(Modifier.height(12.dp))
            StatusCard("Accessibility", "Legibility and touch targets are first-class constraints.")
        }
    }
}

@Composable private fun StatusCard(title: String, detail: String) {
    Card(Modifier.fillMaxWidth(), shape = RoundedCornerShape(16.dp),
        colors = CardDefaults.cardColors(containerColor = Green2)) {
        Column(Modifier.padding(16.dp)) {
            Text(title, color = Gold, style = MaterialTheme.typography.titleMedium)
            Spacer(Modifier.height(6.dp))
            Text(detail, color = White)
        }
    }
}
