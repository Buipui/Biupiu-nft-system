# Biupiu R&D OS Mobile

Android client foundation for the Biupiu Research & Development Operating System.

## Current version

**v0.8 API integration foundation**

The application is a client of `software/rnd-os/`.

## Development flow

Android UI → Mobile API abstraction → R&D OS HTTP API → authentication/tenant enforcement → R&D OS domain services → development JSON store / future PostgreSQL.

The Android client must never connect directly to PostgreSQL.

## Development endpoint

Android Emulator can reach a development server on the host through `http://10.0.2.2:3000`.

This is development-only. Production builds must use a verified HTTPS endpoint.

## Next gate

Implement concrete Android HTTP transport, authenticated session UI, dashboard loading and Android unit/instrumentation tests.
