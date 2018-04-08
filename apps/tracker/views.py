from django.db.models import Avg, Min, Max
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

from apps.tracker import models, access, mixins


class IssueListView(mixins.PermissionsMixin, ListView):
    model = models.Issue
    paginate_by = 2
    permission_func = access.user_has_read_access

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        aggregation = context['object_list'].aggregate(
            average=Avg('duration'),
            shortest=Min('duration'),
            longest=Max('duration')
        )

        context.update(aggregation)

        return context


class IssueCreateView(mixins.PermissionsMixin, CreateView):
    model = models.Issue
    fields = ('title', 'description', 'status', 'category', 'submitter', 'solver')
    success_url = reverse_lazy('tracker:issue_list')
    permission_func = access.user_has_create_access


class IssueDetailView(mixins.PermissionsMixin, DetailView):
    model = models.Issue
    fields = ('title', 'description', 'status', 'category', 'submitter', 'solver')
    permission_func = access.user_has_read_access


class IssueUpdateView(mixins.PermissionsMixin, UpdateView):
    model = models.Issue
    fields = ('title', 'description', 'status', 'category', 'submitter', 'solver')
    success_url = reverse_lazy('tracker:issue_list')
    permission_func = access.user_has_update_access


class IssueDeleteView(mixins.PermissionsMixin, DeleteView):
    model = models.Issue
    success_url = reverse_lazy('tracker:issue_list')
    permission_func = access.user_has_delete_access
