from django.apps import AppConfig


class AskbuddieConfig(AppConfig):
    name = 'askbuddie'
    def ready(self):
        from . import signals