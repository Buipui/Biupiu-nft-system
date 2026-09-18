# Biupiu World Market Architecture v1.0

## Core flow
Browse -> Select -> BPU Price -> Wallet Check -> Buy BPU if Needed -> Authorize -> Settle -> Receipt -> Fulfil

## Fiat route
Rands/USD/etc. -> approved on-ramp/payment provider -> BPU -> Biupiu World checkout

## Cryptocurrency route
Approved cryptocurrency -> approved swap/payment route -> BPU -> Biupiu World checkout

## Existing BPU route
BPU wallet -> payment authorization -> BPU settlement -> receipt

## Market domains
- NFT/art markets
- Biupiu World virtual goods
- digital software/modules
- research/data access where commercially permitted
- creator releases
- laboratory/service bookings
- approved physical-product markets
- virtual assets if later introduced

## Order state machine
DRAFT -> PRICE_LOCKED -> PAYMENT_REQUIRED -> PAYMENT_AUTHORIZED -> SETTLEMENT_PENDING -> PAID -> FULFILLED

Failure states: EXPIRED, CANCELLED, REFUNDED, PAYMENT_FAILED

An order cannot enter FULFILLED until payment verification succeeds.

## Pricing
Prices may be denominated in BPU. Fiat or other-crypto amounts shown are indicative conversion amounts until the required BPU is actually acquired/settled.

## Future APIs
quoteItem(), getBpuBalance(), createBuyBpuRequest(), createOrder(), authorizeBpuPayment(), submitSettlement(), verifySettlement(), issueReceipt(), fulfilOrder(), refundOrder()

These are interface requirements, not claims that live payment rails already exist.
