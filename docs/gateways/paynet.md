# Paynet

Import: `from unipay_uz import PaynetGateway`
(or `from unipay_uz.gateways.paynet.client import PaynetGateway`)

Amount unit: **tiyin** (1 UZS = 100 tiyin). The amount is optional.

## Constructor

```python
PaynetGateway(
    merchant_id: str | int,
    is_test_mode: bool = False,
    **kwargs,
)
```

## Create a payment link

```python
url = paynet.create_payment(
    id="ORD-998877",
    amount=25000000,                       # tiyin (= 250,000 UZS)
)
# e.g. https://app.paynet.uz/?m={merchant_id}&c=ORD-998877&a=25000000
```

## Methods

| Method | Signature | Returns |
|---|---|---|
| `create_payment` | `(id, amount=None, **kwargs)` | URL `str` |
| `create_payment_async` | same args (async) | URL `str` |
| `generate_pay_link` | `(id, amount=None)` | URL `str` |
| `generate_pay_link_async` | same args (async) | URL `str` |
| `check_payment` | `(transaction_id)` | raises `NotImplementedError` |
| `cancel_payment` | `(transaction_id, reason=None)` | raises `NotImplementedError` |

!!! warning "Webhook-only"
    Paynet confirms fulfillment via **JSON-RPC 2.0 webhooks**, not return URLs or
    polling. `check_payment` / `cancel_payment` intentionally raise
    `NotImplementedError`. Implement a Paynet webhook handler
    ([Django](../integrations/django.md)) to settle orders.
