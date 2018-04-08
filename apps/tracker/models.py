from datetime import timedelta

from django.conf import settings
from django.db import models

from apps.tracker import choices


class Issue(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    status = models.CharField(max_length=50, choices=choices.IssueStatuses.choices, default=choices.IssueStatuses.TO_DO)
    category = models.CharField(max_length=50, choices=choices.IssueCategories.choices)
    duration = models.DurationField(default=timedelta())

    submitter = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  blank=True, null=True,
                                  on_delete=models.SET_NULL,
                                  related_name='submitted_issues')

    solver = models.ForeignKey(settings.AUTH_USER_MODEL,
                               blank=True, null=True,
                               on_delete=models.SET_NULL,
                               related_name='solved_issues')

    def __str__(self):
        return self.title

    def get_duration(self):
        # FIXME: It might be inefficient

        duration = timedelta()
        logs = self.logs.order_by('moment')

        for idx, log in enumerate(logs):
            if log.action == choices.IssueStatuses.IN_PROGRESS:
                in_progress_moment = log.moment

                try:
                    next_log = logs[idx + 1]
                except IndexError:
                    return duration

                next_log_moment = next_log.moment

                duration += next_log_moment - in_progress_moment

        return duration


class IssueLog(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='logs')
    action = models.CharField(max_length=50, choices=choices.IssueStatuses.choices)
    moment = models.DateTimeField(auto_now_add=True)
