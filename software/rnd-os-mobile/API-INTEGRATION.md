# Android API integration — Gate 05

The Android client now has a typed Retrofit contract for the shared R&D OS API.

Production implementation must provide:
- Retrofit/OkHttp dependency configuration.
- Secure authenticated session/token handling.
- TLS certificate validation.
- Role-aware UI.
- Offline queue + conflict resolution.
- Error/retry handling.
- Instrumented end-to-end tests.

No private key or blockchain secret belongs in the Android application.