from django.forms import ModelForm

from clients.models import Phone


class PhoneForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['phone_type'].widget.attrs.update({'class': 'form-control col-md-6'})
        self.fields['number'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Phone

        fields = ['phone_type', 'number']
