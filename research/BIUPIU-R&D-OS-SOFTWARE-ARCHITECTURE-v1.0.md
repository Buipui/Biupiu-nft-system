# Biupiu R&D OS — Software Architecture v1.0

**Status:** Product architecture / reference specification  
**Repository role:** R&D OS reference implementation and validation environment  
**Date:** 18 September 2026

## 1. Purpose

Biupiu R&D OS is the proposed commercial software layer built from the Biupiu Research & Innovation Centre architecture. It is intended to provide a unified operating environment for research, engineering, experimentation, innovation management, evidence control, intellectual-property protection, simulation, prototyping and technology development.

The repository remains the research/reference environment. The commercial product must be developed as a separate software product with its own codebase, security model, customer data boundary, licensing terms and deployment infrastructure.

## 2. Product positioning

The product sits across several established software categories rather than functioning as a conventional electronic laboratory notebook alone:

- Research data and electronic laboratory notebook (ELN)
- Innovation management
- Experimental planning and control
- Engineering simulation orchestration
- Technology readiness and evidence management
- Knowledge graph / research intelligence
- IP and prior-art workflow
- Digital-twin and manufacturing workflow integration
- Portfolio and commercialisation management

Existing products demonstrate commercial demand for parts of this space. LabArchives provides ELN, research-data management, collaboration, auditability and enterprise plans; Benchling provides a unified scientific data model, workflows, APIs and R&D connectivity. Biupiu's proposed differentiation is the integration of the research-to-validation-to-invention lifecycle across scientific, engineering, materials, agriculture, photonics, robotics and other multidisciplinary domains.

## 3. Core lifecycle

```text
PROJECT
  ↓
RESEARCH OBJECT
  ↓
SOURCE → CLAIM → HYPOTHESIS
  ↓
MODEL → SIMULATION
  ↓
EXPERIMENT → DATASET → RESULT
  ↓
VALIDATION → REPLICATION
  ↓
TECHNOLOGY READINESS / EVIDENCE
  ↓
IP / PRIOR ART
  ↓
PROTOTYPE
  ↓
PRODUCT / LICENCE / DEPLOYMENT
```

Every transition should be traceable, versioned and permission-aware.

## 4. Platform architecture

### Layer A — Identity and tenancy
- Organisation/workspace management
- Users, teams, roles and permissions
- Multi-tenant architecture
- Project and department boundaries
- SSO/MFA-ready enterprise identity
- Tenant-level encryption and retention policies

### Layer B — Research object model
Core entities:

`Organisation`, `User`, `Project`, `Department`, `ResearchObject`, `Source`, `Claim`, `Hypothesis`, `Model`, `Experiment`, `Dataset`, `Measurement`, `Result`, `Replication`, `Failure`, `Material`, `Algorithm`, `Prototype`, `Technology`, `IPAsset`, `Patent`, `PriorArt`, `Product`, `Licence`, `Collaboration`, `Decision`, `AuditEvent`.

Every object receives a stable identifier, version, owner, status, evidence state and provenance chain where applicable.

### Layer C — Evidence engine
Evidence states:

`ESTABLISHED`, `SUPPORTED`, `PRELIMINARY`, `HYPOTHESIS`, `SPECULATIVE`, `CONTRADICTED`, `INCONCLUSIVE`.

The software must prevent speculative or unverified information from silently appearing as established evidence. Source provenance, confidence, test status and reviewer decisions remain visible.

### Layer D — Experimental Control Centre
Implements the repository's existing execution model:

`SOURCE → CLAIM → HYPOTHESIS → MODEL → SIMULATION → EXPERIMENT → MEASUREMENT → VALIDATION → REPLICATION → IP/PRODUCT PATH`.

Functions include experiment templates, controls, variables, expected outcomes, acceptance criteria, measurement plans, result capture, failure logging and replication gates.

### Layer E — Intelligence Layer
- Semantic search across the research graph
- Evidence-aware retrieval
- Research-gap detection
- Related-source discovery
- Hypothesis generation
- Suggested next tests
- Contradiction detection
- Cross-department relationship discovery
- Automated research summaries

AI output must retain provenance and distinguish retrieved evidence from generated hypotheses.

### Layer F — Automated Experiment Generator
Input:
`claim + hypothesis + objective + constraints`

Output:
`testable hypothesis + variables + controls + apparatus + procedure + measurements + acceptance criteria + safety/compliance checklist + expected data structure`.

The system should support human approval before an experiment becomes executable.

### Layer G — Virtual Laboratory
Connector architecture for:
- CFD
- FEA/FEM
- thermal simulation
- electromagnetic simulation
- optics/photonics
- materials modelling
- agricultural/biological models
- energy systems
- robotics
- manufacturing
- geometry/CAD

The OS orchestrates jobs and stores model metadata, inputs, outputs and reproducibility information rather than claiming to replace specialist simulation packages in the first release.

### Layer H — Materials Genome
Searchable material records containing:
- composition
- structure
- processing route
- physical properties
- mechanical properties
- thermal/electrical/optical properties
- environmental attributes
- test results
- manufacturing constraints
- candidate applications
- provenance
- prior art/IP links

### Layer I — Technology Combination Engine
Creates structured candidate combinations across departments.

Example:
`material + geometry + manufacturing process + sensor + control algorithm + application`.

Each generated combination is treated as a hypothesis or design candidate until independently validated.

### Layer J — Knowledge Graph
Relationships include:

`source supports claim`  
`claim motivates hypothesis`  
`hypothesis tested by experiment`  
`experiment produces dataset`  
`dataset supports/contradicts result`  
`material used in prototype`  
`algorithm controls system`  
`technology has prior art`  
`technology generates IP candidate`  
`prototype becomes product candidate`.

Graph traversal should support research discovery, dependency analysis and technology-family mapping.

### Layer K — Failure and Lessons Register
Failed, negative and inconclusive results are first-class records.

Required fields:
- test ID
- hypothesis
- conditions
- expected result
- observed result
- failure classification
- probable causes
- confirmed causes
- corrective action
- repeat-test status
- lessons learned

### Layer L — IP Firewall
Data states:

`PUBLIC → INTERNAL → CONFIDENTIAL → PRE-IP → IP-CANDIDATE → PATENT/TRADE-SECRET WORKFLOW`.

The software should support access restrictions, disclosure logging, prior-art links, invention records and export controls. It must not represent an invention as legally protected merely because an IP-candidate record exists.

### Layer M — Digital Twin and Digital Factory
Interfaces for:
- sensors
- CAD/geometry
- GIS
- machine data
- manufacturing workflows
- robotics
- machine vision
- simulation outputs
- maintenance data
- optimisation loops

The initial product should expose connector interfaces and data schemas before attempting universal device control.

### Layer N — Innovation Portfolio
Portfolio views for:
- research projects
- hypotheses
- technology candidates
- prototypes
- TRL/R-maturity
- IP candidates
- commercialisation candidates
- funding stages
- collaborations
- resource requirements

## 5. API-first architecture

Recommended services:

```text
Web / Desktop / Mobile UI
          ↓
API Gateway
          ↓
Identity + Permissions
          ↓
Research Service
Experiment Service
Evidence Service
Knowledge Graph Service
AI/Intelligence Service
Simulation Connector Service
Materials Service
IP Service
Portfolio Service
Audit Service
          ↓
PostgreSQL / Object Storage / Search Index / Graph Layer
```

External integrations should use versioned APIs and webhooks where appropriate.

## 6. Data and audit requirements

Minimum controls:
- immutable audit-event design
- object version history
- source provenance
- experiment timestamps
- user attribution
- dataset checksums where appropriate
- controlled status transitions
- exportable research records
- backup and recovery
- configurable retention
- tenant isolation

Enterprise validation, regulated workflows and formal compliance certifications are separate engineering programmes and must not be claimed until actually achieved.

## 7. Deployment model

Target deployment modes:

1. **Cloud SaaS** — default commercial offering.
2. **Private cloud** — customer-controlled infrastructure.
3. **On-premise** — enterprise, laboratory or government environments.
4. **Research sandbox** — local/developer edition.
5. **Hybrid** — sensitive data retained locally while approved services connect to the platform.

## 8. Licensing model

Potential commercial structure:

### Community / Research Edition
- limited users/projects
- local deployment
- core research objects
- basic experiment records
- export/import

### Professional Edition
- team collaboration
- knowledge graph
- evidence engine
- experiment generator
- portfolio management
- AI research assistance

### Enterprise Edition
- multi-tenant administration
- SSO/MFA integration
- advanced audit controls
- private deployment options
- API and integration layer
- custom workflows
- advanced security controls
- support/SLA packages

### Academic / Government Edition
- institutional licensing
- controlled deployment
- research collaboration
- grant/project reporting workflows
- configurable governance

### Industrial Edition
- engineering, manufacturing, materials, robotics and digital-twin integrations
- supplier/project workflows
- technology-development portfolio
- prototype-to-production pipeline

Pricing should be validated through customer discovery rather than fixed prematurely.

## 9. Commercial differentiation hypothesis

The central product hypothesis is:

> A multidisciplinary R&D operating system that connects evidence, hypotheses, experiments, simulation, failure learning, materials, algorithms, IP, prototypes and commercialisation in one traceable lifecycle can solve workflow fragmentation that conventional point solutions do not fully address.

This is a product hypothesis, not a proven market claim. Validation requires customer interviews, workflow studies, competitor analysis, prototype testing and willingness-to-pay evidence.

## 10. Minimum Viable Product

The first commercial prototype should NOT attempt to implement the complete OS.

### MVP-1
- authentication and organisations
- projects/departments
- research-object registry
- source/claim/hypothesis records
- experiment records
- evidence states
- audit history
- document/file attachment metadata
- search
- basic dashboard
- exportable project record

### MVP-2
- knowledge graph
- AI-assisted research retrieval
- automated experiment generator
- failure register
- IP firewall
- technology readiness

### MVP-3
- simulation connectors
- materials genome
- digital-twin interfaces
- robotics/manufacturing connectors
- portfolio/commercialisation engine

## 11. Reference implementation relationship

The existing GitHub repository is the **reference research environment**, not the production SaaS backend.

Repository → validates ontology, workflows, templates, algorithms and research methodology.

Commercial OS → implements secure multi-user software, APIs, databases, interfaces, billing/licensing, customer isolation, deployment and support.

This separation protects Biupiu's research/IP while allowing the methodology to become a licensable software platform.

## 12. Product development gates

**Gate P0 — Architecture:** object model and system boundaries defined.  
**Gate P1 — Prototype:** working research-object and experiment registry.  
**Gate P2 — Alpha:** multi-user workflow and audit history.  
**Gate P3 — Beta:** AI/evidence/knowledge graph integration.  
**Gate P4 — Pilot:** external research team uses system on real projects.  
**Gate P5 — Commercial:** security, deployment, licensing, documentation and support readiness.  
**Gate P6 — Scale:** enterprise integrations and validated customer demand.

## 13. IP and ownership strategy

The product programme should maintain explicit separation between:

- Biupiu's proprietary software code
- open-source dependencies
- repository research content
- customer data
- generated AI outputs
- third-party source material
- patented or patent-pending inventions
- trade secrets
- public documentation

A software licence and IP policy must define which components customers receive rights to use, modify, host or redistribute.

## 14. Immediate build queue

1. Define machine-readable research-object schema.
2. Define PostgreSQL relational schema.
3. Define graph relationships.
4. Define REST/GraphQL API contract.
5. Build authentication and tenant model.
6. Build project/research/hypothesis/experiment registry.
7. Build evidence-state engine.
8. Build audit/version service.
9. Build search and repository synchronisation layer.
10. Create minimal web dashboard.
11. Create experiment-generator prototype.
12. Create knowledge-graph prototype.
13. Run internal Biupiu research projects through the prototype.
14. Record usability failures and workflow friction.
15. Conduct external customer discovery before committing to full commercial build.

## 15. Validation principle

The software itself follows the same Biupiu research doctrine:

**Do not assume the software concept is commercially validated because the architecture is sophisticated. Build the smallest testable system, run real research workflows through it, measure time saved, traceability, usability and research outcomes, then iterate.**

## 16. Status

**Architecture status:** Defined / reference specification  
**Commercial validation:** Not yet established  
**Production software:** Not yet built  
**Production SaaS:** Not launched  
**Licensing:** Proposed model only  
**Next step:** MVP architecture and machine-readable schema

## P0 Multi-Language Kernel Integration — 20 September 2026
The R&D OS software architecture now adopts the repository's controlled C/C++/Rust core stack. C provides the durable ABI/HAL boundary; Rust is preferred for new safety-sensitive kernel services; C++ provides native high-performance simulation, geometry and scientific components. AI-generated or translated code remains non-authoritative until licence, build, ABI, security and regression gates pass.

Executable source-level seed: `core/multilang/`. Host/runtime deployment remains unverified.
