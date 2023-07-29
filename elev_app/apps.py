from django.apps import AppConfig

class ElevAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'elev_app'

    def ready(self):
        from .logic import initialize_elevator_system
        initialize_elevator_system()
