# Quickstart

## 1. Create a gateway

Every gateway takes your merchant credentials and an `is_test_mode` flag. Import
directly, or use the [factory](gateways/index.md#factory).

```python
from unipay_uz import PaymeGateway, ClickGateway

payme = PaymeGateway(
    payme_id="MERCHANT_ID_HERE",
    payme_key="SECRET_KEY_HERE",
    is_test_mode=True,             # flip to False in production
)

click = ClickGateway(
    service_id="APP_SERVICE_ID",
    merchant_id="APP_MERCHANT_ID",
    merchant_user_id="APP_USER_ID",
    secret_key="SECRET_HASH_KEY",
    is_test_mode=True,
)
```

## 2. Generate a checkout link

`create_payment(...)` returns a **URL string** you redirect the customer to.

```python
checkout_url_payme = payme.create_payment(
    id="ORD-998877",
    amount=250000,                 # UZS (Som)
    return_url="https://your-platform.uz/checkout/success",
    account_field_name="order_id",
)

checkout_url_click = click.create_payment(
    id="ORD-998877",
    amount=250000,                 # UZS (Som)
    description="Subscription Renewal",
    return_url="https://your-platform.uz/checkout/success",
)
```

!!! warning "Amount units differ per gateway"
    Payme, Click, Uzum, and Octo take amounts in **UZS (Som)**. **Paynet takes
    tiyin** (1 UZS = 100 tiyin). Each [gateway page](gateways/index.md) states
    its convention explicitly.

## 3. Confirm payment via webhooks

Providers notify your server of the final payment result through webhooks — not
the `return_url`. UniPay UZ ships base webhook classes so you only implement the
"payment succeeded / cancelled" logic:

- **Django:** see the [Django integration](integrations/django.md).
- **FastAPI:** see the [FastAPI integration](integrations/fastapi.md).

```python
# Django example — views.py
from unipay_uz.integrations.django.views import BasePaymeWebhookView
from shop.models import Order

class PaymeWebhook(BasePaymeWebhookView):
    def successfully_payment(self, params, transaction):
        Order.objects.get(ref_id=transaction.account_id).mark_as_paid()

    def cancelled_payment(self, params, transaction):
        Order.objects.get(ref_id=transaction.account_id).mark_as_failed()
```

## 4. (Optional) check or cancel a payment

Where the provider supports it, gateways expose `check_payment` and
`cancel_payment`:

```python
status = payme.check_payment(transaction_id="...")
payme.cancel_payment(transaction_id="...", reason="customer_request")
```

!!! note
    Paynet is webhook-only — its `check_payment` / `cancel_payment` raise
    `NotImplementedError`. Uzum Biller links are confirmed via webhooks too.

Next: pick your provider in the **[Gateways reference](gateways/index.md)**.
