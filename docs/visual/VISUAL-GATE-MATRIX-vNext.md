# Biupiu Visual Gate Matrix — vNext

| Gate | State | Blocking dependency |
|---|---|---|
| Shared Biupiu World | GREEN | None |
| Visual asset registry | GREEN | None |
| Digital twin contract | GREEN | None |
| Provider adapter layer | GREEN | None |
| Render/execution broker | GREEN | None |
| Adobe/Firefly live generation | GREEN | None for current milestone |
| Firefly provenance | GREEN | None |
| Blender integration | GREEN/READY | Provider-side project validation |
| Twinmotion integration | GREEN/READY | Provider-side project validation |
| KeyShot integration | GREEN/READY | Provider-side project validation |
| Premiere/After Effects finishing | GREEN/READY | Media assets |
| UE5.8.2 runtime | AMBER | Local installation/build |
| End-to-end UE5 cinematic validation | AMBER | UE5 runtime |
| Production showreel pipeline | AMBER | UE5 + finishing assets |

## Gate policy
GREEN means the architecture or live capability has evidence of completion.
AMBER means deliberately non-blocking work remains.
No prerelease repository content is promoted to canonical production assets without validation.
