from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='account_settings'), name='account'),
    url(r'^login/$', views.LoginView.as_view(), name='account_login'),
    url(r'^signup/$', views.SignUpView.as_view(), name='account_signup'),
    url(r'^logout/$', login_required(views.LogoutView.as_view()), name='account_logout'),
    url(r'^settings/$', login_required(views.Settings.as_view()), name='account_settings'),
    url(r'^password-change/$', login_required(views.PasswordChangeView.as_view()), name='account_password')
]
