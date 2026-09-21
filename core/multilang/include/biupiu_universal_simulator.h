#pragma once
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    const char* simulation_id;
    const char* simulator_id;
    const char* domain;
    const char* model_version;
    const char* source_commit;
    const char* units;
    double time_s;
    double dt_s;
    uint64_t seed;
} BiupiuSimContext;

typedef struct {
    double input_hash64;
    double output_hash64;
    double residual;
    double confidence;
    uint32_t flags;
} BiupiuSimObservation;

/* 0 success; negative values reject malformed state. */
int biupiu_sim_validate_context(const BiupiuSimContext* ctx);
int biupiu_sim_record_observation(const BiupiuSimContext* ctx,
                                  double input_hash64,
                                  double output_hash64,
                                  double residual,
                                  double confidence,
                                  uint32_t flags,
                                  BiupiuSimObservation* out);

#ifdef __cplusplus
}
#endif
