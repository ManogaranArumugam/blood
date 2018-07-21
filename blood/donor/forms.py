from django import forms
from blood.donor.models import DonorInformation
from blood.donor.constants import *

class DonorInformationForm(forms.ModelForm):
	""""""
	class Meta:
		model = DonorInformation
		widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'Email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'Phone': forms.TextInput(attrs={'placeholder': 'Phone'}),
            'Age': forms.TextInput(attrs={'placeholder': 'Age'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),

        }
		fields = ('first_name', 'last_name' ,'Email','Phone', 'Age', 'city', 'group', 'reason' )
    