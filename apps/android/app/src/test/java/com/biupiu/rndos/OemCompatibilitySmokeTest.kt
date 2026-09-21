package com.biupiu.rndos

import org.junit.Assert.assertTrue
import org.junit.Test

class OemCompatibilitySmokeTest {
    @Test
    fun everyOemProfileHasResourceCoverage() {
        val families = OemCompatibilityRegistry.profiles.map { it.family }.toSet()
        val covered = OemResourceRegistry.modules.map { it.family }.toSet()
        assertTrue(families.all { it in covered })
    }

    @Test
    fun hardwareCapabilitiesRemainVendorNeutral() {
        assertTrue(HardwareCapabilityRegistry.supported.isNotEmpty())
        assertTrue(HardwareCapabilityRegistry.supported.all { it.requiresNativeAdapter })
    }

    @Test
    fun platformMatrixContainsAndroid() {
        assertTrue(PlatformMatrix.targets.any { it.target == PlatformTarget.ANDROID })
    }
}
