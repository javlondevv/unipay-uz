# Django Integration

The Django integration turns provider webhooks into clean override points and
persists every transaction for you.

Install with the extra:

```bash
pip install "unipay-uz[django]"
```

## 1. Register the app

```python
# settings.py
INSTALLED_APPS = [
    # ...
    "unipay_uz.integrations.django",
]
```

Run `python manage.py migrate` to create the `PaymentTransaction` table.

## 2. Configure credentials

Add a `TOLOV` dict to `settings.py`. Each provider block carries its keys plus
how to resolve the order being paid:

```python
TOLOV = {
    "PAYME": {
        "PAYME_ID": "STORE_ID",
        "PAYME_KEY": "STORE_KEY",
        "ACCOUNT_MODEL": "shop.models.Order",   # optional
        "ACCOUNT_FIELD": "ref_id",               # default: "id"
        "AMOUNT_FIELD": "total_amount",          # default: "amount"
        "ONE_TIME_PAYMENT": True,
    },
    "CLICK": {
        "SERVICE_ID": "SRV_ID",
        "MERCHANT_ID": "MCH_ID",
        "MERCHANT_USER_ID": "USR_ID",
        "SECRET_KEY": "SECRET",
        "ACCOUNT_MODEL": "shop.models.Order",
        "ACCOUNT_FIELD": "ref_id",
        "COMMISSION_PERCENT": 0.0,
        "ONE_TIME_PAYMENT": True,
    },
    # "UZUM", "PAYNET", "OCTO" follow the same shape.
}
```

## 3. Implement webhook views

Subclass the base view for each provider and override the lifecycle hooks you
care about:

```python
# views.py
from unipay_uz.integrations.django.views import (
    BasePaymeWebhookView,
    BaseClickWebhookView,
)
from shop.models import Order

class PaymeCallbackReceiver(BasePaymeWebhookView):
    def successfully_payment(self, params, transaction):
        Order.objects.get(ref_id=transaction.account_id).mark_as_paid()

    def cancelled_payment(self, params, transaction):
        Order.objects.get(ref_id=transaction.account_id).mark_as_failed()

class ClickCallbackReceiver(BaseClickWebhookView):
    def successfully_payment(self, params, transaction):
        Order.objects.get(ref_id=transaction.account_id).mark_as_paid()

    def cancelled_payment(self, params, transaction):
        Order.objects.get(ref_id=transaction.account_id).mark_as_failed()
```

Available base views: `BasePaymeWebhookView`, `BaseClickWebhookView`,
`BaseUzumWebhookView`, `BasePaynetWebhookView`, `BaseOctoWebhookView`.

### Overridable hooks

| Hook | When it fires |
|---|---|
| `successfully_payment(params, transaction)` | payment succeeded |
| `cancelled_payment(params, transaction)` | payment cancelled |
| `before_check_perform_transaction(params, account)` | pre-check (Payme) |
| `transaction_already_exists(params, transaction)` | duplicate transaction (Payme) |
| `transaction_created(params, transaction, account)` | after creation (Payme) |
| `check_transaction(params, transaction)` | validation phase (Payme) |
| `get_statement(params, transactions)` | statement request (Payme) |
| `get_check_data(params, account)` | extra check-response data (Payme/Uzum/Paynet) |

## 4. Wire up URLs

```python
# urls.py
from django.urls import path
from .views import PaymeCallbackReceiver, ClickCallbackReceiver

urlpatterns = [
    path("api/v1/webhooks/payme/", PaymeCallbackReceiver.as_view()),
    path("api/v1/webhooks/click/", ClickCallbackReceiver.as_view()),
]
```

## The `PaymentTransaction` model

Each callback is recorded as a `PaymentTransaction` with fields: `gateway`,
`transaction_id`, `account_id`, `amount`, `state`, `reason`, `extra_data`,
`created_at`, `updated_at`, `performed_at`, `cancelled_at`.

Helpful methods: `mark_as_paid()`, `mark_as_cancelled(reason=None)`,
`mark_as_cancelled_during_init(reason)`, and the classmethods
`create_transaction()` / `update_transaction()`.

Access the model lazily (avoids `AppRegistryNotReady`):

```python
from unipay_uz.integrations.django.models import get_payment_transaction_model
PaymentTransaction = get_payment_transaction_model()
```

## Signals

Connect to these instead of (or in addition to) overriding hooks:

| Signal | Sent when |
|---|---|
| `payment_created` | a new transaction is created |
| `payment_successful` | transaction state → `SUCCESSFULLY` |
| `payment_cancelled` | transaction state → `CANCELED` / `CANCELED_DURING_INIT` |

```python
from django.dispatch import receiver
from unipay_uz.integrations.django.signals import payment_successful

@receiver(payment_successful)
def on_paid(sender, transaction, **kwargs):
    ...
```

## Transaction states

```python
from unipay_uz.core.constants import TransactionState

TransactionState.CREATED               # 0
TransactionState.INITIATING            # 1
TransactionState.SUCCESSFULLY          # 2
TransactionState.CANCELED              # -2
TransactionState.CANCELED_DURING_INIT  # -1
```
