package com.biupiu.rndos

enum class PlatformTarget {
    ANDROID,
    WINDOWS,
    MACOS,
    LINUX,
    UNIX,
    IOS,
    WEB
}

data class PlatformSupport(
    val target: PlatformTarget,
    val ui: String,
    val runtime: String,
    val nativeAdapter: Boolean,
    val distribution: String
)

object PlatformMatrix {
    val targets = listOf(
        PlatformSupport(PlatformTarget.ANDROID, "Compose/Android", "Kotlin/JVM", true, "OEM stores + direct APK/AAB"),
        PlatformSupport(PlatformTarget.WINDOWS, "Compose Desktop", "Kotlin/JVM/Native", true, "MSIX/installer"),
        PlatformSupport(PlatformTarget.MACOS, "Compose Desktop", "Kotlin/Native/JVM", true, "DMG/PKG"),
        PlatformSupport(PlatformTarget.LINUX, "Compose Desktop", "Kotlin/JVM/Native", true, "AppImage/DEB/RPM"),
        PlatformSupport(PlatformTarget.UNIX, "Native/desktop adapter", "POSIX-specific", true, "Platform-specific"),
        PlatformSupport(PlatformTarget.IOS, "Compose Multiplatform", "Kotlin/Native", true, "App Store"),
        PlatformSupport(PlatformTarget.WEB, "Compose/Wasm or web adapter", "Wasm/JS", true, "Web deployment")
    )
}
