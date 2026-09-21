# VIS-NATIVE-06 Asset/Material Pipeline Gate v1.0
**Status:** SOURCE FOUNDATION IMPLEMENTED / EXTERNAL SDK PROVIDERS OPEN

Implemented:
- native image/HDR resource descriptor
- colour-transform boundary
- native GPU pipeline-state descriptor/lifecycle
- C ABI and C++20 implementation
- deterministic smoke fixture

Provider integrations remain explicit gates:
- DXC / glslang: real shader compilation
- MaterialX: material interchange/translation
- OpenColorIO: production colour transforms
- OpenImageIO: image IO
- OpenEXR: HDR IO
- Vulkan/DX12: real pipeline creation

No provider is represented as runtime-verified until a host execution artifact exists.
