from django.apps import AppConfig
from django.db.models.signals import post_save


class TrackerConfig(AppConfig):
    name = 'apps.tracker'

    def ready(self):
        from apps.tracker.models import Issue
        from apps.tracker.signals import issue_post_save_signal

        post_save.connect(issue_post_save_signal, sender=Issue)
