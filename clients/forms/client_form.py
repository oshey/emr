from django.forms import ModelForm

from clients.models import Client


class ClientForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['web'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Client

        fields = ['name', 'email', 'web']
