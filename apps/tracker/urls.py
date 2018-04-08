from django.conf.urls import url

from . import views

issue_list_view = views.IssueListView.as_view()
issue_create_view = views.IssueCreateView.as_view()
issue_detail_view = views.IssueDetailView.as_view()
issue_update_view = views.IssueUpdateView.as_view()
issue_delete_view = views.IssueDeleteView.as_view()

urlpatterns = [
    url(r'^$', issue_list_view, name='issue_list'),
    url(r'^create/$', issue_create_view, name='issue_create'),
    url(r'^(?P<pk>\d+)/$', issue_detail_view, name='issue_detail'),
    url(r'^(?P<pk>\d+)/edit/$', issue_update_view, name='issue_update'),
    url(r'^(?P<pk>\d+)/delete/$', issue_delete_view, name='issue_delete'),
]
