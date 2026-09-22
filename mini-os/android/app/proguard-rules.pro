# ONNX Runtime Android uses reflection for runtime classes.
-keep class ai.onnxruntime.** { *; }

# Federation provider identifiers are resolved by explicit adapters.
-keep class com.biupiu.minios.federation.** { *; }
