---
title: "Why I built UniPay UZ: one Python API for Uzbekistan's payment gateways"
published: false
description: "Integrating Payme, Click, Uzum, Paynet and Octo in Python without re-writing the same glue every time."
tags: python, django, fastapi, opensource
canonical_url: https://github.com/javlondevv/unipay-uz
---

> `published: false` — flip to `true` when you're ready. On Medium, paste the
> body and add the same tags manually.

## The problem

If you build software for the Uzbek market, you integrate payments against local
gateways: **Payme, Click, Uzum, Paynet, and Octo**. None of them share an API.
Each has its own:

- authentication scheme,
- amount unit (som vs. *tiyin* — off-by-100 bugs are a rite of passage),
- and webhook/callback contract for confirming a payment.

I'd written this integration layer three times across different projects before
I admitted it should be a library. So I made one.

## UniPay UZ

[UniPay UZ](https://github.com/javlondevv/unipay-uz) puts all five gateways
behind a single, predictable Python API. It's MIT-licensed and on PyPI:

```bash
pip install unipay-uz
```

### Creating a checkout link

The same shape works across providers — you construct a gateway and call
`create_payment`:

```python
from unipay_uz.gateways.payme import PaymeGateway
from unipay_uz.gateways.click import ClickGateway

payme = PaymeGateway(
    payme_id="MERCHANT_ID_HERE",
    payme_key="SECRET_KEY_HERE",
    is_test_mode=True,  # toggle for production
)

checkout_url = payme.create_payment(
    id="ORD-998877",
    amount=250000,                 # in som (UZS)
    return_url="https://your-platform.uz/checkout/success",
    account_field_name="order_id",
)
```

A subtle one: **Paynet works in tiyin** (1 UZS = 100 tiyin), so the library is
explicit about units instead of silently guessing:

```python
paynet_url = paynet.create_payment(id="ORD-998877", amount=25000000)  # 250,000 UZS
```

### The part that actually saves time: webhooks

Generating a payment URL is the easy 20%. The other 80% is correctly handling
the provider's asynchronous callback — verifying the signature, mapping it to
your order, and moving the transaction through its state machine. UniPay UZ
gives you base classes so you only write the business logic.

In Django, register the app and declare your credentials:

```python
# settings.py
INSTALLED_APPS = [
    # ...
    "unipay_uz.integrations.django",
]

TOLOV = {
    "PAYME": {
        "PAYME_ID": "STORE_ID",
        "PAYME_KEY": "STORE_KEY",
        "ACCOUNT_MODEL": "shop.models.Transaction",
        "ACCOUNT_FIELD": "ref_id",
        "AMOUNT_FIELD": "total_amount",
        "ONE_TIME_PAYMENT": True,
    },
}
```

Then your callback receiver is just the two methods that matter:

```python
# views.py
from unipay_uz.integrations.django.views import BasePaymeWebhookView
from shop.models import Transaction

class PaymeCallbackReceiver(BasePaymeWebhookView):
    def successfully_payment(self, params, transaction):
        Transaction.objects.get(ref_id=transaction.account_id).mark_as_paid()

    def cancelled_payment(self, params, transaction):
        Transaction.objects.get(ref_id=transaction.account_id).mark_as_failed()
```

Signature verification and transaction bookkeeping happen in the base class.
There are extras for **FastAPI** and **Flask** too:

```bash
pip install unipay-uz[django]   # or [fastapi] / [flask]
```

## Design notes

- **One contract, many gateways.** Every provider subclasses a common
  `BasePaymentGateway`, and a small factory lets you pick a gateway by name —
  so adding a new one is a contained change.
- **Explicit over magic.** Amount units and test/production mode are explicit
  parameters, because payment bugs are expensive.
- **Bring your own models.** The Django integration points at *your* transaction
  model via settings rather than forcing its own schema on you.

## What's next

I'd love help with:

- a clean **test harness** for the gateways (the hard part is sandbox creds),
- a fuller **FastAPI** example,
- and an **Uzbek** translation of the docs.

These are open as `good first issue`s on the repo.

## Try it

```bash
pip install unipay-uz
```

Repo: **https://github.com/javlondevv/unipay-uz** (there's a Russian README too).

If it saves you a weekend, a ⭐ helps other Uzbek developers find it. You can even
drop a live star button on your own site with [GitHub Buttons](https://buttons.github.io/):

```html
<a class="github-button"
   href="https://github.com/javlondevv/unipay-uz"
   data-icon="octicon-star"
   data-size="large"
   data-show-count="true"
   aria-label="Star javlondevv/unipay-uz on GitHub">Star</a>
<script async defer src="https://buttons.github.io/buttons.js"></script>
```

Feedback and PRs welcome — especially from anyone shipping payments in Uzbekistan.
