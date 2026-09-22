/**
 * Biupiu Federation Harvest Gate
 *
 * Native, dependency-free implementation of the external-harvest promotion
 * boundary. This module validates records; it does not execute untrusted
 * adapters, install dependencies, or grant runtime authority.
 */

export type HarvestStatus =
  | "CANDIDATE"
  | "REPOSITORY_VERIFIED_UNTESTED"
  | "VERIFIED_WORKING"
  | "QUARANTINED"
  | "SUPERSEDED";

export interface HarvestEvidence {
  source: string;
  licenceReviewed: boolean;
  provenanceRecorded: boolean;
  versionCompared: boolean;
  dependencyCheckPassed: boolean;
  normalisationPassed: boolean;
  staticTestPassed: boolean;
  buildPassed: boolean;
  securityReviewPassed: boolean;
  integrationTestPassed: boolean;
  regressionPassed: boolean;
  runtimeTestPassed: boolean;
  rollbackReference?: string;
  testReferences: string[];
}

export interface HarvestRecord {
  id: string;
  name: string;
  version: string;
  repositoryPath?: string;
  status: HarvestStatus;
  evidence: HarvestEvidence;
  supersedes?: string;
  quarantineReason?: string;
}

export interface PromotionResult {
  promotable: boolean;
  reasons: string[];
}

const nonEmpty = (value: string): boolean => value.trim().length > 0;

export function evaluateHarvestPromotion(record: HarvestRecord): PromotionResult {
  const reasons: string[] = [];

  if (!nonEmpty(record.id) || !nonEmpty(record.name) || !nonEmpty(record.version)) {
    reasons.push("identity/version metadata is incomplete");
  }

  if (!nonEmpty(record.evidence.source)) {
    reasons.push("harvest source is missing");
  }

  if (record.repositoryPath !== undefined && !nonEmpty(record.repositoryPath)) {
    reasons.push("repository placement is empty");
  }

  if (record.status === "QUARANTINED" || record.status === "SUPERSEDED") {
    reasons.push(`record status is ${record.status}`);
  }

  const evidence = record.evidence;
  const checks: Array<[boolean, string]> = [
    [evidence.provenanceRecorded, "provenance is not recorded"],
    [evidence.versionCompared, "version comparison is incomplete"],
    [evidence.licenceReviewed, "licence/IP review is incomplete"],
    [evidence.dependencyCheckPassed, "dependency check has not passed"],
    [evidence.normalisationPassed, "normalisation has not passed"],
    [evidence.staticTestPassed, "static tests have not passed"],
    [evidence.buildPassed, "build has not passed"],
    [evidence.securityReviewPassed, "security review has not passed"],
    [evidence.integrationTestPassed, "integration tests have not passed"],
    [evidence.regressionPassed, "regression tests have not passed"],
    [evidence.runtimeTestPassed, "runtime verification has not passed"],
    [evidence.testReferences.length > 0, "test evidence references are missing"],
    [nonEmpty(evidence.rollbackReference ?? ""), "rollback reference is missing"],
  ];

  for (const [passed, reason] of checks) {
    if (!passed) reasons.push(reason);
  }

  return { promotable: reasons.length === 0, reasons };
}

export function quarantineHarvest(record: HarvestRecord, reason: string): HarvestRecord {
  if (!nonEmpty(reason)) throw new Error("quarantine reason is required");
  return { ...record, status: "QUARANTINED", quarantineReason: reason };
}
