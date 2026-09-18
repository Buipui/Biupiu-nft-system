# Biupiu KeyShot Integration Architecture v1.0

## Position in Biupiu R&D OS

CAD / Blender / Unreal Engine 5 / Twinmotion
        |
        v
  Asset Preparation
        |
        v
 KeyShot Connector
   |        |
   |        +--> Material / HDRI Profiles
   |
   +------------> Camera / Render Profiles
        |
        v
 Professional Render Outputs
        |
        +--> Biupiu Showcase
        +--> Product Development Showreel
        +--> Digital Twin Review
        +--> Investor / presentation assets

## Package
@biupiu/keyshot-visualization

## Core responsibilities
- Track licensed KeyShot installation/configuration.
- Maintain render-profile metadata.
- Maintain material/HDRI provenance records.
- Define import/export hand-off points.
- Keep proprietary KeyShot content outside the repository.
- Connect render jobs to Showcase and Digital Twin asset IDs.

## Initial render profiles
- automotive-concept
- marine-concept
- evtol-helicopter
- microturbine
- biocomposite
- bio-adhesive-resin
- textile-fibre
- product-hero
- engineering-exploded
- turntable-showreel

## Asset provenance
Every external asset should record:
- source URL
- author/vendor
- license
- acquisition date
- allowed use
- modification rights
- redistribution restriction
- local asset hash when applicable

## Security/legal boundary
The package contains schemas, metadata and adapters only. It must not redistribute KeyShot installers, license files, activation credentials or proprietary libraries.
