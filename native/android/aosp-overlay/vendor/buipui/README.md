# Buipui AOSP Overlay

This directory is intended to be imported into an AOSP checkout as vendor-scoped Buipui source.

The native daemon is intentionally a minimal bootstrap implementation. It does not bypass SELinux, AVB, KeyMint, permissions, or Android framework security. Stable Binder/AIDL APIs and higher-level Intelligence/DMS clients are added only after the baseline boots and the service passes CTS/VTS/security validation.

## Integration

1. Sync AOSP using the locked manifest branch.
2. Copy or expose this overlay under the selected vendor/device integration path.
3. Add the vendor sepolicy directory through the device build configuration.
4. Add the Soong package to the product/device makefile.
5. Build userdebug.
6. Boot Cuttlefish.
7. Verify SELinux mode, service startup, logs, and SELinux denials.
8. Promote only after clean policy/build/security results.
