# Subscriber Service Authorization v1

Gate 22 binds department service execution to the existing SubscriberAccount entitlement model.

Authorization sequence:

1. Account must be active.
2. Account must hold the department entitlement.
3. The requested service maps to a subscriber capability.
4. The account tier must provide that capability.
5. Only then is the service adapter invoked.

The gateway does not create entitlements and does not bypass the existing subscriber policy. Production authorization remains server-side.
