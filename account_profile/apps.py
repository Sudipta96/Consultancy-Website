from django.apps import AppConfig


class AccountProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account_profile'

    def ready(self):
        import account_profile.signals
