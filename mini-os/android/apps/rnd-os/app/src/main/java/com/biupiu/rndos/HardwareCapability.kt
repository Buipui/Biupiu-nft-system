package com.biupiu.rndos

/**
 * Vendor-neutral hardware capability model.
 * Applications bind to capabilities; platform/OEM adapters implement transport.
 */
enum class HardwareTransport {
    USB,
    BLUETOOTH_LE,
    WIFI,
    ETHERNET,
    SERIAL,
    CAN,
    CAN_FD,
    GPIO,
    I2C,
    SPI,
    NFC,
    CAMERA,
    SENSOR,
    OPC_UA,
    MQTT,
    MODBUS,
    ROS2
}

data class HardwareCapability(
    val id: String,
    val transport: HardwareTransport,
    val category: String,
    val readOnlyByDefault: Boolean = true,
    val requiresNativeAdapter: Boolean = true,
    val safetyClass: String = "OBSERVE"
)

object HardwareCapabilityRegistry {
    val supported = listOf(
        HardwareCapability("SENSOR_TELEMETRY", HardwareTransport.SENSOR, "telemetry"),
        HardwareCapability("BLE_DEVICE", HardwareTransport.BLUETOOTH_LE, "connectivity"),
        HardwareCapability("USB_DEVICE", HardwareTransport.USB, "connectivity"),
        HardwareCapability("NFC_READER", HardwareTransport.NFC, "identity"),
        HardwareCapability("CAMERA_CAPTURE", HardwareTransport.CAMERA, "vision"),
        HardwareCapability("CAN_TELEMETRY", HardwareTransport.CAN, "automotive"),
        HardwareCapability("CANFD_TELEMETRY", HardwareTransport.CAN_FD, "automotive"),
        HardwareCapability("SERIAL_DEVICE", HardwareTransport.SERIAL, "industrial"),
        HardwareCapability("GPIO_EDGE", HardwareTransport.GPIO, "embedded"),
        HardwareCapability("I2C_SENSOR", HardwareTransport.I2C, "embedded"),
        HardwareCapability("SPI_SENSOR", HardwareTransport.SPI, "embedded"),
        HardwareCapability("OPCUA_ENDPOINT", HardwareTransport.OPC_UA, "industrial"),
        HardwareCapability("MQTT_ENDPOINT", HardwareTransport.MQTT, "iot"),
        HardwareCapability("MODBUS_ENDPOINT", HardwareTransport.MODBUS, "industrial"),
        HardwareCapability("ROS2_HARDWARE", HardwareTransport.ROS2, "robotics")
    )
}
