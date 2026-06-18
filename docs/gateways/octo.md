# Octo

Import: `from unipay_uz import OctoGateway`
(or `from unipay_uz.gateways.octo.client import OctoGateway`)

Amount unit: **UZS (Som)**.

## Constructor

```python
OctoGateway(
    octo_shop_id: int,
    octo_secret: str,
    notify_url: str = "",
    is_test_mode: bool = False,
    **kwargs,
)
```

## Create a checkout link

```python
url = octo.create_payment(
    id="ORD-998877",
    amount=250000,                         # UZS
    return_url="https://shop.uz/success",
    description="Order #998877",
    currency="UZS",
    language="uz",
)
```

`create_payment(id, amount, return_url="", **kwargs)` accepts these keyword
arguments: `currency` (default `"UZS"`), `description`, `basket`,
`payment_methods`, `language` (default `"uz"`), `ttl` (default `15`), and
`user_data`. Returns a URL `str`.

## Methods

| Method | Signature | Returns |
|---|---|---|
| `create_payment` | `(id, amount, return_url="", **kwargs)` | URL `str` |
| `check_payment` | `(transaction_id)` | `dict` |
| `cancel_payment` | `(transaction_id, amount=0, reason=None, **kwargs)` | `dict` |

## Payment methods

```python
from unipay_uz.gateways.octo.constants import OctoPaymentMethods

OctoPaymentMethods.BANK_CARD
OctoPaymentMethods.UZCARD
OctoPaymentMethods.HUMO
```

Pass a list via the `payment_methods` keyword to restrict the options shown.
