#include "biupiu_universal_simulator.h"
#include <cmath>
#include <cstdint>

static bool finite(double v) { return std::isfinite(v); }

extern "C" int biupiu_sim_validate_context(const BiupiuSimContext* ctx) {
    if (!ctx || !ctx->simulation_id || !ctx->simulator_id || !ctx->domain ||
        !ctx->model_version || !ctx->source_commit || !ctx->units) return -1;
    if (!*ctx->simulation_id || !*ctx->simulator_id || !*ctx->domain ||
        !*ctx->model_version || !*ctx->source_commit || !*ctx->units) return -2;
    if (!finite(ctx->time_s) || !finite(ctx->dt_s) || ctx->dt_s <= 0.0) return -3;
    return 0;
}

extern "C" int biupiu_sim_record_observation(const BiupiuSimContext* ctx,
                                             double input_hash64,
                                             double output_hash64,
                                             double residual,
                                             double confidence,
                                             uint32_t flags,
                                             BiupiuSimObservation* out) {
    if (biupiu_sim_validate_context(ctx) != 0 || !out) return -1;
    if (!finite(input_hash64) || !finite(output_hash64) || !finite(residual) ||
        !finite(confidence) || confidence < 0.0 || confidence > 1.0) return -2;
    out->input_hash64 = input_hash64;
    out->output_hash64 = output_hash64;
    out->residual = residual;
    out->confidence = confidence;
    out->flags = flags;
    return 0;
}
