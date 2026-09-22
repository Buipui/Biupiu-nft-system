# Biupiu Enterprise Android — Deep Harvest v1

Updated: 2026-09-21
Status: HARVESTED / SOURCE-READY / RUNTIME PENDING

## Scope
Enterprise optimisation of the Biupiu Native Android ROM, DMS, Intelligence, security, diagnostics and commercial system interfaces.

## Authoritative Android Enterprise capabilities
Use AOSP Android Enterprise primitives rather than replacing them:
- DevicePolicyManager
- managed profiles
- fully managed/device-owner mode
- corporate-owned work profile / COPE
- dedicated-device mode
- managed configurations
- provisioning flows
- package/app policy
- user/profile separation
- enterprise security controls

Android 17 CDD requires managed-profile support through DevicePolicyManager for devices declaring managed users and specifies profile separation and UI/data-accounting requirements.

## Android 17 enterprise additions
Route these into Biupiu through official APIs/policies:
- agentic automation policy boundaries
- cross-profile localhost restrictions
- local-network runtime permission administration
- Certificate Transparency default behaviour
- HID permission/control
- USB data-signalling policy
- USB4/Thunderbolt physical-layer restrictions
- App Functions policy
- device-level data for authorised on-device assistants, with work-profile data excluded

## GitHub code/module harvest

### KEEP-AOSP / REFERENCE
1. AOSP DevicePolicyManager / enterprise framework
2. Android Enterprise Samples
3. TestDPC
4. Mainline/APEX modular architecture
5. AOSP Cuttlefish enterprise validation target

### Android Enterprise Samples
Repository: android/enterprise-samples
Useful patterns:
- managed configurations
- work-profile setup
- enterprise application policy integration
Licence: Apache-2.0 according to repository metadata.
Use as implementation/reference material; do not copy wholesale.

### TestDPC
Repository: googlesamples/android-testdpc
Useful patterns:
- Device Owner provisioning
- Profile Owner provisioning
- managed profile testing
- policy API exploration
- DPC role-holder testing
- enterprise test harness patterns
Licence: Apache-2.0.
Treat as test/reference code, not production DPC code.

### Other GitHub results
Third-party DevicePolicyManager wrappers and historical framework mirrors were discovered. They are NOT promotion candidates because they duplicate platform APIs or may represent obsolete platform revisions. They remain research/reference only unless independently provenance/licence/compatibility/security validated.

## OpenBooks / repository research lane
No specific OpenBooks project was uniquely identified by the current search as an authoritative Android Enterprise implementation source. No OpenBooks code is promoted.
The existing Biupiu OpenBooks/research protocol remains a discovery lane:
DISCOVER -> IDENTIFY -> PROVENANCE -> LICENCE -> COMPATIBILITY -> SECURITY -> TEST -> PROMOTION.

## Security harvest
Android 17 enterprise changes are treated as security boundaries, especially:
- cross-profile isolation
- local-network access
- USB/HID controls
- AI/App Functions policy
- managed-profile data separation
- certificate/network trust
- provisioning identity

September 2026 Android security bulletins include critical/high issues affecting Android 17. Enterprise builds must track current AOSP security patches and must not freeze an older security level.

## Commercial architecture conclusion
Biupiu should not replace Android Enterprise. It should provide an enterprise control plane layered on AOSP Enterprise primitives:
AOSP Enterprise -> Buipui Policy Broker -> Buipui DMS -> Buipui Intelligence/Federation -> Enterprise Applications/Digital Twins.

This reduces duplicated privileged code and improves interoperability.
