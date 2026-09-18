# SF-34 — Verification Runner Implementation

## Purpose
Implement a deterministic repository verification runner for the SF-33 contract suite.

Status: RUNNER SPECIFICATION / EXECUTION PENDING

## Runner inputs
SF31 episode package test; SF32 runtime/mobile contract; SF33 contract test manifest; SF33 cross-platform matrix; SF26 title/caption manifest; SF27 asset validation manifest; SF29 publication manifest.

## Runner outputs
For every test: test_id, domain, expected_state, observed_state, result, blocking, evidence_reference.

Allowed results: PASS, FAIL, BLOCKED, NOT_TESTED.

## Critical tests
CT-01 through CT-10 from SF-33.

## Release rule
A release candidate cannot advance when any critical test is FAIL or BLOCKED.

The runner validates repository contracts and metadata. It does not substitute for actual media rendering, device testing or human approval.
