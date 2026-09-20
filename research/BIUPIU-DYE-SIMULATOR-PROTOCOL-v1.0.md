# Biupiu Natural Colour / Dye Simulator Protocol v1.0

**Status:** IMPLEMENTED — research/configuration layer

## Objective
Model expected colour output of plant- and fruit-derived dyes across textiles and selected bio-material surfaces while keeping prediction separate from measured colour.
## Inputs
plant/feedstock species and cultivar; plant part; maturity/growing conditions; extraction method/solvent/temperature/time/pH; concentration; mordant or bio-mordant; fibre/substrate; dyeing temperature/time; post-treatment; drying/curing; exposure conditions.
## Outputs
predicted colour family; predicted CIELAB range; RGB/HEX visual approximation; colour-strength estimate; fastness risk; reproducibility risk; substrate compatibility; recommended measurement test; provenance and literature links.
## Candidate feedstock library
Pomegranate peel/rind; orange/citrus peel; lemon peel; banana peel; avocado skins/pits; grape/pomace; berry residues; hibiscus; annatto; turmeric; saffron; papaya; indigo; woad; madder; eucalyptus; walnut; acacia/black wattle; tea; coffee; tannin-rich bark/leaf residues.
## Calibration rule
The simulator must not output a single authoritative HEX value from feedstock alone. Natural colour varies with source, maturity, extraction, water chemistry, mordant and substrate. Output ranges and uncertainty; measured CIELAB/spectral calibration is required before a colour becomes a production specification.
## Cross-links
TEXTILES → BPU-COL → BPU-TEX → dye recipe → colour measurement → fastness record.
COAT → BPU-COL → resin/adhesive/coating compatibility → ageing/UV/chemical testing.
COMPOSITES → BPU-COL → resin/pigment dispersion → laminate coupon → mechanical/thermal/weathering record.
## Digital twin objects
BPU-SIM-COL-001 = natural dye colour-prediction model.
BPU-TST-COL-001 = colour measurement/calibration campaign.
BPU-ALG-COL-001 = colour-space conversion/configuration engine.