# Biupiu System Logging, Cross-Division & Component Digital-Twin Protocol v1.0

**Status:** IMPLEMENTED — Phase 2 consolidation
**Date:** 20 September 2026

## Purpose
Convert the repository from vehicle/project-centric indexing into a component-centric cross-division intelligence and catalogue system.

## Core rule
Vehicles, vessels, aircraft, eVTOLs and helicopters are assemblies/applications, not the primary digital-twin object. The primary twin object is the component, subsystem, material, process, algorithm, control module or test article.

## Object hierarchy
PLANT → FEEDSTOCK → MATERIAL → PROCESS → COMPONENT → SUBSYSTEM → ASSEMBLY → PLATFORM → APPLICATION

## Stable ID families
BPU-MAT-#### = material; BPU-PRO-#### = process; BPU-CMP-#### = physical component; BPU-SUB-#### = subsystem; BPU-ALG-#### = algorithm/control; BPU-SIM-#### = simulation/model; BPU-TST-#### = test; BPU-REF-#### = external reference; BPU-CAT-#### = catalogue entry; BPU-PLT-#### = complete platform; BPU-APP-#### = application.

## Cross-division relationship codes
XDIV-MAT, XDIV-AERO, XDIV-ENERGY, XDIV-MFG, XDIV-ROBOT, XDIV-AI, XDIV-OPT, XDIV-MAR, XDIV-AUTO, XDIV-AG.

## Component twin minimum fields
ID; owner; secondary departments; function; geometry revision; material revision; manufacturing revision; simulation revision; evidence state; external references; provenance; licence/IP state; test status; sensor channels; environment; failure modes; uncertainty; dependencies; compatible platforms; catalogue state; superseded-by/derived-from links.

## Evidence promotion
T0 literature candidate → T1 material coupon → T2 laminate/coupon → T3 component test → T4 rotating/subassembly test → T5 controlled prototype → T6 integrated system test → T7 representative environment → T8 independent replication/qualification → T9 production-qualified evidence.

Evidence state is separate from TRL and certification.

## Department allocation
Materials owns formulations, laminates, coatings and material tests. Aerodynamics owns airflow, drag/downforce, air-brake, diffuser and flow-control components. Energy owns turbine/generator/storage/power conversion. Electrical owns HV buses, inverters, motors and electrical machines. Robotics owns actuators/mechatronics. AI/Compute owns optimisation, control software and digital-twin models. Advanced Manufacturing owns manufacturing processes/tooling/automation. Automotive owns vehicle integration. Marine owns vessel integration. Aerospace owns aircraft/eVTOL/helicopter integration. CG-3D owns computational geometry methods; physical components remain with their engineering owner.

## Platform rule
A complete platform gets a platform record and assembly map. Its technical components are referenced by component IDs rather than duplicated.

## Catalogue rule
Catalogue entries point to stable component twins and evidence records. Showroom renders are presentation assets, not engineering evidence.

## Audit rule
No new design is logged until stable ID, owner, evidence state, provenance and cross-links exist.

RESEARCH-INDEX.md remains the discovery index; component twin files are engineering source-of-truth; catalogue files are the controlled presentation layer.
