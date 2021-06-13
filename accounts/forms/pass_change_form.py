from django.contrib.auth.forms import PasswordChangeForm


class PassChangeForm(PasswordChangeForm):

    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)

        classes = {'class': 'form-control'}

        self.fields['old_password'].widget.attrs.update(classes)
        self.fields['new_password1'].widget.attrs.update(classes)
        self.fields['new_password2'].widget.attrs.update(classes)
