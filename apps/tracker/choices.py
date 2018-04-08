from django.utils.translation import ugettext_lazy as _


class IssueStatuses:
    TO_DO = 'to_do'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'

    choices = (
        (TO_DO, _('To Do')),
        (IN_PROGRESS, _('In Progress')),
        (DONE, _('Done')),
    )


class IssueCategories:
    FEATURE = 'to_do'
    BUG = 'in_progress'
    IMPROVEMENT = 'done'

    choices = (
        (FEATURE, _('Feature')),
        (BUG, _('Bug')),
        (IMPROVEMENT, _('Improvement')),
    )
