export type RenderEngine = "BLENDER_CYCLES"|"OCTANE"|"V_RAY"|"UNREAL_ENGINE_5"|"TWINMOTION"|"LUMION"|"KEYSHOT";

export const RENDER_ENGINE_ROUTE: Record<RenderEngine, { role: string; proprietary: boolean }> = {
  BLENDER_CYCLES: { role: "baseline_path_tracer", proprietary: false },
  OCTANE: { role: "gpu_path_tracer", proprietary: true },
  V_RAY: { role: "production_path_tracer", proprietary: true },
  UNREAL_ENGINE_5: { role: "real_time_virtual_production", proprietary: true },
  TWINMOTION: { role: "rapid_real_time_visualization", proprietary: true },
  LUMION: { role: "environment_visualization", proprietary: true },
  KEYSHOT: { role: "product_visualization", proprietary: true }
};