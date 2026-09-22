package com.biupiu.rndos

import android.app.Activity
import android.os.Bundle
import android.graphics.Color
import android.view.Gravity
import android.widget.Button
import android.widget.LinearLayout
import android.widget.TextView

abstract class DepartmentScreenActivity : Activity() {
    protected abstract val screenId: String
    protected abstract val title: String
    protected abstract val modulePackageName: String
    protected abstract val route: String

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val root = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setPadding(32, 32, 32, 32)
        }

        root.addView(TextView(this).apply {
            text = "BIUPIU R&D OS\n$title"
            textSize = 26f
            gravity = Gravity.CENTER
            setTextColor(Color.BLACK)
        })
        root.addView(TextView(this).apply {
            text = "$screenId  •  $modulePackageName"
            gravity = Gravity.CENTER
            setPadding(0, 12, 0, 16)
        })

        listOf("OVERVIEW", "TOOLS", "RESEARCH", "SETTINGS").forEach { action ->
            root.addView(Button(this).apply {
                text = action
                setOnClickListener { }
            })
        }

        CapabilityRegistry.core.filter { it.id == route }.forEach { capability ->
            root.addView(Button(this).apply {
                text = capability.id.replace('_', ' ')
                setOnClickListener { }
            })
        }
        setContentView(root)
    }
}

class SmartFarmingActivity : DepartmentScreenActivity() {
    override val screenId = "FARMING_WORLD"
    override val title = "Smart Farming"
    override val modulePackageName = "@biupiu/smart-farming"
    override val route = "SMART_FARMING"
}

class SmartMetallurgyActivity : DepartmentScreenActivity() {
    override val screenId = "METAL_MAKING_WORLD"
    override val title = "Smart Metal Workshop"
    override val packageName = "@biupiu/smart-metallurgy"
    override val route = "SMART_METAL_WORKSHOP"
}

class RndOsActivity : DepartmentScreenActivity() {
    override val screenId = "RND_OS_HOME"
    override val title = "Biupiu R&D OS"
    override val packageName = "@biupiu/rnd-os"
    override val route = "RND_OS"
}
