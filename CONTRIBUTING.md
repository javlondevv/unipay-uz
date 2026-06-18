# Contributing

Thanks for your interest in `unipay-uz`! Contributions — bug fixes, new gateway
support, docs, and translations — are all welcome.

## Development setup

```bash
git clone https://github.com/javlondevv/unipay-uz.git
cd unipay-uz
python -m venv .venv && source .venv/bin/activate
pip install -e ".[django,fastapi,flask]"
```

## Code style

The project uses `black`, `isort`, `flake8`, and `mypy`:

```bash
black .
isort .
flake8 .
mypy unipay_uz
```

Please run these before opening a PR. CI runs an install + import smoke test
across Python 3.9–3.13.

## Conventions

- Keep provider logic inside `unipay_uz/gateways/<provider>/`; shared logic lives
  in `unipay_uz/core/`. Framework code lives under `unipay_uz/integrations/`.
- New gateways should follow the existing `BasePaymentGateway` contract and be
  wired into `factory.py`.
- Update `CHANGELOG.md` under `[Unreleased]` for any user-facing change.
- For user-facing README changes, please update `README.ru.md` too.
- **Never commit secrets** — merchant keys, `.env` files, or PyPI recovery codes.

## Adding a new payment gateway

1. Create `unipay_uz/gateways/<provider>/` with a `client.py` exposing a gateway
   class subclassing `BasePaymentGateway`.
2. Add constants/receipts modules as needed (see existing providers).
3. Register the provider in `unipay_uz/factory.py` and `unipay_uz/core/constants.py`.
4. Document it in both READMEs and add an entry to the changelog.

## Releases

Maintainers bump `version` in `pyproject.toml` **and** `__version__` in
`unipay_uz/__init__.py` (keep them in sync), move `[Unreleased]` changelog
entries under the new version, tag `vX.Y.Z`, and publish to PyPI with `twine`.
