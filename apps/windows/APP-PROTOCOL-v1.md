# Gate 15 — Native Deep-Link Registration

Biupiu uses the biupiu://department/<target> URI namespace.

Android registers the biupiu scheme through the application manifest.

Windows exposes a matching protocol-handling contract through DeepLinkRouter. Native OS protocol registration is intentionally left to the Windows installer/package configuration and is not claimed active until that package declares it.

Targets:
- biupiu://department/smart-farming
- biupiu://department/smart-metal-workshop
- biupiu://department/rnd-os

Routes still pass through the runtime entitlement layer before privileged department access.