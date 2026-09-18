# BIUPIU COIN INTERFACE v1

## Purpose
Define a provider-neutral interface so the R&D OS and Biupiu World can support a future Biupiu Coin without coupling the applications to an unlaunched blockchain.

## Application interface

`getAssetInfo()` — symbol, decimals, network, contract/native-asset status, version.

`getWallet()` — public wallet/account identifier and supported networks.

`getBalance()` — available and pending balances.

`createPaymentRequest()` — recipient, amount, asset, purpose and expiry.

`authorizePayment()` — requires explicit user authorization.

`submitTransaction()` — sends through the configured wallet/network adapter.

`getTransactionStatus()` — pending/confirmed/failed/replaced.

`verifyReceipt()` — validates transaction identity and trust-layer linkage.

`estimateFee()` — reports network fee separately from the payment amount.

`disableAsset()` — immediately disables an unsafe or unsupported asset adapter.

## Compatibility model

The OS should support:
- future native Biupiu Coin;
- approved external tokens/chains if later required;
- off-chain internal credits only if separately defined and clearly labelled as non-blockchain credits.

No balance is considered spendable merely because an application database says it exists.
