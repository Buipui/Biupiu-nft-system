# BIUPIU Colour & Material Catalogue v1.0

**Status:** IMPLEMENTED — Phase 2 catalogue
**Date:** 20 September 2026

## Purpose
Unified catalogue for colour, pigments, bio-resins, adhesives, coatings, vinyl/PPF, composites and textiles. A colour is not treated as a single RGB value: each catalogue record binds appearance to substrate, finish, material chemistry, provenance and evidence.

## Existing Biupiu colour architecture
Historical Biupiu records established AP Automotive, AX Armour, EL Eco-Living, TX Textiles, CR Resin, BP Biomaterial Pigments, BA building/bio-adhesive context, SF Surface Finish, WR Wrap, AD Adhesive, CG Computational Graphics and CN Cellulose Nanomaterials. Current ownership: TEXTILES owns fibre/textile dyeing; COAT owns adhesives/coatings/graphic materials including PPF/wrap; COMPOSITES owns natural-fibre/advanced composite panels; MATERIALS owns advanced-material records; AUTOMOTIVE owns vehicle integration.

## Colour record
BPU-COL-####
Required: ID; name; family; source; plant/feedstock; extraction/process; pigment/dye chemistry where known; substrate; finish; CIELAB; RGB/HEX preview; spectral data when available; fastness; transparency/opacity; gloss; metallic/pearlescent status; resin compatibility; adhesive compatibility; textile compatibility; vinyl/film compatibility; provenance; references; evidence state; formulation/twin links.

## Product catalogue codes
CAT-COL-#### colour | CAT-RES-#### resin | CAT-ADH-#### adhesive | CAT-WRAP-#### vinyl/wrap | CAT-TEX-#### textile | CAT-CMP-#### composite | CAT-FIN-#### finish

## Initial colour families
BIUPIU Core: Deep Forest, Biotech Emerald, Teal Flow, Warm Gold, Pale Gold, Soft Ivory, Carbon Black.
Carbon/Luxury: Black Diamond, Forged Carbon, Graphite, Smoke, Titanium Grey.
Botanical: Olive Leaf, Hemp Leaf, Moss, Sage, Fern, Bamboo, Eucalyptus.
Earth/Mineral: Terracotta, Clay, Ochre, Umber, Sand, Basalt, Slate.
Fruit/Anthocyanin: Pomegranate, Berry, Hibiscus, Plum, Grape.
Carotenoid: Annatto, Turmeric, Saffron, Papaya, Citrus.
Indigo: Indigo, Woad Blue.
Tannin: Bark Brown, Walnut, Acacia, Tea, Coffee.
Premium Italian-inspired working names: Rosso Heritage, Verde Atelier, Blu Modena, Oro Satinato, Argento Titanio. These are Biupiu working names, not Ferrari/Pagani trademarks or colour claims.

## Reference architecture
Pagani uses a real-time configurator with deep personalisation and HQ photorealistic output; its showroom model combines digital visualisation with physical colour/leather samples. Ferrari Tailor Made combines themed collections with leather, Alcantara, wool, cashmere, corduroy, denim, technical fabrics, Kevlar and carbon-fibre trims. Biupiu adopts the material-first studio approach but adds provenance and measured material-performance metadata.

## NFS reference
Need for Speed II provides the historical baseline of preset factory colour swatches. Later NFS generations add custom colour, HSB/PBR controls and vinyl/livery systems. Biupiu uses the simple swatch layer first, then exposes advanced colour/material controls.

## Natural-colour rule
Plant and fruit colour research supports roots, bark, leaves, flowers, fruits and agricultural by-products. Natural dyes require process-specific testing because shade reproducibility and fastness depend on feedstock, extraction, mordant, fibre and process conditions.

## Catalogue rule
Digital preview colour is labelled visual approximation until measured material data exists. A render colour is never represented as a tested pigment/resin/vinyl formulation.