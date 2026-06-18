# UniPay UZ

[![PyPI version](https://img.shields.io/pypi/v/unipay-uz.svg)](https://pypi.org/project/unipay-uz/)
[![Python Versions](https://img.shields.io/pypi/pyversions/unipay-uz.svg)](https://pypi.org/project/unipay-uz/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/javlondevv/unipay-uz/blob/main/LICENSE)

**One unified Python API for Uzbekistan's payment gateways — Payme, Click, Uzum,
Paynet & Octo.** First-class integrations for Django, FastAPI, and Flask.

UniPay UZ handles the heavy lifting of API communication, webhook verification,
and transaction state management behind a single, predictable interface, so you
can focus on your product instead of five different provider SDKs.

## Features

- 🔌 **Unified interface** — one consistent API across all providers; stop writing redundant wrappers.
- 🇺🇿 **Five gateways** — Payme, Click, Uzum, Paynet, and Octo.
- 🧰 **Framework integrations** — out-of-the-box Django and FastAPI support (Flask planned).
- 🔔 **Webhook base classes** — handle async payment callbacks by overriding a couple of methods.
- 🏭 **Factory pattern** — instantiate any gateway by name with `create_gateway(...)`.
- 🧪 **Test mode** — explicit `is_test_mode` toggle on every gateway.
- 💳 **Card & receipt operations** — Payme cards/receipts and Click card-token flows.
- 🧱 **Extensible** — add a new gateway by subclassing `BasePaymentGateway`.

## Documentation

<div class="grid cards" markdown>

- :material-download: **[Installation](installation.md)** — pip install + framework extras.
- :material-rocket-launch: **[Quickstart](quickstart.md)** — first checkout link in minutes.
- :material-bank: **[Gateways](gateways/index.md)** — per-provider reference (Payme, Click, Uzum, Paynet, Octo).
- :material-language-python: **[Django](integrations/django.md)** & **[FastAPI](integrations/fastapi.md)** — webhook integration guides.
- :material-alert: **[Exceptions](exceptions.md)** — the error hierarchy.

</div>

## Install

```bash
pip install unipay-uz
```

## At a glance

```python
from unipay_uz import PaymeGateway

payme = PaymeGateway(
    payme_id="MERCHANT_ID_HERE",
    payme_key="SECRET_KEY_HERE",
    is_test_mode=True,
)

checkout_url = payme.create_payment(
    id="ORD-998877",
    amount=250000,                 # UZS
    return_url="https://your-platform.uz/checkout/success",
    account_field_name="order_id",
)
```

Or instantiate by name with the factory:

```python
from unipay_uz import create_gateway

click = create_gateway("click", service_id="...", merchant_id="...", secret_key="...")
```

Continue to the **[Quickstart](quickstart.md)**.

---

If UniPay UZ saves you time, please [⭐ star it on GitHub](https://github.com/javlondevv/unipay-uz) — it helps other developers in Uzbekistan find it.
