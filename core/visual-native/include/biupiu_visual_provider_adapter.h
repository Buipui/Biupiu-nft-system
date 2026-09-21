#ifndef BIUPIU_VISUAL_PROVIDER_ADAPTER_H
#define BIUPIU_VISUAL_PROVIDER_ADAPTER_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef enum {
  BIUPIU_PROVIDER_ADAPTER_UNAVAILABLE = 0,
  BIUPIU_PROVIDER_ADAPTER_CONTRACT_ONLY = 1,
  BIUPIU_PROVIDER_ADAPTER_HOST_READY = 2
} biupiu_provider_adapter_state;
typedef struct {
  const char* name;
  const char* version;
  uint64_t capabilities;
  biupiu_provider_adapter_state state;
} biupiu_provider_adapter_info;
int biupiu_provider_adapter_usd(biupiu_provider_adapter_info* out);
int biupiu_provider_adapter_otio(biupiu_provider_adapter_info* out);
int biupiu_provider_adapter_opensubdiv(biupiu_provider_adapter_info* out);
int biupiu_provider_adapter_execute(const char* provider, char* output, uint32_t capacity, uint32_t* written);
int biupiu_provider_adapter_run_usd_fixture(uint64_t* canonical_output_hash);
#ifdef __cplusplus
}
#endif
#endif
