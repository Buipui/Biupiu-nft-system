package com.biupiu.rndos

import android.app.Activity
import android.os.Bundle
import android.graphics.Color
import android.view.Gravity
import android.widget.LinearLayout
import android.widget.TextView

class RenderPipelineActivity : Activity() {
 override fun onCreate(savedInstanceState:Bundle?){super.onCreate(savedInstanceState)
  val root=LinearLayout(this).apply{orientation=LinearLayout.VERTICAL;gravity=Gravity.CENTER;setPadding(48,48,48,48)}
  root.addView(TextView(this).apply{text="BIUPIU RENDER PIPELINE";textSize=24f;gravity=Gravity.CENTER;setTextColor(Color.BLACK)})
  root.addView(TextView(this).apply{text="Create jobs • monitor queue • review outputs • inspect provenance";textSize=16f;gravity=Gravity.CENTER})
  setContentView(root)
 }
}