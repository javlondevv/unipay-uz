# Gateways

UniPay UZ ships five gateways. Each exposes a `create_payment(...)` method that
returns a checkout **URL string**, plus provider-specific extras.

## At a glance

| Gateway | `create_payment` arguments | Amount unit | Check/Cancel |
|---|---|---|---|
| [**Payme**](payme.md) | `id, amount, return_url="", account_field_name="order_id"` | UZS | ✅ |
| [**Click**](click.md) | `id, amount, description=…, return_url=…, merchant_user_id=…` | UZS | ✅ |
| [**Uzum**](uzum.md) | `id, amount, return_url, service_id=…` | UZS | refund only |
| [**Paynet**](paynet.md) | `id, amount=None` | **tiyin** | webhook-only |
| [**Octo**](octo.md) | `id, amount, return_url="", currency="UZS", description=…, …` | UZS | ✅ |

!!! warning "Amount units"
    Paynet expects **tiyin** (1 UZS = 100 tiyin); all other gateways take **UZS
    (Som)** and convert internally where needed.

## Factory

Instead of importing a class, you can create any gateway by name:

```python
from unipay_uz import create_gateway

gateway = create_gateway(
    "payme",                       # "payme" | "click" | "uzum" | "paynet"
    payme_id="...",
    payme_key="...",
    is_test_mode=True,
)
```

`create_gateway(gateway_type, **kwargs)` is case-insensitive and forwards
`**kwargs` to the gateway constructor. It raises `ValueError` for an unknown
type.

The supported names come from the `PaymentGateway` enum:

```python
from unipay_uz import PaymentGateway

PaymentGateway.PAYME   # "payme"
PaymentGateway.CLICK   # "click"
PaymentGateway.UZUM    # "uzum"
PaymentGateway.PAYNET  # "paynet"
PaymentGateway.OCTO    # "octo"
```

## The base contract

All gateways subclass `BasePaymentGateway`, which defines the common interface:

```python
class BasePaymentGateway(ABC):
    def __init__(self, is_test_mode: bool = False) -> None: ...

    @abstractmethod
    def create_payment(self, id, amount, **kwargs): ...

    @abstractmethod
    def check_payment(self, transaction_id: str): ...

    @abstractmethod
    def cancel_payment(self, transaction_id: str, reason=None): ...
```

To add your own provider, subclass `BasePaymentGateway` and implement these
three methods — see [Contributing](../contributing.md).
