from django.forms import ModelForm

from clients.models import Email


class EmailForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['address'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Email

        fields = ['address']
