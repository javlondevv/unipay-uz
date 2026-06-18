# Installation

## Requirements

- Python **3.9+**
- `requests` and `loguru` (installed automatically)

## Standard install

```bash
pip install unipay-uz
```

This gives you all five gateways (Payme, Click, Uzum, Paynet, Octo) and the
factory — everything you need to **generate checkout links and call provider
APIs**.

## Framework extras

Install the matching extra only if you want the bundled webhook integration for
that framework:

=== "Django"

    ```bash
    pip install "unipay-uz[django]"
    ```

=== "FastAPI"

    ```bash
    pip install "unipay-uz[fastapi]"
    ```

=== "Flask"

    ```bash
    pip install "unipay-uz[flask]"
    ```

!!! note "Flask"
    The Flask extra installs Flask dependencies, but the bundled Flask webhook
    integration is still in progress. Django and FastAPI integrations are
    available today.

## Checking what's available at runtime

```python
import unipay_uz

print(unipay_uz.__version__)
print(unipay_uz.HAS_DJANGO, unipay_uz.HAS_FASTAPI, unipay_uz.HAS_FLASK)

# Or assert a framework's deps are present:
from unipay_uz import check_dependencies, get_missing_dependencies
check_dependencies("django", raise_error=True)   # raises DependencyError if missing
print(get_missing_dependencies("fastapi"))         # -> list of missing packages
```
