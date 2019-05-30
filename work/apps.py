from django.apps import AppConfig


class WorkConfig(AppConfig):
    name = 'work'
    
    def ready(self):
        """
        Import signal to create specs when Project is created.
        """
        import work.signals
