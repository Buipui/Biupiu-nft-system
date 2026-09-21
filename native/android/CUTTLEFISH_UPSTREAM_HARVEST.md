# Cuttlefish Upstream Harvest

## Current upstream signals

September 2026 upstream Cuttlefish commits include:
- standalone host preparation for podcvd
- sharded cvd end-to-end tests
- Gfxstream update
- Linux 6.1 header compatibility fixes for minijail
- Bazel 7 build macro support
- pKVM/virtualization-related work in the current project history

## Integration policy

Consume these through the selected AOSP/Cuttlefish source revisions. Do not vendor arbitrary GitHub commits into Buipui. Any cherry-pick must be license-reviewed, dependency-reviewed, and tested against the locked AOSP release.

## First Cuttlefish smoke tests

1. host/KVM preflight
2. CVD launch
3. ADB connectivity
4. boot completion
5. SELinux enforcing
6. Buipui core process/service
7. Control APK launch
8. logcat/AVC audit
9. shutdown/restart
10. repeat boot
