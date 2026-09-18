# Biupiu Coin (BPU) Tokenomics & Marketplace Economic Specification v1.0

## Purpose

This document converts the Biupiu World marketplace requirement into a future BPU economic specification.

Biupiu World uses **BPU itself** as its intended native settlement asset. It must not create or sell a second substitute "World token".

This is a design specification only. It does not create, issue, sell, or list BPU.

## 1. Core economic model

The target system is:

`Real money / approved cryptocurrency -> approved BPU acquisition -> BPU wallet -> Biupiu World -> genuine purchase -> transparent settlement -> seller + service + treasury/ecosystem allocations`

The economic objective is to build **real utility and legitimate demand**, not to manufacture a market price.

No mechanism in this specification guarantees that BPU will increase in value.

## 2. Supply model — launch decision required

The following parameters must be explicitly fixed before production issuance:

| Parameter | Status | Requirement |
|---|---|---|
| Maximum BPU supply | TBD | Publish before genesis |
| Genesis supply | TBD | Publish before launch |
| Initial circulating supply | TBD | Publish before launch |
| Treasury allocation | TBD | Public allocation schedule |
| Ecosystem/research allocation | TBD | Vesting and release rules |
| Creator/developer allocation | TBD | Vesting and eligibility |
| Liquidity reserve | TBD | Transparent custody and reporting |
| Team/director allocation | TBD | Vesting and disclosure |
| Future issuance | TBD | Must be protocol-defined |
| Burn policy | TBD | Optional; must be explicit |
| Transaction fee policy | TBD | Must be disclosed |

**No percentage is treated as final until the BPU tokenomics design is approved and documented.**

## 3. Marketplace settlement allocation

Every BPU-priced marketplace item should have a transparent settlement policy.

Conceptual example only:

- Seller/creator: 70%
- Marketplace/service operations: 15%
- Ecosystem/treasury: 10%
- Liquidity/network development: 5%

These percentages are **illustrative placeholders, not launch parameters**.

The production system must read the actual published allocation schedule rather than hard-code these example values.

## 4. Treasury and ecosystem use

A disclosed ecosystem allocation may support:

- blockchain/network infrastructure
- security audits
- marketplace infrastructure
- research and development grants
- creator/developer incentives
- ecosystem tooling
- approved liquidity operations
- operating reserves

Treasury movements should be recorded in an auditable ledger and, where appropriate, anchored on-chain.

## 5. Liquidity and market integrity

If legally and technically permitted, a separately disclosed liquidity reserve may be used to support orderly market access and reduce avoidable liquidity fragmentation.

It must **not** be used to:

- fabricate trading volume
- wash trade
- self-trade to create apparent demand
- spoof or fake orders
- coordinate artificial price movements
- promise a minimum or guaranteed price
- misrepresent reserves or liquidity
- create misleading market statistics

Market price remains a function of independent supply and demand.

## 6. Value-creation model

The intended economic flywheel is:

`Useful products/services
-> more Biupiu World activity
-> more genuine BPU utility
-> more legitimate BPU demand
-> greater transaction activity
-> deeper/healthier liquidity
-> better price discovery
-> additional ecosystem participation
`

This is a design objective, **not a price forecast**.

## 7. BPU acquisition

Before production launch, the system may support:

1. Fiat -> approved on-ramp -> BPU
2. Approved cryptocurrency -> compliant conversion route -> BPU
3. Existing BPU -> direct marketplace settlement

The exact providers and supported assets remain TBD.

The application must never imply that an on-ramp is live until an actual provider integration is deployed and verified.

## 8. Wallet architecture

The user's own external wallet should remain the custody authority.

Target architecture:

`User wallet <-> secure wallet connection/signature layer <-> Biupiu OS <-> Biupiu World <-> BPU network`

Requirements:

- never request or store seed phrases in Biupiu World
- never hard-code private keys
- display network, asset, recipient and amount before authorization
- require explicit signing for transfers
- verify settlement before granting marketplace fulfilment
- support transaction receipts and status tracking

## 9. Marketplace price and accounting rules

Each item should expose:

- BPU price
- seller/issuer
- inventory
- applicable marketplace fee
- ecosystem/treasury allocation
- liquidity allocation, if applicable
- delivery/fulfilment terms
- cancellation/refund rules
- NFT mint trigger, where applicable
- provenance/trust reference

The checkout should calculate allocations deterministically from the published rules.

## 10. Transparent BPU dashboard

Biupiu OS should eventually expose:

- total supply
- circulating supply
- treasury balance
- ecosystem reserve balance
- liquidity reserve balance
- marketplace volume
- BPU spent in marketplace
- BPU acquired through supported routes
- transaction count
- network status
- allocation/vesting schedule
- audit and contract references

Any unavailable metric must be marked unavailable rather than estimated as fact.

## 11. Governance and controls

Before production launch, define:

- who can change marketplace allocation rules
- who can authorize treasury transfers
- multisignature or equivalent treasury controls
- spending limits
- emergency pause authority
- contract upgrade policy
- audit requirements
- public change log
- conflict-of-interest disclosures where applicable

Changes should use the Biupiu trust/audit layer and produce versioned configuration records.

## 12. Economic experiments

The Biupiu digital lab may simulate different tokenomics before real deployment.

Permitted simulations include:

- supply/velocity scenarios
- marketplace fee scenarios
- treasury accumulation
- liquidity-depth scenarios
- user-growth scenarios
- inventory turnover
- creator payout models
- stress testing
- volatility and slippage simulations

Simulation outputs must be labelled as models and must not be presented as predictions of BPU market price.

## 13. Production gates

### Gate BPU-01 — Token specification
Define supply, issuance, allocation, vesting and fee rules.

### Gate BPU-02 — Network specification
Select or design the blockchain/network and define wallet standards.

### Gate BPU-03 — Economic specification
Approve marketplace allocations, treasury rules and liquidity policy.

### Gate BPU-04 — Legal/compliance
Complete applicable legal, financial, tax, consumer-protection and AML/KYC analysis.

### Gate BPU-05 — Security
Audit wallet, payment, treasury and settlement contracts.

### Gate BPU-06 — Testnet
Run local/testnet issuance, transfers, checkout, refunds and receipt verification.

### Gate BPU-07 — Transparency
Publish tokenomics, treasury controls, vesting, contract/network identity and reporting methodology.

### Gate BPU-08 — Production
Only after the preceding gates pass may production BPU commerce be activated.

## 14. Current status

**Architecture/specification only.**

Not yet:

- a live BPU coin
- a production blockchain
- a public BPU sale
- a live exchange listing
- a connected user wallet
- a guaranteed-value asset

The next technical phase is economic simulation plus a testnet/local BPU prototype, without real-money settlement.
