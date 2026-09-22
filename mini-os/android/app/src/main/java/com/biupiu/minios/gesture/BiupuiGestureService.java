package com.biupiu.minios.gesture;

import android.accessibilityservice.AccessibilityService;
import android.view.accessibility.AccessibilityEvent;

public final class BiupuiGestureService extends AccessibilityService {
    @Override protected void onServiceConnected() { super.onServiceConnected(); }
    @Override public void onAccessibilityEvent(AccessibilityEvent event) {}
    @Override public void onInterrupt() {}
}
