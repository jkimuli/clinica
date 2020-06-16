from django.apps import AppConfig

class AssetConfig(AppConfig):
    name = 'assets'

    def ready(self):
        import assets.signals