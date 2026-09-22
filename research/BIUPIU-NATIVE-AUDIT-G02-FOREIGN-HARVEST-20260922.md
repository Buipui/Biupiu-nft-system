# Native Audit G02 — Foreign-Language Federation Harvest and Semantic Fix Record

Date: 2026-09-22
Status: IMPLEMENTED / SOURCE-LEVEL VERIFIED / CI RUNTIME PENDING

## Scope

Cross-reference the native coding philosophy, multilanguage matrix, Mini-OS compute ABI,
Rust FFI boundary, heterogeneous compute federation and Android security boundary.

## Literature filing

Complete literature filing is recorded in `research/BIUPIU-G02-LITERATURE-FILING-20260922.md`. The filing audit is recorded in `research/BIUPIU-G02-LITERATURE-FILING-AUDIT-20260922.md`.

## Foreign-language / international reference harvest

### Rust FFI and unsafe boundary
- Rust official documentation confirms that unsafe blocks discharge obligations the
  compiler cannot verify and that FFI signatures are part of the safety contract.
- Rust guidance recommends explicit SAFETY reasoning around unsafe operations and
  safe wrappers around raw FFI where practical.
- References:
  - https://doc.rust-lang.org/reference/unsafe-keyword.html
  - https://doc.rust-lang.org/book/ch19-01-unsafe-rust.html
  - https://doc.rust-lang.org/nomicon/ffi.html

### GNU Scientific Library
- GNU's official GSL page identifies Japanese and Portuguese reference-manual
  translations and documents stable API, portability and thread-safety material.
- The harvest confirms that multilingual documentation is useful evidence but is
  not runtime authority; the canonical implementation remains the native adapter.
- References:
  - https://www.gnu.org/s/gsl
  - https://www.gnu.org/software/gsl/doc/html/

### Android security
- Android's official security documentation supports Android Keystore for protected
  key material and Network Security Configuration for declarative cleartext/network
  trust controls.
- The multilingual Android security pages were cross-referenced to ensure the same
  architectural rule is preserved across language/localization surfaces.
- References:
  - https://developer.android.com/privacy-and-security/keystore
  - https://developer.android.com/privacy-and-security/security-config
  - https://developer.android.com/privacy-and-security/security-tips?hl=hi
  - https://developer.android.com/privacy-and-security/security-tips?hl=ar

## Findings and fixes

### F-001 — Rust Mini-OS unsafe block lacked an explicit SAFETY rationale
Fix:
- Added a local SAFETY comment documenting null validation, writable ABI contract
  and bounded struct writes.
- Expanded the native semantic auditor to detect Rust unsafe blocks without a
  nearby SAFETY comment.

### F-002 — Mini-OS minimum/preferred compute semantics required an explicit contract
Finding:
- The Mini-OS ABI contains one minimum class and one preferred class.
- The correct fail-closed interpretation is:
  1. minimum class is a hard exact requirement;
  2. preferred class may select immediately only within that required class;
  3. if preference differs from the hard minimum, capacity is the deterministic
     fallback within the required class;
  4. a numerically higher enum value never satisfies a different minimum class.

Fix:
- Added the same contract to Rust and C++ implementations.
- Added Rust and C++ regression tests for preferred-vs-minimum conflict,
  unavailable NPU and capacity fallback.

### F-003 — Native audit coverage was narrower than the declared matrix
Fix:
- Expanded source inventory to C/C++, Rust, Python, TypeScript/JavaScript,
  Kotlin, Java, C#, Swift.
- Excludes vendored/third-party/build output from governance scanning.
- Added language inventory as a gate result.
- Added repository-wide Rust SAFETY checks.
- Retained Python syntax, TypeScript forbidden-authority checks, contract token
  checks and AI hard-gate validation.

## Missing-module assessment

No new runtime authority module is promoted from this harvest.

Required supporting modules are already represented by existing architecture:
- native ABI / FFI boundary;
- heterogeneous compute federation;
- capability registry;
- adapter/provider boundary;
- provenance/licence/security state;
- fail-closed dispatch;
- semantic audit;
- CI verification.

Potential future modules remain verification adapters rather than core authority:
- live GPU/NPU enumeration;
- platform-specific compute telemetry;
- Rust 2024 FFI migration checks;
- Android NDK/Gradle runtime verification;
- hardware/HIL adapters.

## Gate rule

Source implementation is not runtime verification.

This gate can close only its source/semantic portion after CI executes the new
audit and native tests. Hardware, Android device, GPU/NPU and HIL gates remain
separate.

## Status

**SOURCE INTEGRATION: IMPLEMENTED**
**SEMANTIC FIXES: IMPLEMENTED**
**FOREIGN-LANGUAGE HARVEST: RECORDED**
**CI EXECUTION: PENDING**
**HARDWARE/DEVICE: OPEN**
