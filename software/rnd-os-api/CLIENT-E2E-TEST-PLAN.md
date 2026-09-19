# Gate 10 client E2E test plan

## Shared lifecycle
Authenticate → research → experiment → asset → provenance → stale-sync conflict → reviewer resolution → audit → controlled release.

## Web
Run the lifecycle through the PWA/API adapter.

## Android
Run the same lifecycle through the typed Retrofit client.

## Security
Test expired/invalid tokens, viewer mutation denial, researcher release denial, reviewer conflict resolution and admin final release.

No test stores private keys or production secrets in client storage.