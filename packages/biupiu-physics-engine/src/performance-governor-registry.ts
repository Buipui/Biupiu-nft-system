export type GovernorState = "REFERENCE" | "INTEGRATED_CONTRACT" | "RUNTIME_VERIFIED";

export interface PerformanceGovernorContract {
  id: string;
  family: "zram" | "cpufreq" | "devfreq-gpu";
  source: string;
  license: "GPL-2.0-only" | "GPL-2.0-or-later" | "Apache-2.0" | "REFERENCE_ONLY";
  capabilities: readonly string[];
  safety: "ADVISORY_ONLY" | "BOUNDED_CONTROL";
  state: GovernorState;
}

export const PERFORMANCE_GOVERNOR_PROVIDERS: readonly PerformanceGovernorContract[] = [
  {
    id: "linux-zram",
    family: "zram",
    source: "https://docs.kernel.org/admin-guide/blockdev/zram.html",
    license: "GPL-2.0-only",
    capabilities: [
      "compressed-ram-block-device",
      "swap-backed-memory",
      "compression-algorithm-selection",
      "multi-compressor-recompression",
      "writeback-and-idle-recompression",
      "sysfs-observability",
    ],
    safety: "ADVISORY_ONLY",
    state: "INTEGRATED_CONTRACT",
  },
  {
    id: "linux-cpufreq-schedutil",
    family: "cpufreq",
    source: "https://docs.kernel.org/admin-guide/pm/cpufreq.html",
    license: "GPL-2.0-only",
    capabilities: ["scheduler-utilization-driven-frequency-selection", "policy-tunables", "cpu-capacity-scaling"],
    safety: "ADVISORY_ONLY",
    state: "INTEGRATED_CONTRACT",
  },
  {
    id: "linux-cpufreq-performance-powersave",
    family: "cpufreq",
    source: "https://docs.kernel.org/admin-guide/pm/cpufreq.html",
    license: "GPL-2.0-only",
    capabilities: ["maximum-frequency-request", "minimum-frequency-request", "policy-bounds"],
    safety: "ADVISORY_ONLY",
    state: "INTEGRATED_CONTRACT",
  },
  {
    id: "linux-devfreq-gpu",
    family: "devfreq-gpu",
    source: "https://docs.kernel.org/driver-api/devfreq.html",
    license: "GPL-2.0-only",
    capabilities: ["device-frequency-scaling", "busy-time-feedback", "governor-selection", "opp-table-awareness"],
    safety: "ADVISORY_ONLY",
    state: "INTEGRATED_CONTRACT",
  },
  {
    id: "android-qcom-adreno-devfreq",
    family: "devfreq-gpu",
    source: "https://android.googlesource.com/kernel/msm.git/+/refs/heads/main/drivers/gpu/msm/Kconfig",
    license: "GPL-2.0-only",
    capabilities: ["adreno-devfreq", "simple-ondemand", "performance", "adreno-tz", "gpu-bandwidth-monitor"],
    safety: "ADVISORY_ONLY",
    state: "INTEGRATED_CONTRACT",
  },
];

export interface GovernorTuningModel {
  id: string;
  inputs: readonly string[];
  outputs: readonly string[];
  constraints: readonly string[];
  promotion: "PROPOSE_ONLY";
}

export const BIUPIU_GOVERNOR_TUNING_MODELS: readonly GovernorTuningModel[] = [
  {
    id: "load-latency-energy-model-v1",
    inputs: ["cpu-utilization", "gpu-busy-time", "memory-pressure", "thermal-state", "frame-latency", "battery-state"],
    outputs: ["recommended-cpufreq-policy", "recommended-gpu-devfreq-policy", "zram-compression-profile"],
    constraints: [
      "never writes hardware controls directly",
      "respect platform min/max bounds",
      "thermal throttling is authoritative",
      "unknown telemetry fails closed",
      "recommendation requires runtime evidence",
    ],
    promotion: "PROPOSE_ONLY",
  },
  {
    id: "zram-memory-pressure-model-v1",
    inputs: ["available-memory", "swap-pressure", "compression-ratio", "compress-decompress-latency", "page-temperature"],
    outputs: ["recommended-compressor", "recommended-recompression-policy"],
    constraints: [
      "algorithm availability must be observed from the target zram device",
      "compression parameters are algorithm-specific",
      "no writeback/recompression claim without device support",
    ],
    promotion: "PROPOSE_ONLY",
  },
];

export function performanceGovernorContractSmokeTest(): boolean {
  return PERFORMANCE_GOVERNOR_PROVIDERS.length >= 5 &&
    BIUPIU_GOVERNOR_TUNING_MODELS.length === 2 &&
    PERFORMANCE_GOVERNOR_PROVIDERS.every((provider) => provider.state === "INTEGRATED_CONTRACT") &&
    BIUPIU_GOVERNOR_TUNING_MODELS.every((model) => model.promotion === "PROPOSE_ONLY");
}
