# Reddit & community posts

**Read each subreddit's rules first** — some require a flair, some have a
self-promo ratio or a weekly "show your project" thread. Post one at a time,
a few hours apart. Reply to every comment.

---

## r/Python

Use the **"I Made This"** flair.

**Title:**
```
I built UniPay UZ — one Python API for all of Uzbekistan's payment gateways (Payme, Click, Uzum, Paynet, Octo)
```

**Body:**
```
Payments in Uzbekistan mean integrating a handful of local gateways, each with
its own auth, amount units (som vs. tiyin), and webhook contract. I'd written
that glue more than once, so I packaged it.

UniPay UZ wraps Payme, Click, Uzum, Paynet and Octo behind one consistent API:

    from unipay_uz.gateways.payme import PaymeGateway
    payme = PaymeGateway(payme_id="...", payme_key="...", is_test_mode=True)
    url = payme.create_payment(id="ORD-1", amount=250000, return_url="...")

Webhooks are the bit I'm happiest with — you subclass a base view and implement
`successfully_payment` / `cancelled_payment`; signature checks and transaction
state are handled. Extras for Django, FastAPI and Flask. MIT, on PyPI:
`pip install unipay-uz`.

Repo: https://github.com/javlondevv/unipay-uz

Would love feedback on the API design and on how you'd structure tests for
payment providers where the hard part is sandbox credentials.
```

---

## r/django

**Title:**
```
Django payments for Uzbekistan (Payme/Click/Uzum/Paynet/Octo) without re-writing webhook handling every time
```

**Body:**
```
If you build for the Uzbek market, you've probably hand-rolled Payme/Click
webhook views more than once. I extracted mine into a reusable library.

In Django you add it to INSTALLED_APPS, drop your credentials in a TOLOV dict in
settings.py, and your callback receiver looks like:

    from unipay_uz.integrations.django.views import BasePaymeWebhookView

    class PaymeCallbackReceiver(BasePaymeWebhookView):
        def successfully_payment(self, params, transaction):
            Order.objects.get(ref_id=transaction.account_id).mark_as_paid()

        def cancelled_payment(self, params, transaction):
            Order.objects.get(ref_id=transaction.account_id).mark_as_failed()

Signature verification and transaction state are handled by the base class.
MIT, `pip install unipay-uz[django]`.

Repo: https://github.com/javlondevv/unipay-uz — feedback on the settings schema
welcome.
```

---

## r/fastapi

**Title:**
```
UniPay UZ — Uzbekistan payment gateways (Payme, Click, Uzum, Paynet, Octo) with FastAPI support
```

**Body:**
```
A small library that unifies Uzbekistan's payment gateways behind one Python API,
with a FastAPI extra (`pip install unipay-uz[fastapi]`).

    from unipay_uz.gateways.click import ClickGateway
    click = ClickGateway(service_id="...", merchant_id="...",
                         merchant_user_id="...", secret_key="...", is_test_mode=True)
    url = click.create_payment(id="ORD-1", amount=250000,
                               description="Subscription", return_url="...")

I'm actively working on a fuller FastAPI webhook example (there's an open
`good first issue` for it). MIT. Repo: https://github.com/javlondevv/unipay-uz
— would genuinely value FastAPI-idiomatic API feedback.
```

---

## r/flask

**Title:**
```
Unified Uzbekistan payments (Payme/Click/Uzum/Paynet/Octo) for Flask apps
```

**Body:**
```
I made a library that puts Uzbekistan's payment gateways behind one API, with a
Flask extra (`pip install unipay-uz[flask]`). Core usage is framework-agnostic —
create a checkout URL, then handle the provider's callback:

    from unipay_uz.gateways.payme import PaymeGateway
    payme = PaymeGateway(payme_id="...", payme_key="...", is_test_mode=True)
    url = payme.create_payment(id="ORD-1", amount=250000, return_url="...")

MIT, repo: https://github.com/javlondevv/unipay-uz. Happy to take Flask-specific
suggestions.
```

---

## Telegram / CIS dev communities

The biggest local audience is on Telegram, not Reddit. Post in Python/Django/UZ
dev channels and chats you're already part of (and the relevant `@uzbek_developers`
/ Central-Asia dev groups). Keep it short, lead with the problem, link the repo.
Pin a message in your own channel (`@DevFlowJavlon`) — see `social.md`.

### Russian-language variant (for RU/CIS channels and r/ru-ish communities)

```
Запостил опенсорс: UniPay UZ — единый Python-API для платёжных систем Узбекистана
(Payme, Click, Uzum, Paynet, Octo).

Надоело каждый раз заново писать обёртки и обработку вебхуков под каждый шлюз,
поэтому собрал всё в одну библиотеку. Есть интеграции для Django, FastAPI и Flask,
проверка подписи и управление состоянием транзакций — из коробки.

    pip install unipay-uz

Лицензия MIT, есть README на русском.
Репозиторий: https://github.com/javlondevv/unipay-uz

Буду рад фидбэку по API и звезде на GitHub, если пригодится 🙌
```
