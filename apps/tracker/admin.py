from django.contrib import admin

from apps.tracker import models

admin.site.register(models.Issue)
admin.site.register(models.IssueLog)
