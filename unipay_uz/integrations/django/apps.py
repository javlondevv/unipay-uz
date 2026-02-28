"""
Django app configuration for UniPay UZ.
"""
from django.apps import AppConfig


class UniPay UZConfig(AppConfig):
    """
    Django app configuration for UniPay UZ.
    """
    name = 'unipay_uz.integrations.django'
    verbose_name = 'UniPay UZ'

    default_auto_field = 'django.db.models.AutoField'

    def ready(self):
        """
        Initialize the app.
        """
        try:
            import unipay_uz.integrations.django.signals  # noqa
        except ImportError:
            pass
