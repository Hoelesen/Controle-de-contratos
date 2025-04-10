from django.apps import AppConfig

class ContratosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contratos'

    def ready(self):
        import contratos.signals  # Importa os sinais ao carregar o app
        