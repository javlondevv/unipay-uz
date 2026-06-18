# Exceptions

All payment errors derive from `PaymentException` (in
`unipay_uz.core.exceptions`). Each carries a `code`, a `message`, and optional
`data`, and exposes an `as_dict()` helper for serialising error responses.

```python
class PaymentException(Exception):
    code: str
    message: str
    data: dict | None

    def as_dict(self) -> dict: ...
```

## Hierarchy

=== "Authentication"

    | Exception | `code` |
    |---|---|
    | `AuthenticationError` | `authentication_error` |
    | `InvalidCredentials` | `invalid_credentials` |
    | `PermissionDenied` | `permission_denied` |
    | `InvalidServiceId` | `invalid_service_id` |

=== "Transaction"

    | Exception | `code` |
    |---|---|
    | `TransactionError` | `transaction_error` |
    | `TransactionNotFound` | `transaction_not_found` |
    | `TransactionAlreadyExists` | `transaction_already_exists` |
    | `AlreadyPaid` | `already_paid` |
    | `PaymentAlreadyMade` | `payment_already_made` |
    | `TransactionCancelled` | `transaction_cancelled` |
    | `TransactionInProgress` | `transaction_in_progress` |
    | `TransactionCompleted` | `transaction_completed` |

=== "Account & Amount"

    | Exception | `code` |
    |---|---|
    | `AccountError` | `account_error` |
    | `AccountNotFound` | `account_not_found` |
    | `InvalidAccount` | `invalid_account` |
    | `AmountError` | `amount_error` |
    | `InvalidAmount` | `invalid_amount` |
    | `InsufficientFunds` | `insufficient_funds` |

=== "Method & System"

    | Exception | `code` |
    |---|---|
    | `MethodError` | `method_error` |
    | `MethodNotFound` | `method_not_found` |
    | `UnsupportedMethod` | `unsupported_method` |
    | `ServiceNotFound` | `service_not_found` |
    | `SystemError` | `system_error` |
    | `InternalServiceError` | `internal_service_error` |
    | `ExternalServiceError` | `external_service_error` |
    | `TimeoutError` | `timeout_error` |

## Dependency errors

`DependencyError` (subclasses `ImportError`) is raised when a framework's
optional dependencies are missing — e.g. calling a Django integration without
installing `unipay-uz[django]`. Check ahead of time with `check_dependencies()`
(see [Installation](installation.md)).

## Handling errors

```python
from unipay_uz.core.exceptions import PaymentException, TransactionNotFound

try:
    status = payme.check_payment(transaction_id="...")
except TransactionNotFound:
    ...  # specific case
except PaymentException as exc:
    return exc.as_dict()   # {"code": ..., "message": ..., "data": ...}
```
