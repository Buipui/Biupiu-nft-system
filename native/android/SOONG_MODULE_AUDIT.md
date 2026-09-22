# Soong Module Audit

## buipui-core

Type: cc_binary
Namespace: vendor-scoped overlay
Inputs: C++ native source
Dependencies: libbase, liblog, libbinder_ndk
Init: buipui-core.rc
Policy: buipui_core domain

## BuipuiControl

Type: android_app
Purpose: native control/diagnostic boundary
Platform APIs: enabled
Privileged: yes
Certificate: platform

## Audit rule

The privileged APK is not considered security-verified. It remains a bootstrap client until package permissions, SELinux domains, signing, privileged-permission allowlist, CTS, and runtime behavior are validated in the selected product.
