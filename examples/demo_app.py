"""
UniPay UZ demo app (FastAPI).

Shows the shape of a unipay-uz integration without real merchant credentials:

* ``GET  /providers``               - supported gateways and what the demo can do with each
* ``GET  /checkout/{provider}``     - build a checkout URL offline (Payme, Click, Uzum, Paynet)
* ``GET  /orders``                  - in-memory demo orders the webhooks resolve against
* ``POST /webhooks/payme``          - the library's ``PaymeWebhookHandler`` (JSON-RPC)
* ``POST /webhooks/click``          - the library's ``ClickWebhookHandler`` (form data)

Credentials are read from environment variables and default to obviously fake
placeholders. Links built with placeholders will not open a real checkout:
real payments need real merchant credentials from each provider.

Run locally::

    pip install ".[fastapi]" uvicorn
    uvicorn examples.demo_app:app --reload
"""
import os
from typing import Any, Dict, Iterator, Optional

from fastapi import Depends, FastAPI, HTTPException, Query, Request
from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

import unipay_uz
from unipay_uz import ClickGateway, PaymeGateway, PaymentGateway, UzumGateway
from unipay_uz.gateways.paynet import PaynetGateway
from unipay_uz.integrations.fastapi.models import Base
from unipay_uz.integrations.fastapi.routes import (
    ClickWebhookHandler,
    PaymeWebhookHandler,
)

# --- Configuration (placeholders unless overridden by env) -------------------

PLACEHOLDERS: Dict[str, str] = {
    "PAYME_ID": "demo-payme-merchant-id",
    "PAYME_KEY": "demo-payme-key",
    "CLICK_SERVICE_ID": "00000",
    "CLICK_MERCHANT_ID": "00000",
    "CLICK_MERCHANT_USER_ID": "00000",
    "CLICK_SECRET_KEY": "demo-click-secret",
    "UZUM_SERVICE_ID": "000000000",
    "PAYNET_MERCHANT_ID": "00000",
}


def env(name: str) -> str:
    return os.getenv(name) or PLACEHOLDERS[name]


def is_placeholder(*names: str) -> bool:
    return any(not os.getenv(name) for name in names)


TEST_MODE = os.getenv("UNIPAY_TEST_MODE", "true").lower() in ("1", "true", "yes")
DEFAULT_RETURN_URL = os.getenv("DEMO_RETURN_URL", "https://example.com/payment/done")

NOTICE = (
    "Demo only. Values not set via environment variables are placeholders, so "
    "generated links will not open a real checkout. Real payments need real "
    "merchant credentials from each provider."
)

# --- Demo storage: in-memory SQLite with a minimal Order model ---------------

engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Order(Base):
    """The "account" model the webhook handlers look orders up in."""

    __tablename__ = "demo_orders"

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)  # UZS (som)
    description = Column(String(255), nullable=False)


Base.metadata.create_all(engine)
with SessionLocal() as _db:
    if not _db.query(Order).count():
        _db.add_all([
            Order(id=1, amount=10000, description="Demo order #1"),
            Order(id=2, amount=250000, description="Demo order #2"),
        ])
        _db.commit()


def get_db() -> Iterator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --- App ----------------------------------------------------------------------

app = FastAPI(
    title="UniPay UZ demo",
    version=unipay_uz.__version__,
    description=NOTICE,
)

OFFLINE_CHECKOUT = {"payme", "click", "uzum", "paynet"}
WEBHOOKS = {"payme": "/webhooks/payme", "click": "/webhooks/click"}
ENV_VARS = {
    "payme": ["PAYME_ID", "PAYME_KEY"],
    "click": ["CLICK_SERVICE_ID", "CLICK_MERCHANT_ID",
              "CLICK_MERCHANT_USER_ID", "CLICK_SECRET_KEY"],
    "uzum": ["UZUM_SERVICE_ID"],
    "paynet": ["PAYNET_MERCHANT_ID"],
    "octo": [],
}


@app.get("/")
def index() -> Dict[str, Any]:
    return {
        "name": "unipay-uz demo",
        "version": unipay_uz.__version__,
        "test_mode": TEST_MODE,
        "notice": NOTICE,
        "endpoints": {
            "providers": "/providers",
            "checkout": "/checkout/{provider}?order_id=1&amount=10000",
            "orders": "/orders",
            "webhooks": list(WEBHOOKS.values()),
            "docs": "/docs",
        },
    }


@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok"}


@app.get("/providers")
def providers() -> Dict[str, Any]:
    items = []
    for gateway in PaymentGateway:
        name = gateway.value
        items.append({
            "name": name,
            "offline_checkout_url": name in OFFLINE_CHECKOUT,
            "webhook": WEBHOOKS.get(name),
            "env": ENV_VARS[name],
            "using_placeholders": bool(ENV_VARS[name]) and is_placeholder(*ENV_VARS[name]),
        })
    return {
        "providers": items,
        "note": (
            "Octo checkout URLs come from a live Octo API call (prepare_payment) "
            "and need real credentials, so this demo does not build them."
        ),
    }


@app.get("/orders")
def orders(db: Session = Depends(get_db)) -> Dict[str, Any]:
    return {
        "orders": [
            {"id": o.id, "amount": o.amount, "description": o.description}
            for o in db.query(Order).order_by(Order.id)
        ]
    }


@app.get("/checkout/{provider}")
def checkout(
    provider: str,
    order_id: str = Query("1", description="Your order / account id"),
    amount: float = Query(10000, gt=0, description="Amount in UZS (som)"),
    return_url: Optional[str] = Query(None, description="Where to send the payer afterwards"),
) -> Dict[str, Any]:
    provider = provider.lower()
    return_url = return_url or DEFAULT_RETURN_URL
    if amount.is_integer():
        amount = int(amount)  # render 10000, not 10000.0, in the URL

    if provider == "payme":
        url = PaymeGateway(
            payme_id=env("PAYME_ID"), payme_key=env("PAYME_KEY"), is_test_mode=TEST_MODE,
        ).create_payment(id=order_id, amount=amount, return_url=return_url)
    elif provider == "click":
        url = ClickGateway(
            service_id=env("CLICK_SERVICE_ID"),
            merchant_id=env("CLICK_MERCHANT_ID"),
            merchant_user_id=env("CLICK_MERCHANT_USER_ID"),
            secret_key=env("CLICK_SECRET_KEY"),
            is_test_mode=TEST_MODE,
        ).create_payment(id=order_id, amount=amount, return_url=return_url)
    elif provider == "uzum":
        url = UzumGateway(
            service_id=env("UZUM_SERVICE_ID"), is_test_mode=TEST_MODE,
        ).create_payment(id=order_id, amount=amount, return_url=return_url)
    elif provider == "paynet":
        # Paynet takes the amount in tiyin (1 UZS = 100 tiyin) and has no return URL.
        url = PaynetGateway(
            merchant_id=env("PAYNET_MERCHANT_ID"), is_test_mode=TEST_MODE,
        ).create_payment(id=order_id, amount=int(round(amount * 100)))
    elif provider == "octo":
        raise HTTPException(
            status_code=501,
            detail="Octo checkout URLs require a live Octo API call with real credentials.",
        )
    else:
        raise HTTPException(status_code=404, detail=f"Unknown provider: {provider}")

    return {
        "provider": provider,
        "order_id": order_id,
        "amount_uzs": amount,
        "test_mode": TEST_MODE,
        "checkout_url": url,
        "using_placeholders": is_placeholder(*ENV_VARS[provider]),
        "notice": NOTICE,
    }


@app.post("/webhooks/payme")
async def payme_webhook(request: Request, db: Session = Depends(get_db)):
    """Payme Merchant API (JSON-RPC). Payme authenticates with Basic auth ``Paycom:<PAYME_KEY>``."""
    handler = PaymeWebhookHandler(
        db=db,
        payme_id=env("PAYME_ID"),
        payme_key=env("PAYME_KEY"),
        account_model=Order,
        account_field="order_id",  # Payme sends params.account.order_id
        amount_field="amount",
    )
    return await handler.handle_webhook(request)


@app.post("/webhooks/click")
async def click_webhook(request: Request, db: Session = Depends(get_db)):
    """Click SHOP API prepare/complete callbacks (form data, signed with CLICK_SECRET_KEY)."""
    handler = ClickWebhookHandler(
        db=db,
        service_id=env("CLICK_SERVICE_ID"),
        secret_key=env("CLICK_SECRET_KEY"),
        account_model=Order,
    )
    return await handler.handle_webhook(request)
