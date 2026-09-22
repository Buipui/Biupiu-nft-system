# BIUPIU Native Audit G02 — Literature Filing Register
Date: 2026-09-22
Status: FILED / CROSS-REFERENCED / SOURCE-ONLY EVIDENCE

This register is the canonical filing index for the literature harvested for Gate G02.
External literature is evidence/reference material only and never becomes runtime authority.

## LIT-G02-RUST — Rust safety and FFI

| ID | Source | Topic | Biupiu mapping | Evidence state |
|---|---|---|---|---|
| LIT-G02-RUST-001 | https://doc.rust-lang.org/reference/unsafe-keyword.html | unsafe contracts | Mini-OS unsafe boundary / SAFETY comments | ESTABLISHED |
| LIT-G02-RUST-002 | https://doc.rust-lang.org/reference/unsafety.html | unsafe operations | native memory-safety audit | ESTABLISHED |
| LIT-G02-RUST-003 | https://doc.rust-lang.org/reference/behavior-considered-undefined.html | undefined behavior | fail-closed native verification | ESTABLISHED |
| LIT-G02-RUST-004 | https://doc.rust-lang.org/book/ch19-01-unsafe-rust.html | unsafe Rust and FFI | Rust/C ABI engineering | ESTABLISHED |
| LIT-G02-RUST-005 | https://doc.rust-lang.org/nomicon/ffi.html | FFI contracts | durable C ABI boundary | ESTABLISHED |
| LIT-G02-RUST-006 | https://doc.rust-lang.org/edition-guide/rust-2024/unsafe-extern.html | Rust 2024 unsafe extern | future FFI migration check | ESTABLISHED |
| LIT-G02-RUST-007 | https://doc.rust-lang.org/edition-guide/rust-2024/unsafe-attributes.html | unsafe attributes | future symbol/export audit | ESTABLISHED |
| LIT-G02-RUST-008 | https://doc.rust-lang.org/stable/core/keyword.extern.html | extern/FFI | ABI boundary documentation | ESTABLISHED |

## LIT-G02-GSL — GNU Scientific Library

| ID | Source | Topic | Biupiu mapping | Evidence state |
|---|---|---|---|---|
| LIT-G02-GSL-001 | https://www.gnu.org/s/gsl | GSL overview, portability, API and multilingual documentation | numerical-library reference/adaptor candidate | ESTABLISHED |
| LIT-G02-GSL-002 | https://www.gnu.org/software/gsl/doc/html/ | GSL reference manual | numerical adapter/reference | ESTABLISHED |

International documentation noted during harvest includes Japanese and Portuguese GSL reference material. Localized documentation is retained as discovery/supporting evidence; canonical implementation and compatibility remain native repository gates.

## LIT-G02-ANDROID — Android security

| ID | Source | Topic | Biupiu mapping | Evidence state |
|---|---|---|---|---|
| LIT-G02-ANDROID-001 | https://developer.android.com/privacy-and-security/keystore | protected key material | Android security boundary | ESTABLISHED |
| LIT-G02-ANDROID-002 | https://developer.android.com/privacy-and-security/security-config | network trust / cleartext / pinning | Android network-security adapter | ESTABLISHED |
| LIT-G02-ANDROID-003 | https://developer.android.com/privacy-and-security/security-tips?hl=hi | Hindi security guidance | multilingual semantic cross-check | ESTABLISHED |
| LIT-G02-ANDROID-004 | https://developer.android.com/privacy-and-security/security-tips?hl=ar | Arabic security guidance | multilingual semantic cross-check | ESTABLISHED |
| LIT-G02-ANDROID-005 | https://developer.android.com/reference/android/security/net/config/NetworkSecurityConfig | API reference | runtime/API compatibility reference | ESTABLISHED |

## Filing rules

1. Original publisher/standards documentation is preferred.
2. External source text is not copied into executable authority.
3. Every harvested source receives a stable filing ID and architecture mapping.
4. Foreign-language/localized material retains locale/source identity.
5. External code or implementation patterns require licence, provenance, security, compatibility, build, regression and human-promotion gates.
6. A literature filing is not a claim that a dependency is installed or runtime-verified.

## Cross-links

- Research record: `research/BIUPIU-NATIVE-AUDIT-G02-FOREIGN-HARVEST-20260922.md`
- Native philosophy/matrix: `research/BIUPIU-NATIVE-CODING-PHILOSOPHY-AND-ENGINEERING-MATRIX-v1.0.md`
- Native semantic audit: `intelligence/BIUPIU-NATIVE-SEMANTIC-CODE-AUDIT.py`
- G02 CI: `.github/workflows/biupiu-native-audit-g02.yml`

