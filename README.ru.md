<p align="center">
  <a href="https://github.com/javlondevv/unipay-uz">
    <img src="assets/banner.svg" alt="UniPay UZ" width="100%">
  </a>
</p>

<h1 align="center">💳 UniPay UZ</h1>

<p align="center">
  <b>Единый Python-API для платёжных систем Узбекистана —
  Payme · Click · Uzum · Paynet · Octo.</b><br>
  Готовые интеграции для Django, FastAPI и Flask.
</p>

<p align="center">
  <a href="https://pypi.org/project/unipay-uz/"><img src="https://img.shields.io/pypi/v/unipay-uz.svg" alt="PyPI version"></a>
  <a href="https://pypi.org/project/unipay-uz/"><img src="https://img.shields.io/pypi/pyversions/unipay-uz.svg" alt="Python Versions"></a>
  <a href="https://pypi.org/project/unipay-uz/"><img src="https://img.shields.io/pypi/dm/unipay-uz.svg?color=blue" alt="PyPI downloads"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://github.com/javlondevv/unipay-uz/actions/workflows/ci.yml"><img src="https://github.com/javlondevv/unipay-uz/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://javlondevv.github.io/unipay-uz/"><img src="https://img.shields.io/badge/docs-mkdocs--material-blue.svg" alt="Documentation"></a>
  <br>
  <a href="https://github.com/javlondevv/unipay-uz/stargazers"><img src="https://img.shields.io/github/stars/javlondevv/unipay-uz?style=social" alt="GitHub stars"></a>
  <a href="https://github.com/javlondevv/unipay-uz/issues"><img src="https://img.shields.io/github/issues/javlondevv/unipay-uz.svg" alt="Open issues"></a>
  <a href="https://github.com/javlondevv/unipay-uz/commits/main"><img src="https://img.shields.io/github/last-commit/javlondevv/unipay-uz.svg" alt="Last commit"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <b>🌐 Русский</b>
</p>

<p align="center">
  <b>Экономит вам неделю возни с платёжными интеграциями? Поставьте <a href="https://github.com/javlondevv/unipay-uz">⭐ звезду</a> — так библиотеку найдут другие разработчики.</b>
  &nbsp;·&nbsp;
  <a href="https://twitter.com/intent/tweet?text=UniPay%20UZ%20%E2%80%94%20%D0%B5%D0%B4%D0%B8%D0%BD%D1%8B%D0%B9%20Python-API%20%D0%B4%D0%BB%D1%8F%20Payme%2C%20Click%2C%20Uzum%2C%20Paynet%20%D0%B8%20Octo&url=https://github.com/javlondevv/unipay-uz&hashtags=Python,Uzbekistan,fintech"><img src="https://img.shields.io/badge/Tweet-%D0%BF%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8%D1%82%D1%8C%D1%81%D1%8F-1DA1F2?logo=twitter&logoColor=white" alt="Tweet"></a>
</p>

---

## 📑 Содержание

- [Почему UniPay UZ?](#-почему-unipay-uz)
- [Установка](#️-установка)
- [Быстрый старт](#-быстрый-старт)
  - [Создание ссылок на оплату](#1-создание-ссылок-на-оплату)
  - [Особенности провайдеров](#2-особенности-провайдеров)
- [Подробно: интеграция с Django](#️-подробно-интеграция-с-django)
- [Участие в разработке](#-участие-в-разработке)
- [Поддержать проект](#-поддержать-проект)
- [Об авторе](#-об-авторе)
- [Лицензия](#-лицензия)

---

**UniPay UZ** — это комплексная и надёжная библиотека для интеграции с ведущими платёжными системами Узбекистана. Создаёте ли вы крупную e-commerce платформу или масштабируемый SaaS-продукт — библиотека упрощает работу с транзакциями для **Payme, Click, Uzum, Paynet и Octo**.

Она спроектирована с упором на масштабируемость и удобство для разработчика и берёт на себя всю рутину: общение с API, проверку вебхуков и управление состоянием транзакций, — чтобы вы могли сосредоточиться на своём продукте.

---

## ⚡ Почему UniPay UZ?

- **Единый интерфейс:** Хватит писать однотипные обёртки над API! Работайте со всеми провайдерами через один предсказуемый интерфейс.
- **Проверенная безопасность:** Проверки целостности и безопасности данных встроены изначально.
- **Готовые интеграции с фреймворками:** Полноценная поддержка **Django**, **FastAPI** и **Flask** «из коробки».
- **Простые вебхуки:** Обрабатывайте асинхронные платёжные уведомления (callback'и) с помощью удобных базовых классов.
- **Гибкая архитектура:** Легко расширяется под новые или нишевые платёжные шлюзы по мере роста вашего бизнеса.

## 🛠️ Установка

Установка занимает считанные секунды через pip.

**Стандартная установка:**
```bash
pip install unipay-uz
```

**Установка под конкретный фреймворк:**
```bash
# Зависимости для Django
pip install unipay-uz[django]

# Зависимости для FastAPI
pip install unipay-uz[fastapi]

# Зависимости для Flask
pip install unipay-uz[flask]
```

---

## 🚀 Быстрый старт

### 1. Создание ссылок на оплату

Укажите учётные данные мерчанта и мгновенно создавайте защищённые платёжные ссылки.

```python
from unipay_uz.gateways.payme import PaymeGateway
from unipay_uz.gateways.click import ClickGateway
from unipay_uz.gateways.uzum.client import UzumGateway
from unipay_uz.gateways.paynet import PaynetGateway

# Настройка Payme
payme_client = PaymeGateway(
    payme_id="MERCHANT_ID_HERE",
    payme_key="SECRET_KEY_HERE",
    is_test_mode=True  # Переключите для продакшена
)

# Настройка Click
click_client = ClickGateway(
    service_id="APP_SERVICE_ID",
    merchant_id="APP_MERCHANT_ID",
    merchant_user_id="APP_USER_ID",
    secret_key="SECRET_HASH_KEY",
    is_test_mode=True
)

# Создание счёта / ссылки на оплату
checkout_url_payme = payme_client.create_payment(
    id="ORD-998877",
    amount=250000,  # Сумма в сумах (UZS)
    return_url="https://your-platform.uz/checkout/success",
    account_field_name="order_id"  # Ключ идентификатора, который ожидает Payme
)

# Создание счёта Click
checkout_url_click = click_client.create_payment(
    id="ORD-998877",
    amount=250000,
    description="Продление подписки",
    return_url="https://your-platform.uz/checkout/success"
)
```

### 2. Особенности провайдеров

#### Paynet
Paynet обрабатывает счета преимущественно через мобильные устройства, формируя ссылки прямого перехода в приложение.
```python
# Создание счёта Paynet (сумма в тийинах: 1 UZS = 100 тийин)
paynet_url = paynet_client.create_payment(
    id="ORD-998877",
    amount=25000000
)
# Возвращает: https://app.paynet.uz/?m={merchant_id}&c=ORD-998877&a=25000000
```
*Примечание: для подтверждения оплаты Paynet использует вебхуки по JSON-RPC 2.0, а не return URL.*

#### Интеграция с Uzum
Сформируйте редирект на шлюз экосистемы Uzum.
```python
uzum_url = uzum_client.create_payment(
    id="ORD-998877",
    amount=50000,  # Сумма в сумах (UZS)
    return_url="https://your-platform.uz/sync"
)
```

---

## 🏗️ Подробно: интеграция с Django

Обновление состояния транзакций в реальном времени для Django встроено в `unipay-uz`.

### Настройка
Сначала добавьте учётные данные в `settings.py`:
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

### Обработка вебхуков
Создайте view-классы, наследующиеся от базовых классов вебхуков.

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

Подключите обработчики в `urls.py`:
```python
from django.urls import path
from .views import PaymeCallbackReceiver, ClickCallbackReceiver

urlpatterns = [
    path('api/v1/webhooks/payme/', PaymeCallbackReceiver.as_view()),
    path('api/v1/webhooks/click/', ClickCallbackReceiver.as_view()),
]
```

---

## 🤝 Участие в разработке

Мы рады вкладам, сообщениям об ошибках и предложениям новых шлюзов! Описание процесса
разработки — в [`CONTRIBUTING.md`](CONTRIBUTING.md). Удобные точки входа отмечены меткой
[**good first issue**](https://github.com/javlondevv/unipay-uz/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22).
Пожалуйста, соблюдайте наш [Кодекс поведения](CODE_OF_CONDUCT.md).

## ⭐ Поддержать проект

Если UniPay UZ экономит вам время — лучшая благодарность это **звезда на GitHub**: она
напрямую помогает другим разработчикам Узбекистана найти библиотеку.

Хотите живую кнопку «Star» на своём сайте или в документации? Используйте
[GitHub Buttons](https://buttons.github.io/):

```html
<!-- Разместите один раз перед </body> -->
<a class="github-button"
   href="https://github.com/javlondevv/unipay-uz"
   data-icon="octicon-star"
   data-size="large"
   data-show-count="true"
   aria-label="Star javlondevv/unipay-uz on GitHub">Star</a>
<script async defer src="https://buttons.github.io/buttons.js"></script>
```

## 👨‍💻 Об авторе

**Джавлон Бахтиёров (javlondevv)**
> «Создаю бэкенд-системы, которые думают наперёд: автоматизируют задачи, масштабируют API и делают код незаметным, когда он работает как надо. Лучший код решает проблемы людей, а не только технические задачи.»

Джавлон — увлечённый инженер-программист, специализирующийся на проектировании масштабируемых инструментов, наставничестве и построении качественных систем. Его экспертиза — бэкенд на Python, Django, FastAPI, Celery и других современных фреймворках.

Если этот пакет помог вам или вашей компании упростить платёжные интеграции — будем рады знакомству!
- **LinkedIn:** [javlon-baxtiyorov](https://www.linkedin.com/in/javlon-baxtiyorov-178051261/)
- **GitHub:** [@javlondevv](https://github.com/javlondevv)
- **Telegram:** [@DevFlowJavlon](https://t.me/DevFlowJavlon)

## 📄 Лицензия

Распространяется по лицензии MIT. Подробнее — в файле [`LICENSE`](LICENSE).
