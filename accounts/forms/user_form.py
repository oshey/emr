from django.forms import ModelForm

from accounts.models import User


class UserForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        classes = {'class': 'form-control'}

        self.fields['title'].widget.attrs.update(classes)
        self.fields['first_name'].widget.attrs.update(classes)
        self.fields['middle_initial'].widget.attrs.update(classes)
        self.fields['last_name'].widget.attrs.update(classes)

    class Meta:
        model = User

        fields = ['title', 'first_name', 'middle_initial', 'last_name']


class UserUpdateForm(UserForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reg'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User

        fields = ['title', 'first_name', 'middle_initial', 'last_name', 'reg']
