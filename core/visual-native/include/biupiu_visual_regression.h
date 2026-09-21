#ifndef BIUPIU_VISUAL_REGRESSION_H
#define BIUPIU_VISUAL_REGRESSION_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef struct {
  uint64_t fixture_id;
  uint64_t input_hash;
  uint64_t output_hash;
  uint32_t frame;
  uint32_t pass;
} biupiu_visual_regression_record;
uint64_t biupiu_visual_regression_hash_bytes(const void* data, uint64_t size);
int biupiu_visual_regression_make(uint64_t fixture_id, uint32_t frame,
                                  const void* input, uint64_t input_size,
                                  const void* output, uint64_t output_size,
                                  biupiu_visual_regression_record* out);
int biupiu_visual_regression_compare(const biupiu_visual_regression_record* expected,
                                     const biupiu_visual_regression_record* actual);
#ifdef __cplusplus
}
#endif
#endif
