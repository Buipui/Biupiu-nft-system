# Biupiu Toroidal Geometry × Electrical & Photovoltaic R&D

**Record:** BPU-RES-TORUS-001  
**Status:** Research / hypothesis-development  
**Date:** September 2026

## Purpose

This record establishes **torus / toroidal geometry** as a cross-disciplinary computational research primitive for the Biupiu repository. It links computational geometry to electrical engineering, electromagnetics, photonics and photovoltaic engineering.

A torus is treated here as a geometric structure that can be modelled, parameterised and experimentally tested. Artistic or unconventional interpretations remain hypotheses unless independently validated.

## Core geometry parameters

- Major radius `R`
- Minor radius `r`
- Aspect ratio `R/r`
- Cross-section: circular, elliptical or custom
- Surface winding / channel path
- Symmetry order and periodicity
- Material and refractive-index distribution
- Electrical and optical boundary conditions

## Research branches

### 1. Toroidal electromagnetics

Investigate electric and magnetic field distributions, inductance, leakage flux, resonant modes, radiation loss, multipole moments and coupled toroidal/electric/magnetic excitations.

ResearchGate literature reports toroidal dipole and toroidal-metasurface behaviour, including high-Q resonances, near-field localisation and radiation-control mechanisms. A 2026 study also investigates nonlinear generation control with torus metasurfaces.  
Sources: 
- https://www.researchgate.net/publication/357409096_Toroidal_electromagnetically_induced_transparency_based_meta-surfaces_and_its_applications
- https://www.researchgate.net/publication/305715767_Dual-band_toroidal-dipole-induced_transparency_in_optical_regime
- https://www.researchgate.net/publication/403299952_Nonlinear_generation_control_with_torus_metasurfaces

### 2. Toroidal electrical machines and magnetics

Model toroidal cores, windings and axial-flux/permanent-magnet machine geometries. Key variables include winding topology, leakage flux, core losses, thermal loading, efficiency and manufacturability.

Emerald's COMPEL literature includes FEM-backed analysis of a TORUS-type non-slotted axial-flux permanent-magnet machine and research on toroidal windings, winding factor and Joule-loss/thermal behaviour. Emerald also contains toroidal-coordinate field expansions and toroidal-core magnetic-loss modelling.

Sources:
- https://www.emerald.com/insight/content/doi/10.1108/compel-05-2017-0196/full/pdf
- https://www.emerald.com/compel/article-abstract/31/1/88/88906/Investigation-of-winding-topologies-for-permanent-magnet-in-wheel-motors
- https://www.emerald.com/compel/article-abstract/28/4/1044/91872/Plane-elliptic-or-toroidal-multipole-expansions
- https://www.emerald.com/compel/article-abstract/38/6/1874/113068/Modeling-of-core-loss-for-non-oriented-electrical

### 3. Toroidal photovoltaic concentration

Investigate toroidal concentrators, receiver placement, non-uniform illumination, bifacial PV receivers, optical losses, concentration ratio and thermal management.

ResearchGate hosts a peer-reviewed Energy Reports study specifically on **solar-energy toroidal concentrators** and identifies toroidal concentrators as a route for concentrating solar radiation onto photovoltaic receivers while discussing limitations and design economics.

Source:
- https://www.researchgate.net/publication/356280467_Solar_energy_toroidal_concentrators

### 4. Toroidal optical waveguides for solar systems

Model circular-cross-section torus waveguides using total internal reflection, coupling solar radiation to photovoltaic or thermal receivers. Parameters should include bend radius, refractive index, absorption, scattering, aperture geometry and receiver coupling efficiency.

ResearchGate records a 2025 study evaluating optical efficiency of a torus waveguide for solar-energy transmission to a solar cell or thermal reservoir using Zemax OpticStudio simulations.

Source:
- https://www.researchgate.net/publication/402343649_Evaluation_of_Optical_Efficiency_of_Circular_Cross-Section_Torus_Waveguide_via_Changing_the_Optical_Parameters

### 5. Photovoltaic electrical modelling

Keep the photovoltaic device/electrical model connected to the toroidal optical model rather than treating optical concentration as a standalone concept.

Recommended simulation chain:

`Solar spectrum → toroidal optical geometry → irradiance distribution → PV I–V model → MPPT/DC conversion → storage → load`

Emerald COMPEL literature includes a photovoltaic-generator equivalent-circuit approach using nonlinear I–V equations and Newton–Raphson numerical treatment.

Source:
- https://www.emerald.com/insight/content/doi/10.1108/03321641211227492/full/pdf

### 6. Broader Biupiu electrical / energy R&D cross-links

This toroidal stream should cross-reference the repository's existing work on:

- photovoltaic conversion and light harvesting
- quantum-dot solar-cell concepts
- photovoltaic + battery systems
- photovoltaic + supercapacitor systems
- light-based energy storage and conversion
- hemp-based energy-storage concepts / supercapacitor research
- crystal and materials research
- photonic communications and optical energy delivery
- structured light and optical field control
- optical / photonic computing
- atmospheric optical propagation
- electromagnetic and resonant-material simulation
- electrical machinery, generators and power-electronics modelling
- computational geometry and generative CAD

## Proposed testable experiments

**TORUS-PV-01:** Compare a conventional planar/reflective concentrator with a parameterised toroidal concentrator under identical incident irradiance.

**TORUS-PV-02:** Sweep `R/r`, receiver position and refractive-index distribution for a toroidal waveguide and measure coupling efficiency.

**TORUS-EM-01:** Perform FEM/FDTD multipole decomposition to distinguish electric, magnetic and toroidal contributions.

**TORUS-MAG-01:** Compare toroidal-core and conventional-core inductors/transformers for inductance, leakage, temperature rise and loss.

**TORUS-AFPM-01:** Model toroidal winding layouts for axial-flux/permanent-magnet machine concepts and compare Joule loss, cooling and torque density.

**TORUS-STORAGE-01:** Evaluate whether toroidal geometry provides a measurable advantage in thermal, electromagnetic or packaging characteristics for energy-storage subsystems. No performance advantage is assumed before testing.

## Evidence classification

- **Established / supported:** Toroidal geometry is a valid mathematical and engineering geometry; toroidal electrical-machine, magnetic-field, metamaterial, waveguide and PV-concentrator research exists.
- **Plausible model:** Geometry-specific optimisation may improve a particular optical, magnetic, thermal or packaging objective.
- **Unresolved:** Any claim that a toroidal form inherently creates anomalous energy, self-sustaining power, over-unity output or other violation of conservation laws.
- **Speculative / inspirational:** Historical or unconventional energy interpretations of toroidal forms.

## Research integrity rule

The presence of a toroidal geometry in a computational model or artwork does not establish a physical effect. All proposed advantages must be compared with conventional control geometries using measurable quantities and reproducible simulation/experimental conditions.

## Source-network rule

ResearchGate is used for discovery and source-level cross-referencing. Emerald Insight is used as an additional scholarly source network, particularly for electrical machines, electromagnetics, FEM, power systems and photovoltaic modelling. Individual papers remain subject to their own evidence quality, licensing and peer-review status.
