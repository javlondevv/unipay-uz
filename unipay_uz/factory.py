from unipay_uz.core.base import BasePaymentGateway
from unipay_uz.core.constants import PaymentGateway

from unipay_uz.gateways.payme.client import PaymeGateway
from unipay_uz.gateways.click.client import ClickGateway
from unipay_uz.gateways.uzum.client import UzumGateway
from unipay_uz.gateways.paynet.client import PaynetGateway


def create_gateway(gateway_type: str, **kwargs) -> BasePaymentGateway:
    """
    Create a payment gateway instance.

    Arguments:
        gateway_type: Type of gateway ('payme', 'click', 'uzum', or 'paynet')
        **kwargs: Gateway-specific configuration

    Yields:
        Payment gateway instance

    Raises:
        ValueError: If the gateway type is not supported
        ImportError: If the required gateway module is not available
    """
    if gateway_type.lower() == PaymentGateway.PAYME.value:
        return PaymeGateway(**kwargs)
    if gateway_type.lower() == PaymentGateway.CLICK.value:
        return ClickGateway(**kwargs)
    if gateway_type.lower() == PaymentGateway.UZUM.value:
        return UzumGateway(**kwargs)
    if gateway_type.lower() == PaymentGateway.PAYNET.value:
        return PaynetGateway(**kwargs)

    raise ValueError(f"Unsupported gateway type: {gateway_type}")
