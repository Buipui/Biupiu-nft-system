# Biupiu Foreign/OEM Resource Harvest — Gate 28

**Date:** 21 September 2026  
**Status:** IMPLEMENTED — SOURCE/ARCHITECTURE GATE; RUNTIME/OEM DEVICE VERIFICATION PENDING

## Objective

Harvest usable engineering patterns from foreign-language repositories and cross-reference them against XDA Developers, AOSP, official OEM/open-device sources, GitHub device trees/kernels, and OpenBooks/open-knowledge resources where the scope is relevant.

The harvest is evidence-led. Language is a discovery axis, not a trust signal.

## Foreign-language search lanes

- Chinese + English: Android/OEM device trees, firmware structure, extraction manifests and kernel references.
- Korean + English: Samsung/device-tree and kernel patterns.
- Japanese + English: Sony/open-device and device configuration patterns.
- German + Italian: industrial automation, instrumentation, PLC/SPS and machine-interface terminology.
- French/Spanish/Portuguese: localisation, deployment and device-community documentation.
- Russian + English: supplementary device/kernel discovery; independent verification required.

## Usable patterns isolated

### 1. Treble/VINTF boundary
AOSP documents the system/vendor split and versioned vendor-interface boundary. Biupiu adopts this as an adapter boundary rather than a vendor-specific implementation.

### 2. Device-tree modularity
LineageOS and public OEM/community trees demonstrate reusable common-device and target-device layers. Biupiu records these as metadata profiles rather than copying device trees into the proprietary runtime.

### 3. Partition-aware resource model
AOSP documents system, system_ext, vendor, odm, boot/init_boot and related boundaries. Biupiu treats these as inspectable capabilities, not assumptions about a target device.

### 4. Proprietary extraction provenance
LineageOS documents proprietary-files manifests and extraction utilities. Biupiu records extraction manifests and provenance requirements but does not ingest vendor blobs automatically.

### 5. Mainline portability
Public Xiaomi/Sony/Lineage trees show the value of common device-tree layers and mainline-oriented abstractions. Mainline portability is now a validation dimension.

### 6. Localisation and knowledge workflow
OpenBooks search results are ambiguous because several unrelated projects use the same name. Only relevant open-knowledge/localisation patterns are recorded; no OpenBooks executable code is imported. Where an OpenBooks project exposes multilingual catalogues or audit/idempotency concepts, these remain conceptual references subject to licence and scope review.

## XDA cross-reference

XDA is retained as a discovery/community channel. It does not become an authority for firmware, vendor blobs, security claims or licensing. XDA-discovered features must be cross-checked against AOSP, official OEM/open-device material, source repository evidence and licence/security review.

Direct live XDA retrieval was not used as authoritative evidence in this gate.

## Official-source boundary

Official/AOSP/OEM sources outrank community sources for ABI/HAL contracts, boot and partition semantics, security/attestation behaviour, vendor compatibility, firmware provenance, licensing and redistribution rights. Community repositories remain useful for implementation patterns, device-specific edge cases and reproducible build techniques.

## Integrated Biupiu module

ForeignResourceRegistry now registers AOSP Treble/VINTF, LineageOS device-tree/extraction patterns, Chinese/Xiaomi patterns, Japanese/Sony patterns, Korean/Samsung patterns, XDA discovery, and OpenBooks multilingual/audit workflow references.

The registry is metadata-only and vendor-neutral. No proprietary system dump, vendor blob, GMS package, OEM secret, signing key or copied third-party implementation is integrated.

## Promotion pipeline

DISCOVER -> TRANSLATE -> SOURCE/AUTHORITY CHECK -> LICENSE -> EXTRACT PATTERN -> MAP TO CONTRACT -> IMPLEMENT INDEPENDENTLY -> UNIT/STATIC TEST -> DEVICE/HIL TEST -> VERIFY

## Next validation gates

1. Android unit/build/emulator smoke.
2. Real OEM-device matrix using physical devices.
3. Vendor HAL/firmware adapters using target-device source/licence evidence.
4. System-dump parser as a metadata inspection tool only; dumps are never redistributed.
5. Multilingual regression corpus for technical terminology and translation quality.
