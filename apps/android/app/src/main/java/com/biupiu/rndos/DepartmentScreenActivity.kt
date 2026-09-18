package com.biupiu.rndos

import android.app.Activity
import android.os.Bundle
import android.graphics.Color
import android.view.Gravity
import android.widget.TextView

abstract class DepartmentScreenActivity : Activity() {
    protected abstract val screenId: String

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(TextView(this).apply {
            text = "BIUPIU R&D OS\n$screenId"
            textSize = 24f
            gravity = Gravity.CENTER
            setTextColor(Color.BLACK)
        })
    }
}

class SmartFarmingActivity : DepartmentScreenActivity() {
    override val screenId = "FARMING_WORLD"
}

class SmartMetallurgyActivity : DepartmentScreenActivity() {
    override val screenId = "METAL_MAKING_WORLD"
}

class RndOsActivity : DepartmentScreenActivity() {
    override val screenId = "RND_OS_HOME"
}
