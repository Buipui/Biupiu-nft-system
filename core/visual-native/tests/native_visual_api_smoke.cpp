#include "../include/biupiu_visual_native.h"
#include <cassert>
int main() {
  biupiu_visual_capabilities caps{};
  assert(biupiu_visual_get_capabilities(&caps)==BIUPIU_VISUAL_OK);
  assert(caps.api_version==BIUPIU_VISUAL_API_V1);
  biupiu_render_request req{};
  req.scene_asset=1; req.backend=BIUPIU_RENDER_NATIVE; req.width=320; req.height=180;
  req.frame_start=1; req.frame_end=1; req.frame_rate=24.0;
  biupiu_visual_job job=0;
  assert(biupiu_visual_render_submit(&req,&job)==BIUPIU_VISUAL_OK);
  uint32_t state=99;
  assert(biupiu_visual_job_status(job,&state)==BIUPIU_VISUAL_OK);
  assert(biupiu_visual_job_cancel(job)==BIUPIU_VISUAL_OK);
  assert(biupiu_visual_release(job)==BIUPIU_VISUAL_OK);
  return 0;
}
