# Biupiu Security Hardening Integration v1.0

**Date:** 2026-09-20  
**Status:** IMPLEMENTED architecture + defensive policy scaffold; external production deployment remains gated.

## Purpose

Integrate high-assurance defensive security patterns into the Biupiu Core OS and Biupiu AI without allowing external code, AI output, or research material to bypass the authoritative OS validation/audit boundary.

This security track is separate from the NFT/IP release path. External code is reference-only until licence, security, compatibility, deterministic-test and provenance gates pass.

## Evidence and design inputs

- NASA: lifecycle software assurance, rigorous verification/validation, formal inspections, secure coding, vulnerability and supply-chain controls.
- NIST: zero-trust architecture; secure software development; post-quantum standards.
- NSA/CISA: layered security, hardening, phishing-resistant authentication, patching, restricted administration, signed logging and segmentation.
- U.S. Treasury: zero trust, least privilege, continuous identity verification, compartmentalization/microsegmentation, encryption and quantum-resistant cryptography.
- Fort Knox / U.S. Mint public material: used only as a high-level analogy for defense-in-depth and separation of duties/knowledge; no sensitive facility procedures are reproduced.
- CIA/declassified historical material: used only as historical evidence for the importance of secure communications, compartmentation and the risk of aggregated information exposure. No operational intelligence tradecraft is implemented.
- Stanford / Harvard / ResearchGate / Emerald / Wits: research and engineering references only. Academic/media sources do not become runtime dependencies merely by being indexed.
- Foreign-language research: Russian GOST material and Chinese cryptography implementations were inspected as interoperability/reference sources. They remain gated external backends.

## Security architecture

### 1. Hardware/root of trust

Target controls:
- UEFI/verified boot where platform supports it.
- Measured boot with TPM 2.0.
- TPM-backed key material and attestation adapters.
- Secure key storage; secrets never committed to source.
- Optional future TEE/secure-enclave adapters.

### 2. Runtime isolation

Target controls:
- least privilege and explicit authority boundaries;
- OS sandboxing using available platform primitives such as seccomp/Landlock on Linux;
- capability-style authority modelling for high-assurance components;
- microkernel/seL4 research track kept separate from the current OS runtime until platform proof and integration requirements are met;
- restricted package/module loading and fail-closed promotion.

### 3. Identity and access

Target controls:
- zero trust: authenticate and authorize each protected operation;
- short-lived credentials/tokens;
- workload identity adapters using SPIFFE/SPIRE-style identities where appropriate;
- role/attribute-based authorization in the authoritative OS;
- phishing-resistant MFA for privileged human administration when a production identity provider is connected;
- separation of deployment credentials from treasury/signing custody.

### 4. Cryptographic agility

The core contract remains algorithm-agile rather than hard-coding a single future cipher suite.

Baseline:
- SHA-256 for the existing deterministic provenance/hash contract.

Post-quantum adaptation layer:
- FIPS 203 ML-KEM for key establishment;
- FIPS 204 ML-DSA for digital signatures;
- FIPS 205 SLH-DSA for hash-based signatures.

Foreign/legacy interoperability:
- GOST-family adapters such as GmSSL/go-gostcrypto remain optional references until compatibility, licensing, security testing and policy fit are verified.

No hand-written replacement cryptography is introduced in the OS/AI core.

### 5. Software supply chain

Reference/adapter modules:
- TUF / python-tuf for secure update metadata verification;
- Sigstore / Cosign for signed artifacts;
- in-toto for provenance/attestation;
- OpenSSF Scorecard for repository security posture checks;
- Syft for SBOM generation;
- Grype for dependency/vulnerability scanning.

Promotion rule:
RESEARCH -> REFERENCE -> LICENCE REVIEW -> SECURITY REVIEW -> COMPATIBILITY -> DETERMINISTIC TEST -> PROVENANCE -> HUMAN APPROVAL -> MAIN OS APPROVAL -> AUTHORITATIVE INTEGRATION

A compromised upstream repository, dependency or signing key must not automatically become a trusted Biupiu dependency.

### 6. Tamper-evident trust records

The existing Biupiu trust chain remains authoritative:
- deterministic canonicalization;
- SHA-256 record hashes;
- chained event hashes;
- versioned signature metadata;
- replay/sequence controls;
- optional checkpoint anchoring.

Secrets and private keys remain off-record.

### 7. AI security boundary

Biupiu AI may:
- retrieve and compare security research;
- classify resources;
- propose adapters, tests and remediation;
- generate preventative tests.

Biupiu AI may not:
- bypass OS authorization;
- directly mutate authoritative state;
- promote external code without the required gates;
- fabricate security verification;
- execute an external backend merely because it is discovered.

The new security_guard.py implements this policy as a fail-closed decision layer.

## Foreign-language protocol

Search families include:
- Russian: криптография, ГОСТ, защищенная загрузка, доверенная вычислительная среда, безопасность цепочки поставок.
- Chinese: 国密, SM2, SM3, SM4, TLS, 可信执行环境.
- Japanese: セキュアOS, TPM, セキュアブート, 暗号, サプライチェーン.
- English cross-checks: NASA, NIST, NSA/CISA, Treasury, Stanford, Harvard, ResearchGate, Emerald Insight, Wits, GitHub/OpenSSF.

Translation is evidence-preserving: original-language material remains retained and machine translations are untrusted until validated.

## High-security module registry

See research/BIUPIU-SECURITY-MODULE-MANIFEST-v1.0.json.

## Gate status

SECURITY-01: EXECUTED — architecture and fail-closed AI security guard implemented in the development branch.

SECURITY-02: MODULE-REGISTRY — implemented as a machine-readable reference/adapter manifest.

SECURITY-03: SMOKE — local policy tests and Python compilation passed.

SECURITY-04: REGRESSION — GitHub Actions workflow added; remote CI result remains subject to GitHub runner execution.

Production claims remain blocked until real hardware/platform, identity, storage, boot-chain and independent security assessments are performed.
