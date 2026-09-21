import {
  ArcadeLaunchDecision,
  GameResource,
  ModdingStationJob,
  RightsState,
} from './types';

const BLOCKED_RIGHTS: RightsState[] = ['RED', 'ORANGE', 'GREY', 'BLUE', 'YELLOW'];

export class NativeResourceRegistry {
  private readonly resources = new Map<string, GameResource>();

  register(resource: GameResource): void {
    if (!resource.resourceId.trim()) throw new Error('resourceId is required');
    if (this.resources.has(resource.resourceId)) {
      throw new Error(`resource already registered: ${resource.resourceId}`);
    }
    this.resources.set(resource.resourceId, structuredClone(resource));
  }

  get(resourceId: string): GameResource | undefined {
    const resource = this.resources.get(resourceId);
    return resource ? structuredClone(resource) : undefined;
  }

  canLaunch(resourceId: string): ArcadeLaunchDecision {
    const resource = this.resources.get(resourceId);
    if (!resource) return { allowed: false, reasons: ['resource_not_found'] };

    const reasons: string[] = [];
    if (BLOCKED_RIGHTS.includes(resource.rightsState)) reasons.push('rights_not_cleared');
    if (!resource.commercialUse || !resource.redistributionAllowed) {
      reasons.push('commercial_distribution_not_authorized');
    }
    if (resource.compatibilityStatus !== 'PASS') reasons.push('compatibility_not_verified');
    if (resource.securityStatus !== 'PASS') reasons.push('security_not_verified');
    if (resource.approval !== 'APPROVED') reasons.push('approval_missing');
    if (resource.verificationState !== 'VERIFIED' && resource.verificationState !== 'RELEASED') {
      reasons.push('verification_gate_incomplete');
    }

    return { allowed: reasons.length === 0, reasons };
  }

  validateModJob(job: ModdingStationJob): string[] {
    const errors: string[] = [];
    if (!job.jobId.trim()) errors.push('job_id_required');
    if (!job.creatorId.trim()) errors.push('creator_id_required');
    if (!job.packagePath.trim()) errors.push('package_path_required');
    if (!job.declaredLicence.trim()) errors.push('licence_declaration_required');
    if (job.dependencies.some((dependency) => !dependency.trim())) {
      errors.push('invalid_dependency_entry');
    }
    return errors;
  }
}
