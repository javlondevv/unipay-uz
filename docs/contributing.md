# Contributing

Contributions — bug fixes, new gateways, docs, and translations — are all
welcome!

## Development setup

```bash
git clone https://github.com/javlondevv/unipay-uz.git
cd unipay-uz
python -m venv .venv && source .venv/bin/activate
pip install -e ".[django,fastapi,flask]"
```

## Code style

```bash
black .
isort .
flake8 .
mypy unipay_uz
```

CI runs an install + import smoke test across Python 3.9–3.13.

## Adding a new gateway

1. Create `unipay_uz/gateways/<provider>/` with a `client.py` exposing a class
   that subclasses `BasePaymentGateway` and implements `create_payment`,
   `check_payment`, and `cancel_payment`.
2. Add constants/receipts modules as needed (follow the existing providers).
3. Register the provider in `unipay_uz/factory.py` and
   `unipay_uz/core/constants.py` (`PaymentGateway` enum).
4. Document it: add a page under `docs/gateways/`, update both READMEs
   (`README.md` and `README.ru.md`), and add a `CHANGELOG.md` entry.

## Conventions

- Update `CHANGELOG.md` under `[Unreleased]` for any user-facing change.
- For user-facing README changes, update `README.ru.md` too.
- **Never commit secrets** — merchant keys, `.env` files, or PyPI recovery codes.

Browse the
[**good first issue**](https://github.com/javlondevv/unipay-uz/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
label for friendly starting points, and read the
[Code of Conduct](https://github.com/javlondevv/unipay-uz/blob/main/CODE_OF_CONDUCT.md).
