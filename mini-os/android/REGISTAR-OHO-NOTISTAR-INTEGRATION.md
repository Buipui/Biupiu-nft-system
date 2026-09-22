# Buipui Mini OS — RegiStar / One Hand Operation+ / NotiStar harvest

## Integration target
Native Android equivalents are integrated as first-party Buipui Mini OS modules rather than bundling Samsung Good Lock binaries.

### RegiStar-derived capability map
- Settings home organisation: local Buipui control-center categories and ordering.
- Back-tap actions: capability adapter; hardware-specific back-tap is not universally exposed by Android.
- Side-key actions: capability adapter; interception is OEM/privileged dependent and is not claimed as universally available.
- Settings change history: Buipui event/audit layer.
- Searchable settings: local Mini OS settings index.

Samsung documents RegiStar as providing settings-home reconfiguration, settings-change search, back-tap on supported Galaxy devices, and side-key actions. These behaviours are therefore treated as harvested design requirements, not copied Samsung implementation.

### One Hand Operation+ capability map
- Edge gesture adapter.
- Back/Home/Recent/notification-panel/quick-panel actions where Android permissions allow.
- One-handed reachability adapter.
- Per-app exclusions.
- Gesture sensitivity configuration.

Samsung's current One Hand Operation+ supports left/right edge handles and configurable horizontal/diagonal gestures. The Buipui implementation uses Android-native accessibility/gesture primitives instead of Samsung private APIs.

### NotiStar capability map
- NotificationListenerService capture.
- Local notification history.
- Keyword search.
- Per-app filtering.
- Configurable retention policy (planned persistence layer).
- Lock-screen access is deliberately not enabled by default because it can expose private notification content.

## Verification boundaries
- VERIFIED: repository integration files and native Android module skeleton.
- VERIFIED: Android service declarations compile structurally against the Android SDK APIs used.
- OPEN: physical build/Gradle execution until an Android build environment is available.
- OPEN: true OEM back-tap and side-key interception; requires supported hardware/OEM privileged hooks.
- OPEN: persistent encrypted notification database and retention UI.
