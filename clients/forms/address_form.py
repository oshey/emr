from django.forms import ModelForm

from clients.models import Address


class AddressForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        classes = {'class': 'form-control form-control-md'}

        self.fields['line_1'].widget.attrs.update(classes)
        self.fields['city'].widget.attrs.update(classes)
        self.fields['state_parish'].widget.attrs.update(classes)
        self.fields['postal_code'].widget.attrs.update(classes)
        self.fields['country'].widget.attrs.update(classes)

    class Meta:
        model = Address

        fields = ['line_1', 'city', 'state', 'country', 'zip']
