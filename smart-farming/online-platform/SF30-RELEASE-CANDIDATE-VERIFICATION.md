# SF-30 — Release Candidate Verification & Biupiu World Runtime Integration Test

## Purpose
Perform a repository-level verification of the SF-29 release candidate and define the controlled runtime integration test.

Status: VERIFIED SPECIFICATION / RUNTIME MEDIA PENDING

## Verification matrix

| Gate | Check | Result |
|---|---|---|
| SF-22 | Shot sequence exists | PASS |
| SF-25 | Render/edit order exists | PASS |
| SF-26 | Titles/captions/delivery workflow exists | PASS |
| SF-27 | Asset validation controls exist | PASS |
| SF-28 | Editorial QA controls exist | PASS |
| SF-29 | Publication/archive controls exist | PASS |
| Media | Final rendered media present | PENDING |
| Human QA | Final editorial approval | PENDING |
| Rights | Final production asset clearance | PENDING |
| Runtime | Live world activation | BLOCKED |

## Runtime integration test

### Test RT-01 — Episode launch
Load BPU-WORLD-E01 from the World Launcher and verify episode metadata resolves.

### Test RT-02 — Scene traversal
Verify the sequence:
WORLD GATEWAY → AIR-01 → MAR-01 → AGR-01 → CONS-01 → AI-01 → WORLD MONTAGE.

### Test RT-03 — Context bridge
At each scene verify:
department_id, scene_id, hero_asset_id, research_link, digital_lab_link, academy_link.

### Test RT-04 — Claim labels
Verify each concept/research label is visible and remains attached to its corresponding asset.

### Test RT-05 — Commerce separation
Verify marketplace/gallery links are available where configured but do not imply that research concepts are currently commercial products.

### Test RT-06 — Rollback
Verify a prior approved version can be restored without deleting source/archive records.

## Runtime release states
INTEGRATION_BLOCKED → TEST_READY → TEST_PASS → HUMAN_APPROVAL → RUNTIME_ENABLED

Runtime must remain disabled until media QA and human approval are complete.
