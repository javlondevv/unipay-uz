# FastAPI Integration

Install with the extra:

```bash
pip install "unipay-uz[fastapi]"
```

The FastAPI integration provides webhook **handlers**, SQLAlchemy models, Pydantic
schemas, and a ready-to-include router under
`unipay_uz.integrations.fastapi`.

## Webhook handlers

`PaymeWebhookHandler` and `ClickWebhookHandler` wrap the verification + state
machine; you subclass them and override the lifecycle hooks.

```python
from unipay_uz.integrations.fastapi.routes import PaymeWebhookHandler
```

### `PaymeWebhookHandler` constructor

```python
PaymeWebhookHandler(
    db: Session,
    payme_id: str,
    payme_key: str,
    account_model: Any,
    account_field: str = "id",
    amount_field: str = "amount",
    one_time_payment: bool = True,
)
```

### Overridable hooks

| Hook | When |
|---|---|
| `before_check_perform_transaction(params, account)` | pre-check |
| `successfully_payment(params, transaction)` | payment succeeded |
| `cancelled_payment(params, transaction)` | payment cancelled |

```python
class MyPaymeHandler(PaymeWebhookHandler):
    def successfully_payment(self, params, transaction):
        order = self.db.query(Order).filter_by(ref_id=transaction.account_id).one()
        order.paid = True
        self.db.commit()
```

Handle the incoming request:

```python
@app.post("/webhooks/payme")
async def payme_webhook(request: Request):
    handler = MyPaymeHandler(db=Session(), payme_id="...", payme_key="...",
                             account_model=Order, account_field="ref_id")
    return await handler.handle_webhook(request)
```

`ClickWebhookHandler` follows the same pattern.

## Models & migrations

`unipay_uz.integrations.fastapi.models` defines a SQLAlchemy `PaymentTransaction`
(columns: `id`, `gateway`, `transaction_id`, `account_id`, `amount`, `state`,
`reason`, `extra_data`, and the timestamp fields) with `create_transaction()`,
`mark_as_paid()`, and `mark_as_cancelled()`.

Create the tables:

```python
from unipay_uz.integrations.fastapi.models import run_migrations
run_migrations(engine)
```

## Schemas & router

Pydantic schemas (`PaymentTransactionCreate`, `PaymeWebhookRequest`,
`PaymeWebhookResponse`, `ClickWebhookRequest`, …) live in
`unipay_uz.integrations.fastapi.schemas`, and a prebuilt `router: APIRouter` is
available to `include_router` directly.
