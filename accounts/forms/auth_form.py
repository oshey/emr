from django.contrib.auth.forms import AuthenticationForm


class AuthForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        classes = {'class': 'form-control'}

        self.fields['username'].widget.attrs.update(classes)
        self.fields['password'].widget.attrs.update(classes)
