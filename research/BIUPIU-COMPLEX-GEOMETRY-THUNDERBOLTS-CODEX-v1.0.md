# Biupiu Complex Geometry × Thunderbolts-Inspired CODEX Framework v1.0

**Record:** BPU-RES-CG-TB-001  
**Created:** 16 September 2026  
**Status:** Active research / computational-design framework  
**Domains:** GEOMETRY · COMPUTE/CODEX · ELECTROMAG · PHOTONICS · AERO · MARINE · MATERIALS · NFT-ART · SPEC

## Purpose

Extend the Biupiu computational-geometry and CODEX architecture with a reusable library of complex mathematical shapes and field-inspired structures discussed or illustrated in Thunderbolts Project material. These shapes are treated as **mathematical/computational primitives and research inspiration**, not as proof of the physical or cosmological interpretations presented by Thunderbolts.

Thunderbolts material explicitly discusses geometry, nested Platonic solids, spirals, wave-within-wave structures, plasma filaments, hourglass forms, toroidal structures and stacked toruses. Their material also presents these ideas within the Electric Universe hypothesis. Those source claims remain separately classified and must be independently tested before being treated as scientific conclusions.

## Source anchors

- Thunderbolts Project, **Geometry of the Electric Universe** (Buddy James): geometry, nested Platonic solids, spinning structures, spirals and wave-within-wave/Dougherty-set discussion.
- Thunderbolts Project, **What Is the Electric Universe? / Beginner's Guide**: plasma filaments, spiraling filaments and structured plasma claims.
- Thunderbolts Project, **Electromagnetic Fire** and related solar-plasma pages: plasma torus, rope-like/hollow tendrils and discharge geometry.
- Thunderbolts Project / *Thunderbolts of the Gods*: stacked disks/toruses and Birkeland-current-pair geometry are presented as part of a plasma-discharge interpretation.
- Thunderbolts Project, **Stickman on Stone**: hourglass/toroidal 3-D discharge geometry and rotational invariance are discussed.

## Evidence-control rule

The repository separates:

1. **Mathematics** — exact definitions and reproducible geometry.
2. **Computation** — algorithms that generate, transform, mesh, render or analyse the geometry.
3. **Physical interpretation** — claims about plasma, electromagnetism, cosmology or archaeology.
4. **Artwork** — original visual compositions derived from mathematical procedures.

A successful mathematical reconstruction does **not** validate a physical interpretation. A visually similar natural or archaeological structure does **not** establish common physical origin.

## Shape and structure taxonomy

| ID | Geometry family | Mathematical/computational representation | Primary CODEX use |
|---|---|---|---|
| CG-TORUS-001 | Torus | `(R + r cos v)(cos u, sin u), r sin v` | base primitive, field surface, NFT geometry |
| CG-TORUS-002 | Nested / multi-torus | concentric or recursively scaled toroidal surfaces | multiscale geometry, parameter studies |
| CG-TORUS-003 | Stacked toruses | torus sequence along an axis with variable radii | axial structures, visual morphology studies |
| CG-TORUS-004 | Twisted torus | torus with angular/radial modulation | topology and symmetry studies |
| CG-TORUS-005 | Toroidal field lines | toroidal/poloidal winding curves | vector-field visualisation |
| CG-HELIX-001 | Helix / double helix | parametric helical curves and paired helices | filament and flow geometry |
| CG-BIRK-001 | Braided filament pair | coupled helices with phase/spacing controls | filament topology / visual simulation |
| CG-SPIRAL-001 | Planar spiral | Archimedean/logarithmic/other parameterised spiral | scale and growth studies |
| CG-SPIRAL-002 | 3-D spiral | cylindrical/spherical helical spiral | volumetric structures |
| CG-HOUR-001 | Hourglass / bipolar form | paired lobes, signed axial radius function | morphology and symmetry |
| CG-PLAT-001 | Platonic solids | tetrahedron/cube/octahedron/dodecahedron/icosahedron | nested symmetry / polyhedral studies |
| CG-PLAT-002 | Nested polyhedra | recursively scaled/rotated polyhedra | symmetry and projection studies |
| CG-WAVE-001 | Nested waves | superposed periodic fields with scale ratios | interference / harmonic artwork |
| CG-VORT-001 | Vortex / vortex-ring | circulation-based curve/surface models | flow and topology studies |
| CG-CELL-001 | Cellular / shell structure | implicit surfaces, level sets, periodic cells | materials and morphology |
| CG-FIL-001 | Filament network | graph/curve network with curvature and branching | network geometry and field visualisation |
| CG-MOBIUS-001 | Möbius surface | half-twisted parameterised strip | topology and one-sided surface studies |
| CG-KNOT-001 | Parametric knots | torus knots / Lissajous-type curves | topology and generative art |
| CG-SUPER-001 | Superformula surfaces | generalised polar/spherical modulation | complex natural-form synthesis |

## Core torus parameterisation

For major radius `R > 0`, tube radius `r > 0`, and angles `u,v ∈ [0,2π)`:

`x = (R + r cos(v)) cos(u)`  
`y = (R + r cos(v)) sin(u)`  
`z = r sin(v)`

The CODEX implementation must expose `R`, `r`, angular resolution and transforms as parameters. Degenerate cases and self-intersection rules must be documented when `r >= R`.

## Higher-order toroidal operators

### Toroidal stack
Generate `N` toruses along an axis:

`z_i = z0 + i·Δz`  
`R_i = R0·f_R(i)`  
`r_i = r0·f_r(i)`

Optional phase, tilt, ellipticity and rotation functions produce controlled variants.

### Toroidal braid
Represent each centreline as a helix and sweep a circular/elliptical profile around it. Pair or multiply strands with phase offsets. Preserve the centreline and sweep parameters in the manifest so every rendered object is reproducible.

### Toroidal field visualisation
Separate **geometry** from **physics**. A toroidal/poloidal vector field may be visualised mathematically without claiming that it represents an actual plasma field. Any physical field solver must specify governing equations, boundary conditions, units, numerical method and validation dataset.

## Platonic / nested-solid operators

Implement deterministic constructors for the five Platonic solids, normalise their circumradius/inradius, then support:

- recursive nesting;
- controlled scale ratios;
- rotations around arbitrary axes;
- dual-polyhedron pairing;
- edge/face/vertex graph extraction;
- spherical projection;
- signed-distance or mesh representations.

## Wave-within-wave operator

Represent a family of nested periodic functions:

`F(x,t) = Σ A_k sin(k·ωx + φ_k t + ψ_k)`

where the harmonic/scale sequence is explicit. This is a mathematical superposition model, not evidence for any particular cosmological mechanism.

## Hourglass / bipolar operator

Define a smooth radial envelope around an axial coordinate:

`ρ(z) = ρ_min + (ρ_max - ρ_min)·g(|z|)`

and generate a surface or volumetric field using cylindrical coordinates. Parameterise waist, lobe length, taper, twist and asymmetry independently.

## CODEX architecture

Recommended module family:

`codex/geometry/primitives/torus.py`  
`codex/geometry/primitives/platonic.py`  
`codex/geometry/primitives/spiral.py`  
`codex/geometry/primitives/helix.py`  
`codex/geometry/primitives/vortex.py`  
`codex/geometry/primitives/hourglass.py`  
`codex/geometry/operators/nested.py`  
`codex/geometry/operators/stack.py`  
`codex/geometry/operators/braid.py`  
`codex/geometry/operators/wave_superposition.py`  
`codex/geometry/operators/sweep.py`  
`codex/geometry/analysis/symmetry.py`  
`codex/geometry/analysis/topology.py`  
`codex/geometry/analysis/curvature.py`  
`codex/geometry/export/mesh.py`

Actual source files should be added incrementally with tests; this record does not claim that every module already exists.

## Algorithm-network integration

New algorithms must use the existing lineage:

`RESEARCH ID → ALGORITHM FAMILY/VERSION → PARAMETERS + SEED → ARTWORK RELEASE → MANIFEST → HASHES → BLOCKCHAIN RECORD`

Suggested family registrations:

- `BIU-ALG-GEO-TORUS-001` — toroidal primitive family.
- `BIU-ALG-GEO-NEST-001` — recursive/nested geometry family.
- `BIU-ALG-GEO-BRAID-001` — braided filament family.
- `BIU-ALG-GEO-WAVE-001` — nested-wave/superposition family.
- `BIU-ALG-GEO-VORTEX-001` — vortex and vortex-ring family.
- `BIU-ALG-GEO-SYMM-001` — symmetry/polyhedral analysis family.

Initial versions should remain pre-release until executable implementations, deterministic tests and provenance manifests are present.

## Validation ladder

1. Unit tests for parameterisation and topology.
2. Determinism test: same parameters + seed → identical geometry/hash.
3. Mesh validity: normals, manifold checks where applicable, self-intersection diagnostics.
4. Symmetry metrics and numerical invariants.
5. Comparison with analytic solutions where available.
6. Numerical convergence tests for any field/physics solver.
7. Experimental validation only after a physical model is explicitly defined.

## NFT integration

These geometry families may generate future Biupiu computational artworks. Each artwork must preserve:

- source/research ID;
- geometry family and exact algorithm version;
- parameters;
- seed;
- software/dependency versions;
- generated asset hash;
- provenance artwork hash;
- standalone artwork hash;
- release manifest;
- IP/licence status.

The geometry itself is the computational source material; the Thunderbolts source is provenance/inspiration and must not be represented as ownership of the resulting original artwork.

## Research status

**Classification:** Supported as a mathematical/computational research direction; Thunderbolts physical interpretations remain controlled speculative/hypothesis inputs unless independently verified.  
**Next execution layer:** implement deterministic geometry primitives and tests in CODEX, then register executable versions in the algorithm graph.
