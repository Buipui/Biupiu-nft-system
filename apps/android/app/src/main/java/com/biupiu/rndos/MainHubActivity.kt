package com.biupiu.rndos

import android.app.Activity
import android.os.Bundle
import android.graphics.Color
import android.widget.LinearLayout
import android.widget.TextView
import android.view.Gravity

class MainHubActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val root = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            gravity = Gravity.CENTER
            setPadding(48, 48, 48, 48)
        }
        root.addView(TextView(this).apply {
            text = "BIUPIU R&D OS"
            textSize = 28f
            gravity = Gravity.CENTER
            setTextColor(Color.BLACK)
        })
        val session = RuntimeSession("local-preview", "PUBLIC", "active", emptyList())
        listOf("SMART_FARMING", "SMART_METAL_WORKSHOP", "RND_OS").forEach { route ->
            val state = BiupiuRuntime.resolveRoute(session, route)
            root.addView(TextView(this).apply {
                text = if (state.enterable) "ENTER  $route" else "LOCKED  $route"
                textSize = 18f
                gravity = Gravity.CENTER
                setPadding(24, 28, 24, 28)
            })
        }
        setContentView(root)
    }
}
