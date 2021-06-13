from django.forms import ModelForm

from clients.models import Branch


class BranchForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['tel_1'].widget.attrs.update({'class': 'form-control'})
        self.fields['tel_2'].widget.attrs.update({'class': 'form-control'})
        self.fields['fax'].widget.attrs.update({'class': 'form-control'})
        self.fields['line_1'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'class': 'form-control'})
        self.fields['state'].widget.attrs.update({'class': 'form-control'})
        self.fields['country'].widget.attrs.update({'class': 'form-control'})
        self.fields['zip'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Branch
        fields = ['name', 'tel_1', 'tel_2', 'fax', 'line_1', 'city', 'state', 'country', 'zip']
