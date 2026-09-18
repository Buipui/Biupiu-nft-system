package com.biupiu.world

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.biupiu.world.data.ShowcaseRegistry

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { BiupiuWorldApp() }
    }
}

@Composable
fun BiupiuWorldApp() {
    MaterialTheme {
        Scaffold(topBar = { TopAppBar(title = { Text("Biupiu World") }) }) { padding ->
            LazyColumn(
                modifier = Modifier.padding(padding).padding(16.dp),
                verticalArrangement = Arrangement.spacedBy(12.dp)
            ) {
                item { Text("Development Showcase", style = MaterialTheme.typography.headlineSmall) }
                items(ShowcaseRegistry.developments) { showcase ->
                    Card(modifier = Modifier.fillMaxWidth()) {
                        Column(Modifier.padding(16.dp)) {
                            Text(showcase.title, style = MaterialTheme.typography.titleMedium)
                            Text(showcase.department)
                            Text("Scene: " + showcase.scene)
                            Text("Status: " + showcase.status)
                            Text("Claim: " + showcase.claimClass)
                        }
                    }
                }
            }
        }
    }
}
