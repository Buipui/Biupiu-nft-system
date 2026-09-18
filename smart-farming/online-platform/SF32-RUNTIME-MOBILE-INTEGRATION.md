# SF-32 — Runtime + Mobile Architecture Integration

## Purpose
Connect the SF-31 simulation contract to the Biupiu World runtime and mobile-app architecture without enabling live publication.

## Integration layers
1. World Launcher
2. Episode Package Loader
3. Scene Resolver
4. Asset Resolver
5. Context Bridge
6. Claim/Rights Guard
7. Mobile Navigation Adapter
8. Digital Lab / Academy Deep-Link Adapter
9. Commerce/Gallery Adapter
10. Verification Reporter

## Mobile route model
- Home
- World
- Episode
- Department
- Research
- Digital Lab
- Academy
- Gallery
- Marketplace
- Profile

The same stable IDs must work across desktop/world and mobile interfaces.

## Runtime contract
Required session fields:
user_id, episode_id, scene_id, department_id, hero_asset_id, avatar_id, property_id, lesson_id, experiment_id.

## Mobile constraints
- Touch-first navigation.
- Responsive 16:9/9:16 media handling.
- Low-bandwidth fallback for previews.
- Deferred loading of heavy 3D assets.
- Accessibility captions and readable status labels.
- No live purchase action unless commerce service explicitly reports availability.

## Guard
The Claim/Rights Guard must prevent unapproved or rights-incomplete assets from becoming publicly active runtime content.

Live runtime remains disabled until SF-32 verification passes and human release approval is recorded.
