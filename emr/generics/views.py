from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from emr.mixins import NavBarItemMixin


class BaseSecureView(LoginRequiredMixin, PermissionRequiredMixin):
    pass


class SecureNavbarView(BaseSecureView, NavBarItemMixin):
    pass
