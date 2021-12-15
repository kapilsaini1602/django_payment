from django.apps import AppConfig


class PaypalIntegConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'paypal_integ'

    def ready(self):
        # import signal handlers
        import paypal_integ.signals



