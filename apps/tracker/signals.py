from apps.tracker.models import IssueLog


def issue_post_save_signal(sender, signal, instance, **kwargs):
    last_log: IssueLog = IssueLog.objects.filter(issue=instance).order_by('-moment').first()

    if (last_log is not None) and (instance.status == last_log.action):
        return

    IssueLog.objects.create(
        issue=instance,
        action=instance.status
    )

    instance.duration = instance.get_duration()
    instance.save()
