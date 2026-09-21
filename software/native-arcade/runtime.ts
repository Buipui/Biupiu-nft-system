import { ArcadeLaunchDecision, GameResource } from './types';
import { NativeResourceRegistry } from './registry';

export type RuntimeSessionState = 'IDLE' | 'STARTING' | 'RUNNING' | 'STOPPING' | 'STOPPED' | 'FAILED';

export interface ArcadeRuntimeContext {
  sessionId: string;
  resourceId: string;
  platform: string;
  adapterId: string;
}

export interface ArcadeRuntimeAdapter {
  readonly adapterId: string;
  canHandle(resource: GameResource): boolean;
  start(context: ArcadeRuntimeContext): Promise<void>;
  stop(context: ArcadeRuntimeContext): Promise<void>;
}

export interface ArcadeSession {
  context: ArcadeRuntimeContext;
  state: RuntimeSessionState;
}

export class BiupiuArcadeRuntime {
  private readonly sessions = new Map<string, ArcadeSession>();

  constructor(
    private readonly registry: NativeResourceRegistry,
    private readonly adapters: ArcadeRuntimeAdapter[] = [],
  ) {}

  launch(resourceId: string, sessionId: string): ArcadeLaunchDecision {
    if (!sessionId.trim()) return { allowed: false, reasons: ['session_id_required'] };

    const decision = this.registry.canLaunch(resourceId);
    if (!decision.allowed) return decision;

    if (this.sessions.has(sessionId)) {
      return { allowed: false, reasons: ['session_already_exists'] };
    }

    const resource = this.registry.get(resourceId);
    if (!resource) return { allowed: false, reasons: ['resource_not_found'] };

    const adapter = this.adapters.find((candidate) => candidate.canHandle(resource));
    if (!adapter) return { allowed: false, reasons: ['runtime_adapter_not_available'] };

    this.sessions.set(sessionId, {
      context: {
        sessionId,
        resourceId,
        platform: resource.platform,
        adapterId: adapter.adapterId,
      },
      state: 'STARTING',
    });

    return { allowed: true, reasons: [] };
  }

  getSession(sessionId: string): ArcadeSession | undefined {
    const session = this.sessions.get(sessionId);
    return session ? structuredClone(session) : undefined;
  }

  async start(sessionId: string): Promise<void> {
    const session = this.sessions.get(sessionId);
    if (!session) throw new Error('session_not_found');
    if (session.state !== 'STARTING') throw new Error('session_not_startable');

    const resource = this.registry.get(session.context.resourceId);
    if (!resource) {
      session.state = 'FAILED';
      throw new Error('resource_not_found');
    }

    const adapter = this.adapters.find((candidate) => candidate.adapterId === session.context.adapterId);
    if (!adapter) {
      session.state = 'FAILED';
      throw new Error('runtime_adapter_not_available');
    }

    try {
      await adapter.start(session.context);
      session.state = 'RUNNING';
    } catch (error) {
      session.state = 'FAILED';
      throw error;
    }
  }

  async stop(sessionId: string): Promise<void> {
    const session = this.sessions.get(sessionId);
    if (!session) throw new Error('session_not_found');
    if (session.state !== 'RUNNING') throw new Error('session_not_stoppable');

    const adapter = this.adapters.find((candidate) => candidate.adapterId === session.context.adapterId);
    if (!adapter) {
      session.state = 'FAILED';
      throw new Error('runtime_adapter_not_available');
    }

    session.state = 'STOPPING';
    try {
      await adapter.stop(session.context);
      session.state = 'STOPPED';
    } catch (error) {
      session.state = 'FAILED';
      throw error;
    }
  }
}
