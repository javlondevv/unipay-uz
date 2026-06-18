# Click

Import: `from unipay_uz import ClickGateway`
(or `from unipay_uz.gateways.click.client import ClickGateway`)

Amount unit: **UZS (Som)**.

## Constructor

```python
ClickGateway(
    service_id: str,
    merchant_id: str,
    merchant_user_id: str | None = None,
    secret_key: str | None = None,
    is_test_mode: bool = False,
    **kwargs,
)
```

## Create a checkout link

```python
url = click.create_payment(
    id="ORD-998877",
    amount=250000,                          # UZS
    description="Subscription Renewal",
    return_url="https://shop.uz/success",
)
```

`create_payment(id, amount, **kwargs)` accepts `description`, `return_url`, and
`merchant_user_id` via keyword arguments. Returns a URL `str`.

## Methods

| Method | Signature | Returns |
|---|---|---|
| `create_payment` | `(id, amount, **kwargs)` | URL `str` |
| `check_payment` | `(transaction_id)` | `dict` |
| `cancel_payment` | `(transaction_id, reason=None)` | `dict` |
| `card_token_request` | `(card_number, expire_date, temporary=0)` | `dict` |
| `card_token_verify` | `(card_token, sms_code)` | `dict` |
| `card_token_payment` | `(card_token, amount, transaction_parameter)` | `dict` |

## Card-token flow

```python
req = click.card_token_request(card_number="8600...", expire_date="0399")
click.card_token_verify(card_token=req["card_token"], sms_code=12345)
click.card_token_payment(
    card_token=req["card_token"],
    amount=250000,
    transaction_parameter="ORD-998877",
)
```

`click.merchant_api` exposes lower-level merchant API operations. For server-side
confirmation, implement a [Django](../integrations/django.md) or
[FastAPI](../integrations/fastapi.md) Click webhook handler.
