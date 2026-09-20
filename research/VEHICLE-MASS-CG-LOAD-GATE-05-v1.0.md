# Vehicle Gate 05 — Mass, CG & First-Order Load Ledger

Date: 20 September 2026
Status: EXECUTED — source/ledger framework and boundary-case calculations; physical/CAD measurements OPEN

## Evidence refresh

Current IVECO material confirms the Daily 4x4 range includes 3,480, 3,780 and 4,175 mm wheelbases, with 7,000 kg GVM and 10,500 kg GCM on relevant configurations. The 2026 specification identifies 132 kW at 3,500 rpm and 430 Nm at 1,500 rpm; the 4,175 mm wheelbase remains 7,000 kg GVM. These are manufacturer-published ratings, not measured converted-vehicle values.

Audi technical data available through Audi MediaCenter confirms the R8 ASF architecture and a 2,650 mm wheelbase. A published R8 technical sheet gives 4,429 mm length, 1,940 mm width and 1,236 mm height; these dimensions are retained as envelope references, not proof of the exact first-generation V8 donor configuration.

## Boundary-case axle calculations

Using the Gate 04 equations and treating x as CG distance from the front axle:

### Hypercar — illustrative only
Assume M = 1,000 kg and L = 2,650 mm.

| CG x | Front share | Rear share |
|---:|---:|---:|
| 1,100 mm | 58.5% | 41.5% |
| 1,200 mm | 54.7% | 45.3% |
| 1,300 mm | 50.9% | 49.1% |
| 1,400 mm | 47.2% | 52.8% |

These are mathematical sensitivity cases only. They do not represent the actual R8 donor or the proposed converted vehicle.

### Overlander — illustrative only
Assume M = 7,000 kg and L = 4,175 mm.

| CG x | Front share | Rear share |
|---:|---:|---:|
| 1,700 mm | 59.3% | 40.7% |
| 1,900 mm | 54.5% | 45.5% |
| 2,100 mm | 49.7% | 50.3% |
| 2,300 mm | 44.9% | 55.1% |

Again, these are sensitivity cases and are not an axle-rating approval.

## Mass-ledger control

No target mass is declared achieved. The ledger requires measured/sourced entries for:
- retained chassis/structure
- engine and ancillaries
- transmission/transfer case/differentials/shafts
- motors/inverters/HV battery
- cooling and exhaust
- suspension/brakes
- wheels/tyres
- composite body and bonding
- glazing/closures
- seats/restraints/crash systems
- wiring/control units
- fluids/fuel
- service equipment
- payload
- uncertainty margin

## Load-case preparation

Gate 05 registers, but does not execute FEA:
1. Static axle-load case.
2. Longitudinal acceleration/braking transfer.
3. Lateral load transfer.
4. Combined longitudinal/lateral envelope.
5. Vertical bump/landing load.
6. Powertrain torque reaction.
7. Composite joint/interface load path.
8. Overlander chassis twist/articulation case.

FEA, multibody dynamics, crash simulation and physical testing remain separate validation gates.

## Gate result

EXECUTED:
- current manufacturer evidence refresh
- source boundary clarification
- numerical axle-load sensitivity calculations
- controlled mass-ledger schema
- first-order load-case register

OPEN:
- exact donor year/configuration
- measured component masses
- exact CG
- axle ratings
- CAD geometry
- suspension travel
- structural load paths
- FEA/CAE
- thermal analysis
- crash validation
- physical testing

Next Gate 06: obtain exact donor documentation/measurements and convert the sensitivity ledger into an evidence-backed vehicle mass/CG model before any FEA promotion.
