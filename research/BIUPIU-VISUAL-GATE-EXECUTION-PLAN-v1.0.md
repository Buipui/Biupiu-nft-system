# Biupiu Visual Gate Execution Plan v1.0

## Gate order
VIS-NATIVE-02 capability and language/SDK audit
VIS-NATIVE-03 scene graph + transform + provider registry
VIS-NATIVE-04 native renderer/GPU abstraction
VIS-NATIVE-05 material/shader/colour/image stack
VIS-NATIVE-06 animation/timeline/subdivision
VIS-NATIVE-07 frame capture + video/codec
VIS-NATIVE-08 USD/OTIO/OpenSubdiv provider tests
VIS-NATIVE-09 deterministic regression/provenance
VIS-NATIVE-10 Unity/UE5 provider validation

## Rule
Do not wait for UE5 compilation to complete before implementing independent native modules. Unity remains deferred until VIS-NATIVE-09.
