# Payme

Import: `from unipay_uz import PaymeGateway`
(or `from unipay_uz.gateways.payme.client import PaymeGateway`)

Amount unit: **UZS (Som)** — converted to tiyin internally where the API needs it.

## Constructor

```python
PaymeGateway(
    payme_id: str,
    payme_key: str | None = None,
    fallback_id: str | None = None,
    is_test_mode: bool = False,
    **kwargs,
)
```

## Create a checkout link

```python
url = payme.create_payment(
    id="ORD-998877",
    amount=250000,                       # UZS
    return_url="https://shop.uz/success",
    account_field_name="order_id",       # identifier key Payme expects
)
```

| Method | Signature | Returns |
|---|---|---|
| `create_payment` | `(id, amount, return_url="", account_field_name="order_id")` | URL `str` |
| `create_payment_async` | same args (async) | URL `str` |
| `generate_pay_link` | `(id, amount, return_url, account_field_name="order_id")` | URL `str` |
| `generate_pay_link_async` | same args (async) | URL `str` |
| `check_payment` | `(transaction_id)` | `dict` |
| `cancel_payment` | `(transaction_id, reason=None)` | `dict` |

## Cards

`payme.cards` exposes card operations:

```python
payme.cards.create(card_number="8600...", expire_date="03/99", save=True)
payme.cards.verify(...)
payme.cards.check(...)
payme.cards.remove(...)
```

## Receipts

`payme.receipts` exposes the receipts API (amounts in **tiyin** here):

```python
payme.receipts.create(amount=25000000, account={"order_id": "ORD-998877"})
payme.receipts.pay(...)
payme.receipts.check(...)
payme.receipts.cancel(...)
payme.receipts.send(...)
payme.receipts.get(...)
```

For server-side confirmation, implement a [Django](../integrations/django.md) or
[FastAPI](../integrations/fastapi.md) Payme webhook handler.
