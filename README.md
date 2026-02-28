# 💳 UniPay UZ

[![PyPI version](https://badge.fury.io/py/unipay-uz.svg)](https://badge.fury.io/py/unipay-uz)
[![Python Versions](https://img.shields.io/pypi/pyversions/unipay-uz.svg)](https://pypi.org/project/unipay-uz/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

**UniPay UZ** is an all-in-one, robust payment integration library designed specifically for Uzbekistan's leading payment gateways. Whether you're building a massive e-commerce platform or a scalable SaaS product, this tool streamlines the transaction workflows for **Payme, Click, Uzum, Paynet, and Octo**. 

Built with scalability and developer experience in mind, it handles the heavy lifting of API communications, webhook verifications, and transaction state management so you can focus on your core product.

---

## ⚡ Why Choose UniPay UZ?

- **Unified Interface:** Stop writing redundant API wrappers! Engage with multiple providers using a standardized, predictable API.
- **Battle-tested Security:** Data integrity and security checks are baked right in.
- **Plug-and-Play Frameworks:** First-class, out-of-the-box integration for **Django**, **FastAPI**, and **Flask**.
- **Effortless Webhooks:** Handle complex asynchronous payment notifications (callbacks) with our elegant webhook base classes.
- **Architectural Flexibility:** Easily extensible to accommodate new or niche payment gateways as your business targets grow.

## 🛠️ Installation Guide

Get up and running in seconds using pip.

**Standard Installation:**
```bash
pip install unipay-uz
```

**Framework-Optimized Installation:**
```bash
# Opt for Django-specific dependencies
pip install unipay-uz[django]

# Opt for FastAPI dependencies
pip install unipay-uz[fastapi]

# Opt for Flask dependencies
pip install unipay-uz[flask]
```

---

## 🚀 Jumpstart Your Integration

### 1. Generating Checkout Links

Drop in your merchant credentials and generate secure payment references instantly.

```python
from unipay_uz.gateways.payme import PaymeGateway
from unipay_uz.gateways.click import ClickGateway
from unipay_uz.gateways.uzum.client import UzumGateway
from unipay_uz.gateways.paynet import PaynetGateway

# Setup Payme 
payme_client = PaymeGateway(
    payme_id="MERCHANT_ID_HERE",
    payme_key="SECRET_KEY_HERE",
    is_test_mode=True  # Toggle for production deployment
)

# Setup Click 
click_client = ClickGateway(
    service_id="APP_SERVICE_ID",
    merchant_id="APP_MERCHANT_ID",
    merchant_user_id="APP_USER_ID",
    secret_key="SECRET_HASH_KEY",
    is_test_mode=True 
)

# Create an invoice / checkout URL
checkout_url_payme = payme_client.create_payment(
    id="ORD-998877",
    amount=250000,  # Value in UZS (Som)
    return_url="https://your-platform.uz/checkout/success",
    account_field_name="order_id"  # Identifier key requested by Payme
)

# Generate Click invoice
checkout_url_click = click_client.create_payment(
    id="ORD-998877",
    amount=250000, 
    description="Subscription Renewal",
    return_url="https://your-platform.uz/checkout/success"
)
```

### 2. Provider-Specific Details

#### Paynet Interactions
Paynet processes invoices predominantly via mobile devices, rendering direct app redirection links.
```python
# Create a Paynet invoice (amount in Tiyin: 1 UZS = 100 Tiyin)
paynet_url = paynet_client.create_payment(
    id="ORD-998877", 
    amount=25000000 
)
# Returns: https://app.paynet.uz/?m={merchant_id}&c=ORD-998877&a=25000000
```
*Note: Paynet relies on JSON-RPC 2.0 Webhooks for fulfillment acknowledgment, not return URLs.*

#### Uzum Biller Integration
Generate an open-service gateway redirect for the Uzum ecosystem.
```python
uzum_url = uzum_client.create_payment(
    id="ORD-998877",  
    amount=50000,  # Value in UZS
    return_url="https://your-platform.uz/sync"  
)
```

---

## 🏗️ Deep Dive: Django Blueprint

Integrating real-time transaction state updates using Django is built into `unipay-uz`.

### Configuration Requirements
First, add your credentials in `settings.py`:
```python
INSTALLED_APPS = [
    # ...
    'unipay_uz.integrations.django',
]

TOLOV = {
    'PAYME': {
        'PAYME_ID': 'STORE_ID',
        'PAYME_KEY': 'STORE_KEY',
        'ACCOUNT_MODEL': 'shop.models.Transaction',
        'ACCOUNT_FIELD': 'ref_id',
        'AMOUNT_FIELD': 'total_amount',
        'ONE_TIME_PAYMENT': True,
    },
    'CLICK': {
        'SERVICE_ID': 'SRV_ID',
        'MERCHANT_ID': 'MCH_ID',
        'MERCHANT_USER_ID': 'USR_ID',
        'SECRET_KEY': 'SECRET',
        'ACCOUNT_MODEL': 'shop.models.Transaction',
        'ACCOUNT_FIELD': 'ref_id',
        'COMMISSION_PERCENT': 0.0,
        'ONE_TIME_PAYMENT': True,
    }
}
```

### Listening to Webhooks
Create specialized views that inherit from our base webhook classes.

```python
# views.py
from unipay_uz.integrations.django.views import BasePaymeWebhookView, BaseClickWebhookView
from shop.models import Transaction

class PaymeCallbackReceiver(BasePaymeWebhookView):
    def successfully_payment(self, params, transaction):
        order = Transaction.objects.get(ref_id=transaction.account_id)
        order.mark_as_paid()

    def cancelled_payment(self, params, transaction):
        order = Transaction.objects.get(ref_id=transaction.account_id)
        order.mark_as_failed()

class ClickCallbackReceiver(BaseClickWebhookView):
    def successfully_payment(self, params, transaction):
        order = Transaction.objects.get(ref_id=transaction.account_id)
        order.mark_as_paid()

    def cancelled_payment(self, params, transaction):
        order = Transaction.objects.get(ref_id=transaction.account_id)
        order.mark_as_failed()
```

Map these receivers in your `urls.py`:
```python
from django.urls import path
from .views import PaymeCallbackReceiver, ClickCallbackReceiver

urlpatterns = [
    path('api/v1/webhooks/payme/', PaymeCallbackReceiver.as_view()),
    path('api/v1/webhooks/click/', ClickCallbackReceiver.as_view()),
]
```

---

## 👨‍💻 Meet the Author

**Javlon Baxtiyorov (javlondevv)**
> "Building backend systems that think ahead—automating tasks, scaling APIs, and making code feel invisible when it's working right. The best code solves human problems, not just technical ones."

Javlon is a dedicated software engineer with a deep passion for designing scalable tools, mentoring fellow developers, and architecting high-quality systems. His expertise lies in backend technologies, relying heavily on Python, Django, FastAPI, Celery, and other modern frameworks to deliver robust solutions.

If this package has helped you or your company streamline payment integrations, feel free to connect!
- **LinkedIn:** [javlon-baxtiyorov](https://www.linkedin.com/in/javlon-baxtiyorov-178051261/)
- **GitHub:** [@javlondevv](https://github.com/javlondevv)
- **Telegram:** [@DevFlowJavlon](https://t.me/DevFlowJavlon)

## 📄 Licensing

Distributed under the MIT License. See `LICENSE.txt` for more information.
