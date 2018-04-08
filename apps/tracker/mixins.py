from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse


class PermissionsMixin:
    def dispatch(self, request, *args, **kwargs):
        assert hasattr(self, 'permission_func'), '"permission_func" is a required attribute.'

        has_access = self.permission_func(request.user)

        if not has_access:
            if not request.user.is_authenticated:
                return HttpResponseRedirect(reverse('account_login'))

            raise PermissionDenied()

        return super().dispatch(request, *args, **kwargs)
