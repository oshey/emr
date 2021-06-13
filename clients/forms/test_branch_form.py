from django.forms import ModelForm

from clients.models import Branch, Address


class TestBranchForm(ModelForm):

    def save(self, commit=True):
        address = Address()
        address.line_1 = self.cleaned_data.get('line_1')
        address.city = self.cleaned_data.get('city')
        address.state = self.cleaned_data.get('state')
        address.country = self.cleaned_data.get('country')
        address.zip = self.cleaned_data.get('zip', None)
        address.save()

        branch = super().save(commit)
        branch.address = address
        branch.save()

        return branch

    class Meta:
        model = Branch
        fields = ['name', 'tel_1', 'tel_2', 'fax', 'line_1', 'city', 'state', 'country', 'zip']
