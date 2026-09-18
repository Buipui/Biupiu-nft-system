package com.biupiu.world

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.material3.*
import androidx.compose.runtime.Composable

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { BiupiuWorldApp() }
    }
}

@Composable
fun BiupiuWorldApp() {
    MaterialTheme {
        Surface {
            Text("Biupiu World — Showcase Foundation")
        }
    }
}
