from django.apps import AppConfig
from django.core.signals import request_finished

class SchoolAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'school_app'

    def ready(self):
        from . import signals
        request_finished.connect(signals.send_email_to_student)
