# SF-16 — Biupiu Department Vehicle Showcase System

Date: 2026-09-18

## Purpose
Biupiu World vehicles are original digital representations of vehicles, machines and mobility concepts associated with Biupiu's real-world departments. They are primarily **parked showcase assets** used for advertising, education, product storytelling and future interactive demonstrations.

They are not copies of GTA V, Forza, Assassin's Creed or other proprietary game vehicles.

## Showcase model
Each department can have a dedicated vehicle or machine displayed at:
- department headquarters
- research campus
- showroom
- marketplace
- academy
- Digital Lab
- relevant environment/field site

A parked vehicle acts as a digital billboard with optional interaction.

## Department-to-vehicle mapping
Initial catalogue:
- Regenerative Agriculture -> smart farm utility vehicle
- Plant Research -> mobile plant-research laboratory
- Conservation -> field conservation vehicle
- Textiles/Fibres -> mobile fibre/materials transport
- Composite Materials -> materials demonstrator vehicle
- Biochemical Research -> mobile biochemical laboratory
- Genetics & Seed Breeding -> controlled research transport
- Advanced Materials -> materials testing vehicle
- Robotics/Automation -> autonomous robotics support vehicle
- AI/Intelligence Hub -> mobile AI research/command vehicle
- Photonics/Optical Communications -> optical communications demonstrator
- Energy Systems -> energy research vehicle
- Marine/Hydrofoil -> Biupiu marine research craft
- Academy -> mobile training/showcase vehicle
- Digital Gallery/NFT -> branded gallery/showcase vehicle
- Logistics/Manufacturing -> low-emission logistics vehicle

## Advertising interaction
Selecting a parked vehicle can open:
1. department overview
2. product/service description
3. specifications
4. research projects
5. Digital Lab experiments
6. Academy courses
7. gallery/media
8. contact/enquiry pathway
9. future catalogue/purchase pathway

## Vehicle presentation states
- PARKED_SHOWCASE
- INTERACTIVE_DISPLAY
- RESEARCH_DEMO
- FIELD_SIMULATION
- FUTURE_DRIVEABLE

The initial SF-16 implementation uses PARKED_SHOWCASE as the default state.

## Branding
Vehicles should use the approved Biupiu visual identity and department-specific visual language while remaining visually coherent across the world.

## Reality boundary
If a vehicle is conceptual rather than commercially manufactured, the UI must label it as a concept, prototype, simulation or research design. Marketing copy must not imply physical availability unless it exists and is actually offered.

## Future expansion
The same vehicle record can later support:
- 3D product configurator
- engineering specification views
- telemetry
- Digital Lab experiments
- virtual test drives
- customer enquiries
- commercial product pages
- AR/mobile experiences
