#ifndef BIUPIU_VISUAL_PROVIDER_VALIDATION_H
#define BIUPIU_VISUAL_PROVIDER_VALIDATION_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef struct {
  const char* provider;
  const char* version;
  uint8_t discovered;
  uint8_t linked;
  uint8_t runtime_probe;
  uint8_t deterministic_pass;
  uint8_t state;
  uint64_t input_hash;
  uint64_t output_hash;
} biupiu_visual_provider_validation;
int biupiu_visual_provider_validate(const char* provider, const void* input, uint64_t input_size,
                                    const void* canonical_output, uint64_t output_size,
                                    biupiu_visual_provider_validation* out);
#ifdef __cplusplus
}
#endif
#endif
