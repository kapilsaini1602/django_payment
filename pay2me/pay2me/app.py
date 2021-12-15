from django.apps import AppConfig


class PaypalIntegConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pay2me'

    def ready(self):
        # import signal handlers
        import pay2me.signals
        print("WOR")
