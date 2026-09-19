# Biupiu UE5 Architecture

```
Research / Experiments
        |
        v
Digital Twin Schemas + validated data
        |
        +-------------------+
        |                   |
        v                   v
Python simulators       Unreal Engine 5
                            |
             +--------------+--------------+
             |              |              |
          World          Digital Twin    Showcase
             |              |              |
             +--------------+--------------+
                            |
                     Windows / Android
```

UE5 is the presentation/interactive simulation layer, not the canonical research database.

## Repository mappings
- packages/biupiu-rnd-os → BiupiuCore/Data integration
- packages/biupiu-showcase → BiupiuShowcase
- packages/biupiu-civilisation-world + world/ → BiupiuWorld
- digital-twin/ → BiupiuDigitalTwin
- simulators/ → BiupiuSimulation adapters
- showcase/ → UE render/cinematic asset pipeline
- apps/windows/ → primary desktop host
- apps/android/ → mobile control/runtime integration
