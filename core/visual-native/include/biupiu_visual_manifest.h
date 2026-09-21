#ifndef BIUPIU_VISUAL_MANIFEST_H
#define BIUPIU_VISUAL_MANIFEST_H
#ifdef __cplusplus
extern "C" {
#endif
typedef struct { const char* asset_id; const char* source; const char* input_hash; const char* provider; const char* output_hash; const char* license; } biupiu_visual_manifest_record;
int biupiu_visual_manifest_validate(const biupiu_visual_manifest_record* r);
int biupiu_visual_manifest_write(const biupiu_visual_manifest_record* r,const char* path);
#ifdef __cplusplus
}
#endif
#endif
