# VIS-NATIVE-19 — Native Resource & Memory Runtime Gate v1.0

## Purpose
Establish the first-party, backend-neutral resource lifetime and memory accounting layer beneath the native visual runtime.

## Implemented
- C-compatible opaque allocation handles.
- Buffer/image resource classification.
- CPU, upload, GPU-local and readback memory domains.
- Alignment and capacity validation.
- Allocation/release lifecycle.
- Map/unmap lifecycle for host-visible backing storage.
- Live/peak/capacity accounting.
- Invariant validation and double-release rejection.
- Deterministic CTest smoke coverage.
- Cross-platform C++20 implementation.

## Backend boundary
This gate does not claim that a Vulkan VkDeviceMemory object or Direct3D 12 heap has been allocated. GPU backend allocation remains a subsequent implementation layer. The native memory contract is the authoritative ownership/accounting boundary, while Vulkan/DX12 become backend providers.

The next GPU-backed layer must connect native allocation, backend resource, backend memory, synchronization and retirement.

## Search/evidence protocol
Khronos documentation confirms that Vulkan applications explicitly manage resource synchronization and memory dependencies, and Synchronization 2 is core in Vulkan 1.3:
https://docs.vulkan.org/guide/latest/synchronization.html
https://docs.vulkan.org/spec/latest/chapters/synchronization.html
https://docs.vulkan.org/guide/latest/extensions/VK_KHR_synchronization2.html

Vulkan Memory Allocator is a relevant optional provider for Vulkan allocation integration; it is not authoritative in this gate:
https://gpuopen.com/vulkan-memory-allocator/

The implementation remains fail-closed: optional backend providers are not promoted from SDK discovery alone.

## Gate state
- REGISTERED: yes
- IMPLEMENTED: yes
- HOST_VERIFIED: pending CI execution
- VERIFIED: pending reviewed CI evidence

## Next gate
VIS-NATIVE-20 — Executable Shader Pipeline, with GPU-backed resource allocation/synchronization integration tracked as a required dependency.
