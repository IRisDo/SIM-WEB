from django import forms

from .models import Operator, SIM, Guest

class Payment(forms.ModelForm):

    class Meta:
        model = Guest
        fields = ('name', 'number_phone','CMND','address')
