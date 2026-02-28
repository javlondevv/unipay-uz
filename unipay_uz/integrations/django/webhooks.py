"""
Django webhook handlers for UniPay UZ.

Public webhook classes that provide type hints and IDE support.
These classes inherit from internal webhooks which contain the compiled business logic.
"""
from loguru import logger

from .internal_webhooks import (
    PaymeWebhook as PaymeWebhookInternal,
    ClickWebhook as ClickWebhookInternal,
    UzumWebhook as UzumWebhookInternal,
    PaynetWebhook as PaynetWebhookInternal,
    OctoWebhook as OctoWebhookInternal,
)



class PaymeWebhook(PaymeWebhookInternal):
    """
    Primary Django webhook handler for the Payme gateway.

    Processes incoming webhooks originating from Payme.
    Inherit from this handler and override specific event hooks to tailor
    the required business logic.

    Implementation Example:
    ```python
    from unipay_uz.integrations.django.webhooks import PaymeWebhook

    class CustomPaymeWebhook(PaymeWebhook):
        def successfully_payment(self, params, transaction):
            # Insert custom business logic below
            print(f"Payment successful: {transaction.transaction_id}")

            # Modify the state of your corresponding order
            order = Order.objects.get(id=transaction.account_id)
            order.status = 'paid'
            order.save()
    ```
    """

    # Hook methods designed to be overridden by child classes

    def before_check_perform_transaction(self, params, account):
        """
        Fired prior to validating whether a transaction is permitted.

        Arguments:
            params: Incoming payload or request parameters
            account: The associated account instance
        """
        pass

    def transaction_already_exists(self, params, transaction):
        """
        Triggered if the requested transaction is already present in the system.

        Arguments:
            params: Incoming payload or request parameters
            transaction: The related transaction instance
        """
        pass

    def transaction_created(self, params, transaction, account):
        """
        Fired immediately after a new transaction record is generated.

        Arguments:
            params: Incoming payload or request parameters
            transaction: The related transaction instance
            account: The associated account instance
        """
        pass

    def successfully_payment(self, params, transaction):
        """
        Triggered upon successful completion of a payment.

        Arguments:
            params: Incoming payload or request parameters
            transaction: The related transaction instance
        """
        pass

    def check_transaction(self, params, transaction):
        """
        Invoked during the transaction validation and checking phase.

        Arguments:
            params: Incoming payload or request parameters
            transaction: The related transaction instance
        """
        pass

    def cancelled_payment(self, params, transaction):
        """
        Invoked when a payment process is aborted or cancelled by the user or system.

        Arguments:
            params: Incoming payload or request parameters
            transaction: The related transaction instance
        """
        pass

    def get_statement(self, params, transactions):
        """
        Triggered when a request for a transaction statement is received.

        Arguments:
            params: Incoming payload or request parameters
            transactions: A collection of transaction records
        """
        pass

    def get_check_data(self, params, account):
        """
        Customize this method to supply extra payload data for the CheckPerformTransaction phase.

        Arguments:
            params: Incoming payload or request parameters
            account: The associated account instance

        Yields:
            A dictionary with extra fields to inject into the final response payload.
            Implementation Example:
            {
                "additional": {"key": "value"}, # for example {"first_name": "Anvarbek", "balance": 1000000}
                "detail": {
                    "receipt_type": 0,
                    "shipping": {"title": "Yetkazib berish", "price": 10000},
                    "items": [
                        {
                            "discount": 0,
                            "title": "Mahsulot nomi",
                            "price": 500000,
                            "count": 1,
                            "code": "00001",
                            "units": 1,
                            "vat_percent": 0,
                            "package_code": "123456"
                        }
                    ]
                }
            }
        """
        pass


class ClickWebhook(ClickWebhookInternal):
    """
    Primary Django webhook handler for the Click gateway.

    Processes incoming webhooks originating from Click.
    Inherit from this handler and override specific event hooks to tailor
    the required business logic.

    Implementation Example:
    ```python
    from unipay_uz.integrations.django.webhooks import ClickWebhook

    class CustomClickWebhook(ClickWebhook):
        def successfully_payment(self, params, transaction):
            # Insert custom business logic below
            print(f"Payment successful: {transaction.transaction_id}")

            # Modify the state of your corresponding order
            order = Order.objects.get(id=transaction.account_id)
            order.status = 'paid'
            order.save()
    ```
    """

    # Hook methods designed to be overridden by child classes

    def before_check_perform_transaction(self, params, account):
        """
        Fired prior to validating whether a transaction is permitted.

        Arguments:
            params: Incoming payload or request parameters
            account: The associated account instance
        """
        pass

    def transaction_already_exists(self, params, transaction):
        """
        Triggered if the requested transaction is already present in the system.

        Arguments:
            params: Incoming payload or request parameters
            transaction: The related transaction instance
        """
        pass

    def transaction_created(self, params, transaction, account):
        """
        Fired immediately after a new transaction record is generated.

        Arguments:
            params: Incoming payload or request parameters
            transaction: The related transaction instance
            account: The associated account instance
        """
        pass

    def successfully_payment(self, params, transaction):
        """
        Triggered upon successful completion of a payment.

        Arguments:
            params: Incoming payload or request parameters
            transaction: The related transaction instance
        """
        pass

    def cancelled_payment(self, params, transaction):
        """
        Invoked when a payment process is aborted or cancelled by the user or system.

        Arguments:
            params: Incoming payload or request parameters
            transaction: The related transaction instance
        """
        pass




class UzumWebhook(UzumWebhookInternal):
    """
    Primary Django webhook handler for the Uzum gateway.

    Implementation Example:
    ```python
    from unipay_uz.integrations.django.webhooks import UzumWebhook

    class CustomUzumWebhook(UzumWebhook):
        def successfully_payment(self, params, transaction):
            # Insert custom business logic below
            print(f"Payment successful: {transaction.transaction_id}")
            
        def get_check_data(self, params, account):
            return {
                "fio": {
                    "value": f"{account.first_name} {account.last_name}"
                }
            }
    ```
    """

    def successfully_payment(self, params, transaction):
        pass

    def cancelled_payment(self, params, transaction):
        pass
        
    def get_check_data(self, params, account):
        """
        Customize this method to supply additional data within the check response.
        By default returns empty dict.
        """
        pass

class PaynetWebhook(PaynetWebhookInternal):
    """
    Primary Django webhook handler for the Paynet gateway.

    Processes incoming webhooks originating from Paynet.
    Inherit from this handler and override specific event hooks to tailor
    the required business logic.

    Implementation Example:
    ```python
    from unipay_uz.integrations.django.webhooks import PaynetWebhook

    class CustomPaynetWebhook(PaynetWebhook):
        def successfully_payment(self, params, transaction):
            # Insert custom business logic below
            print(f"Payment successful: {transaction.transaction_id}")
    ```
    """

    def successfully_payment(self, params, transaction):
        """
        Triggered upon successful completion of a payment.

        Arguments:
            params: Incoming payload or request parameters
            transaction: The related transaction instance
        """
        pass

    def cancelled_payment(self, params, transaction):
        """
        Invoked when a payment process is aborted or cancelled by the user or system.

        Arguments:
            params: Incoming payload or request parameters
            transaction: The related transaction instance
        """
        pass

    def get_check_data(self, params, account):
        """
        Customize this method to supply extra payload data for the GetInformation phase.

        Arguments:
            params: Incoming payload or request parameters
            account: The associated account instance

        Yields:
            A dictionary with extra fields to inject into the final response payload.
            Implementation Example:
            {
                "fields": {"first_name": "Vali"},
                "balance": 10000
            }
        """
        pass


class OctoWebhook(OctoWebhookInternal):
    """
    Primary Django webhook handler for the Octo gateway.

    Processes callbacks and notifications sent by Octo.
    Inherit from this handler and override specific event hooks to tailor
    the required business logic.

    Implementation Example:
    ```python
    from unipay_uz.integrations.django.webhooks import OctoWebhook

    class CustomOctoWebhook(OctoWebhook):
        def successfully_payment(self, params, transaction):
            # Insert custom business logic below
            print(f"Payment successful: {transaction.transaction_id}")

            # Modify the state of your corresponding order
            order = Order.objects.get(id=transaction.account_id)
            order.status = 'paid'
            order.save()
    ```
    """

    def successfully_payment(self, params, transaction):
        """
        Triggered upon successful completion of a payment.

        Arguments:
            params: Callback data from Octo
            transaction: PaymentThe related transaction instance
        """
        pass

    def cancelled_payment(self, params, transaction):
        """
        Called when a payment is cancelled or failed.

        Arguments:
            params: Callback data from Octo
            transaction: PaymentThe related transaction instance
        """
        pass

