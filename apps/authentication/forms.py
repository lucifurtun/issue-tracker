from django import forms
from django.core.mail import send_mail


class SignupForm(forms.Form):
    def signup(self, request, user):
        user.is_active = True
        user.save()
