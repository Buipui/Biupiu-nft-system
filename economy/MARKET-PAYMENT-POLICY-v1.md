# Biupiu World Market Payment Policy v1.0

## Objective
Biupiu World markets are designed so that purchases of listed items require Biupiu Coin (BPU), or an explicitly approved cryptocurrency payment route that is converted/settled into the required BPU amount before the order is completed.

## Purchase rule
1. Buyer selects an item.
2. Checkout calculates the BPU price and disclosed fees.
3. Buyer must have sufficient available BPU.
4. If the buyer starts with fiat money or another cryptocurrency, the platform routes them through an approved on-ramp/exchange/payment provider to acquire the required BPU.
5. The order remains pending until payment is authorized and verified.
6. The marketplace issues a receipt and records a trust event.
7. Delivery/access/minting occurs only after settlement passes.

## Payment sources
- Fiat -> approved payment/on-ramp -> BPU -> marketplace checkout.
- Approved cryptocurrency -> approved conversion/payment route -> BPU -> marketplace checkout.
- Existing BPU balance -> direct BPU payment.

Biupiu World must not represent an unlaunched BPU asset as live or imply that an undeployed blockchain is live.

## Wallet and balance
The OS/World wallet should show BPU available, pending and reserved balances, transaction history, account/address identifier, network/asset status, and an estimated fiat value where a verified price source exists.

Balances are ledger state; the interface must distinguish confirmed, pending, reserved and unavailable amounts.

## Market controls
Each item declares its BPU price, inventory, seller/issuer, delivery type, refund/cancellation policy, fees, settlement status, NFT-mint trigger if applicable, and trust/provenance reference where applicable.

## Security gates
- No private keys or seed phrases stored in the repository.
- Monetary actions require explicit user authorization.
- Never fabricate a transaction confirmation.
- Verify recipient, asset/network and amount before submission.
- Protect against replay, duplicate checkout and double-spend conditions.
- Keep payment records auditable.
- Separate marketplace entitlement from blockchain settlement.

## Launch dependency
A real BPU purchase system requires a defined BPU asset/network, wallet/key model, issuance rules, legal/compliance review, payment/on-ramp providers, security testing and production deployment.
