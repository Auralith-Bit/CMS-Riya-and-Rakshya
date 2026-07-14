from django.apps import AppConfig


class CmsConfig(AppConfig):
    name = 'cms'

    def ready(self):
        from django.core.management import call_command
        from cms.models import Feedback
        if not Feedback.objects.exists():
            call_command('seed_cms')
