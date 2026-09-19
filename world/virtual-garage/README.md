# Biupiu Virtual Garage & Digital Workshop

The Virtual Garage is the spatial R&D environment for the Automotive Digital Twin.

## Zones
1. Vehicle intake / scanning
2. Configuration bay
3. Parts library
4. Materials laboratory
5. Powertrain/dyno bay
6. Suspension and wheel-clearance rig
7. Aerodynamics review bay
8. Manufacturing/robotics cell
9. Presentation/showreel bay
10. Archive/provenance terminal

## World integration
The garage consumes Biupiu World environment assets and the shared Vehicle Digital Twin. Vehicle configurations can be instantiated as persistent workshop states.

## Unreal Engine 5 target
The eventual UE5 implementation should expose:
- VehicleTwin actor
- CustomizationManager
- PartSlot components
- MaterialParameterController
- PerformanceSimulationAdapter
- WorkshopCameraRig
- BuildRevisionSave/Load
- AssetLicenceValidator

## Local R&D mode
The workshop is intended to run locally with the user's Unreal installation and local asset library. No cloud dependency is required for the core configuration model.

## IP boundary
NFSU2 is used only as a reference for modular customization UX and technical categories. Biupiu assets must be original, user-created, licensed or otherwise legally usable.
