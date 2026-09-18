package com.biupiu.rndos.lab

data class DeviceSummary(val deviceId: String, val deviceType: String, val firmwareVersion: String, val status: String)
data class SensorReadingDto(val deviceId: String, val sensorId: String, val timestamp: String, val value: Double, val unit: String, val quality: String = "unclassified")
