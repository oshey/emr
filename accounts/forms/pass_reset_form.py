from django.contrib.auth.forms import PasswordResetForm
from django import forms
from django.utils.translation import ugettext_lazy as _


class PassResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'type': 'email'}
        )
    )
