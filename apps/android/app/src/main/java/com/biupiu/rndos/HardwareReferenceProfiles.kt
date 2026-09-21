package com.biupiu.rndos

/**
 * Reference hardware classes, not hard-coded device dependencies.
 * Runtime discovery remains authoritative.
 */
data class HardwareReferenceProfile(
    val id: String,
    val className: String,
    val primaryUse: String,
    val interfaces: Set<HardwareTransport>
)

object HardwareReferenceProfiles {
    val current = listOf(
        HardwareReferenceProfile(
            "RPI5_CLASS",
            "Raspberry Pi 5 / Compute Module 5 class",
            "ARM64 gateway, local DMS/edge compute, GPIO and lab integration",
            setOf(HardwareTransport.USB, HardwareTransport.WIFI, HardwareTransport.BLUETOOTH_LE,
                HardwareTransport.ETHERNET, HardwareTransport.GPIO, HardwareTransport.I2C, HardwareTransport.SPI)
        ),
        HardwareReferenceProfile(
            "RP2350_CLASS",
            "Raspberry Pi Pico 2 / RP2350 class",
            "Low-cost deterministic MCU sensor/actuator edge node",
            setOf(HardwareTransport.GPIO, HardwareTransport.I2C, HardwareTransport.SPI, HardwareTransport.SERIAL, HardwareTransport.USB)
        ),
        HardwareReferenceProfile(
            "ESP32_CLASS",
            "Espressif ESP32-C6/C61/P4 class",
            "Wireless edge node, sensor gateway and embedded compute",
            setOf(HardwareTransport.WIFI, HardwareTransport.BLUETOOTH_LE,
                HardwareTransport.GPIO, HardwareTransport.I2C, HardwareTransport.SPI, HardwareTransport.SERIAL, HardwareTransport.USB)
        ),
        HardwareReferenceProfile(
            "NRF54L_CLASS",
            "Nordic nRF54L class",
            "Ultra-low-power BLE/Thread/Zigbee/Matter sensor node",
            setOf(HardwareTransport.BLUETOOTH_LE, HardwareTransport.I2C, HardwareTransport.SPI, HardwareTransport.SERIAL)
        )
    )
}
