# Uzum

Import: `from unipay_uz import UzumGateway`
(or `from unipay_uz.gateways.uzum.client import UzumGateway`)

Amount unit: **UZS (Som)** for `create_payment` (converted to tiyin internally).
`cancel_payment` takes the amount in **tiyin**.

## Constructor

```python
UzumGateway(
    service_id: str,
    is_test_mode: bool = False,
    terminal_id: str | None = None,
    api_key: str | None = None,
    **kwargs,
)
```

## Create a checkout link (Uzum Biller)

```python
url = uzum.create_payment(
    id="ORD-998877",
    amount=50000,                          # UZS
    return_url="https://shop.uz/sync",
)
```

`create_payment(id, amount, return_url, **kwargs)` builds an Uzum Biller redirect
URL. Pass `service_id` in `**kwargs` to override the instance default. Returns a
URL `str`.

## Methods

| Method | Signature | Returns |
|---|---|---|
| `create_payment` | `(id, amount, return_url, **kwargs)` | URL `str` |
| `create_payment_async` | same args (async) | URL `str` |
| `check_payment` | `(id)` | `dict` |
| `cancel_payment` | `(id, amount, operation_id=None)` — amount in **tiyin** | `dict` |

!!! note
    Payment status for Biller links is delivered via **webhooks**, not
    `check_payment`. Use a webhook handler to mark orders paid.
