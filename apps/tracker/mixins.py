from django.core.exceptions import PermissionDenied


class PermissionsMixin:
    def dispatch(self, request, *args, **kwargs):
        assert hasattr(self, 'permission_func'), '"permission_func" is a required attribute.'

        has_access = self.permission_func(request.user)

        if not has_access:
            raise PermissionDenied()

        return super().dispatch(request, *args, **kwargs)
