"""
Django views for UniPay UZ.
"""
from loguru import logger

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .webhooks import PaymeWebhook, ClickWebhook, UzumWebhook, PaynetWebhook, OctoWebhook



@method_decorator(csrf_exempt, name='dispatch')
class BasePaymeWebhookView(PaymeWebhook):
    """
    Default Payme webhook view.

    This view handles webhook requests from the Payme payment system.
    Inherit from this handler and override specific event hooks to tailor
    the required business logic.

    Implementation Example:
    ```python
    from unipay_uz.integrations.django.views import PaymeWebhookView

    class CustomPaymeWebhookView(PaymeWebhookView):
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
            params: Incoming payload or request parameters
            transaction: The related transaction instance
        """
        logger.info(f"Payme payment successful: {transaction.transaction_id}")

    def cancelled_payment(self, params, transaction):
        """
        Invoked when a payment process is aborted or cancelled by the user or system.

        Arguments:
            params: Incoming payload or request parameters
            transaction: The related transaction instance
        """
        logger.info(f"Payme payment cancelled: {transaction.transaction_id}")

    def get_check_data(self, params, account):
        """
        Customize this method to supply additional data within the check response.
        By default returns empty dict.
        """


@method_decorator(csrf_exempt, name='dispatch')
class BaseClickWebhookView(ClickWebhook):
    """
    Default Click webhook view.

    This view handles webhook requests from the Click payment system.
    Inherit from this handler and override specific event hooks to tailor
    the required business logic.

    Implementation Example:
    ```python
    from unipay_uz.integrations.django.views import ClickWebhookView

    class CustomClickWebhookView(ClickWebhookView):
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
            params: Incoming payload or request parameters
            transaction: The related transaction instance
        """
        logger.info(f"Click payment successful: {transaction.transaction_id}")

    def cancelled_payment(self, params, transaction):
        """
        Invoked when a payment process is aborted or cancelled by the user or system.

        Arguments:
            params: Incoming payload or request parameters
            transaction: The related transaction instance
        """
        logger.info(f"Click payment cancelled: {transaction.transaction_id}")



@method_decorator(csrf_exempt, name='dispatch')
class BaseUzumWebhookView(UzumWebhook):
    """
    Default Uzum webhook view.

    This view handles webhook requests from the Uzum payment system.
    Inherit from this handler and override specific event hooks to tailor
    the required business logic.

    Implementation Example:
    ```python
    from unipay_uz.integrations.django.views import BaseUzumWebhookView

    class CustomUzumWebhookView(BaseUzumWebhookView):
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
        """
        logger.info(f"Uzum payment successful: {transaction.transaction_id}")

    def cancelled_payment(self, params, transaction):
        """
        Invoked when a payment process is aborted or cancelled by the user or system.
        """
        logger.info(f"Uzum payment cancelled: {transaction.transaction_id}")

    def get_check_data(self, params, account):
        """
        Customize this method to supply additional data within the check response.
        By default returns empty dict.
        """


@method_decorator(csrf_exempt, name='dispatch')
class BasePaynetWebhookView(PaynetWebhook):
    """
    Default Paynet webhook view.

    This view handles webhook requests from the Paynet payment system.
    Inherit from this handler and override specific event hooks to tailor
    the required business logic.

    Implementation Example:
    ```python
    from unipay_uz.integrations.django.views import BasePaynetWebhookView

    class CustomPaynetWebhookView(BasePaynetWebhookView):
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
        """
        logger.info(f"Paynet payment successful: {transaction.transaction_id}")

    def cancelled_payment(self, params, transaction):
        """
        Invoked when a payment process is aborted or cancelled by the user or system.
        """
        logger.info(f"Paynet payment cancelled: {transaction.transaction_id}")

    def get_check_data(self, params, account):
        """
        Customize this method to supply additional data within the check response.
        By default returns empty dict.
        """


@method_decorator(csrf_exempt, name='dispatch')
class BaseOctoWebhookView(OctoWebhook):
    """
    Default Octo webhook view.

    This view handles callback notifications from the Octo payment system.
    Inherit from this handler and override specific event hooks to tailor
    the required business logic.

    Implementation Example:
    ```python
    from unipay_uz.integrations.django.views import BaseOctoWebhookView

    class CustomOctoWebhookView(BaseOctoWebhookView):
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
        """
        logger.info(f"Octo payment successful: {transaction.transaction_id}")

    def cancelled_payment(self, params, transaction):
        """
        Invoked when a payment process is aborted or cancelled by the user or system.
        """
        logger.info(f"Octo payment cancelled: {transaction.transaction_id}")
